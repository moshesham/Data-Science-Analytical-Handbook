"""
MCP Integration Example for Streamlit App

This module shows how to integrate the DS Interview Prep MCP server
with the Streamlit Product Analytics app.

Usage:
    import asyncio
    from mcp_integration import MCPQuizClient
    
    client = MCPQuizClient()
    question = asyncio.run(client.generate_question("sql_basics", "intermediate"))

Note: This requires the MCP server to be running or uses direct function calls
for simplicity.
"""

import asyncio
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

import streamlit as st

# For direct integration (without running MCP server separately)
# We can import the tools directly
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "mcp-server" / "src"))

try:
    from ds_interview_mcp.config import Config
    from ds_interview_mcp.tools import quiz_tools, stats_tools, ab_testing_tools
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False


@dataclass
class QuizQuestion:
    """Represents a quiz question."""
    question_id: str
    question: str
    options: list[str]
    correct_index: int
    explanation: str
    topic: str
    difficulty: str


class MCPQuizClient:
    """Client for interacting with MCP quiz tools."""
    
    def __init__(self, workspace_path: Optional[str] = None):
        """Initialize the client."""
        if workspace_path is None:
            # Find the workspace root
            current = Path(__file__).parent
            while current != current.parent:
                if (current / "_data" / "quizzes.yml").exists():
                    workspace_path = str(current)
                    break
                current = current.parent
            else:
                workspace_path = str(Path.cwd())
        
        self.workspace_path = Path(workspace_path)
        
        if MCP_AVAILABLE:
            self.config = Config(workspace_path=self.workspace_path)
        else:
            self.config = None
    
    async def generate_question(
        self, 
        topic: str, 
        difficulty: str,
        subtopic: Optional[str] = None
    ) -> Optional[QuizQuestion]:
        """Generate a quiz question."""
        if not MCP_AVAILABLE:
            return self._fallback_question(topic, difficulty)
        
        args = {
            "topic": topic,
            "difficulty": difficulty,
        }
        if subtopic:
            args["subtopic"] = subtopic
        
        result = await quiz_tools.generate_quiz_question(args, self.config)
        
        return QuizQuestion(
            question_id=result["question_id"],
            question=result["question"],
            options=result["options"],
            correct_index=result["correct_index"],
            explanation=result["explanation"],
            topic=result["topic"],
            difficulty=result["difficulty"]
        )
    
    async def grade_answer(
        self,
        question: QuizQuestion,
        selected_index: int
    ) -> dict[str, Any]:
        """Grade a user's answer."""
        if not MCP_AVAILABLE:
            return {
                "is_correct": selected_index == question.correct_index,
                "correct_answer": question.options[question.correct_index],
                "explanation": question.explanation
            }
        
        args = {
            "question_text": question.question,
            "options": question.options,
            "correct_index": question.correct_index,
            "selected_index": selected_index
        }
        
        return await quiz_tools.grade_quiz_response(args, self.config)
    
    async def get_existing_quiz(self, topic: str, limit: int = 5) -> list[dict]:
        """Get existing quiz questions from quizzes.yml."""
        if not MCP_AVAILABLE:
            return []
        
        args = {"topic": topic, "limit": limit, "shuffle": True}
        result = await quiz_tools.get_quiz_by_topic(args, self.config)
        
        if "error" in result:
            return []
        
        return result.get("questions", [])
    
    def _fallback_question(self, topic: str, difficulty: str) -> QuizQuestion:
        """Provide a fallback question when MCP is not available."""
        return QuizQuestion(
            question_id="fallback_001",
            question="What does SQL stand for?",
            options=[
                "Structured Query Language",
                "Simple Query Language", 
                "Standard Query Language",
                "Sequential Query Language"
            ],
            correct_index=0,
            explanation="SQL stands for Structured Query Language, used to manage and query relational databases.",
            topic=topic,
            difficulty=difficulty
        )


class MCPSampleSizeCalculator:
    """Client for A/B test sample size calculations."""
    
    def __init__(self):
        self.config = Config(workspace_path=Path.cwd()) if MCP_AVAILABLE else None
    
    async def calculate_sample_size(
        self,
        metric_type: str,
        baseline_value: float,
        minimum_detectable_effect: float,
        standard_deviation: Optional[float] = None,
        alpha: float = 0.05,
        power: float = 0.8
    ) -> dict[str, Any]:
        """Calculate sample size for A/B test."""
        if not MCP_AVAILABLE:
            return self._fallback_calculation(baseline_value, minimum_detectable_effect)
        
        args = {
            "metric_type": metric_type,
            "baseline_value": baseline_value,
            "minimum_detectable_effect": minimum_detectable_effect,
            "alpha": alpha,
            "power": power
        }
        if standard_deviation:
            args["standard_deviation"] = standard_deviation
        
        return await stats_tools.calculate_sample_size(args, self.config)
    
    def _fallback_calculation(self, baseline: float, mde: float) -> dict[str, Any]:
        """Simple fallback calculation."""
        # Rough approximation
        effect = baseline * mde
        n = int(16 * (baseline * (1 - baseline)) / (effect ** 2))
        return {
            "sample_size": {
                "per_variant": n,
                "total": n * 2
            }
        }


# Streamlit UI Components

def render_quiz_interface():
    """Render the quiz interface in Streamlit."""
    st.header("📝 Practice Quiz")
    
    # Initialize session state
    if "quiz_client" not in st.session_state:
        st.session_state.quiz_client = MCPQuizClient()
    
    if "current_question" not in st.session_state:
        st.session_state.current_question = None
    
    if "answer_submitted" not in st.session_state:
        st.session_state.answer_submitted = False
    
    # Topic and difficulty selection
    col1, col2 = st.columns(2)
    
    with col1:
        topic = st.selectbox(
            "Topic",
            ["sql_basics", "python_data_analysis", "statistics_probability", "ab_testing"],
            format_func=lambda x: x.replace("_", " ").title()
        )
    
    with col2:
        difficulty = st.selectbox(
            "Difficulty",
            ["beginner", "intermediate", "advanced"],
            format_func=str.title
        )
    
    # Generate question button
    if st.button("🎲 Generate Question", type="primary"):
        with st.spinner("Generating question..."):
            question = asyncio.run(
                st.session_state.quiz_client.generate_question(topic, difficulty)
            )
            st.session_state.current_question = question
            st.session_state.answer_submitted = False
    
    # Display current question
    if st.session_state.current_question:
        q = st.session_state.current_question
        
        st.markdown(f"### {q.question}")
        st.caption(f"Topic: {q.topic.replace('_', ' ').title()} | Difficulty: {q.difficulty.title()}")
        
        # Answer options
        selected = st.radio(
            "Select your answer:",
            options=range(len(q.options)),
            format_func=lambda i: f"{chr(65+i)}. {q.options[i]}",
            key="answer_selection"
        )
        
        # Submit button
        if not st.session_state.answer_submitted:
            if st.button("Submit Answer"):
                result = asyncio.run(
                    st.session_state.quiz_client.grade_answer(q, selected)
                )
                st.session_state.answer_submitted = True
                st.session_state.last_result = result
        
        # Show result
        if st.session_state.answer_submitted:
            result = st.session_state.last_result
            
            if result["is_correct"]:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect. The correct answer is: {result['correct_answer']}")
            
            with st.expander("📖 Explanation", expanded=True):
                st.write(q.explanation)


def render_sample_size_calculator():
    """Render the sample size calculator in Streamlit."""
    st.header("📊 Sample Size Calculator")
    
    if "size_calc" not in st.session_state:
        st.session_state.size_calc = MCPSampleSizeCalculator()
    
    col1, col2 = st.columns(2)
    
    with col1:
        metric_type = st.selectbox(
            "Metric Type",
            ["proportion", "mean"]
        )
        
        baseline = st.number_input(
            "Baseline Value",
            min_value=0.001,
            max_value=1.0 if metric_type == "proportion" else 1000000.0,
            value=0.05 if metric_type == "proportion" else 100.0,
            format="%.4f" if metric_type == "proportion" else "%.2f"
        )
        
        if metric_type == "mean":
            std_dev = st.number_input(
                "Standard Deviation",
                min_value=0.001,
                value=20.0
            )
        else:
            std_dev = None
    
    with col2:
        mde = st.slider(
            "Minimum Detectable Effect (%)",
            min_value=1,
            max_value=50,
            value=10
        ) / 100
        
        alpha = st.selectbox(
            "Significance Level (α)",
            [0.01, 0.05, 0.10],
            index=1
        )
        
        power = st.selectbox(
            "Statistical Power",
            [0.80, 0.85, 0.90, 0.95],
            index=0
        )
    
    if st.button("Calculate Sample Size", type="primary"):
        with st.spinner("Calculating..."):
            result = asyncio.run(
                st.session_state.size_calc.calculate_sample_size(
                    metric_type=metric_type,
                    baseline_value=baseline,
                    minimum_detectable_effect=mde,
                    standard_deviation=std_dev,
                    alpha=alpha,
                    power=power
                )
            )
        
        if "error" in result:
            st.error(result["error"]["message"])
        else:
            sample_size = result["sample_size"]
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Per Variant", f"{sample_size['per_variant']:,}")
            col2.metric("Total", f"{sample_size['total']:,}")
            
            if "estimated_duration_days" in sample_size:
                col3.metric("Est. Duration", f"{sample_size['estimated_duration_days']} days")


# Main app integration
def main():
    """Main function to run the MCP-integrated Streamlit app."""
    st.set_page_config(
        page_title="DS Interview Prep",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("📊 Data Science Interview Prep")
    st.caption("Powered by MCP Tools")
    
    tab1, tab2, tab3 = st.tabs(["Quiz", "Sample Size Calculator", "About"])
    
    with tab1:
        render_quiz_interface()
    
    with tab2:
        render_sample_size_calculator()
    
    with tab3:
        st.markdown("""
        ## About This App
        
        This interactive app is powered by the DS Interview Prep MCP Server, 
        providing AI-enhanced tools for:
        
        - 📝 **Quiz Generation**: Practice questions across SQL, statistics, Python, and A/B testing
        - 📊 **Sample Size Calculator**: Plan your A/B experiments
        - 🎯 **Case Studies**: Product analytics scenarios for interview prep
        
        ### MCP Integration
        
        This app uses the Model Context Protocol (MCP) to access intelligent tools
        that can generate personalized content and validate your work.
        """)
        
        if MCP_AVAILABLE:
            st.success("✅ MCP server integration is active")
        else:
            st.warning("⚠️ Running in fallback mode (MCP server not available)")


if __name__ == "__main__":
    main()

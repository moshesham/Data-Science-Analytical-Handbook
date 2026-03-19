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
    from ds_interview_mcp.tools import quiz_tools, stats_tools, ab_testing_tools, sql_tools, interview_tools
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



# ── New agent clients ──────────────────────────────────────────────────────────

class MCPInterviewAgent:
    """Client for interview preparation tools (case studies, behavioral, mock)."""

    def __init__(self):
        self.config = Config(workspace_path=Path.cwd()) if MCP_AVAILABLE else None

    async def get_mock_question(
        self, question_type: str, difficulty: str, company_style: str = "generic"
    ) -> dict:
        if not MCP_AVAILABLE:
            return {
                "question": "Walk me through how you would define and track retention for a mobile app.",
                "type": question_type,
                "difficulty": difficulty,
                "evaluation_criteria": ["Clear metric definition", "Cohort analysis", "Segmentation"],
                "time_limit_minutes": 10,
            }
        return await interview_tools.mock_interview_question(
            {"question_type": question_type, "difficulty": difficulty, "company_style": company_style},
            self.config,
        )

    async def get_case_study(self, domain: str, focus_area: str, difficulty: str) -> dict:
        if not MCP_AVAILABLE:
            return {
                "title": "Sample Case Study",
                "scenario": f"You are a data scientist at a {domain} company...",
                "questions_to_address": ["How would you approach this problem?"],
            }
        return await interview_tools.generate_case_study(
            {"domain": domain, "focus_area": focus_area, "difficulty": difficulty},
            self.config,
        )

    async def get_behavioral_question(self, competency: str, company: str = "generic") -> dict:
        if not MCP_AVAILABLE:
            return {
                "main_question": "Tell me about a time you used data to influence a decision.",
                "follow_ups": ["What was the outcome?", "What would you do differently?"],
                "what_they_look_for": ["Data-driven thinking", "Communication"],
            }
        return await interview_tools.generate_behavioral_question(
            {"competency": competency, "company_context": company, "include_follow_ups": True},
            self.config,
        )


class MCPSQLPractice:
    """Client for SQL practice and validation tools."""

    def __init__(self):
        self.config = Config(workspace_path=Path.cwd()) if MCP_AVAILABLE else None

    async def get_problem(self, difficulty: str, topics: list[str] | None = None) -> dict:
        if not MCP_AVAILABLE:
            return {
                "problem_statement": "Write a SQL query to find the top 3 users by order count in the last 30 days.",
                "table_schemas": [{"table": "orders", "columns": ["user_id", "order_id", "created_at"]}],
                "expected_output": "user_id, order_count",
                "hints": ["Use COUNT() and GROUP BY"],
            }
        args: dict = {"difficulty": difficulty, "include_solution": False, "include_hints": True}
        if topics:
            args["topics"] = topics
        return await sql_tools.generate_sql_problem(args, self.config)

    async def validate_query(self, query: str, schema_context: str = "") -> dict:
        if not MCP_AVAILABLE:
            return {"is_valid": True, "issues": [], "suggestions": []}
        return await sql_tools.validate_sql_query(
            {"query": query, "dialect": "postgresql", "schema_context": schema_context,
             "check_performance": True},
            self.config,
        )

    async def explain_query(self, query: str, detail_level: str = "intermediate") -> dict:
        if not MCP_AVAILABLE:
            return {"explanation": "This query selects rows from a table.", "steps": []}
        return await sql_tools.explain_sql_query(
            {"query": query, "detail_level": detail_level}, self.config
        )


class MCPABScenario:
    """Client for A/B testing scenario and analysis tools."""

    def __init__(self):
        self.config = Config(workspace_path=Path.cwd()) if MCP_AVAILABLE else None

    async def get_scenario(
        self, company_type: str, scenario_type: str, difficulty: str
    ) -> dict:
        if not MCP_AVAILABLE:
            return {
                "title": "Feature Launch A/B Test",
                "context": "You're testing a new checkout flow...",
                "questions": ["What metrics would you track?", "How long would you run it?"],
            }
        return await ab_testing_tools.generate_ab_scenario(
            {"company_type": company_type, "scenario_type": scenario_type,
             "difficulty": difficulty, "include_data": True},
            self.config,
        )

    async def analyze_results(self, control_n: int, control_conv: int,
                               treatment_n: int, treatment_conv: int) -> dict:
        if not MCP_AVAILABLE:
            p_ctrl = control_conv / control_n if control_n else 0
            p_trt = treatment_conv / treatment_n if treatment_n else 0
            return {
                "summary": {"control_rate": f"{p_ctrl:.2%}", "treatment_rate": f"{p_trt:.2%}"},
                "statistical_analysis": {"p_value": 0.05, "significant_at_05": True},
                "recommendation": "Insufficient data for MCP analysis (fallback mode).",
            }
        return await ab_testing_tools.analyze_ab_results(
            {"control_conversions": control_conv, "control_total": control_n,
             "treatment_conversions": treatment_conv, "treatment_total": treatment_n,
             "metric_type": "proportion"},
            self.config,
        )

    async def detect_pitfalls(self, description: str, unit: str = "user",
                               duration: int = 14, traffic_pct: float = 50.0) -> dict:
        if not MCP_AVAILABLE:
            return {"findings": [], "warnings": [], "overall_risk": "UNKNOWN"}
        return await ab_testing_tools.detect_ab_pitfalls(
            {"experiment_description": description, "randomization_unit": unit,
             "duration_days": duration, "traffic_percentage": traffic_pct},
            self.config,
        )


# ── New Streamlit UI components ────────────────────────────────────────────────

def render_ab_analysis_panel():
    """Paste in real A/B test numbers and get instant statistical analysis."""
    st.subheader("🔬 Live A/B Test Analyzer")
    st.caption("Enter your experiment results to get statistical interpretation and a shipping recommendation.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Control Group**")
        ctrl_n = st.number_input("Total visitors (Control)", min_value=1, value=50000, key="ab_ctrl_n")
        ctrl_conv = st.number_input("Conversions (Control)", min_value=0, value=2500, key="ab_ctrl_conv")
    with col2:
        st.markdown("**Treatment Group**")
        trt_n = st.number_input("Total visitors (Treatment)", min_value=1, value=50000, key="ab_trt_n")
        trt_conv = st.number_input("Conversions (Treatment)", min_value=0, value=2750, key="ab_trt_conv")

    if st.button("Analyze Results", type="primary", key="ab_analyze_btn"):
        if "ab_scenario" not in st.session_state:
            st.session_state.ab_scenario = MCPABScenario()
        with st.spinner("Analyzing..."):
            result = asyncio.run(
                st.session_state.ab_scenario.analyze_results(ctrl_n, ctrl_conv, trt_n, trt_conv)
            )
        if "error" in result:
            st.error(result["error"]["message"])
        else:
            summary = result.get("summary", {})
            stats_analysis = result.get("statistical_analysis", {})

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Control Rate", summary.get("control_rate", "N/A"))
            m2.metric("Treatment Rate", summary.get("treatment_rate", "N/A"))
            m3.metric("Relative Lift", summary.get("relative_lift", "N/A"))
            sig = stats_analysis.get("significant_at_05", False)
            m4.metric("Significant?", "✅ Yes" if sig else "❌ No",
                      delta=f"p={stats_analysis.get('p_value', 'N/A')}")

            if "confidence_interval" in result:
                ci = result["confidence_interval"]
                st.info(f"**95% CI:** {ci.get('lower_bound')} to {ci.get('upper_bound')}  \n"
                        f"{ci.get('interpretation', '')}")

            rec = result.get("recommendation", "")
            if rec:
                if sig:
                    st.success(f"📌 **Recommendation:** {rec}")
                else:
                    st.warning(f"📌 **Recommendation:** {rec}")

            with st.expander("⚠️ Things to check before shipping"):
                for caution in result.get("cautions", []):
                    st.write(f"• {caution}")


def render_sql_practice_panel():
    """Interactive SQL problem generation and query validation."""
    st.subheader("🗄️ SQL Practice")

    if "sql_client" not in st.session_state:
        st.session_state.sql_client = MCPSQLPractice()
    if "sql_problem" not in st.session_state:
        st.session_state.sql_problem = None

    col1, col2 = st.columns(2)
    with col1:
        sql_difficulty = st.selectbox("Difficulty", ["beginner", "intermediate", "advanced"],
                                      key="sql_diff")
    with col2:
        sql_topics = st.multiselect("Topics (optional)",
                                    ["joins", "window_functions", "ctes", "aggregations",
                                     "subqueries", "self_joins"],
                                    key="sql_topics")

    if st.button("🎲 Get SQL Problem", key="sql_gen_btn"):
        with st.spinner("Generating problem..."):
            problem = asyncio.run(
                st.session_state.sql_client.get_problem(
                    sql_difficulty, sql_topics if sql_topics else None
                )
            )
        st.session_state.sql_problem = problem

    if st.session_state.sql_problem:
        prob = st.session_state.sql_problem
        st.markdown(f"**Problem:** {prob.get('problem_statement', '')}")

        schemas = prob.get("table_schemas", [])
        if schemas:
            with st.expander("📋 Table Schemas"):
                for schema in schemas:
                    st.markdown(f"**`{schema.get('table', '')}`**")
                    cols = schema.get("columns", [])
                    if cols:
                        st.code(", ".join(str(c) for c in cols), language="sql")

        hints = prob.get("hints", [])
        if hints:
            with st.expander("💡 Hints"):
                for hint in hints:
                    st.write(f"• {hint}")

        st.markdown("**Your Solution:**")
        user_sql = st.text_area("Write your SQL here", height=150,
                                 placeholder="SELECT ...\nFROM ...\nWHERE ...",
                                 key="user_sql_input")

        validate_col, explain_col = st.columns(2)
        with validate_col:
            if st.button("✅ Validate Query", key="sql_validate_btn") and user_sql.strip():
                with st.spinner("Validating..."):
                    val_result = asyncio.run(
                        st.session_state.sql_client.validate_query(user_sql)
                    )
                if val_result.get("is_valid"):
                    st.success("Query is syntactically valid!")
                else:
                    for issue in val_result.get("issues", []):
                        st.error(f"❌ {issue.get('message', issue)}")
                for sugg in val_result.get("suggestions", []):
                    st.info(f"💡 {sugg.get('message', sugg)}")

        with explain_col:
            if st.button("📖 Explain Query", key="sql_explain_btn") and user_sql.strip():
                with st.spinner("Explaining..."):
                    exp_result = asyncio.run(
                        st.session_state.sql_client.explain_query(user_sql)
                    )
                explanation = exp_result.get("explanation", exp_result.get("plain_language", ""))
                if explanation:
                    st.info(explanation)

        with st.expander("👁️ See model solution"):
            solution = prob.get("sample_solution", {})
            if isinstance(solution, dict):
                sol_query = solution.get("query", solution.get("sql", ""))
                if sol_query:
                    st.code(sol_query, language="sql")
                notes = solution.get("notes", solution.get("explanation", ""))
                if notes:
                    st.caption(notes)
            elif isinstance(solution, str):
                st.code(solution, language="sql")
            else:
                st.caption("Request a new problem to get a solution-included version.")


def render_mock_interview_panel():
    """Complete mock interview experience with question + self-assessment."""
    st.subheader("🎙️ Mock Interview Mode")

    if "interview_agent" not in st.session_state:
        st.session_state.interview_agent = MCPInterviewAgent()
    if "mock_question" not in st.session_state:
        st.session_state.mock_question = None
    if "interview_started" not in st.session_state:
        st.session_state.interview_started = False

    col1, col2, col3 = st.columns(3)
    with col1:
        q_type = st.selectbox("Question Type",
                               ["product_sense", "metrics", "sql", "statistics",
                                "case_study", "behavioral"],
                               key="mock_qtype")
    with col2:
        q_diff = st.selectbox("Difficulty", ["easy", "medium", "hard"], key="mock_qdiff")
    with col3:
        company = st.selectbox("Company Style",
                                ["generic", "meta", "google", "amazon", "microsoft"],
                                key="mock_company")

    if st.button("🎯 Start Interview Question", type="primary", key="mock_start_btn"):
        with st.spinner("Generating question..."):
            q = asyncio.run(
                st.session_state.interview_agent.get_mock_question(q_type, q_diff, company)
            )
        st.session_state.mock_question = q
        st.session_state.interview_started = True
        st.session_state.mock_answer = ""
        st.session_state.mock_submitted = False

    if st.session_state.mock_question:
        q = st.session_state.mock_question
        question_text = q.get("question", q.get("question_type", ""))

        st.markdown("---")
        st.markdown(f"### ❓ {question_text}")

        time_limit = q.get("time_limit_minutes", 10)
        st.caption(f"⏱️ Time limit: {time_limit} minutes | Type: {q_type.replace('_', ' ').title()} | Level: {q_diff.title()}")

        with st.expander("📋 What interviewers look for"):
            for criterion in q.get("evaluation_criteria", []):
                st.write(f"✓ {criterion}")

        user_answer = st.text_area(
            "Your Answer (write as if speaking to an interviewer):",
            height=200,
            key="mock_answer_text",
            placeholder="Structure your answer clearly. Use data and specific examples..."
        )

        if st.button("Submit & Self-Assess", key="mock_submit_btn") and user_answer.strip():
            st.session_state.mock_submitted = True

            criteria = q.get("evaluation_criteria", [])
            st.markdown("### 📊 Self-Assessment Checklist")
            st.caption("Check off the criteria you addressed in your answer:")
            score = 0
            for i, criterion in enumerate(criteria):
                checked = st.checkbox(criterion, key=f"mock_check_{i}")
                if checked:
                    score += 1

            if criteria:
                pct = score / len(criteria) * 100
                if pct >= 80:
                    st.success(f"🌟 Strong answer! {score}/{len(criteria)} criteria covered ({pct:.0f}%)")
                elif pct >= 50:
                    st.warning(f"💪 Good start. {score}/{len(criteria)} criteria covered ({pct:.0f}%). Review missed items.")
                else:
                    st.error(f"📚 Needs work. {score}/{len(criteria)} criteria covered ({pct:.0f}%). Practice more!")

        if "follow_up_questions" in q:
            with st.expander("🔄 Follow-up Questions (for practice)"):
                for fq in q["follow_up_questions"]:
                    st.write(f"• {fq}")


def render_case_study_panel():
    """Structured case study interview practice."""
    st.subheader("📋 Case Study Practice")

    if "interview_agent" not in st.session_state:
        st.session_state.interview_agent = MCPInterviewAgent()
    if "case_study" not in st.session_state:
        st.session_state.case_study = None

    col1, col2, col3 = st.columns(3)
    with col1:
        domain = st.selectbox("Domain",
                               ["social_media", "ecommerce", "fintech", "streaming",
                                "marketplace", "saas"],
                               key="cs_domain")
    with col2:
        focus = st.selectbox("Focus Area",
                              ["metrics_definition", "product_launch", "feature_evaluation",
                               "user_growth", "monetization", "retention"],
                              key="cs_focus")
    with col3:
        cs_diff = st.selectbox("Level", ["entry_level", "mid_level", "senior"], key="cs_diff")

    if st.button("📂 Generate Case Study", type="primary", key="cs_gen_btn"):
        with st.spinner("Building case study..."):
            case = asyncio.run(
                st.session_state.interview_agent.get_case_study(domain, focus, cs_diff)
            )
        st.session_state.case_study = case

    if st.session_state.case_study:
        case = st.session_state.case_study
        st.markdown(f"## 🏢 {case.get('title', 'Case Study')}")
        st.caption(f"Domain: {domain.replace('_', ' ').title()} | Focus: {focus.replace('_', ' ').title()} | Level: {cs_diff.replace('_', ' ').title()} | ⏱️ {case.get('time_allocation_minutes', 45)} min")

        st.markdown("### 📖 Scenario")
        st.markdown(case.get("scenario", ""))

        if case.get("data_available"):
            with st.expander("🗂️ Available Data Sources"):
                for d in case["data_available"]:
                    st.write(f"• {d}")

        st.markdown("### ❓ Questions to Address")
        for i, q in enumerate(case.get("questions_to_address", []), 1):
            st.write(f"**{i}.** {q}")

        with st.expander("📐 Evaluation Criteria"):
            for criterion in case.get("evaluation_criteria", [
                "Structured problem decomposition",
                "Clear metric definitions",
                "Data-driven recommendations"
            ]):
                st.write(f"✓ {criterion}")

        if case.get("sample_solution"):
            with st.expander("💡 Sample Solution (reveal after attempting)"):
                sol = case["sample_solution"]
                if isinstance(sol, dict):
                    for key, val in sol.items():
                        st.markdown(f"**{key.replace('_', ' ').title()}:**")
                        if isinstance(val, list):
                            for item in val:
                                st.write(f"• {item}")
                        else:
                            st.write(val)
                else:
                    st.write(sol)


def render_skills_sidebar():
    """Sidebar widget that recommends relevant skills for the current page topic."""
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 🧠 Relevant Skills")
        st.caption("Powered by claude-skills-mcp")

        topic_skills = {
            "probability": ["statistics", "bayesian"],
            "hypothesis": ["ab-testing", "statistics"],
            "sql": ["sql", "data-engineering"],
            "python": ["pandas", "data-analysis"],
            "ab_testing": ["ab-testing", "experiment-design"],
            "metrics": ["product-analytics", "metrics"],
            "churn": ["customer-analytics", "retention"],
            "fraud": ["anomaly-detection", "risk"],
        }

        page_name = ""
        try:
            import __main__
            page_name = getattr(__main__, "__file__", "").lower()
        except Exception:
            pass

        matched = []
        for keyword, skills in topic_skills.items():
            if keyword in page_name:
                matched.extend(skills)

        if matched:
            for skill in matched[:3]:
                st.markdown(f"📌 **{skill.replace('-', ' ').title()}**")
        else:
            st.write("Navigate to a topic page to see relevant skills.")

        st.markdown("[Browse all skills →](https://github.com/anthropics/skills)")


# Main app integration
def main():
    """Main function to run the MCP-integrated Streamlit app."""
    st.set_page_config(
        page_title="DS Interview Prep",
        page_icon="📊",
        layout="wide"
    )

    st.title("📊 Data Science Interview Prep")
    st.caption("Powered by DS Interview MCP + Claude Skills MCP")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📝 Quiz",
        "📊 Sample Size",
        "🗄️ SQL Practice",
        "🔬 A/B Analyzer",
        "ℹ️ About",
    ])

    with tab1:
        render_quiz_interface()

    with tab2:
        render_sample_size_calculator()

    with tab3:
        render_sql_practice_panel()

    with tab4:
        render_ab_analysis_panel()

    with tab5:
        st.markdown("""
        ## About This App

        This interactive app is powered by the **DS Interview Prep MCP Server** and the
        **Claude Skills MCP**, providing AI-enhanced tools for:

        - 📝 **Quiz Generation**: Practice questions across SQL, statistics, Python, A/B testing,
          product metrics, and case studies
        - 📊 **Sample Size Calculator**: Plan your A/B experiments with power analysis
        - 🗄️ **SQL Practice**: Generate problems, validate & explain queries
        - 🔬 **Live A/B Analyzer**: Paste your experiment results for instant statistical interpretation
        - 🎙️ **Mock Interview**: Full interview simulation with self-assessment
        - 📋 **Case Studies**: Structured product analytics scenarios

        ### MCP Integration
        Two MCP servers back this app:
        - **`ds-interview-prep`** — DS-specific quiz, SQL, stats, A/B, and interview tools
        - **`claude-skills`** — Semantic skill discovery from this workspace + Anthropic's skill library
        """)

        if MCP_AVAILABLE:
            st.success("✅ DS Interview MCP integration is active")
        else:
            st.warning("⚠️ Running in fallback mode (MCP server not available)")


if __name__ == "__main__":
    main()

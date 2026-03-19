"""
Interview Practice — DS Interview Prep Hub
===========================================
Full-stack interview practice powered by the DS Interview MCP server.
Covers mock questions, case studies, SQL, A/B analysis, and behavioral prep.
"""

import sys
from pathlib import Path

import streamlit as st

# Ensure mcp_integration is importable
sys.path.insert(0, str(Path(__file__).parent.parent))
from mcp_integration import (
    MCPInterviewAgent,
    MCPSQLPractice,
    MCPABScenario,
    MCPQuizClient,
    MCP_AVAILABLE,
    render_mock_interview_panel,
    render_case_study_panel,
    render_sql_practice_panel,
    render_ab_analysis_panel,
    render_quiz_interface,
)

st.set_page_config(
    page_title="Interview Practice | DS Handbook",
    page_icon="🎙️",
    layout="wide",
)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🎙️ Data Science Interview Practice Hub")
st.markdown(
    "Comprehensive AI-powered interview prep. "
    "Practice every question type you'll face in a DS/Analytics interview."
)

if MCP_AVAILABLE:
    st.success("✅ DS Interview MCP is active — live AI tools enabled")
else:
    st.warning(
        "⚠️ Running in fallback mode. "
        "Start the DS Interview MCP server for full AI-powered responses."
    )

st.markdown("---")

# ── Navigation tabs ───────────────────────────────────────────────────────────
tab_mock, tab_case, tab_sql, tab_ab, tab_quiz, tab_behavioral = st.tabs([
    "🎙️ Mock Interview",
    "📋 Case Studies",
    "🗄️ SQL Practice",
    "🔬 A/B Analysis",
    "📝 Knowledge Quiz",
    "💬 Behavioral Prep",
])

with tab_mock:
    st.markdown(
        "Simulate a live interview. Get a question, write your answer in the text box, "
        "then reveal and self-score against the evaluation criteria used by real interviewers."
    )
    render_mock_interview_panel()

with tab_case:
    st.markdown(
        "Structured product analytics case studies. Choose your domain and focus area, "
        "then work through a realistic scenario before revealing the sample approach."
    )
    render_case_study_panel()

with tab_sql:
    st.markdown(
        "Generate SQL challenges from beginner JOINs to advanced window functions. "
        "Write your solution and validate syntax or get a plain-English explanation."
    )
    render_sql_practice_panel()

with tab_ab:
    st.markdown(
        "Paste your real A/B test numbers (or textbook examples) to get instant "
        "statistical interpretation, confidence intervals, and a shipping recommendation."
    )
    render_ab_analysis_panel()

with tab_quiz:
    st.markdown(
        "Multiple-choice knowledge checks across SQL, statistics, Python, A/B testing, "
        "product metrics, and case-study frameworks."
    )
    render_quiz_interface()

with tab_behavioral:
    st.markdown(
        "Generate behavioral questions targeting key data science competencies. "
        "Practice the STAR framework with follow-up prompts."
    )

    if "interview_agent" not in st.session_state:
        st.session_state.interview_agent = MCPInterviewAgent()
    if "behavioral_q" not in st.session_state:
        st.session_state.behavioral_q = None

    import asyncio

    col1, col2 = st.columns(2)
    with col1:
        competency = st.selectbox(
            "Competency",
            [
                "data_driven_decision_making",
                "cross_functional_collaboration",
                "handling_ambiguity",
                "project_prioritization",
                "communication",
                "technical_depth",
                "ownership",
                "learning_agility",
            ],
            format_func=lambda x: x.replace("_", " ").title(),
            key="beh_competency",
        )
    with col2:
        beh_company = st.selectbox(
            "Company Style",
            ["generic", "meta", "google", "amazon", "microsoft"],
            key="beh_company",
        )

    if st.button("🎲 Generate Behavioral Question", type="primary", key="beh_gen_btn"):
        with st.spinner("Generating..."):
            bq = asyncio.run(
                st.session_state.interview_agent.get_behavioral_question(
                    competency, beh_company
                )
            )
        st.session_state.behavioral_q = bq

    if st.session_state.behavioral_q:
        bq = st.session_state.behavioral_q
        st.markdown("---")
        st.markdown(f"### ❓ {bq.get('main_question', '')}")

        what_they_look_for = bq.get("what_they_look_for", bq.get("evaluation_focus", []))
        if what_they_look_for:
            st.markdown("**What interviewers look for:**")
            for item in what_they_look_for:
                st.write(f"✓ {item}")

        st.markdown("**Your STAR Answer:**")
        star_tabs = st.tabs(["Situation", "Task", "Action", "Result"])
        with star_tabs[0]:
            st.text_area("Describe the situation / context:", height=100, key="star_s")
        with star_tabs[1]:
            st.text_area("What was your specific task or responsibility?", height=100, key="star_t")
        with star_tabs[2]:
            st.text_area("What actions did you take?", height=120, key="star_a")
        with star_tabs[3]:
            st.text_area("What was the quantified outcome?", height=100, key="star_r")

        follow_ups = bq.get("follow_up_questions", bq.get("follow_ups", []))
        if follow_ups:
            with st.expander("🔄 Common follow-up questions"):
                for fq in follow_ups:
                    st.write(f"• {fq}")

        tips = bq.get("tips", bq.get("data_angle_tip", ""))
        if tips:
            st.info(f"💡 **Data angle tip:** {tips}")

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "📚 **Resources:** "
    "[Statistics Cheat Sheet](../../supplementary/statistics-cheat-sheet.md) · "
    "[SQL Cheat Sheet](../../supplementary/sql-cheat-sheet.md) · "
    "[21-Day Prep Guide](../../supplementary/21-day-prep-guide.md)"
)

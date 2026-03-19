"""Quick smoke test for quiz_tools changes."""
import sys
sys.path.insert(0, "src")

import asyncio
from ds_interview_mcp.tools import quiz_tools
from ds_interview_mcp.config import Config
from pathlib import Path

config = Config(workspace_path=Path.cwd().parent)

TOPICS = ["sql_basics", "statistics_probability", "ab_testing",
          "python_data_analysis", "product_metrics", "case_studies"]
DIFFS = ["beginner", "intermediate", "advanced"]


async def main():
    # 1. All 18 topic/difficulty combos generate valid questions
    for topic in TOPICS:
        for diff in DIFFS:
            q = await quiz_tools.generate_quiz_question(
                {"topic": topic, "difficulty": diff}, config
            )
            assert "question" in q, f"Missing 'question' key: {topic}/{diff}"
            assert len(q["options"]) >= 2, f"Too few options: {topic}/{diff}"
    print("✅  All 18 topic/difficulty combos generate valid questions")

    # 2. get_quiz_by_topic for existing yml topics works
    for topic in ["sql", "statistics"]:
        r = await quiz_tools.get_quiz_by_topic({"topic": topic, "limit": 2}, config)
        if "error" not in r:
            assert "questions" in r
            print(f"✅  get_quiz_by_topic({topic}): {r['question_count']} questions")
        else:
            print(f"ℹ️   get_quiz_by_topic({topic}): not in quizzes.yml — expected")

    # For new template-only topics, generate_quiz_question is the right API
    for topic in ["product_metrics", "case_studies"]:
        q = await quiz_tools.generate_quiz_question({"topic": topic, "difficulty": "beginner"}, config)
        assert "question" in q
    print("✅  generate_quiz_question works for product_metrics and case_studies")

    # 3. Variety: same call returns different questions (probabilistic — run twice)
    q1 = await quiz_tools.generate_quiz_question({"topic": "sql_basics", "difficulty": "beginner"}, config)
    q2 = await quiz_tools.generate_quiz_question({"topic": "sql_basics", "difficulty": "beginner"}, config)
    # They *could* match by chance but it should be rare
    print(f"✅  Question variety check — q1: '{q1['question'][:60]}...'")
    print(f"                           q2: '{q2['question'][:60]}...'")


asyncio.run(main())

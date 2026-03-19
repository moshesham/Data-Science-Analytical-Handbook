"""Quiz generation and grading tools."""

import hashlib
import json
import random
from typing import Any, Callable, Coroutine

from mcp.types import Tool

from ds_interview_mcp.config import Config


# Topic definitions with subtopics
TOPICS = {
    "sql_basics": {
        "name": "SQL Fundamentals",
        "subtopics": ["joins", "aggregations", "window_functions", "subqueries", "ctes", "self_joins"]
    },
    "python_data_analysis": {
        "name": "Python Data Analysis",
        "subtopics": ["pandas", "numpy", "data_cleaning", "visualization", "groupby", "merge"]
    },
    "statistics_probability": {
        "name": "Statistics & Probability",
        "subtopics": ["descriptive_stats", "probability", "distributions", "hypothesis_testing", "confidence_intervals"]
    },
    "ab_testing": {
        "name": "A/B Testing",
        "subtopics": ["experiment_design", "sample_size", "analysis", "pitfalls", "metrics"]
    },
    "product_metrics": {
        "name": "Product Metrics",
        "subtopics": ["engagement", "retention", "monetization", "growth", "funnel"]
    },
    "case_studies": {
        "name": "Case Studies",
        "subtopics": ["metric_definition", "product_launch", "feature_evaluation", "debugging"]
    }
}


def get_tool_definitions() -> list[Tool]:
    """Return quiz tool definitions."""
    return [
        Tool(
            name="generate_quiz_question",
            description="Generate a multiple-choice quiz question for data science interview prep covering statistics, SQL, Python, or A/B testing topics.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "enum": list(TOPICS.keys()),
                        "description": "The topic category for the question"
                    },
                    "difficulty": {
                        "type": "string",
                        "enum": ["beginner", "intermediate", "advanced"],
                        "description": "Difficulty level"
                    },
                    "subtopic": {
                        "type": "string",
                        "description": "Specific subtopic (optional)"
                    },
                    "context": {
                        "type": "string",
                        "description": "Real-world context (optional)"
                    }
                },
                "required": ["topic", "difficulty"]
            }
        ),
        Tool(
            name="grade_quiz_response",
            description="Evaluate a user's quiz answer and provide feedback.",
            inputSchema={
                "type": "object",
                "properties": {
                    "question_text": {
                        "type": "string",
                        "description": "The quiz question"
                    },
                    "options": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Answer options"
                    },
                    "correct_index": {
                        "type": "integer",
                        "description": "Index of correct answer (0-based)"
                    },
                    "selected_index": {
                        "type": "integer",
                        "description": "User's selected answer (0-based)"
                    }
                },
                "required": ["question_text", "options", "correct_index", "selected_index"]
            }
        ),
        Tool(
            name="explain_quiz_answer",
            description="Provide detailed explanation for a quiz answer.",
            inputSchema={
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                    "options": {"type": "array", "items": {"type": "string"}},
                    "correct_index": {"type": "integer"},
                    "depth": {
                        "type": "string",
                        "enum": ["brief", "standard", "comprehensive"],
                        "default": "standard"
                    }
                },
                "required": ["question", "options", "correct_index"]
            }
        ),
        Tool(
            name="get_quiz_by_topic",
            description="Retrieve existing quiz questions from the handbook's quiz database.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "enum": ["sql_basics", "python_data_analysis", "statistics_probability", "ab_testing"]
                    },
                    "limit": {"type": "integer", "default": 5},
                    "shuffle": {"type": "boolean", "default": True}
                },
                "required": ["topic"]
            }
        )
    ]


def get_available_topics(config: Config) -> dict[str, Any]:
    """Get available topics with question counts."""
    quizzes = config.load_quizzes()
    result = {}
    for topic_id, topic_info in TOPICS.items():
        quiz_data = quizzes.get(topic_id, {})
        questions = quiz_data.get("questions", [])
        result[topic_id] = {
            "name": topic_info["name"],
            "subtopics": topic_info["subtopics"],
            "question_count": len(questions),
            "available": len(questions) > 0
        }
    return result


async def generate_quiz_question(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Generate a quiz question.
    
    Note: In production, this would call an LLM or retrieve from a question bank.
    This implementation provides a template structure.
    """
    topic = args["topic"]
    difficulty = args["difficulty"]
    subtopic = args.get("subtopic")
    context = args.get("context", "")
    
    # Generate a unique question ID
    question_hash = hashlib.md5(
        f"{topic}:{difficulty}:{subtopic}:{context}:{random.random()}".encode()
    ).hexdigest()[:12]
    
    # Template questions by topic (in production, use LLM or question bank)
    templates = {
        "sql_basics": {
            "beginner": {
                "question": "Which SQL clause is used to filter results after grouping?",
                "options": ["WHERE", "HAVING", "FILTER", "GROUP BY"],
                "correct_index": 1,
                "explanation": "HAVING filters grouped results, while WHERE filters individual rows before grouping."
            },
            "intermediate": {
                "question": "What is the difference between RANK() and DENSE_RANK() window functions?",
                "options": [
                    "They are identical",
                    "RANK() skips numbers after ties, DENSE_RANK() doesn't",
                    "DENSE_RANK() skips numbers after ties, RANK() doesn't",
                    "RANK() is faster than DENSE_RANK()"
                ],
                "correct_index": 1,
                "explanation": "RANK() assigns the same rank to tied values but skips the next rank(s), while DENSE_RANK() assigns consecutive ranks without gaps."
            },
            "advanced": {
                "question": "In a self-join to find consecutive events, what is the most efficient approach?",
                "options": [
                    "Use CROSS JOIN with WHERE clause",
                    "Use LAG/LEAD window functions",
                    "Use multiple subqueries",
                    "Use UNION ALL"
                ],
                "correct_index": 1,
                "explanation": "LAG/LEAD window functions provide direct access to adjacent rows without the overhead of a self-join, making them more efficient for consecutive event analysis."
            }
        },
        "statistics_probability": {
            "beginner": {
                "question": "What does the p-value represent in hypothesis testing?",
                "options": [
                    "The probability that the null hypothesis is true",
                    "The probability of observing the data given the null hypothesis is true",
                    "The probability of making a Type II error",
                    "The effect size of the test"
                ],
                "correct_index": 1,
                "explanation": "The p-value is the probability of observing results as extreme as (or more extreme than) the observed results, assuming the null hypothesis is true."
            },
            "intermediate": {
                "question": "When is the Central Limit Theorem applicable?",
                "options": [
                    "Only when the population is normally distributed",
                    "When sample size is at least 30 (rule of thumb)",
                    "Only for continuous variables",
                    "When variance is known"
                ],
                "correct_index": 1,
                "explanation": "The CLT states that the sampling distribution of the mean approaches normality as sample size increases, typically n≥30, regardless of the population distribution."
            },
            "advanced": {
                "question": "In Bayesian inference, what does the posterior probability represent?",
                "options": [
                    "The probability before seeing data",
                    "The likelihood of the data",
                    "The updated probability after incorporating evidence",
                    "The marginal probability"
                ],
                "correct_index": 2,
                "explanation": "The posterior probability combines prior beliefs with the likelihood of observed data to provide an updated probability estimate for the hypothesis."
            }
        },
        "ab_testing": {
            "beginner": {
                "question": "What is the primary purpose of randomization in A/B testing?",
                "options": [
                    "To make the test faster",
                    "To eliminate selection bias",
                    "To increase sample size",
                    "To reduce costs"
                ],
                "correct_index": 1,
                "explanation": "Randomization ensures that treatment and control groups are comparable, eliminating selection bias and enabling causal inference."
            },
            "intermediate": {
                "question": "What is 'peeking' in A/B testing and why is it problematic?",
                "options": [
                    "Looking at competitor tests - it's unethical",
                    "Checking results early and stopping when significant - inflates false positive rate",
                    "Using too many metrics - causes confusion",
                    "Running tests too long - wastes resources"
                ],
                "correct_index": 1,
                "explanation": "Peeking refers to repeatedly checking for statistical significance and stopping early. This inflates the false positive rate above the nominal alpha level."
            },
            "advanced": {
                "question": "When should you use CUPED (Controlled-experiment Using Pre-Experiment Data)?",
                "options": [
                    "When you have no historical data",
                    "When you want to reduce variance and detect smaller effects",
                    "When running sequential tests",
                    "When the metric is binary"
                ],
                "correct_index": 1,
                "explanation": "CUPED uses pre-experiment data to reduce variance in your metric estimates, allowing you to detect smaller effects with the same sample size or run shorter experiments."
            }
        },
        "python_data_analysis": {
            "beginner": {
                "question": "Which pandas method removes duplicate rows from a DataFrame?",
                "options": [
                    "df.remove_duplicates()",
                    "df.drop_duplicates()",
                    "df.unique()",
                    "df.deduplicate()"
                ],
                "correct_index": 1,
                "explanation": "df.drop_duplicates() removes duplicate rows. df.unique() is for Series, not DataFrames."
            },
            "intermediate": {
                "question": "What is the difference between df.apply() and df.transform()?",
                "options": [
                    "They are identical",
                    "apply() can change shape, transform() preserves shape",
                    "transform() is faster than apply()",
                    "apply() only works with lambda functions"
                ],
                "correct_index": 1,
                "explanation": "transform() must return a result that is the same size as the input, while apply() can return aggregated results of different shapes."
            },
            "advanced": {
                "question": "When would you use pd.eval() over regular pandas operations?",
                "options": [
                    "For simple single-column operations",
                    "For complex string operations",
                    "For large DataFrames with chained arithmetic operations",
                    "For groupby operations"
                ],
                "correct_index": 2,
                "explanation": "pd.eval() compiles expressions and can be faster for large DataFrames with complex arithmetic operations by avoiding intermediate copies."
            }
        }
    }
    
    # Get template or create placeholder
    topic_templates = templates.get(topic, templates["sql_basics"])
    question_data = topic_templates.get(difficulty, topic_templates["beginner"])
    
    return {
        "question_id": question_hash,
        "question": question_data["question"],
        "options": question_data["options"],
        "correct_index": question_data["correct_index"],
        "explanation": question_data["explanation"],
        "topic": topic,
        "difficulty": difficulty,
        "subtopic": subtopic,
        "related_concepts": TOPICS[topic]["subtopics"][:3]
    }


async def grade_quiz_response(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Grade a user's quiz response."""
    question_text = args["question_text"]
    options = args["options"]
    correct_index = args["correct_index"]
    selected_index = args["selected_index"]
    
    is_correct = selected_index == correct_index
    
    return {
        "is_correct": is_correct,
        "selected_answer": options[selected_index] if 0 <= selected_index < len(options) else "Invalid",
        "correct_answer": options[correct_index],
        "feedback": (
            "Correct! Great job." if is_correct 
            else f"Incorrect. The correct answer is: {options[correct_index]}"
        ),
        "encouragement": (
            "Keep up the excellent work!" if is_correct
            else "Don't worry, mistakes help us learn. Review the explanation and try again."
        )
    }


async def explain_quiz_answer(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Provide detailed explanation for a quiz answer."""
    question = args["question"]
    options = args["options"]
    correct_index = args["correct_index"]
    depth = args.get("depth", "standard")
    
    # Build explanation structure
    explanation = {
        "question": question,
        "correct_answer": options[correct_index],
        "why_correct": f"'{options[correct_index]}' is correct because...",
        "why_others_wrong": [
            f"'{opt}' is incorrect because..." 
            for i, opt in enumerate(options) if i != correct_index
        ]
    }
    
    if depth in ["standard", "comprehensive"]:
        explanation["related_concepts"] = [
            "Consider reviewing these related topics..."
        ]
        explanation["practice_suggestions"] = [
            "Try similar problems focusing on..."
        ]
    
    if depth == "comprehensive":
        explanation["real_world_example"] = "In a real-world scenario at Meta/Google..."
        explanation["common_mistakes"] = [
            "Common mistakes include..."
        ]
        explanation["further_reading"] = [
            "For deeper understanding, see..."
        ]
    
    return explanation


async def get_quiz_by_topic(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Retrieve existing quiz questions from quizzes.yml."""
    topic = args["topic"]
    limit = args.get("limit", 5)
    shuffle = args.get("shuffle", True)
    
    quizzes = config.load_quizzes()
    
    if topic not in quizzes:
        return {
            "error": {
                "code": "TOPIC_NOT_FOUND",
                "message": f"Topic '{topic}' not found in quiz database",
                "available_topics": list(quizzes.keys())
            }
        }
    
    quiz_data = quizzes[topic]
    questions = quiz_data.get("questions", [])
    
    if shuffle:
        questions = random.sample(questions, min(limit, len(questions)))
    else:
        questions = questions[:limit]
    
    return {
        "topic": topic,
        "title": quiz_data.get("title", topic),
        "description": quiz_data.get("description", ""),
        "question_count": len(questions),
        "questions": questions
    }


# Handler registry
TOOL_HANDLERS: dict[str, Callable[[dict[str, Any], Config], Coroutine[Any, Any, dict[str, Any]]]] = {
    "generate_quiz_question": generate_quiz_question,
    "grade_quiz_response": grade_quiz_response,
    "explain_quiz_answer": explain_quiz_answer,
    "get_quiz_by_topic": get_quiz_by_topic,
}

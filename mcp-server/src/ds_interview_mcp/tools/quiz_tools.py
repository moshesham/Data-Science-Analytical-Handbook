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
                        "enum": list(TOPICS.keys()),
                        "description": "Quiz topic to retrieve"
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
    
    # Template questions by topic — each difficulty is a list for variety
    # random.choice() selects one question per call
    templates: dict[str, dict[str, list[dict]]] = {
        "sql_basics": {
            "beginner": [
                {
                    "question": "Which SQL clause is used to filter results after grouping?",
                    "options": ["WHERE", "HAVING", "FILTER", "GROUP BY"],
                    "correct_index": 1,
                    "explanation": "HAVING filters grouped results, while WHERE filters individual rows before grouping."
                },
                {
                    "question": "What does SELECT DISTINCT do?",
                    "options": [
                        "Sorts results alphabetically",
                        "Returns only unique rows",
                        "Filters NULL values",
                        "Limits the number of rows returned"
                    ],
                    "correct_index": 1,
                    "explanation": "SELECT DISTINCT eliminates duplicate rows from the result set, returning only unique combinations of the selected columns."
                },
                {
                    "question": "Which JOIN type returns all rows from the left table and matching rows from the right?",
                    "options": ["INNER JOIN", "RIGHT JOIN", "LEFT JOIN", "FULL OUTER JOIN"],
                    "correct_index": 2,
                    "explanation": "LEFT JOIN (or LEFT OUTER JOIN) returns all rows from the left table and matching rows from the right. Non-matching right rows are filled with NULLs."
                },
            ],
            "intermediate": [
                {
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
                {
                    "question": "What is the correct order of SQL clauses in a SELECT statement?",
                    "options": [
                        "SELECT, FROM, GROUP BY, WHERE, HAVING, ORDER BY",
                        "SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY",
                        "FROM, SELECT, WHERE, GROUP BY, ORDER BY, HAVING",
                        "SELECT, WHERE, FROM, GROUP BY, HAVING, ORDER BY"
                    ],
                    "correct_index": 1,
                    "explanation": "The logical order is SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY. WHERE filters rows before grouping; HAVING filters groups after aggregation."
                },
                {
                    "question": "What does a CTE (Common Table Expression) improve in SQL?",
                    "options": [
                        "Query execution speed",
                        "Index utilization",
                        "Readability and reusability of subqueries",
                        "Memory consumption"
                    ],
                    "correct_index": 2,
                    "explanation": "CTEs (WITH clauses) improve readability by naming complex subqueries so they can be referenced multiple times, making queries easier to understand and maintain."
                },
            ],
            "advanced": [
                {
                    "question": "In a self-join to find consecutive events, what is the most efficient approach?",
                    "options": [
                        "Use CROSS JOIN with WHERE clause",
                        "Use LAG/LEAD window functions",
                        "Use multiple subqueries",
                        "Use UNION ALL"
                    ],
                    "correct_index": 1,
                    "explanation": "LAG/LEAD window functions provide direct access to adjacent rows without the overhead of a self-join, making them more efficient for consecutive event analysis."
                },
                {
                    "question": "What is the purpose of PARTITION BY in a window function?",
                    "options": [
                        "It limits the rows returned",
                        "It divides result rows into groups for the window calculation",
                        "It sorts results within each window",
                        "It creates separate tables for each partition"
                    ],
                    "correct_index": 1,
                    "explanation": "PARTITION BY divides result rows into partitions (groups), and the window function is applied independently within each partition, similar to GROUP BY but without collapsing rows."
                },
            ],
        },
        "statistics_probability": {
            "beginner": [
                {
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
                {
                    "question": "What is the median of the list [3, 1, 4, 1, 5, 9, 2]?",
                    "options": ["3", "3.57", "4", "1"],
                    "correct_index": 0,
                    "explanation": "Sorted: [1,1,2,3,4,5,9]. The middle value (4th of 7) is 3."
                },
                {
                    "question": "Which measure is most resistant to outliers?",
                    "options": ["Mean", "Variance", "Median", "Standard deviation"],
                    "correct_index": 2,
                    "explanation": "The median is the middle value and is not affected by extreme values (outliers), while the mean can be heavily skewed by them."
                },
            ],
            "intermediate": [
                {
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
                {
                    "question": "What does a confidence interval represent?",
                    "options": [
                        "The probability the true parameter is in the interval",
                        "A range constructed by a procedure that captures the true parameter 95% of the time",
                        "The range of all possible sample means",
                        "The probability the sample mean equals the population mean"
                    ],
                    "correct_index": 1,
                    "explanation": "A 95% CI means: if we repeat the sampling process many times, 95% of the constructed intervals will contain the true parameter. It's a property of the procedure, not the specific interval."
                },
                {
                    "question": "If you run 20 independent hypothesis tests at α=0.05 and all H0 are true, how many false positives do you expect?",
                    "options": ["0", "1", "5", "20"],
                    "correct_index": 1,
                    "explanation": "With α=0.05, each test has a 5% chance of a false positive. Over 20 tests: 20 × 0.05 = 1 expected false positive. This is why multiple testing correction (e.g., Bonferroni) matters."
                },
            ],
            "advanced": [
                {
                    "question": "In Bayesian inference, what does the posterior probability represent?",
                    "options": [
                        "The probability before seeing data",
                        "The likelihood of the data",
                        "The updated probability after incorporating evidence",
                        "The marginal probability"
                    ],
                    "correct_index": 2,
                    "explanation": "The posterior probability combines prior beliefs with the likelihood of observed data to provide an updated probability estimate for the hypothesis."
                },
                {
                    "question": "What is the difference between a Type I and Type II error in A/B testing?",
                    "options": [
                        "Type I: missing a real effect. Type II: detecting a false effect.",
                        "Type I: detecting a false effect (false positive). Type II: missing a real effect (false negative).",
                        "Type I errors are more serious than Type II errors always.",
                        "They are the same thing expressed differently."
                    ],
                    "correct_index": 1,
                    "explanation": "Type I error (α) = false positive (reject H0 when it's true). Type II error (β) = false negative (fail to reject H0 when it's false). Power = 1 - β."
                },
            ],
        },
        "ab_testing": {
            "beginner": [
                {
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
                {
                    "question": "What is meant by 'statistical significance' in an A/B test?",
                    "options": [
                        "The effect is large enough to matter for the business",
                        "The result is unlikely to be due to random chance alone",
                        "The experiment ran long enough",
                        "Both variants had equal sample sizes"
                    ],
                    "correct_index": 1,
                    "explanation": "Statistical significance means the observed result is unlikely to occur by random chance (p < α). It says nothing about the practical/business importance of the effect — that's 'practical significance'."
                },
            ],
            "intermediate": [
                {
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
                {
                    "question": "What is the 'novelty effect' in A/B testing?",
                    "options": [
                        "When a new feature attracts users who've never used the product",
                        "When users engage more with a new feature simply because it's new, not because it's better",
                        "When the experiment design is novel and untested",
                        "When the sample size is too small to detect effects"
                    ],
                    "correct_index": 1,
                    "explanation": "The novelty effect causes inflated initial engagement because users explore new features out of curiosity. Over time, engagement typically returns to baseline, making it important to run tests long enough."
                },
                {
                    "question": "You run an A/B test and get p=0.04. What is the correct interpretation?",
                    "options": [
                        "There's a 96% chance the treatment is better than control",
                        "There's a 4% probability of seeing this result (or more extreme) if H0 is true",
                        "The null hypothesis has a 4% chance of being correct",
                        "The experiment should be stopped and results declared significant"
                    ],
                    "correct_index": 1,
                    "explanation": "p=0.04 means: if the null hypothesis were true, there's a 4% chance of observing a result this extreme or more extreme. It does NOT mean H0 has 4% probability of being true."
                },
            ],
            "advanced": [
                {
                    "question": "When should you use CUPED (Controlled-experiment Using Pre-Experiment Data)?",
                    "options": [
                        "When you have no historical data",
                        "When you want to reduce variance and detect smaller effects",
                        "When running sequential tests",
                        "When the metric is binary"
                    ],
                    "correct_index": 1,
                    "explanation": "CUPED uses pre-experiment data to reduce variance in your metric estimates, allowing you to detect smaller effects with the same sample size or run shorter experiments."
                },
                {
                    "question": "What is 'network interference' (SUTVA violation) in A/B testing?",
                    "options": [
                        "When the test runs on a slow network connection",
                        "When a user in control is affected by treatment users' behavior, violating independence",
                        "When the randomization algorithm has a network bug",
                        "When multiple tests run simultaneously on the same users"
                    ],
                    "correct_index": 1,
                    "explanation": "SUTVA (Stable Unit Treatment Value Assumption) requires that one unit's outcome is unaffected by another's treatment. In social networks or marketplaces, this is violated when treatment users influence control users (e.g., viral features, liquidity effects)."
                },
            ],
        },
        "python_data_analysis": {
            "beginner": [
                {
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
                {
                    "question": "How do you select rows where column 'age' is greater than 30 in pandas?",
                    "options": [
                        "df.filter(df['age'] > 30)",
                        "df[df['age'] > 30]",
                        "df.where('age > 30')",
                        "df.select(age > 30)"
                    ],
                    "correct_index": 1,
                    "explanation": "Boolean indexing df[df['age'] > 30] is the standard pandas approach. It creates a boolean mask and filters the DataFrame."
                },
            ],
            "intermediate": [
                {
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
                {
                    "question": "What does df.merge(left, right, how='left') do?",
                    "options": [
                        "Returns only rows that match in both DataFrames",
                        "Returns all rows from 'left' and matching rows from 'right' (NaN for non-matches)",
                        "Returns all rows from 'right' with left data where available",
                        "Returns all rows from both DataFrames"
                    ],
                    "correct_index": 1,
                    "explanation": "A left merge keeps all rows from the left DataFrame and brings in matching rows from the right. Unmatched right rows produce NaN in the result."
                },
            ],
            "advanced": [
                {
                    "question": "When would you use pd.eval() over regular pandas operations?",
                    "options": [
                        "For simple single-column operations",
                        "For complex string operations",
                        "For large DataFrames with chained arithmetic operations",
                        "For groupby operations"
                    ],
                    "correct_index": 2,
                    "explanation": "pd.eval() compiles expressions and can be faster for large DataFrames with complex arithmetic operations by avoiding intermediate copies."
                },
                {
                    "question": "What is the most memory-efficient way to read a large CSV file in pandas that doesn't fit in RAM?",
                    "options": [
                        "pd.read_csv() with dtype optimization",
                        "Using chunksize parameter to read in batches",
                        "Convert to parquet first",
                        "Use numpy.loadtxt() instead"
                    ],
                    "correct_index": 1,
                    "explanation": "pd.read_csv(filepath, chunksize=N) returns an iterator of DataFrames that can be processed in batches, allowing you to handle files larger than available RAM."
                },
            ],
        },
        "product_metrics": {
            "beginner": [
                {
                    "question": "What is DAU/MAU ratio and what does it indicate?",
                    "options": [
                        "Daily Active Users divided by Monthly Active Users — measures user stickiness",
                        "Daily App Users divided by Monthly App Updates",
                        "Data Analytics Unit divided by Marketing Analytics Unit",
                        "A ratio used only in gaming apps"
                    ],
                    "correct_index": 0,
                    "explanation": "DAU/MAU (stickiness ratio) measures how often monthly users return daily. A value of 0.5 (50%) means half of monthly active users return each day. Facebook historically targets >60%."
                },
                {
                    "question": "What is a 'North Star Metric'?",
                    "options": [
                        "The highest revenue metric",
                        "The single metric that best captures the core value delivered to customers",
                        "A metric that is always increasing",
                        "The metric used for executive reporting"
                    ],
                    "correct_index": 1,
                    "explanation": "The North Star Metric (NSM) is the single metric that best captures the core value the product delivers. For Airbnb it's 'nights booked', for Spotify it's 'time spent listening'. It aligns all teams around what truly matters."
                },
                {
                    "question": "How is Monthly Churn Rate typically calculated?",
                    "options": [
                        "(New customers / Starting customers) × 100",
                        "(Lost customers in month / Starting customers) × 100",
                        "(Active customers / Total customers) × 100",
                        "Revenue lost × 100 / Total revenue"
                    ],
                    "correct_index": 1,
                    "explanation": "Monthly churn rate = (customers lost in the month / customers at start of month) × 100. It represents the percentage of users who stopped using the product in a given period."
                },
            ],
            "intermediate": [
                {
                    "question": "What is LTV (Customer Lifetime Value) and how is it commonly calculated?",
                    "options": [
                        "LTV = Monthly Revenue × Churn Rate",
                        "LTV = Average Revenue Per User / Churn Rate",
                        "LTV = Total Revenue / Total Users",
                        "LTV = Acquisition Cost × Retention Rate"
                    ],
                    "correct_index": 1,
                    "explanation": "LTV = ARPU / Churn Rate is the simplified formula for constant revenue streams. E.g., if ARPU = $10/month and monthly churn = 5%, then LTV = $10 / 0.05 = $200. More complex versions use discounted cash flows."
                },
                {
                    "question": "A product's D30 retention dropped from 25% to 20% MoM. What is the first analysis you'd do?",
                    "options": [
                        "Immediately A/B test a new onboarding flow",
                        "Segment by cohort date to determine when the drop started",
                        "Compare to competitor benchmarks",
                        "Check if the metric definition changed"
                    ],
                    "correct_index": 1,
                    "explanation": "Cohort analysis isolates whether the drop affects all historical cohorts (suggesting a product/experience change) or only recent cohorts (suggesting an acquisition quality issue or new user experience change)."
                },
                {
                    "question": "What is the difference between 'leading' and 'lagging' indicators?",
                    "options": [
                        "Leading indicators are faster to compute",
                        "Leading indicators predict future outcomes; lagging indicators confirm past results",
                        "Lagging indicators are more important for product decisions",
                        "They are the same but named differently by different companies"
                    ],
                    "correct_index": 1,
                    "explanation": "Leading indicators (feature adoption, engagement actions) predict future business outcomes. Lagging indicators (revenue, retention) confirm what already happened. Leading indicators allow proactive intervention; lagging indicators measure outcomes."
                },
            ],
            "advanced": [
                {
                    "question": "What is 'Simpson's Paradox' in product analytics?",
                    "options": [
                        "When a metric improves daily but declines monthly",
                        "When an aggregate trend is reversed when data is segmented",
                        "When A/B test results conflict across platforms",
                        "When two metrics are inversely correlated"
                    ],
                    "correct_index": 1,
                    "explanation": "Simpson's Paradox occurs when a trend present in aggregate disappears or reverses when data is segmented. Classic example: overall conversion rate improves, but decreases for both desktop and mobile users individually — because the mix shifted toward a higher-converting channel."
                },
                {
                    "question": "When should you use ratio metrics vs. absolute metrics in an A/B test?",
                    "options": [
                        "Always use absolute metrics because they're more intuitive",
                        "Use ratio metrics when sample sizes differ between groups; absolute when they're equal",
                        "Prefer ratio metrics (rates/averages) as the primary metric; use absolute for guardrails",
                        "Ratio metrics are only valid for revenue experiments"
                    ],
                    "correct_index": 2,
                    "explanation": "Ratio metrics (e.g., conversion rate, revenue per user) are preferred as primary metrics because they normalize for sample size differences. Absolute metrics (total revenue, total conversions) are useful guardrails but shouldn't be primary as they're affected by traffic allocation."
                },
            ],
        },
        "case_studies": {
            "beginner": [
                {
                    "question": "You notice Instagram Stories engagement dropped 20% last week. What is your FIRST step?",
                    "options": [
                        "Immediately A/B test a new design",
                        "Check if the data pipeline or logging is broken",
                        "Alert the engineering team to roll back recent changes",
                        "Segment by user demographics"
                    ],
                    "correct_index": 1,
                    "explanation": "Always rule out data/instrumentation issues first (metric definition changes, logging bugs, ETL failures). A 20% drop is large enough that a data quality issue is plausible and must be eliminated before spending time on product hypotheses."
                },
                {
                    "question": "What framework helps structure a product metrics investigation?",
                    "options": [
                        "MECE (Mutually Exclusive, Collectively Exhaustive)",
                        "STAR (Situation, Task, Action, Result)",
                        "OSI model",
                        "RACI matrix"
                    ],
                    "correct_index": 0,
                    "explanation": "MECE is the core framework for data decomposition: break the metric into non-overlapping parts that together cover the full picture. E.g., revenue = users × conversion rate × avg order value. Each piece can be examined independently."
                },
            ],
            "intermediate": [
                {
                    "question": "A new feature launches and revenue goes up 5%, but user satisfaction scores drop. How do you resolve this conflict?",
                    "options": [
                        "Revenue is the only metric that matters; ship it",
                        "Satisfaction scores matter more; roll it back",
                        "Investigate the causal chain — which user segments drove revenue up, and what drove satisfaction down",
                        "Run a longer test until the metrics converge"
                    ],
                    "correct_index": 2,
                    "explanation": "Conflicting signals require deeper investigation: Who is generating the revenue increase? Who is expressing dissatisfaction? If high-value users are happy but casual users are not, the calculus differs from the reverse. Always seek to understand the mechanism."
                },
                {
                    "question": "Your team wants to measure success of a new search algorithm. Which metric hierarchy is best?",
                    "options": [
                        "Primary: number of searches. Secondary: time spent on results page.",
                        "Primary: click-through rate on first result. Secondary: search satisfaction survey.",
                        "Primary: task success rate + query success rate. Secondary: clicks, time-to-click, pogo-sticking. Guardrail: search volume.",
                        "Primary: revenue per search. Secondary: DAU."
                    ],
                    "correct_index": 2,
                    "explanation": "Good metric hierarchies layer task-level success metrics (did user find what they needed?) → behavioral proxies (click patterns) → guardrails (don't drop overall search usage). This captures both quality and safety signals."
                },
            ],
            "advanced": [
                {
                    "question": "Uber's surge pricing A/B test shows +15% driver supply but -8% rider demand. How do you make the launch decision?",
                    "options": [
                        "Don't launch — rider demand drop is unacceptable",
                        "Launch — driver supply improvement is the North Star",
                        "Model the marketplace equilibrium: determine if the supply gain matches excess demand during surges, and net impact on completed rides and GMV",
                        "Run a longer test to see if demand recovers"
                    ],
                    "correct_index": 2,
                    "explanation": "Marketplace experiments require modeling both sides. The right question is: does the supply increase fill the gap created by demand drop, leading to more completed trips? If GMV and completion rate improve despite rider demand drop, the marketplace is more efficient, which is positive."
                },
                {
                    "question": "What is 'holdout testing' and when should you use it?",
                    "options": [
                        "Holding out a random sample of users from ALL experiments to measure cumulative experiment effect",
                        "Holding features back from the public for competitive reasons",
                        "Testing a product only in specific geographic holdout regions",
                        "Running a test with a very small treatment group to minimize risk"
                    ],
                    "correct_index": 0,
                    "explanation": "A holdout group is a set of users excluded from all experiments. By comparing holdout vs. non-holdout outcomes over time, you can measure the true cumulative impact of all product changes — important for detecting long-term effects that individual A/B tests miss."
                },
            ],
        },
    }

    # Select a question: use the topic (fallback to sql_basics), then difficulty (fallback to beginner)
    topic_templates = templates.get(topic, templates["sql_basics"])
    question_pool = topic_templates.get(difficulty, topic_templates.get("beginner", []))
    if not question_pool:
        # Final fallback: any difficulty from this topic
        for diff_questions in topic_templates.values():
            if diff_questions:
                question_pool = diff_questions
                break
    question_data = random.choice(question_pool)

    return {
        "question_id": question_hash,
        "question": question_data["question"],
        "options": question_data["options"],
        "correct_index": question_data["correct_index"],
        "explanation": question_data["explanation"],
        "topic": topic,
        "difficulty": difficulty,
        "subtopic": subtopic,
        "related_concepts": TOPICS.get(topic, TOPICS["sql_basics"])["subtopics"][:3]
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

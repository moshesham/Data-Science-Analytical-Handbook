"""SQL validation and explanation tools."""

import re
from typing import Any, Callable, Coroutine

import sqlparse
from mcp.types import Tool

from ds_interview_mcp.config import Config


def get_tool_definitions() -> list[Tool]:
    """Return SQL tool definitions."""
    return [
        Tool(
            name="validate_sql_query",
            description="Validate SQL query syntax and check for common errors, anti-patterns, and potential performance issues.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The SQL query to validate"
                    },
                    "dialect": {
                        "type": "string",
                        "enum": ["postgresql", "mysql", "sqlite", "bigquery", "snowflake"],
                        "default": "postgresql"
                    },
                    "schema_context": {
                        "type": "object",
                        "description": "Optional table schema for semantic validation"
                    },
                    "check_performance": {
                        "type": "boolean",
                        "default": False
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="explain_sql_query",
            description="Explain what a SQL query does, step by step, in plain language.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "detail_level": {
                        "type": "string",
                        "enum": ["beginner", "intermediate", "advanced"],
                        "default": "intermediate"
                    },
                    "include_execution_order": {
                        "type": "boolean",
                        "default": True
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="generate_sql_problem",
            description="Generate a SQL practice problem with table schemas and expected output.",
            inputSchema={
                "type": "object",
                "properties": {
                    "difficulty": {
                        "type": "string",
                        "enum": ["easy", "medium", "hard"]
                    },
                    "topics": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["joins", "aggregations", "window_functions", "subqueries", "ctes", "self_joins", "date_functions", "string_functions"]
                        }
                    },
                    "domain": {
                        "type": "string",
                        "enum": ["social_media", "ecommerce", "fintech", "healthcare", "generic"],
                        "default": "social_media"
                    },
                    "include_solution": {"type": "boolean", "default": False},
                    "include_hints": {"type": "boolean", "default": True}
                },
                "required": ["difficulty", "topics"]
            }
        ),
        Tool(
            name="optimize_sql_query",
            description="Analyze a SQL query and suggest performance optimizations.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "table_sizes": {
                        "type": "object",
                        "description": "Approximate row counts"
                    },
                    "existing_indexes": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["query"]
            }
        )
    ]


# Common SQL anti-patterns
ANTI_PATTERNS = [
    {
        "pattern": r"SELECT\s+\*",
        "message": "Avoid SELECT * in production queries - specify columns explicitly",
        "severity": "warning"
    },
    {
        "pattern": r"NOT\s+IN\s*\([^)]*SELECT",
        "message": "NOT IN with subquery can behave unexpectedly with NULLs - consider NOT EXISTS",
        "severity": "warning"
    },
    {
        "pattern": r"WHERE\s+\w+\s*!=\s*NULL|WHERE\s+\w+\s*<>\s*NULL",
        "message": "Use IS NOT NULL instead of != NULL or <> NULL",
        "severity": "error"
    },
    {
        "pattern": r"WHERE\s+\w+\s*=\s*NULL",
        "message": "Use IS NULL instead of = NULL",
        "severity": "error"
    },
    {
        "pattern": r"ORDER\s+BY\s+\d+",
        "message": "Avoid ORDER BY column position - use column names for clarity",
        "severity": "warning"
    },
    {
        "pattern": r"HAVING\s+(?!.*\b(COUNT|SUM|AVG|MIN|MAX)\b)",
        "message": "HAVING without aggregate - consider using WHERE instead",
        "severity": "warning"
    },
]

# SQL execution order for explanations
EXECUTION_ORDER = [
    ("FROM/JOIN", "Tables are combined and joined"),
    ("WHERE", "Rows are filtered before grouping"),
    ("GROUP BY", "Rows are grouped together"),
    ("HAVING", "Groups are filtered"),
    ("SELECT", "Columns are computed and selected"),
    ("DISTINCT", "Duplicate rows are removed"),
    ("ORDER BY", "Results are sorted"),
    ("LIMIT/OFFSET", "Results are limited"),
]


async def validate_sql_query(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Validate a SQL query for syntax and common issues."""
    query = args["query"]
    dialect = args.get("dialect", "postgresql")
    check_performance = args.get("check_performance", False)
    
    errors = []
    warnings = []
    suggestions = []
    performance_notes = []
    
    # Check query length
    if len(query) > config.max_query_length:
        errors.append({
            "type": "LENGTH_ERROR",
            "message": f"Query exceeds maximum length of {config.max_query_length} characters"
        })
        return {"is_valid": False, "errors": errors}
    
    # Parse with sqlparse
    try:
        parsed = sqlparse.parse(query)
        if not parsed or not parsed[0].tokens:
            errors.append({
                "type": "PARSE_ERROR",
                "message": "Unable to parse SQL query"
            })
    except Exception as e:
        errors.append({
            "type": "PARSE_ERROR",
            "message": f"SQL parsing failed: {str(e)}"
        })
    
    # Check for anti-patterns
    for pattern_def in ANTI_PATTERNS:
        if re.search(pattern_def["pattern"], query, re.IGNORECASE):
            item = {
                "type": pattern_def["severity"].upper(),
                "message": pattern_def["message"]
            }
            if pattern_def["severity"] == "error":
                errors.append(item)
            else:
                warnings.append(pattern_def["message"])
    
    # Basic syntax checks
    query_upper = query.upper()
    
    # Check for unmatched parentheses
    if query.count('(') != query.count(')'):
        errors.append({
            "type": "SYNTAX_ERROR",
            "message": "Unmatched parentheses"
        })
    
    # Check for common clause presence
    if "SELECT" not in query_upper and "INSERT" not in query_upper and "UPDATE" not in query_upper and "DELETE" not in query_upper:
        errors.append({
            "type": "SYNTAX_ERROR",
            "message": "Query missing primary statement (SELECT, INSERT, UPDATE, DELETE)"
        })
    
    # Performance checks
    if check_performance:
        # Check for LIKE with leading wildcard
        if re.search(r"LIKE\s*'%[^%]", query, re.IGNORECASE):
            performance_notes.append("LIKE with leading wildcard prevents index usage")
        
        # Check for functions on indexed columns in WHERE
        if re.search(r"WHERE\s+\w+\s*\([^)]*\)\s*=", query, re.IGNORECASE):
            performance_notes.append("Functions in WHERE clause may prevent index usage")
        
        # Check for OR conditions
        if re.search(r"WHERE.*\bOR\b", query, re.IGNORECASE):
            performance_notes.append("OR conditions can prevent index optimization - consider UNION")
        
        # Check for missing LIMIT
        if "SELECT" in query_upper and "LIMIT" not in query_upper and "TOP" not in query_upper:
            suggestions.append("Consider adding LIMIT to prevent fetching too many rows")
    
    # Suggestions based on query structure
    if "GROUP BY" in query_upper and "HAVING" not in query_upper:
        suggestions.append("Consider using HAVING to filter grouped results if needed")
    
    if re.search(r"JOIN.*JOIN.*JOIN", query, re.IGNORECASE):
        suggestions.append("Multiple JOINs detected - ensure proper indexing on join columns")
    
    is_valid = len(errors) == 0
    
    return {
        "is_valid": is_valid,
        "errors": errors,
        "warnings": warnings,
        "suggestions": suggestions,
        "performance_notes": performance_notes if check_performance else [],
        "query_formatted": sqlparse.format(query, reindent=True, keyword_case='upper')
    }


async def explain_sql_query(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Explain a SQL query in plain language."""
    query = args["query"]
    detail_level = args.get("detail_level", "intermediate")
    include_execution_order = args.get("include_execution_order", True)
    
    # Parse the query
    parsed = sqlparse.parse(query)
    if not parsed:
        return {"error": "Unable to parse query"}
    
    statement = parsed[0]
    
    # Extract key components
    components = {
        "type": statement.get_type(),
        "tables": [],
        "columns": [],
        "conditions": [],
        "aggregations": [],
        "has_groupby": False,
        "has_orderby": False,
        "has_limit": False,
    }
    
    query_upper = query.upper()
    
    # Detect features
    components["has_groupby"] = "GROUP BY" in query_upper
    components["has_orderby"] = "ORDER BY" in query_upper
    components["has_limit"] = "LIMIT" in query_upper or "TOP" in query_upper
    
    # Detect window functions
    has_window = any(fn in query_upper for fn in ["ROW_NUMBER(", "RANK(", "DENSE_RANK(", "LAG(", "LEAD(", "OVER("])
    
    # Detect CTEs
    has_cte = query_upper.strip().startswith("WITH")
    
    # Build explanation
    explanation = {
        "summary": f"This is a {components['type']} query",
        "components": []
    }
    
    # Add component explanations based on detail level
    if has_cte:
        explanation["components"].append({
            "clause": "WITH (CTE)",
            "description": "Creates a temporary named result set (Common Table Expression) that can be referenced in the main query"
        })
    
    if "SELECT" in query_upper:
        explanation["components"].append({
            "clause": "SELECT",
            "description": "Specifies which columns to retrieve from the data"
        })
    
    if "FROM" in query_upper:
        explanation["components"].append({
            "clause": "FROM",
            "description": "Specifies the source table(s) for the data"
        })
    
    if any(join in query_upper for join in ["JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"]):
        join_type = "INNER JOIN" if "INNER JOIN" in query_upper else \
                   "LEFT JOIN" if "LEFT JOIN" in query_upper else \
                   "RIGHT JOIN" if "RIGHT JOIN" in query_upper else \
                   "FULL JOIN" if "FULL JOIN" in query_upper else "JOIN"
        explanation["components"].append({
            "clause": join_type,
            "description": f"Combines rows from multiple tables based on a related column"
        })
    
    if "WHERE" in query_upper:
        explanation["components"].append({
            "clause": "WHERE",
            "description": "Filters rows before any grouping occurs"
        })
    
    if components["has_groupby"]:
        explanation["components"].append({
            "clause": "GROUP BY",
            "description": "Groups rows that have the same values into summary rows"
        })
    
    if "HAVING" in query_upper:
        explanation["components"].append({
            "clause": "HAVING",
            "description": "Filters groups after GROUP BY is applied (unlike WHERE which filters rows)"
        })
    
    if has_window:
        explanation["components"].append({
            "clause": "Window Functions",
            "description": "Performs calculations across a set of rows while preserving individual row data"
        })
    
    if components["has_orderby"]:
        explanation["components"].append({
            "clause": "ORDER BY",
            "description": "Sorts the result set by specified column(s)"
        })
    
    if components["has_limit"]:
        explanation["components"].append({
            "clause": "LIMIT",
            "description": "Restricts the number of rows returned"
        })
    
    # Add execution order if requested
    if include_execution_order:
        explanation["execution_order"] = [
            {"step": i + 1, "clause": clause, "description": desc}
            for i, (clause, desc) in enumerate(EXECUTION_ORDER)
            if clause.split('/')[0] in query_upper or (clause == "DISTINCT" and "DISTINCT" in query_upper)
        ]
    
    # Add detail-level specific content
    if detail_level == "advanced":
        explanation["optimization_notes"] = [
            "Consider index usage on columns in WHERE and JOIN conditions",
            "Aggregate functions process after WHERE filtering",
            "Window functions run after most other processing"
        ]
    
    return explanation


async def generate_sql_problem(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Generate a SQL practice problem."""
    difficulty = args["difficulty"]
    topics = args["topics"]
    domain = args.get("domain", "social_media")
    include_solution = args.get("include_solution", False)
    include_hints = args.get("include_hints", True)
    
    # Domain-specific table schemas
    schemas = {
        "social_media": {
            "users": [
                {"column": "user_id", "type": "INT PRIMARY KEY"},
                {"column": "username", "type": "VARCHAR(50)"},
                {"column": "email", "type": "VARCHAR(100)"},
                {"column": "created_at", "type": "TIMESTAMP"},
                {"column": "country", "type": "VARCHAR(50)"},
            ],
            "posts": [
                {"column": "post_id", "type": "INT PRIMARY KEY"},
                {"column": "user_id", "type": "INT REFERENCES users"},
                {"column": "content", "type": "TEXT"},
                {"column": "created_at", "type": "TIMESTAMP"},
                {"column": "likes_count", "type": "INT"},
            ],
            "engagement": [
                {"column": "engagement_id", "type": "INT PRIMARY KEY"},
                {"column": "user_id", "type": "INT REFERENCES users"},
                {"column": "post_id", "type": "INT REFERENCES posts"},
                {"column": "action_type", "type": "VARCHAR(20)"},
                {"column": "created_at", "type": "TIMESTAMP"},
            ],
        },
        "ecommerce": {
            "customers": [
                {"column": "customer_id", "type": "INT PRIMARY KEY"},
                {"column": "email", "type": "VARCHAR(100)"},
                {"column": "signup_date", "type": "DATE"},
                {"column": "country", "type": "VARCHAR(50)"},
            ],
            "orders": [
                {"column": "order_id", "type": "INT PRIMARY KEY"},
                {"column": "customer_id", "type": "INT REFERENCES customers"},
                {"column": "order_date", "type": "TIMESTAMP"},
                {"column": "total_amount", "type": "DECIMAL(10,2)"},
                {"column": "status", "type": "VARCHAR(20)"},
            ],
            "products": [
                {"column": "product_id", "type": "INT PRIMARY KEY"},
                {"column": "name", "type": "VARCHAR(100)"},
                {"column": "category", "type": "VARCHAR(50)"},
                {"column": "price", "type": "DECIMAL(10,2)"},
            ],
        }
    }
    
    # Problem templates by difficulty and topic
    problems = {
        ("easy", "joins"): {
            "title": "User Post Count",
            "description": "Write a query to find the total number of posts for each user. Include users who have no posts.",
            "expected_output": "user_id | username | post_count",
            "hints": ["Use LEFT JOIN to include users without posts", "COUNT with GROUP BY"],
            "solution": """
SELECT u.user_id, u.username, COUNT(p.post_id) as post_count
FROM users u
LEFT JOIN posts p ON u.user_id = p.user_id
GROUP BY u.user_id, u.username
ORDER BY post_count DESC;
"""
        },
        ("medium", "window_functions"): {
            "title": "Ranking Users by Engagement",
            "description": "Write a query to rank users by their total engagement count within each country. Include the rank and the engagement count.",
            "expected_output": "user_id | country | engagement_count | country_rank",
            "hints": ["Use COUNT with GROUP BY first", "Apply RANK() or DENSE_RANK() with PARTITION BY country"],
            "solution": """
WITH user_engagement AS (
    SELECT u.user_id, u.country, COUNT(e.engagement_id) as engagement_count
    FROM users u
    LEFT JOIN engagement e ON u.user_id = e.user_id
    GROUP BY u.user_id, u.country
)
SELECT 
    user_id,
    country,
    engagement_count,
    RANK() OVER (PARTITION BY country ORDER BY engagement_count DESC) as country_rank
FROM user_engagement;
"""
        },
        ("hard", "ctes"): {
            "title": "User Retention Analysis",
            "description": "Calculate the 7-day retention rate: the percentage of users who engaged again within 7 days of their first engagement. Group by signup month.",
            "expected_output": "signup_month | total_users | retained_users | retention_rate",
            "hints": [
                "First CTE: Find each user's first engagement date",
                "Second CTE: Check if user engaged again within 7 days",
                "Use DATE_TRUNC for monthly grouping"
            ],
            "solution": """
WITH first_engagement AS (
    SELECT user_id, MIN(created_at) as first_date
    FROM engagement
    GROUP BY user_id
),
retained AS (
    SELECT DISTINCT fe.user_id
    FROM first_engagement fe
    JOIN engagement e ON fe.user_id = e.user_id
    WHERE e.created_at > fe.first_date 
    AND e.created_at <= fe.first_date + INTERVAL '7 days'
)
SELECT 
    DATE_TRUNC('month', u.created_at) as signup_month,
    COUNT(DISTINCT u.user_id) as total_users,
    COUNT(DISTINCT r.user_id) as retained_users,
    ROUND(100.0 * COUNT(DISTINCT r.user_id) / COUNT(DISTINCT u.user_id), 2) as retention_rate
FROM users u
LEFT JOIN first_engagement fe ON u.user_id = fe.user_id
LEFT JOIN retained r ON u.user_id = r.user_id
WHERE fe.first_date IS NOT NULL
GROUP BY DATE_TRUNC('month', u.created_at)
ORDER BY signup_month;
"""
        }
    }
    
    # Select appropriate problem
    topic = topics[0] if topics else "joins"
    problem_key = (difficulty, topic)
    
    # Fallback to a default if exact match not found
    if problem_key not in problems:
        problem_key = ("medium", "joins")
    
    problem = problems[problem_key]
    schema = schemas.get(domain, schemas["social_media"])
    
    result = {
        "title": problem["title"],
        "difficulty": difficulty,
        "topics": topics,
        "domain": domain,
        "description": problem["description"],
        "schema": schema,
        "expected_output": problem["expected_output"],
    }
    
    if include_hints:
        result["hints"] = problem["hints"]
    
    if include_solution:
        result["solution"] = problem["solution"].strip()
    
    return result


async def optimize_sql_query(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Analyze and suggest optimizations for a SQL query."""
    query = args["query"]
    table_sizes = args.get("table_sizes", {})
    existing_indexes = args.get("existing_indexes", [])
    
    suggestions = []
    index_recommendations = []
    
    query_upper = query.upper()
    
    # Check for SELECT *
    if "SELECT *" in query.upper():
        suggestions.append({
            "type": "SELECT_STAR",
            "severity": "medium",
            "message": "Replace SELECT * with specific columns to reduce data transfer",
            "impact": "Can significantly reduce query time for wide tables"
        })
    
    # Check for functions on columns in WHERE
    if re.search(r"WHERE.*\b(UPPER|LOWER|DATE|EXTRACT|YEAR|MONTH)\s*\(", query_upper):
        suggestions.append({
            "type": "FUNCTION_IN_WHERE",
            "severity": "high",
            "message": "Functions on columns in WHERE prevent index usage",
            "fix": "Consider creating a functional index or restructuring the query"
        })
    
    # Check for LIKE with leading wildcard
    if re.search(r"LIKE\s*'%", query, re.IGNORECASE):
        suggestions.append({
            "type": "LEADING_WILDCARD",
            "severity": "high",
            "message": "LIKE with leading wildcard prevents index usage",
            "fix": "Consider full-text search or reversing the string for trailing matches"
        })
    
    # Check for OR conditions
    if re.search(r"\bWHERE\b.*\bOR\b", query_upper):
        suggestions.append({
            "type": "OR_CONDITION",
            "severity": "medium",
            "message": "OR conditions can prevent optimal index usage",
            "fix": "Consider using UNION or UNION ALL for better performance"
        })
    
    # Check for missing indexes on JOIN columns
    join_columns = re.findall(r"ON\s+\w+\.(\w+)\s*=\s*\w+\.(\w+)", query_upper)
    for col1, col2 in join_columns:
        index_recommendations.append({
            "columns": [col1, col2],
            "reason": "Columns used in JOIN condition"
        })
    
    # Check for subqueries that could be JOINs
    if re.search(r"WHERE\s+\w+\s+IN\s*\(\s*SELECT", query_upper):
        suggestions.append({
            "type": "SUBQUERY_TO_JOIN",
            "severity": "medium",
            "message": "Subquery in WHERE could potentially be rewritten as JOIN",
            "impact": "JOINs are often more efficiently optimized"
        })
    
    # Check for ORDER BY without LIMIT
    if "ORDER BY" in query_upper and "LIMIT" not in query_upper:
        suggestions.append({
            "type": "ORDER_WITHOUT_LIMIT",
            "severity": "low",
            "message": "ORDER BY without LIMIT sorts entire result set",
            "fix": "Add LIMIT if you don't need all rows"
        })
    
    # Check for DISTINCT
    if "DISTINCT" in query_upper:
        suggestions.append({
            "type": "DISTINCT_CHECK",
            "severity": "low",
            "message": "DISTINCT adds sorting overhead",
            "fix": "Verify if DISTINCT is necessary or if query can be restructured"
        })
    
    # Format the optimized query
    formatted_query = sqlparse.format(query, reindent=True, keyword_case='upper')
    
    return {
        "original_query": query,
        "formatted_query": formatted_query,
        "suggestions": suggestions,
        "index_recommendations": index_recommendations,
        "summary": {
            "high_priority": len([s for s in suggestions if s.get("severity") == "high"]),
            "medium_priority": len([s for s in suggestions if s.get("severity") == "medium"]),
            "low_priority": len([s for s in suggestions if s.get("severity") == "low"])
        }
    }


# Handler registry
TOOL_HANDLERS: dict[str, Callable[[dict[str, Any], Config], Coroutine[Any, Any, dict[str, Any]]]] = {
    "validate_sql_query": validate_sql_query,
    "explain_sql_query": explain_sql_query,
    "generate_sql_problem": generate_sql_problem,
    "optimize_sql_query": optimize_sql_query,
}

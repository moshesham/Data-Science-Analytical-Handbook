# DS Interview Prep MCP Server - Design Document

**Version:** 1.0.0  
**Status:** Design Draft  
**Last Updated:** March 2026

## Executive Summary

This document describes a custom MCP (Model Context Protocol) server designed specifically for the Data Science Analytical Interview Preparation Handbook. The server provides AI-enhanced tools for learning, practice problem generation, quiz creation, SQL validation, and content generation.

---

## System Overview

### Purpose
The DS Interview Prep MCP Server augments the learning platform with intelligent tools that:
- Generate personalized quiz questions
- Validate and explain SQL queries
- Create A/B testing scenarios
- Generate interview questions with solutions
- Review analytics code
- Create case study content

### Why MCP?
MCP provides a standardized protocol for AI tool integration, enabling:
- Consistent tool interfaces across AI assistants
- Type-safe tool definitions with JSON schemas
- Easy integration with VS Code, Cursor, and other IDEs
- Reusable tools across different AI backends

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          Client Applications                             │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────────────────┐     │
│   │  VS Code    │    │  Streamlit  │    │  CLI / Jupyter          │     │
│   │  Copilot    │    │  App        │    │  Notebooks              │     │
│   └──────┬──────┘    └──────┬──────┘    └───────────┬─────────────┘     │
│          │                  │                       │                    │
└──────────┼──────────────────┼───────────────────────┼────────────────────┘
           │                  │                       │
           ▼                  ▼                       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          MCP Transport Layer                             │
│                       (stdio / HTTP / WebSocket)                         │
└─────────────────────────────────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      DS Interview Prep MCP Server                        │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                        Tool Registry                             │    │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐             │    │
│  │  │ Quiz Tools   │ │ SQL Tools    │ │ Stats Tools  │             │    │
│  │  └──────────────┘ └──────────────┘ └──────────────┘             │    │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐             │    │
│  │  │ A/B Testing  │ │ Interview    │ │ Content Gen  │             │    │
│  │  │ Tools        │ │ Tools        │ │ Tools        │             │    │
│  │  └──────────────┘ └──────────────┘ └──────────────┘             │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                     Support Services                             │    │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐             │    │
│  │  │ Validation   │ │ Content      │ │ Analytics    │             │    │
│  │  │ Engine       │ │ Store        │ │ Tracker      │             │    │
│  │  └──────────────┘ └──────────────┘ └──────────────┘             │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         Data Sources                                     │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐    │
│  │ _data/       │ │ _pages/      │ │ Projects/    │ │ Streamlit/   │    │
│  │ quizzes.yml  │ │ content      │ │              │ │              │    │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Tool Categories

### 1. Quiz & Assessment Tools

| Tool | Description |
|------|-------------|
| `generate_quiz_question` | Generate quiz questions for a specific topic |
| `grade_quiz_response` | Evaluate user's quiz answer |
| `explain_quiz_answer` | Provide detailed explanation for a question |
| `get_quiz_by_topic` | Retrieve existing quizzes from _data/quizzes.yml |

### 2. SQL Tools

| Tool | Description |
|------|-------------|
| `validate_sql_query` | Check SQL syntax and common errors |
| `explain_sql_query` | Explain what a SQL query does step-by-step |
| `generate_sql_problem` | Create SQL practice problems with schemas |
| `optimize_sql_query` | Suggest optimizations for SQL queries |
| `compare_sql_solutions` | Compare two SQL approaches |

### 3. Statistics & Probability Tools

| Tool | Description |
|------|-------------|
| `generate_stats_problem` | Create statistics practice problems |
| `solve_hypothesis_test` | Walk through hypothesis testing |
| `calculate_sample_size` | Calculate required sample sizes |
| `explain_distribution` | Explain statistical distributions |

### 4. A/B Testing Tools

| Tool | Description |
|------|-------------|
| `design_ab_experiment` | Help design an A/B test |
| `analyze_ab_results` | Analyze A/B test results |
| `generate_ab_scenario` | Create A/B testing interview scenarios |
| `detect_ab_pitfalls` | Identify common A/B testing mistakes |

### 5. Interview Preparation Tools

| Tool | Description |
|------|-------------|
| `generate_case_study` | Create product analytics case studies |
| `generate_behavioral_question` | Create behavioral interview questions |
| `review_case_response` | Review and score case study response |
| `mock_interview_question` | Generate mock interview questions |

### 6. Code Review Tools

| Tool | Description |
|------|-------------|
| `review_analytics_code` | Review Python/SQL analytics code |
| `suggest_pandas_improvements` | Suggest pandas code improvements |
| `validate_analysis_logic` | Validate analytical approach |

### 7. Content Generation Tools

| Tool | Description |
|------|-------------|
| `generate_handbook_section` | Generate new handbook content |
| `update_quiz_yaml` | Add questions to quizzes.yml |
| `create_project_scaffold` | Create hands-on project structure |

---

## Tool Definitions

### Detailed Tool Specifications

#### generate_quiz_question

```json
{
  "name": "generate_quiz_question",
  "description": "Generate a multiple-choice quiz question for data science interview prep covering statistics, SQL, Python, or A/B testing topics.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "topic": {
        "type": "string",
        "enum": ["sql_basics", "python_data_analysis", "statistics_probability", "ab_testing", "product_metrics", "case_studies"],
        "description": "The topic category for the question"
      },
      "difficulty": {
        "type": "string",
        "enum": ["beginner", "intermediate", "advanced"],
        "description": "Difficulty level of the question"
      },
      "subtopic": {
        "type": "string",
        "description": "Optional specific subtopic (e.g., 'window_functions', 'hypothesis_testing')"
      },
      "context": {
        "type": "string",
        "description": "Optional real-world context for the question (e.g., 'social media engagement metrics')"
      }
    },
    "required": ["topic", "difficulty"]
  }
}
```

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "question": { "type": "string" },
    "options": { 
      "type": "array",
      "items": { "type": "string" },
      "minItems": 4,
      "maxItems": 4
    },
    "correct_index": { "type": "integer", "minimum": 0, "maximum": 3 },
    "explanation": { "type": "string" },
    "topic": { "type": "string" },
    "difficulty": { "type": "string" },
    "related_concepts": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
```

---

#### validate_sql_query

```json
{
  "name": "validate_sql_query",
  "description": "Validate SQL query syntax and check for common errors, anti-patterns, and potential performance issues.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The SQL query to validate"
      },
      "dialect": {
        "type": "string",
        "enum": ["postgresql", "mysql", "sqlite", "bigquery", "snowflake"],
        "default": "postgresql",
        "description": "SQL dialect to validate against"
      },
      "schema_context": {
        "type": "object",
        "description": "Optional table schema context for semantic validation",
        "additionalProperties": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "column": { "type": "string" },
              "type": { "type": "string" }
            }
          }
        }
      },
      "check_performance": {
        "type": "boolean",
        "default": false,
        "description": "Include performance analysis"
      }
    },
    "required": ["query"]
  }
}
```

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "is_valid": { "type": "boolean" },
    "errors": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": { "type": "string" },
          "message": { "type": "string" },
          "line": { "type": "integer" },
          "position": { "type": "integer" }
        }
      }
    },
    "warnings": {
      "type": "array",
      "items": { "type": "string" }
    },
    "performance_notes": {
      "type": "array",
      "items": { "type": "string" }
    },
    "suggestions": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
```

---

#### design_ab_experiment

```json
{
  "name": "design_ab_experiment",
  "description": "Help design an A/B test experiment with proper metrics, sample size calculations, and analysis plan.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "hypothesis": {
        "type": "string",
        "description": "The hypothesis to test (what change you're making and expected impact)"
      },
      "primary_metric": {
        "type": "string",
        "description": "The primary success metric"
      },
      "baseline_rate": {
        "type": "number",
        "description": "Current baseline rate for the primary metric (e.g., 0.05 for 5%)"
      },
      "minimum_detectable_effect": {
        "type": "number",
        "description": "Minimum relative lift you want to detect (e.g., 0.10 for 10% lift)"
      },
      "daily_traffic": {
        "type": "integer",
        "description": "Approximate daily eligible users/sessions"
      },
      "significance_level": {
        "type": "number",
        "default": 0.05,
        "description": "Desired alpha (significance level)"
      },
      "power": {
        "type": "number",
        "default": 0.8,
        "description": "Desired statistical power"
      },
      "guardrail_metrics": {
        "type": "array",
        "items": { "type": "string" },
        "description": "Metrics to monitor that shouldn't regress"
      }
    },
    "required": ["hypothesis", "primary_metric", "baseline_rate", "minimum_detectable_effect"]
  }
}
```

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "experiment_design": {
      "type": "object",
      "properties": {
        "null_hypothesis": { "type": "string" },
        "alternative_hypothesis": { "type": "string" },
        "randomization_unit": { "type": "string" },
        "traffic_split": { "type": "string" }
      }
    },
    "sample_size": {
      "type": "object",
      "properties": {
        "per_variant": { "type": "integer" },
        "total": { "type": "integer" },
        "estimated_duration_days": { "type": "integer" }
      }
    },
    "metrics": {
      "type": "object",
      "properties": {
        "primary": { "type": "string" },
        "secondary": { "type": "array", "items": { "type": "string" } },
        "guardrails": { "type": "array", "items": { "type": "string" } }
      }
    },
    "analysis_plan": {
      "type": "object",
      "properties": {
        "statistical_test": { "type": "string" },
        "corrections_needed": { "type": "string" },
        "decision_criteria": { "type": "string" }
      }
    },
    "potential_pitfalls": {
      "type": "array",
      "items": { "type": "string" }
    },
    "recommendations": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
```

---

#### generate_case_study

```json
{
  "name": "generate_case_study",
  "description": "Generate a product analytics case study for interview practice, including scenario, data description, and evaluation criteria.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "domain": {
        "type": "string",
        "enum": ["social_media", "ecommerce", "fintech", "streaming", "marketplace", "saas"],
        "description": "Industry domain for the case study"
      },
      "focus_area": {
        "type": "string",
        "enum": ["metrics_definition", "product_launch", "feature_evaluation", "user_growth", "monetization", "retention"],
        "description": "Primary focus of the case study"
      },
      "difficulty": {
        "type": "string",
        "enum": ["entry_level", "mid_level", "senior"],
        "description": "Target interview level"
      },
      "time_allocation": {
        "type": "integer",
        "default": 45,
        "description": "Expected time in minutes"
      },
      "include_sample_solution": {
        "type": "boolean",
        "default": false,
        "description": "Include a sample solution framework"
      }
    },
    "required": ["domain", "focus_area", "difficulty"]
  }
}
```

---

#### review_analytics_code

```json
{
  "name": "review_analytics_code",
  "description": "Review Python analytics code for best practices, performance, and correctness.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "code": {
        "type": "string",
        "description": "The Python code to review"
      },
      "context": {
        "type": "string",
        "description": "What the code is supposed to accomplish"
      },
      "review_focus": {
        "type": "array",
        "items": {
          "type": "string",
          "enum": ["correctness", "performance", "readability", "best_practices", "pandas_idioms", "statistical_validity"]
        },
        "default": ["correctness", "best_practices"]
      }
    },
    "required": ["code"]
  }
}
```

---

## State Management

### Server State
- **Stateless per request**: Each tool invocation is independent
- **Session context**: Optional session ID for tracking learning progress
- **Content cache**: Cache quiz questions and generated content

### Persistence
```
data/
├── user_progress/        # Optional: track user progress
│   └── {session_id}.json
├── generated_content/    # Cache generated questions
│   └── questions/
│       └── {hash}.json
└── analytics/            # Usage analytics
    └── tool_usage.jsonl
```

---

## Error Handling

### Error Response Schema
```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string",
          "enum": [
            "INVALID_INPUT",
            "VALIDATION_ERROR",
            "TOPIC_NOT_FOUND",
            "GENERATION_FAILED",
            "RATE_LIMITED",
            "INTERNAL_ERROR"
          ]
        },
        "message": { "type": "string" },
        "details": { "type": "object" },
        "recoverable": { "type": "boolean" }
      },
      "required": ["code", "message"]
    }
  }
}
```

### Error Categories

| Code | Description | Recovery Action |
|------|-------------|-----------------|
| `INVALID_INPUT` | Missing or invalid parameters | Fix input and retry |
| `VALIDATION_ERROR` | Business logic validation failed | Review input constraints |
| `TOPIC_NOT_FOUND` | Requested topic doesn't exist | Use valid topic enum |
| `GENERATION_FAILED` | Content generation failed | Retry with different params |
| `RATE_LIMITED` | Too many requests | Wait and retry |
| `INTERNAL_ERROR` | Unexpected server error | Report and retry |

---

## Security & Safety

### Input Validation
- All SQL queries are parsed and validated (never executed)
- Code review is static analysis only (never executed)
- Input length limits enforced
- Topic and difficulty enums restrict valid values

### Rate Limiting
```python
RATE_LIMITS = {
    "generate_quiz_question": 60,   # per minute
    "validate_sql_query": 120,      # per minute
    "generate_case_study": 20,      # per minute
    "review_analytics_code": 30,    # per minute
}
```

### Content Safety
- Generated content filtered for appropriateness
- No PII generation or storage
- Educational content only

---

## Integration Points

### 1. Streamlit App Integration

```python
# streamlit_app/Product_Analytics/mcp_client.py
from mcp import Client

class MCPQuizClient:
    def __init__(self):
        self.client = Client("ds-interview-prep")
    
    async def get_quiz_question(self, topic: str, difficulty: str):
        result = await self.client.call_tool(
            "generate_quiz_question",
            {"topic": topic, "difficulty": difficulty}
        )
        return result
    
    async def grade_response(self, question_id: str, answer: int):
        return await self.client.call_tool(
            "grade_quiz_response",
            {"question_id": question_id, "selected_option": answer}
        )
```

**Streamlit UI Integration:**
```python
# In streamlit_app.py
if st.button("Generate Practice Question"):
    with st.spinner("Generating..."):
        question = await mcp_client.get_quiz_question(
            topic=selected_topic,
            difficulty=selected_difficulty
        )
    st.session_state.current_question = question
```

### 2. Jekyll Content Generation

The MCP server can generate content for `_pages/`:

```python
# Generate handbook section
result = await client.call_tool(
    "generate_handbook_section",
    {
        "topic": "window_functions",
        "format": "jekyll_markdown",
        "include_examples": True,
        "include_practice_questions": True
    }
)

# Write to _pages/
with open("_pages/foundational_knowledge/window-functions.md", "w") as f:
    f.write(result["content"])
```

### 3. Quiz System Enhancement

```python
# Add generated questions to quizzes.yml
result = await client.call_tool(
    "update_quiz_yaml",
    {
        "topic": "sql_basics",
        "questions": [generated_question],
        "file_path": "_data/quizzes.yml"
    }
)
```

### 4. VS Code Extension Integration

```json
// .vscode/mcp.json
{
  "servers": {
    "ds-interview-prep": {
      "command": "python",
      "args": ["-m", "ds_interview_mcp.server"],
      "env": {
        "MCP_LOG_LEVEL": "INFO"
      }
    }
  }
}
```

---

## Performance Considerations

### Caching Strategy
- Cache generated questions by topic+difficulty hash
- Cache SQL validation results for identical queries
- TTL: 24 hours for generated content

### Async Processing
- All tools support async execution
- Batch operations where applicable
- Timeout: 30 seconds per tool invocation

---

## Testing Strategy

### Unit Tests
- Individual tool logic validation
- Schema validation
- Error handling

### Integration Tests
- End-to-end tool invocation
- MCP protocol compliance
- Client library compatibility

### Content Quality Tests
- Generated question diversity
- Answer correctness validation
- Explanation quality

---

## Deployment

### Local Development
```bash
# Run server in development mode
cd mcp-server
pip install -e .
python -m ds_interview_mcp.server --debug
```

### Production
```bash
# Run as background service
python -m ds_interview_mcp.server --transport stdio
```

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install .
CMD ["python", "-m", "ds_interview_mcp.server"]
```

---

## Versioning Strategy

- **Major version**: Breaking schema changes
- **Minor version**: New tools added
- **Patch version**: Bug fixes, improvements

Tool names never change once released. New functionality = new tool.

---

## Roadmap

### Phase 1 (MVP)
- [ ] Core quiz generation tools
- [ ] SQL validation tools
- [ ] Basic Streamlit integration

### Phase 2
- [ ] A/B testing tools
- [ ] Case study generator
- [ ] Code review tools

### Phase 3
- [ ] Learning progress tracking
- [ ] Adaptive difficulty
- [ ] Multi-language support

### Phase 4
- [ ] Integration with external APIs (LeetCode, etc.)
- [ ] Collaborative learning features
- [ ] Custom curriculum generation

# DS Interview Prep MCP Server

A Model Context Protocol (MCP) server providing AI-enhanced tools for the Data Science Analytical Interview Preparation Handbook.

## Features

- **Quiz Generation**: Generate and grade quiz questions across SQL, statistics, Python, and A/B testing
- **SQL Tools**: Validate, explain, and optimize SQL queries
- **A/B Testing**: Design experiments, calculate sample sizes, analyze results
- **Interview Prep**: Generate case studies, behavioral questions, and mock interviews
- **Content Generation**: Create handbook sections and project scaffolds

## Installation

```bash
# Install from source
cd mcp-server
pip install -e .

# Or install with dev dependencies
pip install -e ".[dev]"
```

## Quick Start

### Run as stdio server (for VS Code / Claude Desktop)

```bash
python -m ds_interview_mcp.server
```

### Development mode with debug logging

```bash
python -m ds_interview_mcp.server --debug
```

## Configuration

### VS Code / Copilot

Add to `.vscode/mcp.json`:

```json
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

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ds-interview-prep": {
      "command": "python",
      "args": ["-m", "ds_interview_mcp.server"],
      "cwd": "/path/to/mcp-server"
    }
  }
}
```

## Available Tools

### Quiz Tools
- `generate_quiz_question` - Generate quiz questions by topic and difficulty
- `grade_quiz_response` - Grade user answers with feedback
- `explain_quiz_answer` - Detailed explanations for answers
- `get_quiz_by_topic` - Retrieve existing quizzes

### SQL Tools
- `validate_sql_query` - Syntax and pattern validation
- `explain_sql_query` - Step-by-step query explanation
- `generate_sql_problem` - Create practice problems
- `optimize_sql_query` - Performance suggestions

### Statistics Tools
- `generate_stats_problem` - Create statistics problems
- `calculate_sample_size` - A/B test sample size calculation

### A/B Testing Tools
- `design_ab_experiment` - Complete experiment design
- `analyze_ab_results` - Statistical analysis of results
- `generate_ab_scenario` - Interview scenarios
- `detect_ab_pitfalls` - Find design issues

### Interview Tools
- `generate_case_study` - Product analytics case studies
- `generate_behavioral_question` - STAR method questions
- `review_analytics_code` - Code review for analytics

### Content Tools
- `generate_handbook_section` - Jekyll-compatible content
- `update_quiz_yaml` - Add questions to quizzes.yml
- `create_project_scaffold` - New project templates

## Development

```bash
# Run tests
pytest

# Format code
black src/

# Lint
ruff check src/

# Type check
mypy src/
```

## License

MIT License

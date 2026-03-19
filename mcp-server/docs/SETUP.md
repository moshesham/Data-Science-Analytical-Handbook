# DS Interview Prep MCP Server - Setup Guide

This guide walks you through setting up and using the MCP server with your Data Science Interview Preparation Handbook.

## Prerequisites

- Python 3.10+
- pip or uv package manager
- The MCP package (`pip install mcp`)

## Installation

### 1. Install the MCP Server

```bash
cd mcp-server
pip install -e ".[dev]"
```

### 2. Verify Installation

```bash
# Test that the module loads correctly
python -c "from ds_interview_mcp import main; print('OK')"
```

## Configuration

### VS Code / GitHub Copilot

Create or update `.vscode/mcp.json` in your workspace:

```json
{
  "servers": {
    "ds-interview-prep": {
      "command": "python",
      "args": ["-m", "ds_interview_mcp.server"],
      "cwd": "${workspaceFolder}/mcp-server",
      "env": {
        "MCP_LOG_LEVEL": "INFO"
      }
    }
  }
}
```

### Claude Desktop

Add to your `claude_desktop_config.json` (location varies by OS):

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
**Linux:** `~/.config/claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "ds-interview-prep": {
      "command": "python",
      "args": ["-m", "ds_interview_mcp.server"],
      "cwd": "/path/to/Data-Science-Analytical-Handbook/mcp-server"
    }
  }
}
```

### Cursor IDE

Add to your Cursor MCP configuration:

```json
{
  "mcpServers": {
    "ds-interview-prep": {
      "command": "python",
      "args": ["-m", "ds_interview_mcp.server"],
      "cwd": "/path/to/your/workspace/mcp-server"
    }
  }
}
```

## Running the Server

### Standalone (for testing)

```bash
# Standard mode
python -m ds_interview_mcp.server

# Debug mode (verbose logging)
python -m ds_interview_mcp.server --debug

# Specify workspace path
python -m ds_interview_mcp.server --workspace /path/to/handbook
```

### As Part of an IDE

Once configured, the MCP server starts automatically when you open your IDE with the workspace.

## Using the Tools

### In VS Code with Copilot

After configuration, you can invoke tools directly in Copilot Chat:

```
Use the generate_quiz_question tool to create an intermediate SQL question about window functions.
```

```
Validate this SQL query for me:
SELECT user_id, COUNT(*) FROM users GROUP BY 1 HAVING COUNT(*) > 5
```

### Example Tool Invocations

#### Generate a Quiz Question
```
@ds-interview-prep generate_quiz_question topic=sql_basics difficulty=intermediate subtopic=window_functions
```

#### Design an A/B Experiment
```
@ds-interview-prep design_ab_experiment hypothesis="Adding a save button will increase user engagement" primary_metric="saves_per_user" baseline_rate=0.05 minimum_detectable_effect=0.1 daily_traffic=50000
```

#### Get a Case Study
```
@ds-interview-prep generate_case_study domain=social_media focus_area=retention difficulty=mid_level
```

## Streamlit Integration

See `streamlit_app/Product_Analytics/mcp_integration.py` for an example of how to integrate the MCP tools with your Streamlit app.

## Troubleshooting

### Server won't start

1. Check Python version: `python --version` (needs 3.10+)
2. Verify MCP is installed: `pip show mcp`
3. Check for import errors: `python -c "from ds_interview_mcp.server import main"`

### Tools not appearing

1. Restart your IDE after configuration changes
2. Check the MCP server logs for errors
3. Verify the path in your configuration is correct

### Connection errors

1. Ensure only one instance of the server is running
2. Check that the specified command path is correct
3. Look for firewall or permission issues

## Development

### Running Tests

```bash
cd mcp-server
pytest tests/ -v
```

### Adding New Tools

1. Create a new tool module in `src/ds_interview_mcp/tools/`
2. Define `get_tool_definitions()` returning `list[Tool]`
3. Define `TOOL_HANDLERS` dict mapping tool names to async handlers
4. Import and register in `tools/__init__.py`
5. Add to `server.py` dispatcher

### Validating Tool Definitions

```bash
python -c "from ds_interview_mcp.server import DSInterviewMCPServer; from ds_interview_mcp.config import Config; s = DSInterviewMCPServer(Config('..')); print([t.name for t in s._get_all_tools()])"
```

## Available Tools Reference

| Category | Tool | Description |
|----------|------|-------------|
| **Quiz** | `generate_quiz_question` | Generate quiz questions by topic |
| | `grade_quiz_response` | Grade user answers |
| | `explain_quiz_answer` | Detailed explanations |
| | `get_quiz_by_topic` | Retrieve existing quizzes |
| **SQL** | `validate_sql_query` | Syntax and pattern validation |
| | `explain_sql_query` | Step-by-step explanation |
| | `generate_sql_problem` | Create practice problems |
| | `optimize_sql_query` | Performance suggestions |
| **Statistics** | `generate_stats_problem` | Create stats problems |
| | `calculate_sample_size` | Sample size calculation |
| | `explain_distribution` | Explain distributions |
| **A/B Testing** | `design_ab_experiment` | Experiment design |
| | `analyze_ab_results` | Result analysis |
| | `generate_ab_scenario` | Interview scenarios |
| | `detect_ab_pitfalls` | Find design issues |
| **Interview** | `generate_case_study` | Case study creation |
| | `generate_behavioral_question` | Behavioral questions |
| | `review_analytics_code` | Code review |
| | `mock_interview_question` | Mock questions |
| **Content** | `generate_handbook_section` | Jekyll content |
| | `update_quiz_yaml` | Quiz YAML updates |
| | `create_project_scaffold` | Project templates |

## Next Steps

1. Start with the quiz tools to test your setup
2. Use SQL tools while working through practice problems
3. Generate case studies for mock interview practice
4. Create new content using the content generation tools

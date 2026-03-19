"""Tests for the DS Interview Prep MCP Server."""

import pytest
import asyncio
from pathlib import Path
from unittest.mock import MagicMock

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ds_interview_mcp.config import Config
from ds_interview_mcp.tools import quiz_tools, sql_tools, stats_tools


@pytest.fixture
def config():
    """Create a test config."""
    return Config(workspace_path=Path(__file__).parent.parent.parent)


class TestQuizTools:
    """Tests for quiz tools."""
    
    @pytest.mark.asyncio
    async def test_generate_quiz_question(self, config):
        """Test quiz question generation."""
        args = {
            "topic": "sql_basics",
            "difficulty": "intermediate"
        }
        result = await quiz_tools.generate_quiz_question(args, config)
        
        assert "question" in result
        assert "options" in result
        assert len(result["options"]) == 4
        assert "correct_index" in result
        assert 0 <= result["correct_index"] <= 3
        assert "explanation" in result
    
    @pytest.mark.asyncio
    async def test_grade_quiz_response_correct(self, config):
        """Test grading a correct answer."""
        args = {
            "question_text": "Test question?",
            "options": ["A", "B", "C", "D"],
            "correct_index": 1,
            "selected_index": 1
        }
        result = await quiz_tools.grade_quiz_response(args, config)
        
        assert result["is_correct"] is True
        assert "feedback" in result
    
    @pytest.mark.asyncio
    async def test_grade_quiz_response_incorrect(self, config):
        """Test grading an incorrect answer."""
        args = {
            "question_text": "Test question?",
            "options": ["A", "B", "C", "D"],
            "correct_index": 1,
            "selected_index": 0
        }
        result = await quiz_tools.grade_quiz_response(args, config)
        
        assert result["is_correct"] is False


class TestSQLTools:
    """Tests for SQL tools."""
    
    @pytest.mark.asyncio
    async def test_validate_sql_query_valid(self, config):
        """Test validation of a valid SQL query."""
        args = {
            "query": "SELECT user_id, COUNT(*) FROM users GROUP BY user_id"
        }
        result = await sql_tools.validate_sql_query(args, config)
        
        assert result["is_valid"] is True
        assert "errors" in result
        assert len(result["errors"]) == 0
    
    @pytest.mark.asyncio
    async def test_validate_sql_query_detects_null_comparison(self, config):
        """Test that NULL comparison is detected."""
        args = {
            "query": "SELECT * FROM users WHERE email = NULL"
        }
        result = await sql_tools.validate_sql_query(args, config)
        
        # Should have either errors or warnings about NULL comparison
        assert len(result["errors"]) > 0 or len(result["warnings"]) > 0
    
    @pytest.mark.asyncio
    async def test_validate_sql_query_unmatched_parens(self, config):
        """Test detection of unmatched parentheses."""
        args = {
            "query": "SELECT * FROM users WHERE (status = 'active'"
        }
        result = await sql_tools.validate_sql_query(args, config)
        
        assert result["is_valid"] is False
        assert any("parentheses" in e["message"].lower() for e in result["errors"])
    
    @pytest.mark.asyncio
    async def test_explain_sql_query(self, config):
        """Test SQL query explanation."""
        args = {
            "query": """
                SELECT u.user_id, COUNT(p.post_id) as post_count
                FROM users u
                LEFT JOIN posts p ON u.user_id = p.user_id
                GROUP BY u.user_id
                ORDER BY post_count DESC
                LIMIT 10
            """
        }
        result = await sql_tools.explain_sql_query(args, config)
        
        assert "summary" in result
        assert "components" in result
        assert len(result["components"]) > 0
    
    @pytest.mark.asyncio
    async def test_generate_sql_problem(self, config):
        """Test SQL problem generation."""
        args = {
            "difficulty": "medium",
            "topics": ["joins", "aggregations"],
            "domain": "social_media"
        }
        result = await sql_tools.generate_sql_problem(args, config)
        
        assert "title" in result
        assert "description" in result
        assert "schema" in result


class TestStatsTools:
    """Tests for statistics tools."""
    
    @pytest.mark.asyncio
    async def test_calculate_sample_size_proportion(self, config):
        """Test sample size calculation for proportions."""
        args = {
            "metric_type": "proportion",
            "baseline_value": 0.05,
            "minimum_detectable_effect": 0.10,
            "alpha": 0.05,
            "power": 0.80
        }
        result = await stats_tools.calculate_sample_size(args, config)
        
        assert "sample_size" in result
        assert "per_variant" in result["sample_size"]
        assert "total" in result["sample_size"]
        assert result["sample_size"]["per_variant"] > 0
        assert result["sample_size"]["total"] == result["sample_size"]["per_variant"] * 2
    
    @pytest.mark.asyncio
    async def test_calculate_sample_size_mean_requires_std(self, config):
        """Test that mean metric requires standard deviation."""
        args = {
            "metric_type": "mean",
            "baseline_value": 100,
            "minimum_detectable_effect": 0.05
            # Missing standard_deviation
        }
        result = await stats_tools.calculate_sample_size(args, config)
        
        assert "error" in result
    
    @pytest.mark.asyncio
    async def test_explain_distribution(self, config):
        """Test distribution explanation."""
        args = {
            "distribution": "normal",
            "include_examples": True,
            "include_formulas": True
        }
        result = await stats_tools.explain_distribution(args, config)
        
        assert "name" in result
        assert "description" in result
        assert "properties" in result
        assert "examples" in result
        assert "formula" in result


class TestToolDefinitions:
    """Tests for tool definitions."""
    
    def test_quiz_tools_have_definitions(self):
        """Test that quiz tools are properly defined."""
        tools = quiz_tools.get_tool_definitions()
        
        assert len(tools) > 0
        tool_names = [t.name for t in tools]
        assert "generate_quiz_question" in tool_names
        assert "grade_quiz_response" in tool_names
    
    def test_sql_tools_have_definitions(self):
        """Test that SQL tools are properly defined."""
        tools = sql_tools.get_tool_definitions()
        
        assert len(tools) > 0
        tool_names = [t.name for t in tools]
        assert "validate_sql_query" in tool_names
        assert "explain_sql_query" in tool_names
    
    def test_all_tools_have_handlers(self):
        """Test that all defined tools have handlers."""
        # Quiz tools
        quiz_defs = quiz_tools.get_tool_definitions()
        for tool in quiz_defs:
            assert tool.name in quiz_tools.TOOL_HANDLERS, f"Missing handler for {tool.name}"
        
        # SQL tools
        sql_defs = sql_tools.get_tool_definitions()
        for tool in sql_defs:
            assert tool.name in sql_tools.TOOL_HANDLERS, f"Missing handler for {tool.name}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

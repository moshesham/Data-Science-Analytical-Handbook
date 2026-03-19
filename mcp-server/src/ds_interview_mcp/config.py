"""Configuration management for the MCP server."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class Config:
    """Server configuration."""
    
    workspace_path: Path
    quiz_file: Path = field(init=False)
    pages_dir: Path = field(init=False)
    projects_dir: Path = field(init=False)
    cache_dir: Path = field(init=False)
    
    # Rate limits (requests per minute)
    rate_limits: dict[str, int] = field(default_factory=lambda: {
        "generate_quiz_question": 60,
        "validate_sql_query": 120,
        "generate_case_study": 20,
        "review_analytics_code": 30,
    })
    
    # Tool settings
    default_sql_dialect: str = "postgresql"
    max_query_length: int = 10000
    max_code_length: int = 50000
    
    def __post_init__(self) -> None:
        """Initialize derived paths."""
        self.quiz_file = self.workspace_path / "_data" / "quizzes.yml"
        self.pages_dir = self.workspace_path / "_pages"
        self.projects_dir = self.workspace_path / "Analytical-HandsOn-Projects"
        self.cache_dir = self.workspace_path / ".mcp_cache"
        
        # Ensure cache directory exists
        self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def load_quizzes(self) -> dict[str, Any]:
        """Load quiz data from YAML file."""
        if self.quiz_file.exists():
            with open(self.quiz_file) as f:
                return yaml.safe_load(f) or {}
        return {}
    
    def get_handbook_pages(self) -> list[dict[str, Any]]:
        """Get list of handbook pages with metadata."""
        pages = []
        if self.pages_dir.exists():
            for md_file in self.pages_dir.rglob("*.md"):
                pages.append({
                    "path": str(md_file.relative_to(self.workspace_path)),
                    "name": md_file.stem,
                })
        return pages

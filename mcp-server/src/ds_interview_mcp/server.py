"""
DS Interview Prep MCP Server

Main entry point for the MCP server that provides AI-enhanced tools
for data science interview preparation.
"""

import argparse
import asyncio
import json
import logging
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    Resource,
    Prompt,
    PromptArgument,
    GetPromptResult,
    PromptMessage,
)

from ds_interview_mcp.tools import (
    quiz_tools,
    sql_tools,
    stats_tools,
    ab_testing_tools,
    interview_tools,
    content_tools,
)
from ds_interview_mcp.config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("ds-interview-mcp")


class DSInterviewMCPServer:
    """MCP Server for DS Interview Prep tools."""
    
    def __init__(self, config: Config):
        self.config = config
        self.server = Server("ds-interview-prep")
        self._register_handlers()
    
    def _register_handlers(self) -> None:
        """Register all MCP handlers."""
        
        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            """List all available tools."""
            return self._get_all_tools()
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
            """Handle tool invocations."""
            logger.info(f"Tool called: {name} with args: {json.dumps(arguments)[:200]}")
            
            try:
                result = await self._dispatch_tool(name, arguments)
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            except Exception as e:
                logger.error(f"Tool {name} failed: {e}")
                error_response = {
                    "error": {
                        "code": "INTERNAL_ERROR",
                        "message": str(e),
                        "recoverable": True
                    }
                }
                return [TextContent(type="text", text=json.dumps(error_response))]
        
        @self.server.list_resources()
        async def list_resources() -> list[Resource]:
            """List available resources."""
            return [
                Resource(
                    uri="quiz://topics",
                    name="Available Quiz Topics",
                    description="List of all quiz topics with question counts",
                    mimeType="application/json"
                ),
                Resource(
                    uri="handbook://pages",
                    name="Handbook Pages",
                    description="Index of handbook pages",
                    mimeType="application/json"
                ),
            ]
        
        @self.server.read_resource()
        async def read_resource(uri: str) -> str:
            """Read a resource by URI."""
            if uri == "quiz://topics":
                return json.dumps(quiz_tools.get_available_topics(self.config))
            elif uri == "handbook://pages":
                return json.dumps(content_tools.get_handbook_index(self.config))
            else:
                raise ValueError(f"Unknown resource: {uri}")
        
        @self.server.list_prompts()
        async def list_prompts() -> list[Prompt]:
            """List available prompts."""
            return [
                Prompt(
                    name="interview_prep_session",
                    description="Start an interactive interview prep session",
                    arguments=[
                        PromptArgument(
                            name="focus_area",
                            description="Focus area (sql, statistics, ab_testing, case_study, behavioral)",
                            required=True
                        ),
                        PromptArgument(
                            name="duration_minutes",
                            description="Session duration in minutes",
                            required=False
                        )
                    ]
                ),
                Prompt(
                    name="daily_practice",
                    description="Generate daily practice problems",
                    arguments=[
                        PromptArgument(
                            name="difficulty",
                            description="Difficulty level",
                            required=False
                        )
                    ]
                ),
                Prompt(
                    name="skills_discovery",
                    description="Find relevant Claude Skills for a data science topic using the claude-skills-mcp server",
                    arguments=[
                        PromptArgument(
                            name="topic",
                            description="Data science topic to find skills for (e.g. 'ab-testing', 'sql', 'statistics')",
                            required=True
                        )
                    ]
                )
            ]
        
        @self.server.get_prompt()
        async def get_prompt(name: str, arguments: dict[str, str] | None) -> GetPromptResult:
            """Get a prompt by name."""
            args = arguments or {}
            
            if name == "interview_prep_session":
                focus_area = args.get("focus_area", "general")
                duration = args.get("duration_minutes", "30")
                return GetPromptResult(
                    description=f"Interview prep session for {focus_area}",
                    messages=[
                        PromptMessage(
                            role="user",
                            content=TextContent(
                                type="text",
                                text=f"""Let's start a {duration}-minute interview prep session focused on {focus_area}.

Please use the DS Interview Prep MCP tools to:
1. Generate relevant practice problems
2. Provide hints when I'm stuck
3. Grade my answers and provide feedback
4. Track my progress through the session

Start by giving me a warm-up question appropriate for {focus_area}."""
                            )
                        )
                    ]
                )
            elif name == "daily_practice":
                difficulty = args.get("difficulty", "intermediate")
                return GetPromptResult(
                    description=f"Daily practice set ({difficulty})",
                    messages=[
                        PromptMessage(
                            role="user",
                            content=TextContent(
                                type="text",
                                text=f"""Generate a daily practice set at {difficulty} level.

Use the DS Interview Prep MCP tools to create:
1. One SQL problem
2. One statistics/probability question  
3. One A/B testing scenario
4. One quiz question

Present each one at a time and wait for my answer before moving to the next."""
                            )
                        )
                    ]
                )
            elif name == "skills_discovery":
                topic = args.get("topic", "data science")
                return GetPromptResult(
                    description=f"Skills discovery for '{topic}'",
                    messages=[
                        PromptMessage(
                            role="user",
                            content=TextContent(
                                type="text",
                                text=f"""I want to learn about '{topic}' in data science.

Please use the claude-skills-mcp tools (find_helpful_skills, list_skills, read_skill_document) to:
1. Search for skills relevant to '{topic}'
2. List the top 3–5 most relevant skills
3. For each skill, briefly describe what it covers and when to use it
4. Recommend which skill document to read first based on my learning goal

After discovering the relevant skills, also use the DS Interview Prep MCP tools to:
- Generate a quiz question on '{topic}' to assess my current understanding
- Suggest a practical exercise or scenario to solidify my knowledge"""
                            )
                        )
                    ]
                )
            else:
                raise ValueError(f"Unknown prompt: {name}")
    
    def _get_all_tools(self) -> list[Tool]:
        """Collect all tool definitions."""
        tools = []
        
        # Quiz tools
        tools.extend(quiz_tools.get_tool_definitions())
        
        # SQL tools
        tools.extend(sql_tools.get_tool_definitions())
        
        # Statistics tools
        tools.extend(stats_tools.get_tool_definitions())
        
        # A/B Testing tools
        tools.extend(ab_testing_tools.get_tool_definitions())
        
        # Interview tools
        tools.extend(interview_tools.get_tool_definitions())
        
        # Content generation tools
        tools.extend(content_tools.get_tool_definitions())
        
        return tools
    
    async def _dispatch_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        """Dispatch tool call to appropriate handler."""
        
        # Quiz tools
        if name in quiz_tools.TOOL_HANDLERS:
            return await quiz_tools.TOOL_HANDLERS[name](arguments, self.config)
        
        # SQL tools
        if name in sql_tools.TOOL_HANDLERS:
            return await sql_tools.TOOL_HANDLERS[name](arguments, self.config)
        
        # Statistics tools
        if name in stats_tools.TOOL_HANDLERS:
            return await stats_tools.TOOL_HANDLERS[name](arguments, self.config)
        
        # A/B Testing tools
        if name in ab_testing_tools.TOOL_HANDLERS:
            return await ab_testing_tools.TOOL_HANDLERS[name](arguments, self.config)
        
        # Interview tools
        if name in interview_tools.TOOL_HANDLERS:
            return await interview_tools.TOOL_HANDLERS[name](arguments, self.config)
        
        # Content tools
        if name in content_tools.TOOL_HANDLERS:
            return await content_tools.TOOL_HANDLERS[name](arguments, self.config)
        
        raise ValueError(f"Unknown tool: {name}")
    
    async def run(self) -> None:
        """Run the MCP server."""
        logger.info("Starting DS Interview Prep MCP Server...")
        
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="DS Interview Prep MCP Server")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging"
    )
    parser.add_argument(
        "--workspace",
        type=str,
        default=None,
        help="Path to the handbook workspace"
    )
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled")
    
    # Determine workspace path
    workspace_path = Path(args.workspace) if args.workspace else Path.cwd()
    
    # Load configuration
    config = Config(workspace_path=workspace_path)
    
    # Create and run server
    server = DSInterviewMCPServer(config)
    asyncio.run(server.run())


if __name__ == "__main__":
    main()

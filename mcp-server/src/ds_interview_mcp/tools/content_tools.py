"""Content generation tools."""

from datetime import datetime
from typing import Any, Callable, Coroutine

from mcp.types import Tool

from ds_interview_mcp.config import Config


def get_tool_definitions() -> list[Tool]:
    """Return content generation tool definitions."""
    return [
        Tool(
            name="generate_handbook_section",
            description="Generate content for a new handbook section in Jekyll-compatible format.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string"},
                    "section_type": {
                        "type": "string",
                        "enum": ["concept_explanation", "tutorial", "cheat_sheet", "practice_problems", "interview_guide"]
                    },
                    "difficulty": {
                        "type": "string",
                        "enum": ["beginner", "intermediate", "advanced"]
                    },
                    "estimated_reading_time": {"type": "integer"},
                    "include_examples": {"type": "boolean", "default": True},
                    "include_practice_questions": {"type": "boolean", "default": True}
                },
                "required": ["topic", "section_type", "difficulty"]
            }
        ),
        Tool(
            name="update_quiz_yaml",
            description="Generate YAML content for adding new questions to quizzes.yml.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "enum": ["sql_basics", "python_data_analysis", "statistics_probability", "ab_testing"]
                    },
                    "questions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "question": {"type": "string"},
                                "options": {"type": "array", "items": {"type": "string"}},
                                "correct": {"type": "integer"},
                                "explanation": {"type": "string"}
                            },
                            "required": ["question", "options", "correct", "explanation"]
                        }
                    }
                },
                "required": ["topic", "questions"]
            }
        ),
        Tool(
            name="create_project_scaffold",
            description="Create a scaffold for a new hands-on analytics project.",
            inputSchema={
                "type": "object",
                "properties": {
                    "project_type": {
                        "type": "string",
                        "enum": ["ab_test", "cohort_analysis", "churn_prediction", "demand_forecasting", "funnel_analysis", "segmentation"]
                    },
                    "project_name": {"type": "string"},
                    "include_sample_data": {"type": "boolean", "default": True},
                    "include_solution_notebook": {"type": "boolean", "default": False}
                },
                "required": ["project_type", "project_name"]
            }
        )
    ]


def get_handbook_index(config: Config) -> dict[str, Any]:
    """Get index of handbook pages."""
    pages = config.get_handbook_pages()
    categorized = {}
    
    for page in pages:
        path = page["path"]
        if "_pages/" in path:
            category = path.split("/")[1] if "/" in path else "root"
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(page)
    
    return {
        "total_pages": len(pages),
        "categories": categorized
    }


async def generate_handbook_section(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Generate content for a new handbook section."""
    topic = args["topic"]
    section_type = args["section_type"]
    difficulty = args["difficulty"]
    reading_time = args.get("estimated_reading_time", 30)
    include_examples = args.get("include_examples", True)
    include_practice = args.get("include_practice_questions", True)
    
    # Generate Jekyll front matter
    front_matter = f"""---
layout: default
title: "{topic.replace('_', ' ').title()}"
permalink: /{topic.lower().replace(' ', '-')}/
difficulty: "{difficulty.title()}"
estimated_time: "{reading_time} mins"
tags: [{', '.join(topic.split('_')[:3])}]
track: "Foundational Knowledge"
---"""
    
    # Section templates by type
    templates = {
        "concept_explanation": {
            "structure": [
                "## Overview",
                "## Key Concepts",
                "## How It Works",
                "## Common Applications",
                "## Common Mistakes to Avoid",
            ]
        },
        "tutorial": {
            "structure": [
                "## Prerequisites",
                "## Step 1: Setup",
                "## Step 2: Basic Implementation",
                "## Step 3: Advanced Features",
                "## Putting It All Together",
                "## Next Steps",
            ]
        },
        "cheat_sheet": {
            "structure": [
                "## Quick Reference",
                "## Syntax",
                "## Common Patterns",
                "## Tips & Tricks",
                "## Common Errors",
            ]
        },
        "practice_problems": {
            "structure": [
                "## Easy Problems",
                "## Medium Problems",
                "## Hard Problems",
                "## Solutions",
            ]
        },
        "interview_guide": {
            "structure": [
                "## What to Expect",
                "## Key Topics",
                "## Common Questions",
                "## How to Approach",
                "## Practice Resources",
            ]
        }
    }
    
    template = templates.get(section_type, templates["concept_explanation"])
    
    content_sections = []
    for section in template["structure"]:
        content_sections.append(f"""
{section}

<div class="card">
  <p>[Content for {section} goes here - this is a placeholder that should be filled with relevant information about {topic}]</p>
</div>
""")
    
    if include_examples:
        content_sections.append("""
## Examples

<div class="card">
  <h3>Example 1</h3>
  <p>[Add a practical example here]</p>
  
  <h3>Example 2</h3>
  <p>[Add another example here]</p>
</div>
""")
    
    if include_practice:
        content_sections.append("""
## Practice Questions

<div class="card">
  <ol>
    <li><strong>Question 1:</strong> [Practice question here]</li>
    <li><strong>Question 2:</strong> [Practice question here]</li>
    <li><strong>Question 3:</strong> [Practice question here]</li>
  </ol>
</div>
""")
    
    full_content = front_matter + "\n\n" + "\n".join(content_sections)
    
    return {
        "topic": topic,
        "section_type": section_type,
        "difficulty": difficulty,
        "estimated_reading_time": reading_time,
        "content": full_content,
        "suggested_filename": f"{topic.lower().replace(' ', '-')}.md",
        "suggested_path": f"_pages/foundational_knowledge/{topic.lower().replace(' ', '-')}.md"
    }


async def update_quiz_yaml(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Generate YAML content for quiz questions."""
    topic = args["topic"]
    questions = args["questions"]
    
    # Generate YAML format
    yaml_lines = [f"\n  # Added on {datetime.now().strftime('%Y-%m-%d')}"]
    
    for q in questions:
        yaml_lines.append(f"""
    - question: "{q['question']}"
      options:""")
        for opt in q['options']:
            yaml_lines.append(f'        - "{opt}"')
        yaml_lines.append(f"      correct: {q['correct']}")
        yaml_lines.append(f'      explanation: "{q["explanation"]}"')
    
    yaml_content = "\n".join(yaml_lines)
    
    return {
        "topic": topic,
        "questions_added": len(questions),
        "yaml_content": yaml_content,
        "instructions": f"""To add these questions:
1. Open _data/quizzes.yml
2. Find the '{topic}' section
3. Add the following YAML under 'questions:':
{yaml_content}
4. Verify YAML syntax is valid
5. Test the quiz locally"""
    }


async def create_project_scaffold(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Create scaffold for a hands-on analytics project."""
    project_type = args["project_type"]
    project_name = args["project_name"]
    include_sample_data = args.get("include_sample_data", True)
    include_solution = args.get("include_solution_notebook", False)
    
    # Project type configurations
    project_configs = {
        "ab_test": {
            "description": "Design, analyze, and interpret an A/B test",
            "objectives": [
                "Calculate required sample size",
                "Set up proper randomization",
                "Analyze results with statistical tests",
                "Interpret findings and make recommendations"
            ],
            "datasets": ["experiment_assignments.csv", "conversion_events.csv"],
            "skills": ["Hypothesis testing", "Sample size calculation", "Statistical significance"]
        },
        "cohort_analysis": {
            "description": "Perform cohort analysis to understand user retention",
            "objectives": [
                "Define and identify cohorts",
                "Calculate retention metrics",
                "Visualize cohort behavior",
                "Draw actionable insights"
            ],
            "datasets": ["user_signups.csv", "user_activity.csv"],
            "skills": ["Retention analysis", "Pandas groupby", "Heatmap visualization"]
        },
        "churn_prediction": {
            "description": "Build a model to predict customer churn",
            "objectives": [
                "Perform exploratory data analysis",
                "Engineer relevant features",
                "Build and evaluate predictive models",
                "Identify key churn drivers"
            ],
            "datasets": ["customer_data.csv", "transaction_history.csv"],
            "skills": ["Classification", "Feature engineering", "Model evaluation"]
        },
        "funnel_analysis": {
            "description": "Analyze conversion funnel to identify optimization opportunities",
            "objectives": [
                "Map the user journey",
                "Calculate conversion rates at each step",
                "Identify drop-off points",
                "Segment analysis by user attributes"
            ],
            "datasets": ["page_events.csv", "user_attributes.csv"],
            "skills": ["Funnel visualization", "Conversion analysis", "Segmentation"]
        }
    }
    
    project_config = project_configs.get(project_type, project_configs["ab_test"])
    
    # Generate README content
    readme_content = f"""# {project_name}

## Project Type: {project_type.replace('_', ' ').title()}

{project_config['description']}

## Learning Objectives

After completing this project, you will be able to:
{chr(10).join(f'- {obj}' for obj in project_config['objectives'])}

## Skills Practiced

{', '.join(project_config['skills'])}

## Dataset Description

This project uses the following datasets:
{chr(10).join(f'- `{ds}`: [Description]' for ds in project_config['datasets'])}

## Getting Started

1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Open `{project_name}.ipynb` and follow the instructions

## Project Structure

```
{project_name}/
├── README.md
├── {project_name}.ipynb      # Main project notebook
├── data/
│   └── [datasets]
├── requirements.txt
└── solutions/                 # (Optional) Reference solutions
```

## Estimated Time

2-4 hours

## Difficulty

Intermediate
"""
    
    # Generate starter notebook structure
    notebook_cells = [
        {
            "type": "markdown",
            "content": f"# {project_name}\n\n{project_config['description']}"
        },
        {
            "type": "markdown",
            "content": "## Setup\n\nFirst, let's import the necessary libraries and load the data."
        },
        {
            "type": "code",
            "content": """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set display options
pd.set_option('display.max_columns', 50)
plt.style.use('seaborn-v0_8-whitegrid')"""
        },
        {
            "type": "markdown",
            "content": "## Task 1: Data Exploration\n\nLoad the data and perform initial exploration."
        },
        {
            "type": "code",
            "content": """# Load the data
# df = pd.read_csv('data/your_data.csv')

# Your exploration code here"""
        },
        {
            "type": "markdown",
            "content": "## Task 2: Analysis\n\n[Detailed instructions for the main analysis task]"
        },
        {
            "type": "code",
            "content": "# Your analysis code here"
        },
        {
            "type": "markdown",
            "content": "## Task 3: Visualization\n\nCreate visualizations to communicate your findings."
        },
        {
            "type": "code",
            "content": "# Your visualization code here"
        },
        {
            "type": "markdown",
            "content": "## Conclusions\n\nSummarize your findings and recommendations."
        }
    ]
    
    files_to_create = {
        f"Analytical-HandsOn-Projects/{project_name}/README.md": readme_content,
        f"Analytical-HandsOn-Projects/{project_name}/requirements.txt": """pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
scipy>=1.9.0
jupyter>=1.0.0"""
    }
    
    return {
        "project_name": project_name,
        "project_type": project_type,
        "description": project_config['description'],
        "structure": {
            "readme": f"Analytical-HandsOn-Projects/{project_name}/README.md",
            "notebook": f"Analytical-HandsOn-Projects/{project_name}/{project_name}.ipynb",
            "data_folder": f"Analytical-HandsOn-Projects/{project_name}/data/",
            "requirements": f"Analytical-HandsOn-Projects/{project_name}/requirements.txt"
        },
        "files_content": files_to_create,
        "notebook_cells": notebook_cells,
        "datasets_needed": project_config['datasets'],
        "next_steps": [
            "Create the directory structure",
            "Write the README.md file",
            "Create the Jupyter notebook with the cell structure",
            "Generate or source sample datasets",
            "Add detailed instructions to each task section"
        ]
    }


# Handler registry
TOOL_HANDLERS: dict[str, Callable[[dict[str, Any], Config], Coroutine[Any, Any, dict[str, Any]]]] = {
    "generate_handbook_section": generate_handbook_section,
    "update_quiz_yaml": update_quiz_yaml,
    "create_project_scaffold": create_project_scaffold,
}

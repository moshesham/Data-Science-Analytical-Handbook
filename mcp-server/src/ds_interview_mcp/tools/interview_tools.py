"""Interview preparation tools."""

from typing import Any, Callable, Coroutine

from mcp.types import Tool

from ds_interview_mcp.config import Config


def get_tool_definitions() -> list[Tool]:
    """Return interview tool definitions."""
    return [
        Tool(
            name="generate_case_study",
            description="Generate a product analytics case study for interview practice.",
            inputSchema={
                "type": "object",
                "properties": {
                    "domain": {
                        "type": "string",
                        "enum": ["social_media", "ecommerce", "fintech", "streaming", "marketplace", "saas"]
                    },
                    "focus_area": {
                        "type": "string",
                        "enum": ["metrics_definition", "product_launch", "feature_evaluation", "user_growth", "monetization", "retention"]
                    },
                    "difficulty": {
                        "type": "string",
                        "enum": ["entry_level", "mid_level", "senior"]
                    },
                    "time_allocation": {"type": "integer", "default": 45},
                    "include_sample_solution": {"type": "boolean", "default": False}
                },
                "required": ["domain", "focus_area", "difficulty"]
            }
        ),
        Tool(
            name="generate_behavioral_question",
            description="Generate a behavioral interview question for data science roles.",
            inputSchema={
                "type": "object",
                "properties": {
                    "competency": {
                        "type": "string",
                        "enum": ["leadership", "collaboration", "problem_solving", "communication", "handling_ambiguity", "impact", "growth_mindset"]
                    },
                    "company_context": {
                        "type": "string",
                        "enum": ["meta", "google", "amazon", "netflix", "startup", "generic"],
                        "default": "generic"
                    },
                    "include_follow_ups": {"type": "boolean", "default": True}
                },
                "required": ["competency"]
            }
        ),
        Tool(
            name="review_analytics_code",
            description="Review Python analytics code for best practices, performance, and correctness.",
            inputSchema={
                "type": "object",
                "properties": {
                    "code": {"type": "string"},
                    "context": {"type": "string", "description": "What the code should accomplish"},
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
        ),
        Tool(
            name="mock_interview_question",
            description="Generate a mock interview question with evaluation criteria.",
            inputSchema={
                "type": "object",
                "properties": {
                    "question_type": {
                        "type": "string",
                        "enum": ["product_sense", "metrics", "sql", "statistics", "case_study", "behavioral"]
                    },
                    "difficulty": {
                        "type": "string",
                        "enum": ["easy", "medium", "hard"]
                    },
                    "company_style": {
                        "type": "string",
                        "enum": ["meta", "google", "amazon", "microsoft", "generic"],
                        "default": "generic"
                    }
                },
                "required": ["question_type", "difficulty"]
            }
        )
    ]


async def generate_case_study(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Generate a product analytics case study."""
    domain = args["domain"]
    focus_area = args["focus_area"]
    difficulty = args["difficulty"]
    time_allocation = args.get("time_allocation", 45)
    include_solution = args.get("include_sample_solution", False)
    
    case_studies = {
        ("social_media", "retention", "mid_level"): {
            "title": "User Retention Crisis",
            "scenario": """You're a Data Scientist at PhotoShare, a photo-sharing social media app with 50M monthly active users. 
The VP of Product has noticed that 30-day retention has dropped from 45% to 38% over the past quarter.

Your task is to investigate the retention drop and recommend actions.""",
            "data_available": [
                "User activity logs (views, posts, likes, comments, shares)",
                "User profile data (signup date, demographics, device type)",
                "Feature usage data (which features users engage with)",
                "Push notification engagement data",
                "App version and update history"
            ],
            "questions": [
                "How would you structure your investigation?",
                "What metrics would you look at first?",
                "What hypotheses would you form?",
                "How would you segment users to understand the problem?",
                "What recommendations would you make based on your analysis?"
            ],
            "evaluation_criteria": [
                "Structured approach to problem-solving",
                "Clear definition of retention metrics",
                "Thoughtful hypothesis generation",
                "Appropriate use of segmentation",
                "Data-driven recommendations"
            ],
            "sample_solution": {
                "approach": [
                    "1. Define retention precisely (D7, D30, rolling vs fixed cohort)",
                    "2. Segment by cohort to identify when the drop started",
                    "3. Cut by user segments (new vs existing, platform, geography)",
                    "4. Analyze feature usage patterns of retained vs churned",
                    "5. Check for external factors (app updates, competitor launches)"
                ],
                "likely_findings": [
                    "A new app update may have introduced bugs",
                    "A specific user segment (e.g., Android users) may be affected",
                    "Core feature engagement may have declined"
                ],
                "recommendations": [
                    "If bug-related: prioritize fixes and monitor recovery",
                    "If feature-related: A/B test improvements",
                    "If competition-related: analyze competitor features"
                ]
            }
        },
        ("ecommerce", "monetization", "senior"): {
            "title": "Subscription Tier Optimization",
            "scenario": """ShopFast, an e-commerce platform, is launching a premium membership program similar to Amazon Prime. 
Current proposal has three tiers:
- Basic: $5/month - Free shipping on orders >$25
- Premium: $10/month - Free shipping all orders + 5% cashback
- Ultra: $20/month - All Premium benefits + early access to sales

You need to advise on the pricing and feature structure.""",
            "data_available": [
                "Historical purchase data for all users",
                "Shipping cost per order",
                "User survey data on willingness to pay",
                "Competitor subscription pricing",
                "User engagement and frequency data"
            ],
            "questions": [
                "How would you segment users to understand potential adoption?",
                "What metrics would drive your pricing recommendations?",
                "How would you model the cannibalization between tiers?",
                "How would you A/B test the pricing?",
                "What would make you recommend launching vs not launching?"
            ]
        },
        ("fintech", "product_launch", "entry_level"): {
            "title": "New Feature Success Metrics",
            "scenario": """MoneyApp is launching a new 'Round-Up Savings' feature that automatically rounds up 
purchases to the nearest dollar and transfers the difference to a savings account.

Before launch, you need to define success metrics and create a measurement plan.""",
            "questions": [
                "What would be your North Star metric for this feature?",
                "What leading indicators would you track?",
                "How would you measure adoption vs engagement vs retention?",
                "What would constitute success at 30, 60, and 90 days post-launch?",
                "What guardrail metrics would you monitor?"
            ]
        }
    }
    
    key = (domain, focus_area, difficulty)
    case = case_studies.get(key)
    
    if not case:
        # Fallback to a generic structure
        case = {
            "title": f"{focus_area.replace('_', ' ').title()} Case Study",
            "scenario": f"You're a Data Scientist at a {domain.replace('_', ' ')} company facing a {focus_area.replace('_', ' ')} challenge.",
            "questions": [
                "How would you approach this problem?",
                "What data would you need?",
                "What metrics would you track?",
                "How would you prioritize your analysis?",
                "What recommendations would you make?"
            ]
        }
    
    result = {
        "title": case["title"],
        "domain": domain,
        "focus_area": focus_area,
        "difficulty": difficulty,
        "time_allocation_minutes": time_allocation,
        "scenario": case["scenario"],
        "questions_to_address": case["questions"]
    }
    
    if "data_available" in case:
        result["data_available"] = case["data_available"]
    
    if "evaluation_criteria" in case:
        result["evaluation_criteria"] = case["evaluation_criteria"]
    
    if include_solution and "sample_solution" in case:
        result["sample_solution"] = case["sample_solution"]
    
    return result


async def generate_behavioral_question(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Generate a behavioral interview question."""
    competency = args["competency"]
    company = args.get("company_context", "generic")
    include_follow_ups = args.get("include_follow_ups", True)
    
    questions = {
        "leadership": {
            "main": "Tell me about a time when you had to lead a project or initiative without having formal authority over the team members involved.",
            "variations": [
                "Describe a situation where you influenced a team to change direction based on your analysis.",
                "Tell me about a time you mentored someone and helped them grow."
            ],
            "follow_ups": [
                "What was your specific role?",
                "How did you get buy-in from stakeholders?",
                "What was the outcome?",
                "What would you do differently?"
            ],
            "what_they_look_for": [
                "Initiative without requiring formal authority",
                "Ability to influence through data and persuasion",
                "Self-awareness about what worked and what didn't"
            ]
        },
        "problem_solving": {
            "main": "Tell me about the most complex analytical problem you've solved. Walk me through your approach.",
            "variations": [
                "Describe a time when you had to solve a problem with incomplete data.",
                "Tell me about a time when your initial analysis led you in the wrong direction."
            ],
            "follow_ups": [
                "How did you break down the problem?",
                "What alternatives did you consider?",
                "How did you validate your solution?",
                "What tools or methods did you use?"
            ],
            "what_they_look_for": [
                "Structured problem decomposition",
                "Critical thinking and hypothesis testing",
                "Technical depth combined with business understanding"
            ]
        },
        "collaboration": {
            "main": "Tell me about a time when you had to work with a stakeholder who disagreed with your analysis or recommendations.",
            "variations": [
                "Describe a cross-functional project where you had to align multiple teams.",
                "Tell me about a time you received critical feedback on your work."
            ],
            "follow_ups": [
                "How did you understand their perspective?",
                "What did you do to reach alignment?",
                "What was the final outcome?",
                "How did the relationship evolve?"
            ],
            "what_they_look_for": [
                "Empathy and active listening",
                "Ability to explain technical concepts clearly",
                "Willingness to incorporate feedback"
            ]
        },
        "communication": {
            "main": "Tell me about a time when you had to present complex analysis to a non-technical audience. How did you make it understandable?",
            "variations": [
                "Describe how you communicated an unpopular insight to leadership.",
                "Tell me about a time when your analysis changed a major decision."
            ],
            "follow_ups": [
                "How did you structure your presentation?",
                "What visualizations did you use?",
                "How did you handle questions?",
                "What was the impact?"
            ],
            "what_they_look_for": [
                "Ability to tailor message to audience",
                "Clear and concise communication",
                "Confidence in presenting findings"
            ]
        },
        "handling_ambiguity": {
            "main": "Tell me about a time when you were given a vague problem with no clear direction. How did you approach it?",
            "variations": [
                "Describe a situation where priorities kept changing while you were working on a project.",
                "Tell me about a time when you had to make a decision with limited information."
            ],
            "follow_ups": [
                "How did you clarify the problem?",
                "What assumptions did you make?",
                "How did you manage stakeholder expectations?",
                "Looking back, was your approach correct?"
            ],
            "what_they_look_for": [
                "Comfort with uncertainty",
                "Ability to scope and prioritize",
                "Proactive communication"
            ]
        },
        "impact": {
            "main": "Tell me about the project you're most proud of. What impact did it have?",
            "variations": [
                "Describe a time when your analysis directly impacted business outcomes.",
                "Tell me about a project where you went above and beyond."
            ],
            "follow_ups": [
                "How do you measure the impact?",
                "What was your specific contribution?",
                "What would you do differently?",
                "What did you learn?"
            ],
            "what_they_look_for": [
                "Quantifiable impact",
                "Ownership and accountability",
                "Learning mindset"
            ]
        },
        "growth_mindset": {
            "main": "Tell me about a time when you made a mistake in your analysis. What happened and what did you learn?",
            "variations": [
                "Describe a skill you've been working to improve.",
                "Tell me about feedback that was hard to hear but helped you grow."
            ],
            "follow_ups": [
                "How did you discover the mistake?",
                "What steps did you take to correct it?",
                "How did you prevent it from happening again?",
                "How has this changed your approach?"
            ],
            "what_they_look_for": [
                "Self-awareness",
                "Accountability",
                "Genuine learning and improvement"
            ]
        }
    }
    
    q = questions.get(competency, questions["problem_solving"])
    
    result = {
        "competency": competency,
        "company_context": company,
        "main_question": q["main"],
        "alternative_phrasings": q["variations"],
        "what_interviewers_look_for": q["what_they_look_for"]
    }
    
    if include_follow_ups:
        result["likely_follow_up_questions"] = q["follow_ups"]
        result["tips"] = [
            "Use the STAR method: Situation, Task, Action, Result",
            "Be specific with numbers and outcomes",
            "Own your role - use 'I' not 'we'",
            "Include what you learned",
            "Practice out loud before the interview"
        ]
    
    return result


async def review_analytics_code(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Review analytics code for best practices."""
    code = args["code"]
    context = args.get("context", "")
    review_focus = args.get("review_focus", ["correctness", "best_practices"])
    
    findings = []
    
    # Check for common pandas anti-patterns
    if "pandas" in review_focus or "best_practices" in review_focus:
        if ".iterrows()" in code:
            findings.append({
                "type": "performance",
                "severity": "high",
                "line_hint": ".iterrows()",
                "issue": "Using iterrows() is slow for large DataFrames",
                "suggestion": "Consider vectorized operations, apply(), or itertuples() for better performance"
            })
        
        if "for " in code and ".append(" in code:
            findings.append({
                "type": "performance",
                "severity": "high",
                "issue": "Building DataFrame by appending in a loop is inefficient",
                "suggestion": "Collect data in a list and create DataFrame once, or use pd.concat()"
            })
        
        if "inplace=True" in code:
            findings.append({
                "type": "best_practices",
                "severity": "low",
                "issue": "inplace=True is being deprecated in future pandas versions",
                "suggestion": "Use assignment instead: df = df.dropna()"
            })
    
    # Check for statistical validity
    if "statistical_validity" in review_focus:
        if "t.test" in code.lower() or "ttest" in code.lower():
            findings.append({
                "type": "statistical",
                "severity": "info",
                "issue": "T-test detected",
                "note": "Ensure assumptions are met: independence, normality (or large n), equal variances (or use Welch's)"
            })
    
    # Check for readability
    if "readability" in review_focus:
        lines = code.split('\n')
        long_lines = [i+1 for i, line in enumerate(lines) if len(line) > 100]
        if long_lines:
            findings.append({
                "type": "readability",
                "severity": "low",
                "issue": f"Long lines detected (>100 chars) on lines: {long_lines[:5]}",
                "suggestion": "Break long lines for better readability"
            })
        
        if "lambda" in code and code.count("lambda") > 3:
            findings.append({
                "type": "readability",
                "severity": "medium",
                "issue": "Multiple lambda functions may reduce readability",
                "suggestion": "Consider named functions for complex transformations"
            })
    
    # Check for correctness patterns
    if "correctness" in review_focus:
        if "pd.merge" in code and "how=" not in code:
            findings.append({
                "type": "correctness",
                "severity": "medium",
                "issue": "pd.merge without explicit 'how' parameter defaults to inner join",
                "suggestion": "Explicitly specify join type: how='left', how='inner', etc."
            })
        
        if ".groupby(" in code and ".mean()" in code and "numeric_only" not in code:
            findings.append({
                "type": "correctness",
                "severity": "info",
                "issue": "groupby().mean() behavior may change in future pandas",
                "suggestion": "Consider adding numeric_only=True for explicit behavior"
            })
    
    summary = {
        "high_priority": len([f for f in findings if f.get("severity") == "high"]),
        "medium_priority": len([f for f in findings if f.get("severity") == "medium"]),
        "low_priority": len([f for f in findings if f.get("severity") == "low"]),
        "info": len([f for f in findings if f.get("severity") == "info"])
    }
    
    return {
        "code_reviewed": code[:500] + "..." if len(code) > 500 else code,
        "context": context,
        "review_focus": review_focus,
        "findings": findings,
        "summary": summary,
        "overall_assessment": (
            "Needs attention - high priority issues found" if summary["high_priority"] > 0 else
            "Good with minor suggestions" if summary["medium_priority"] > 0 else
            "Looks good!" if not findings else
            "Some informational notes"
        )
    }


async def mock_interview_question(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Generate a mock interview question."""
    question_type = args["question_type"]
    difficulty = args["difficulty"]
    company_style = args.get("company_style", "generic")
    
    questions = {
        ("product_sense", "medium"): {
            "question": "Instagram is considering launching a feature that allows users to schedule posts in advance. How would you evaluate whether to build this feature?",
            "time_allocation": "20-25 minutes",
            "structure_hint": "Think about: target users, use cases, success metrics, potential risks, prioritization",
            "evaluation_criteria": [
                "Identifies clear user segments who would benefit",
                "Considers both creator and consumer perspectives",
                "Proposes reasonable success metrics",
                "Acknowledges tradeoffs and risks"
            ]
        },
        ("metrics", "medium"): {
            "question": "You're a data scientist at a ride-sharing company. Rides have been declining for the past month. Walk me through how you would investigate this.",
            "time_allocation": "25-30 minutes",
            "structure_hint": "Consider: defining the metric precisely, segmentation, external factors, funnel analysis",
            "evaluation_criteria": [
                "Asks clarifying questions",
                "Structures investigation logically",
                "Considers multiple hypotheses",
                "Proposes data-driven next steps"
            ]
        },
        ("sql", "hard"): {
            "question": """Given tables:
users(user_id, signup_date, country)
sessions(session_id, user_id, session_date, session_duration)

Write a query to find the country with the highest average 7-day retained users, 
where retention is defined as users who had a session within 7 days of signup.""",
            "time_allocation": "15-20 minutes",
            "evaluation_criteria": [
                "Correct join logic",
                "Proper date handling",
                "Efficient query structure",
                "Handles edge cases"
            ]
        },
        ("case_study", "hard"): {
            "question": "Spotify notices that podcast listening has plateaued after rapid growth. The team hypothesizes that the discovery experience is the problem. Design an experiment to test improvements to podcast recommendations.",
            "time_allocation": "30-35 minutes",
            "evaluation_criteria": [
                "Clear hypothesis formulation",
                "Appropriate metric selection",
                "Thoughtful experiment design",
                "Consideration of risks and guardrails"
            ]
        }
    }
    
    key = (question_type, difficulty)
    q = questions.get(key)
    
    if not q:
        # Fallback
        q = {
            "question": f"A {difficulty} {question_type.replace('_', ' ')} question would be presented here.",
            "time_allocation": "20-30 minutes",
            "evaluation_criteria": ["Clear thinking", "Structured approach", "Data-driven reasoning"]
        }
    
    return {
        "question_type": question_type,
        "difficulty": difficulty,
        "company_style": company_style,
        "question": q["question"],
        "time_allocation": q["time_allocation"],
        "structure_hint": q.get("structure_hint", ""),
        "evaluation_criteria": q["evaluation_criteria"],
        "tips": [
            "Ask clarifying questions before diving in",
            "Think out loud to show your reasoning",
            "Structure your answer before going into details",
            "It's okay to make assumptions - just state them"
        ]
    }


# Handler registry
TOOL_HANDLERS: dict[str, Callable[[dict[str, Any], Config], Coroutine[Any, Any, dict[str, Any]]]] = {
    "generate_case_study": generate_case_study,
    "generate_behavioral_question": generate_behavioral_question,
    "review_analytics_code": review_analytics_code,
    "mock_interview_question": mock_interview_question,
}

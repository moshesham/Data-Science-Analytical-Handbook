"""A/B Testing tools."""

import math
from typing import Any, Callable, Coroutine

from mcp.types import Tool
from scipy import stats

from ds_interview_mcp.config import Config


def get_tool_definitions() -> list[Tool]:
    """Return A/B testing tool definitions."""
    return [
        Tool(
            name="design_ab_experiment",
            description="Help design a complete A/B test experiment with metrics, sample size, and analysis plan.",
            inputSchema={
                "type": "object",
                "properties": {
                    "hypothesis": {"type": "string", "description": "The hypothesis to test"},
                    "primary_metric": {"type": "string", "description": "Primary success metric"},
                    "baseline_rate": {"type": "number", "description": "Current baseline rate"},
                    "minimum_detectable_effect": {"type": "number", "description": "Minimum relative lift"},
                    "daily_traffic": {"type": "integer", "description": "Daily eligible users"},
                    "significance_level": {"type": "number", "default": 0.05},
                    "power": {"type": "number", "default": 0.8},
                    "guardrail_metrics": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["hypothesis", "primary_metric", "baseline_rate", "minimum_detectable_effect"]
            }
        ),
        Tool(
            name="analyze_ab_results",
            description="Analyze A/B test results and provide statistical interpretation.",
            inputSchema={
                "type": "object",
                "properties": {
                    "control_conversions": {"type": "integer"},
                    "control_total": {"type": "integer"},
                    "treatment_conversions": {"type": "integer"},
                    "treatment_total": {"type": "integer"},
                    "metric_type": {
                        "type": "string",
                        "enum": ["proportion", "mean"],
                        "default": "proportion"
                    },
                    "control_mean": {"type": "number"},
                    "treatment_mean": {"type": "number"},
                    "control_std": {"type": "number"},
                    "treatment_std": {"type": "number"}
                },
                "required": ["control_total", "treatment_total"]
            }
        ),
        Tool(
            name="generate_ab_scenario",
            description="Generate an A/B testing interview scenario with questions.",
            inputSchema={
                "type": "object",
                "properties": {
                    "company_type": {
                        "type": "string",
                        "enum": ["social_media", "ecommerce", "fintech", "streaming", "marketplace"]
                    },
                    "scenario_type": {
                        "type": "string",
                        "enum": ["design", "analysis", "debugging", "decision"]
                    },
                    "difficulty": {
                        "type": "string",
                        "enum": ["junior", "mid", "senior"]
                    },
                    "include_data": {"type": "boolean", "default": True}
                },
                "required": ["company_type", "scenario_type", "difficulty"]
            }
        ),
        Tool(
            name="detect_ab_pitfalls",
            description="Analyze an A/B test design for common pitfalls and mistakes.",
            inputSchema={
                "type": "object",
                "properties": {
                    "experiment_description": {"type": "string"},
                    "randomization_unit": {"type": "string"},
                    "metrics": {"type": "array", "items": {"type": "string"}},
                    "duration_days": {"type": "integer"},
                    "traffic_percentage": {"type": "number"}
                },
                "required": ["experiment_description"]
            }
        )
    ]


async def design_ab_experiment(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Design a complete A/B experiment."""
    hypothesis = args["hypothesis"]
    primary_metric = args["primary_metric"]
    baseline = args["baseline_rate"]
    mde = args["minimum_detectable_effect"]
    daily_traffic = args.get("daily_traffic", 10000)
    alpha = args.get("significance_level", 0.05)
    power = args.get("power", 0.8)
    guardrails = args.get("guardrail_metrics", [])
    
    # Calculate sample size
    expected = baseline * (1 + mde)
    pooled_var = (baseline * (1 - baseline) + expected * (1 - expected)) / 2
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(power)
    
    effect = abs(expected - baseline)
    n_per_variant = math.ceil(
        ((z_alpha + z_beta) ** 2 * 2 * pooled_var) / (effect ** 2)
    )
    
    total_needed = n_per_variant * 2
    days_needed = math.ceil(total_needed / daily_traffic) if daily_traffic > 0 else "N/A"
    
    return {
        "experiment_design": {
            "hypothesis_statement": hypothesis,
            "null_hypothesis": f"There is no difference in {primary_metric} between control and treatment",
            "alternative_hypothesis": f"Treatment affects {primary_metric}",
            "randomization_unit": "user_id (recommended)",
            "traffic_split": "50/50 control/treatment"
        },
        "sample_size": {
            "per_variant": n_per_variant,
            "total": total_needed,
            "estimated_duration_days": days_needed,
            "based_on": {
                "baseline_rate": f"{baseline * 100:.1f}%",
                "minimum_detectable_effect": f"{mde * 100:.1f}% relative lift",
                "power": f"{power * 100:.0f}%",
                "significance_level": f"{alpha * 100:.1f}%"
            }
        },
        "metrics": {
            "primary": primary_metric,
            "secondary": [
                f"Components of {primary_metric}",
                "User engagement metrics"
            ],
            "guardrails": guardrails if guardrails else [
                "Page load time",
                "Error rate",
                "Overall user satisfaction"
            ]
        },
        "analysis_plan": {
            "statistical_test": "Two-proportion z-test" if baseline < 1 else "Two-sample t-test",
            "corrections_needed": "Bonferroni if testing multiple variants",
            "decision_criteria": f"Ship if p < {alpha} AND practical significance threshold met"
        },
        "pre_experiment_checklist": [
            "✓ Verify randomization is working (AA test)",
            "✓ Confirm logging is in place for all metrics",
            "✓ Document experiment in experiment management system",
            "✓ Set up monitoring dashboards",
            "✓ Define rollback criteria"
        ],
        "potential_pitfalls": [
            "Novelty effect - new features may show inflated initial results",
            "Carryover effects - if users are exposed to both variants",
            "Selection bias - ensure randomization is truly random",
            "Multiple testing - adjust confidence level if peeking at results"
        ],
        "recommendations": [
            f"Run for at least {max(days_needed, 7)} days to capture weekly patterns",
            "Don't peek at results before reaching required sample size",
            "Watch guardrail metrics throughout the experiment",
            "Document all decisions and findings"
        ]
    }


async def analyze_ab_results(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Analyze A/B test results."""
    metric_type = args.get("metric_type", "proportion")
    
    if metric_type == "proportion":
        control_conv = args.get("control_conversions", 0)
        control_n = args["control_total"]
        treatment_conv = args.get("treatment_conversions", 0)
        treatment_n = args["treatment_total"]
        
        # Calculate rates
        p_control = control_conv / control_n if control_n > 0 else 0
        p_treatment = treatment_conv / treatment_n if treatment_n > 0 else 0
        
        # Pooled proportion
        pooled_p = (control_conv + treatment_conv) / (control_n + treatment_n)
        
        # Standard error
        se = math.sqrt(pooled_p * (1 - pooled_p) * (1/control_n + 1/treatment_n))
        
        # Z-statistic and p-value
        if se > 0:
            z_stat = (p_treatment - p_control) / se
            p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        else:
            z_stat = 0
            p_value = 1.0
        
        # Confidence interval for the difference
        diff = p_treatment - p_control
        se_diff = math.sqrt(
            (p_control * (1 - p_control) / control_n) +
            (p_treatment * (1 - p_treatment) / treatment_n)
        )
        ci_lower = diff - 1.96 * se_diff
        ci_upper = diff + 1.96 * se_diff
        
        # Relative lift
        relative_lift = (p_treatment - p_control) / p_control if p_control > 0 else 0
        
        return {
            "summary": {
                "metric_type": "proportion",
                "control_rate": f"{p_control * 100:.2f}%",
                "treatment_rate": f"{p_treatment * 100:.2f}%",
                "absolute_difference": f"{diff * 100:.2f}%",
                "relative_lift": f"{relative_lift * 100:.2f}%"
            },
            "statistical_analysis": {
                "test_used": "Two-proportion z-test",
                "z_statistic": round(z_stat, 4),
                "p_value": round(p_value, 4),
                "significant_at_05": p_value < 0.05,
                "significant_at_01": p_value < 0.01
            },
            "confidence_interval": {
                "level": "95%",
                "lower_bound": f"{ci_lower * 100:.2f}%",
                "upper_bound": f"{ci_upper * 100:.2f}%",
                "interpretation": f"We are 95% confident the true difference is between {ci_lower * 100:.2f}% and {ci_upper * 100:.2f}%"
            },
            "sample_sizes": {
                "control": control_n,
                "treatment": treatment_n,
                "total": control_n + treatment_n
            },
            "recommendation": (
                "The result is statistically significant. Consider shipping if practical significance is also met."
                if p_value < 0.05 else
                "The result is not statistically significant. Consider running longer or accepting no meaningful difference."
            ),
            "cautions": [
                "Ensure the experiment ran for sufficient time",
                "Check for segment-level differences",
                "Verify no data quality issues",
                "Consider novelty effects if feature is new"
            ]
        }
    else:
        # Mean metric analysis
        control_mean = args.get("control_mean", 0)
        treatment_mean = args.get("treatment_mean", 0)
        control_std = args.get("control_std", 1)
        treatment_std = args.get("treatment_std", 1)
        control_n = args["control_total"]
        treatment_n = args["treatment_total"]
        
        # Welch's t-test
        se = math.sqrt((control_std**2 / control_n) + (treatment_std**2 / treatment_n))
        t_stat = (treatment_mean - control_mean) / se if se > 0 else 0
        
        # Degrees of freedom (Welch-Satterthwaite)
        num = ((control_std**2 / control_n) + (treatment_std**2 / treatment_n))**2
        denom = ((control_std**2 / control_n)**2 / (control_n - 1)) + \
                ((treatment_std**2 / treatment_n)**2 / (treatment_n - 1))
        df = num / denom if denom > 0 else min(control_n, treatment_n) - 1
        
        p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
        
        return {
            "summary": {
                "metric_type": "mean",
                "control_mean": round(control_mean, 4),
                "treatment_mean": round(treatment_mean, 4),
                "difference": round(treatment_mean - control_mean, 4),
                "relative_change": f"{((treatment_mean - control_mean) / control_mean * 100):.2f}%" if control_mean != 0 else "N/A"
            },
            "statistical_analysis": {
                "test_used": "Welch's t-test",
                "t_statistic": round(t_stat, 4),
                "degrees_of_freedom": round(df, 2),
                "p_value": round(p_value, 4),
                "significant_at_05": p_value < 0.05
            },
            "sample_sizes": {
                "control": control_n,
                "treatment": treatment_n
            }
        }


async def generate_ab_scenario(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Generate an A/B testing interview scenario."""
    company_type = args["company_type"]
    scenario_type = args["scenario_type"]
    difficulty = args["difficulty"]
    include_data = args.get("include_data", True)
    
    scenarios = {
        ("social_media", "design", "mid"): {
            "title": "Story Feature Redesign",
            "context": """You're a Data Scientist at a social media company. The product team wants to 
test a new Stories format that shows stories in a horizontal scrollable feed instead of 
the current circular bubbles at the top of the feed.

The hypothesis is that the horizontal feed will increase story consumption because 
it takes up more screen real estate and shows preview thumbnails.""",
            "questions": [
                "What would be your primary metric for this experiment?",
                "What secondary and guardrail metrics would you track?",
                "How would you handle users who use both mobile and web?",
                "The team wants to detect a 5% lift in story views per user. If we have 10M daily active users and the current average is 3 stories viewed per day, how long do you need to run this test?",
                "What potential pitfalls should we watch for?"
            ],
            "data": {
                "dau": 10_000_000,
                "baseline_stories_viewed": 3.0,
                "baseline_story_creation": 0.15,
                "std_dev_views": 5.2
            }
        },
        ("ecommerce", "analysis", "senior"): {
            "title": "Checkout Flow Anomaly",
            "context": """You're analyzing an A/B test on the checkout page. The test simplified the 
checkout process from 3 steps to 2 steps. After 2 weeks, you see:

- Control (3-step): 50,000 visitors, 2,500 conversions (5.0%)
- Treatment (2-step): 50,000 visitors, 2,750 conversions (5.5%)
- p-value: 0.03

However, when you segment by device:
- Desktop: Control 3.8%, Treatment 4.2% (p=0.08)
- Mobile: Control 6.5%, Treatment 7.1% (p=0.12)

The PM is confused - if both segments are not significant, why is the overall result significant?""",
            "questions": [
                "Explain Simpson's paradox and whether it applies here.",
                "What additional analysis would you do?",
                "Should the team ship this change?",
                "How would you present these findings to stakeholders?"
            ],
            "data": {
                "control_total": 50000,
                "treatment_total": 50000,
                "control_conversions": 2500,
                "treatment_conversions": 2750,
                "desktop_share_control": 0.60,
                "desktop_share_treatment": 0.55
            }
        },
        ("streaming", "debugging", "senior"): {
            "title": "Watch Time Regression",
            "context": """A streaming service ran an experiment on their recommendation algorithm. 
Initial results showed a 3% increase in watch time (p < 0.01). The team shipped it.

Two weeks later, executives notice that:
1. Overall watch time has dropped 5% compared to pre-experiment levels
2. Premium subscription downgrades increased by 15%
3. Customer support tickets about "can't find anything to watch" tripled

You're asked to investigate what went wrong.""",
            "questions": [
                "What could cause positive experiment results but negative long-term outcomes?",
                "What metrics should have been guardrailed?",
                "How would you diagnose the root cause?",
                "What changes would you recommend to the experimentation process?"
            ],
            "hints": [
                "Consider novelty effects",
                "Think about what 'watch time' actually measures",
                "Consider content diversity metrics"
            ]
        },
        ("fintech", "decision", "mid"): {
            "title": "Feature Rollout Decision",
            "context": """Your payments app tested a new feature that shows users how much they've 
spent in each category (food, transport, entertainment) with a weekly summary notification.

Results after 4 weeks:
- Primary metric (DAU): +2.1% (p=0.04)
- Transactions per user: -0.5% (p=0.32)
- Revenue per user: -0.8% (p=0.21)
- Push notification opt-out rate: +8% (p=0.001)

The PM wants to ship. The revenue team is concerned.""",
            "questions": [
                "How would you frame the decision?",
                "What additional data would help make the decision?",
                "How do you weigh short-term engagement vs. long-term business metrics?",
                "What would be your recommendation and why?"
            ]
        }
    }
    
    # Find matching scenario or fallback
    key = (company_type, scenario_type, difficulty)
    scenario = scenarios.get(key)
    
    if not scenario:
        # Fallback to any matching company_type
        for k, v in scenarios.items():
            if k[0] == company_type:
                scenario = v
                break
    
    if not scenario:
        scenario = list(scenarios.values())[0]
    
    result = {
        "title": scenario["title"],
        "company_type": company_type,
        "scenario_type": scenario_type,
        "difficulty": difficulty,
        "context": scenario["context"],
        "questions": scenario["questions"]
    }
    
    if include_data and "data" in scenario:
        result["data"] = scenario["data"]
    
    if "hints" in scenario:
        result["hints"] = scenario["hints"]
    
    return result


async def detect_ab_pitfalls(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Analyze A/B test design for common pitfalls."""
    description = args["experiment_description"]
    randomization_unit = args.get("randomization_unit", "unknown")
    metrics = args.get("metrics", [])
    duration = args.get("duration_days", 0)
    traffic_pct = args.get("traffic_percentage", 100)
    
    findings = []
    warnings = []
    recommendations = []
    
    description_lower = description.lower()
    
    # Check for network effects
    if any(word in description_lower for word in ["social", "share", "friend", "message", "feed"]):
        if randomization_unit.lower() in ["user", "user_id", "userid"]:
            findings.append({
                "issue": "Potential SUTVA violation (network effects)",
                "severity": "high",
                "explanation": "Social features may violate Stable Unit Treatment Value Assumption. Users in control may be affected by treatment users' behavior.",
                "recommendation": "Consider cluster randomization by social graph or use geo-based randomization"
            })
    
    # Check duration
    if duration > 0:
        if duration < 7:
            warnings.append({
                "issue": "Short experiment duration",
                "concern": "Less than a week may miss weekly patterns (e.g., weekend vs weekday behavior)",
                "recommendation": "Run for at least 1-2 full weeks"
            })
        elif duration < 14 and any(word in description_lower for word in ["subscription", "purchase", "payment", "revenue"]):
            warnings.append({
                "issue": "Duration may be too short for revenue metrics",
                "concern": "Revenue impacts may take time to materialize",
                "recommendation": "Consider running for 2-4 weeks for revenue-related experiments"
            })
    
    # Check traffic percentage
    if traffic_pct < 1:
        warnings.append({
            "issue": "Very small traffic percentage",
            "concern": f"At {traffic_pct}% traffic, reaching statistical significance may take very long",
            "recommendation": "Increase traffic if the feature is low-risk"
        })
    elif traffic_pct > 50:
        warnings.append({
            "issue": "High traffic exposure",
            "concern": f"Exposing {traffic_pct}% of users limits ability to detect negative impacts",
            "recommendation": "Start with smaller percentage for risky changes"
        })
    
    # Check for multiple metrics without correction
    if len(metrics) > 3:
        findings.append({
            "issue": "Multiple testing problem",
            "severity": "medium",
            "explanation": f"Testing {len(metrics)} metrics increases false positive risk",
            "recommendation": "Clearly define 1-2 primary metrics. Apply Bonferroni or FDR correction for secondary metrics"
        })
    
    # Check for common experiment design issues
    if "notification" in description_lower or "email" in description_lower:
        findings.append({
            "issue": "Notification/email experiment considerations",
            "severity": "medium",
            "explanation": "Frequency and timing of notifications can have long-term effects on user opt-outs",
            "recommendation": "Include notification opt-out rate as a guardrail metric. Consider delayed effects"
        })
    
    if "algorithm" in description_lower or "recommendation" in description_lower or "ml" in description_lower:
        findings.append({
            "issue": "ML/Algorithm experiment considerations",
            "severity": "medium",
            "explanation": "Recommendation changes may have exploration/exploitation tradeoffs",
            "recommendation": "Monitor diversity metrics. Watch for long-term engagement vs short-term metrics"
        })
    
    # Check randomization unit
    if randomization_unit.lower() in ["session", "request", "page_view"]:
        findings.append({
            "issue": "Session/request-level randomization",
            "severity": "high",
            "explanation": "Same user may see both variants across sessions, contaminating the experiment",
            "recommendation": "Use user-level randomization unless specifically testing session-level behavior"
        })
    
    # General recommendations
    recommendations = [
        "Run an AA test first to validate randomization",
        "Pre-register your hypothesis and primary metrics",
        "Set guardrail metrics that must not regress",
        "Document minimum detectable effect before starting",
        "Plan for what happens if results are inconclusive"
    ]
    
    return {
        "experiment_summary": {
            "description": description[:200] + "..." if len(description) > 200 else description,
            "randomization_unit": randomization_unit,
            "metrics_count": len(metrics),
            "planned_duration": f"{duration} days" if duration > 0 else "Not specified",
            "traffic_percentage": f"{traffic_pct}%"
        },
        "findings": findings,
        "warnings": warnings,
        "recommendations": recommendations,
        "overall_risk": (
            "HIGH" if any(f["severity"] == "high" for f in findings) else
            "MEDIUM" if findings or warnings else
            "LOW"
        )
    }


# Handler registry
TOOL_HANDLERS: dict[str, Callable[[dict[str, Any], Config], Coroutine[Any, Any, dict[str, Any]]]] = {
    "design_ab_experiment": design_ab_experiment,
    "analyze_ab_results": analyze_ab_results,
    "generate_ab_scenario": generate_ab_scenario,
    "detect_ab_pitfalls": detect_ab_pitfalls,
}

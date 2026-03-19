"""Statistics and probability tools."""

import math
from typing import Any, Callable, Coroutine

from mcp.types import Tool
from scipy import stats

from ds_interview_mcp.config import Config


def get_tool_definitions() -> list[Tool]:
    """Return statistics tool definitions."""
    return [
        Tool(
            name="generate_stats_problem",
            description="Generate a statistics or probability practice problem.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "enum": ["descriptive_stats", "probability", "hypothesis_testing", "confidence_intervals", "distributions", "regression", "bayesian"]
                    },
                    "difficulty": {
                        "type": "string",
                        "enum": ["beginner", "intermediate", "advanced"]
                    },
                    "context": {
                        "type": "string",
                        "description": "Real-world context"
                    },
                    "include_solution": {"type": "boolean", "default": False}
                },
                "required": ["topic", "difficulty"]
            }
        ),
        Tool(
            name="calculate_sample_size",
            description="Calculate required sample size for an A/B test or survey.",
            inputSchema={
                "type": "object",
                "properties": {
                    "metric_type": {
                        "type": "string",
                        "enum": ["proportion", "mean"]
                    },
                    "baseline_value": {
                        "type": "number",
                        "description": "Current baseline value"
                    },
                    "minimum_detectable_effect": {
                        "type": "number",
                        "description": "Minimum relative lift to detect"
                    },
                    "standard_deviation": {
                        "type": "number",
                        "description": "Standard deviation (for mean metrics)"
                    },
                    "alpha": {"type": "number", "default": 0.05},
                    "power": {"type": "number", "default": 0.8},
                    "sides": {
                        "type": "string",
                        "enum": ["one", "two"],
                        "default": "two"
                    }
                },
                "required": ["metric_type", "baseline_value", "minimum_detectable_effect"]
            }
        ),
        Tool(
            name="explain_distribution",
            description="Explain a statistical distribution with examples and use cases.",
            inputSchema={
                "type": "object",
                "properties": {
                    "distribution": {
                        "type": "string",
                        "enum": ["normal", "binomial", "poisson", "exponential", "uniform", "beta", "gamma", "chi_squared", "t_distribution"]
                    },
                    "include_examples": {"type": "boolean", "default": True},
                    "include_formulas": {"type": "boolean", "default": True}
                },
                "required": ["distribution"]
            }
        )
    ]


async def generate_stats_problem(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Generate a statistics practice problem."""
    topic = args["topic"]
    difficulty = args["difficulty"]
    context = args.get("context", "product analytics")
    include_solution = args.get("include_solution", False)
    
    # Problem templates by topic and difficulty
    problems = {
        "hypothesis_testing": {
            "beginner": {
                "title": "Basic Hypothesis Test",
                "problem": """A product team claims their new feature increases user engagement. 
In a sample of 100 users with the feature, the average session time was 8.5 minutes 
with a standard deviation of 2 minutes. The historical average is 8 minutes.

At α = 0.05, is there evidence that the feature increases engagement?""",
                "data": {
                    "sample_mean": 8.5,
                    "population_mean": 8.0,
                    "std_dev": 2.0,
                    "sample_size": 100,
                    "alpha": 0.05
                },
                "solution": {
                    "approach": "One-sample t-test or z-test",
                    "steps": [
                        "H₀: μ = 8, H₁: μ > 8 (one-tailed)",
                        "Calculate test statistic: z = (8.5 - 8) / (2 / √100) = 2.5",
                        "Find p-value: P(Z > 2.5) ≈ 0.0062",
                        "Compare: 0.0062 < 0.05"
                    ],
                    "conclusion": "Reject H₀. There is significant evidence the feature increases engagement."
                }
            },
            "intermediate": {
                "title": "Two-Sample Comparison",
                "problem": """Two versions of a landing page were tested:
- Version A: 1,000 visitors, 50 conversions
- Version B: 1,000 visitors, 65 conversions

At α = 0.05, is there a significant difference between the two versions?""",
                "data": {
                    "n1": 1000, "x1": 50,
                    "n2": 1000, "x2": 65,
                    "alpha": 0.05
                },
                "solution": {
                    "approach": "Two-proportion z-test",
                    "steps": [
                        "p₁ = 50/1000 = 0.05, p₂ = 65/1000 = 0.065",
                        "Pooled proportion: p̂ = 115/2000 = 0.0575",
                        "SE = √(p̂(1-p̂)(1/n₁ + 1/n₂)) = √(0.0575 × 0.9425 × 0.002) ≈ 0.0104",
                        "z = (0.065 - 0.05) / 0.0104 ≈ 1.44",
                        "Two-tailed p-value ≈ 0.15"
                    ],
                    "conclusion": "Fail to reject H₀. No significant difference at α = 0.05."
                }
            },
            "advanced": {
                "title": "Power Analysis",
                "problem": """You're designing an A/B test where:
- Current conversion rate: 5%
- You want to detect a 20% relative improvement (to 6%)
- Desired power: 80%
- Significance level: 5%

How many users do you need per variant? What if you want 90% power?""",
                "data": {
                    "baseline": 0.05,
                    "expected": 0.06,
                    "mde": 0.20,
                    "power_80": 0.80,
                    "power_90": 0.90,
                    "alpha": 0.05
                },
                "solution": {
                    "approach": "Sample size calculation for proportions",
                    "formula": "n = 2 × ((Z_α/2 + Z_β)² × p̄(1-p̄)) / (p₂ - p₁)²",
                    "calculations": {
                        "80%_power": "~6,200 per variant",
                        "90%_power": "~8,200 per variant"
                    },
                    "insight": "Increasing power from 80% to 90% requires ~32% more sample"
                }
            }
        },
        "probability": {
            "beginner": {
                "title": "Basic Probability",
                "problem": """A user can be classified as:
- New (30% of users)
- Returning (50% of users)
- Churned (20% of users)

If a returning user has a 60% chance of making a purchase, and we randomly select 
a user who made a purchase, what's the probability they are a returning user?

Assume: New users have 10% purchase rate, churned users have 5% purchase rate.""",
                "solution": {
                    "approach": "Bayes' Theorem",
                    "steps": [
                        "P(Purchase) = 0.3×0.1 + 0.5×0.6 + 0.2×0.05 = 0.34",
                        "P(Returning|Purchase) = (0.5 × 0.6) / 0.34 ≈ 0.882"
                    ],
                    "answer": "About 88.2% probability"
                }
            }
        },
        "confidence_intervals": {
            "intermediate": {
                "title": "Confidence Interval Interpretation",
                "problem": """An A/B test shows:
- Control: 5.0% conversion rate (n=10,000)
- Treatment: 5.5% conversion rate (n=10,000)
- 95% CI for the difference: [0.1%, 0.9%]

Interpret this result. Would you ship the treatment? What additional factors 
would you consider?""",
                "solution": {
                    "interpretation": [
                        "The CI doesn't include 0, so the result is statistically significant at α=0.05",
                        "We're 95% confident the true lift is between 0.1% and 0.9% absolute",
                        "This is a 2-18% relative improvement (0.1/5 to 0.9/5)"
                    ],
                    "considerations": [
                        "Practical significance: Is 0.1% absolute lift worth the engineering cost?",
                        "Guardrail metrics: Any negative impacts on other KPIs?",
                        "Segment analysis: Does it help all user segments?",
                        "Long-term effects: Is this a novelty effect?"
                    ]
                }
            }
        }
    }
    
    # Get problem or fallback
    topic_problems = problems.get(topic, problems["hypothesis_testing"])
    problem_data = topic_problems.get(difficulty, list(topic_problems.values())[0])
    
    result = {
        "title": problem_data["title"],
        "topic": topic,
        "difficulty": difficulty,
        "context": context,
        "problem": problem_data["problem"],
    }
    
    if "data" in problem_data:
        result["data"] = problem_data["data"]
    
    if include_solution:
        result["solution"] = problem_data["solution"]
    
    return result


async def calculate_sample_size(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Calculate required sample size for A/B testing."""
    metric_type = args["metric_type"]
    baseline = args["baseline_value"]
    mde = args["minimum_detectable_effect"]  # relative lift
    std_dev = args.get("standard_deviation")
    alpha = args.get("alpha", 0.05)
    power = args.get("power", 0.8)
    sides = args.get("sides", "two")
    
    # Get z-scores
    if sides == "two":
        z_alpha = stats.norm.ppf(1 - alpha / 2)
    else:
        z_alpha = stats.norm.ppf(1 - alpha)
    z_beta = stats.norm.ppf(power)
    
    if metric_type == "proportion":
        # Proportion metric
        p1 = baseline
        p2 = baseline * (1 + mde)  # expected rate after lift
        
        # Pooled proportion for sample size calculation
        p_avg = (p1 + p2) / 2
        
        # Sample size formula for two proportions
        effect = abs(p2 - p1)
        variance = p1 * (1 - p1) + p2 * (1 - p2)
        
        n_per_variant = math.ceil(
            ((z_alpha + z_beta) ** 2 * variance) / (effect ** 2)
        )
    else:
        # Mean metric
        if std_dev is None:
            return {
                "error": {
                    "code": "MISSING_PARAMETER",
                    "message": "standard_deviation required for mean metrics"
                }
            }
        
        # Effect size in absolute terms
        effect = baseline * mde
        
        # Sample size for two-sample t-test
        n_per_variant = math.ceil(
            2 * ((z_alpha + z_beta) ** 2 * std_dev ** 2) / (effect ** 2)
        )
    
    total_sample = n_per_variant * 2
    
    return {
        "metric_type": metric_type,
        "baseline_value": baseline,
        "expected_value": baseline * (1 + mde) if metric_type == "proportion" else baseline + baseline * mde,
        "minimum_detectable_effect": f"{mde * 100:.1f}% relative lift",
        "alpha": alpha,
        "power": power,
        "test_type": f"{sides}-sided",
        "sample_size": {
            "per_variant": n_per_variant,
            "total": total_sample
        },
        "notes": [
            f"Based on {power * 100:.0f}% power and {alpha * 100:.1f}% significance level",
            "Assumes equal sample sizes per variant",
            "For sequential testing, consider adjusting for multiple looks"
        ]
    }


async def explain_distribution(args: dict[str, Any], config: Config) -> dict[str, Any]:
    """Explain a statistical distribution."""
    distribution = args["distribution"]
    include_examples = args.get("include_examples", True)
    include_formulas = args.get("include_formulas", True)
    
    distributions = {
        "normal": {
            "name": "Normal (Gaussian) Distribution",
            "description": "A symmetric, bell-shaped distribution defined by its mean (μ) and standard deviation (σ). Many natural phenomena follow this distribution due to the Central Limit Theorem.",
            "parameters": ["μ (mean)", "σ (standard deviation)"],
            "properties": [
                "Symmetric around the mean",
                "68-95-99.7 rule: 68% within 1σ, 95% within 2σ, 99.7% within 3σ",
                "Mean = Median = Mode"
            ],
            "pdf": "f(x) = (1 / (σ√(2π))) × e^(-(x-μ)²/(2σ²))",
            "examples": [
                "Heights of adults in a population",
                "Measurement errors",
                "Sample means (by CLT)"
            ],
            "ds_applications": [
                "Confidence intervals for means",
                "Z-tests and t-tests",
                "Many ML algorithms assume normally distributed errors"
            ]
        },
        "binomial": {
            "name": "Binomial Distribution",
            "description": "Models the number of successes in n independent trials, each with probability p of success.",
            "parameters": ["n (number of trials)", "p (probability of success)"],
            "properties": [
                "Discrete distribution",
                "Mean = n × p",
                "Variance = n × p × (1-p)",
                "Approaches normal as n increases"
            ],
            "pmf": "P(X=k) = C(n,k) × p^k × (1-p)^(n-k)",
            "examples": [
                "Number of conversions out of n visitors",
                "Number of defective items in a batch",
                "Number of heads in n coin flips"
            ],
            "ds_applications": [
                "A/B test analysis (conversion rates)",
                "Click-through rate modeling",
                "Quality control"
            ]
        },
        "poisson": {
            "name": "Poisson Distribution",
            "description": "Models the number of events occurring in a fixed interval when events happen independently at a constant average rate.",
            "parameters": ["λ (lambda, average rate)"],
            "properties": [
                "Discrete distribution",
                "Mean = Variance = λ",
                "Good approximation for rare events"
            ],
            "pmf": "P(X=k) = (λ^k × e^(-λ)) / k!",
            "examples": [
                "Number of customer support tickets per hour",
                "Server requests per second",
                "Number of app crashes per day"
            ],
            "ds_applications": [
                "Anomaly detection in event counts",
                "Traffic modeling",
                "Queueing theory"
            ]
        },
        "exponential": {
            "name": "Exponential Distribution",
            "description": "Models the time between events in a Poisson process. It's the continuous analog of the geometric distribution.",
            "parameters": ["λ (rate parameter) or β = 1/λ (scale parameter)"],
            "properties": [
                "Continuous distribution",
                "Memoryless property",
                "Mean = 1/λ",
                "Variance = 1/λ²"
            ],
            "pdf": "f(x) = λ × e^(-λx) for x ≥ 0",
            "examples": [
                "Time between customer arrivals",
                "Time till component failure",
                "Time between website visits"
            ],
            "ds_applications": [
                "Survival analysis",
                "Churn modeling",
                "A/B test time-to-event analysis"
            ]
        },
        "beta": {
            "name": "Beta Distribution",
            "description": "A continuous distribution on [0,1], commonly used as a prior for probabilities in Bayesian inference.",
            "parameters": ["α (alpha, shape)", "β (beta, shape)"],
            "properties": [
                "Bounded between 0 and 1",
                "Very flexible shape depending on α and β",
                "Conjugate prior for binomial likelihood"
            ],
            "pdf": "f(x) = (x^(α-1) × (1-x)^(β-1)) / B(α,β)",
            "examples": [
                "Conversion rate uncertainty",
                "Probability of success",
                "Proportion data"
            ],
            "ds_applications": [
                "Bayesian A/B testing",
                "Thompson Sampling for bandits",
                "Modeling proportions"
            ]
        }
    }
    
    dist_info = distributions.get(distribution, distributions["normal"])
    
    result = {
        "name": dist_info["name"],
        "description": dist_info["description"],
        "parameters": dist_info["parameters"],
        "properties": dist_info["properties"]
    }
    
    if include_formulas:
        result["formula"] = dist_info.get("pdf", dist_info.get("pmf", ""))
    
    if include_examples:
        result["examples"] = dist_info.get("examples", [])
        result["ds_applications"] = dist_info.get("ds_applications", [])
    
    return result


# Handler registry
TOOL_HANDLERS: dict[str, Callable[[dict[str, Any], Config], Coroutine[Any, Any, dict[str, Any]]]] = {
    "generate_stats_problem": generate_stats_problem,
    "calculate_sample_size": calculate_sample_size,
    "explain_distribution": explain_distribution,
}

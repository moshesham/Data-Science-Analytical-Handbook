---
name: market-research-reports
description: 'Generate comprehensive market research and analysis reports. Use when: analyzing grant funding landscapes, market sizing exercises, competitive analysis of funding sources, strategic planning for grant applications, creating investment or business case documentation.'
---

# Market Research Reports

## Overview

Generate comprehensive market research and analysis reports for strategic decision-making. This skill applies professional analysis frameworks to understand funding landscapes, competitive dynamics, and market opportunities relevant to grant seeking and research planning.

## When to Use

- Analyzing funding agency landscapes and trends
- Conducting market sizing for research domains
- Evaluating competitive positioning among institutions
- Creating business cases for new initiatives
- Developing strategic plans based on market data
- Supporting grant applications with market context
- Analyzing industry trends for translational research

## Core Frameworks

### 1. TAM/SAM/SOM Analysis

For sizing research funding markets:

```markdown
## Market Size Analysis

### Total Addressable Market (TAM)
Total funding available in the domain
- Federal agency budgets (NSF, NIH, DOE, etc.)
- Foundation giving in the area
- Industry R&D spending

### Serviceable Addressable Market (SAM)
Funding accessible to your institution type
- Geographic restrictions
- Eligibility requirements
- Program-specific limitations

### Serviceable Obtainable Market (SOM)
Realistic capture based on:
- Historical success rates
- Institutional capacity
- Competitive positioning
```

### 2. Porter's Five Forces (Funding Landscape)

| Force | Application to Grants |
|-------|----------------------|
| **Competitive Rivalry** | Number of applicants, success rates |
| **Threat of New Entrants** | New institutions, emerging PIs |
| **Bargaining Power of Funders** | Agency priorities, budget constraints |
| **Bargaining Power of Applicants** | Unique capabilities, track record |
| **Threat of Substitutes** | Alternative funding sources |

### 3. PESTLE Analysis

Analyze external factors affecting funding:

```markdown
## PESTLE Analysis: [Research Domain]

### Political
- Administration priorities
- Congressional appropriations
- Agency leadership changes

### Economic
- Federal budget trends
- Foundation endowment performance
- Industry R&D cycles

### Social
- Public health priorities
- Workforce development needs
- Diversity and inclusion focus

### Technological
- Emerging research areas
- Infrastructure investments
- Technology transfer trends

### Legal
- IP policies
- Data sharing requirements
- Compliance regulations

### Environmental
- Climate research priorities
- Sustainability mandates
- Environmental justice focus
```

### 4. SWOT Analysis

```markdown
## SWOT Analysis: [Institution/Program]

### Strengths
- Unique capabilities
- Infrastructure advantages
- Track record

### Weaknesses
- Capacity limitations
- Gaps in expertise
- Resource constraints

### Opportunities
- Emerging funding programs
- Policy tailwinds
- Partnership possibilities

### Threats
- Budget cuts
- Competition increases
- Shifting priorities
```

## Report Structure

### Executive Summary (1-2 pages)

```markdown
## Executive Summary

### Key Findings
1. [Major finding with quantification]
2. [Second finding]
3. [Third finding]

### Strategic Implications
- [Implication for strategy]
- [Action recommendation]

### Market Snapshot
| Metric | Value |
|--------|-------|
| Total Market Size | $X billion |
| YoY Growth | X% |
| Top Agencies | NSF, NIH, DOE |
| Success Rate | X% |
```

### Market Overview (2-3 pages)

- Definition and scope
- Key stakeholders
- Value chain analysis
- Historical context

### Market Size & Growth (3-4 pages)

- TAM/SAM/SOM analysis
- Historical growth trends
- Forward projections
- Regional/segment breakdown

### Competitive Landscape (3-4 pages)

- Porter's Five Forces
- Top competitors/institutions
- Market share analysis
- Positioning matrix

### Trend Analysis (2-3 pages)

- PESTLE factors
- Emerging technologies
- Policy shifts
- Future outlook

### Strategic Recommendations (1-2 pages)

- Prioritized opportunities
- Risk mitigation strategies
- Implementation roadmap

## Data Sources

### Federal Funding Data

```markdown
## Data Sources

### Primary Sources
- USASpending.gov (obligations data)
- Grants.gov (opportunities)
- NIH RePORTER (awarded grants)
- NSF Award Search

### Agency Budgets
- Congressional appropriations
- Agency strategic plans
- Budget justifications

### Industry Data
- NSF S&E indicators
- USPTO patent data
- Industry association reports
```

### Data Collection Commands

```python
# Example: Pull NSF budget data
import requests

def get_nsf_budget_data(fiscal_year):
    """Fetch NSF budget by directorate."""
    url = f"https://www.nsf.gov/about/budget/fy{fiscal_year}/pdf/fy{fiscal_year}budget.pdf"
    # Parse and extract directorate allocations
    pass

# Example: Query NIH RePORTER
def search_nih_grants(keywords, fiscal_year):
    """Search NIH funded grants."""
    endpoint = "https://api.reporter.nih.gov/v2/projects/search"
    payload = {
        "criteria": {
            "fiscal_years": [fiscal_year],
            "advanced_text_search": {
                "search_text": keywords
            }
        }
    }
    response = requests.post(endpoint, json=payload)
    return response.json()
```

## Visualization Templates

### Market Growth Chart

```
Year    | Funding ($B)
--------|-------------
2020    | ████████░░ $8.0
2021    | █████████░ $9.2
2022    | ██████████ $10.5
2023    | ███████████ $11.8
2024    | ████████████ $13.2 (projected)

CAGR: 12.5%
```

### Competitive Positioning Matrix

```
                    High Success Rate
                          ▲
                          │
         Leader           │         Challenger
        (NIH R01)         │       (New Programs)
    ──────────────────────┼──────────────────────►
         Large Pool       │        Small Pool
                          │
         Niche            │         Developing
       (Specialized)      │        (Emerging)
                          │
                    Low Success Rate
```

### Funding Allocation Pie Chart

```
NSF Budget FY2024 ($9.5B)

Research & Related ████████████░░░░░░░░ 58%
Education & HR     ████░░░░░░░░░░░░░░░░ 12%
Major Equipment    ███░░░░░░░░░░░░░░░░░  8%
Agency Operations  ██░░░░░░░░░░░░░░░░░░  6%
Other              ████░░░░░░░░░░░░░░░░ 16%
```

## Integration with Grant System

Use this skill with scraped grant data to:

1. **Trend identification**: Analyze aggregated grants for funding patterns
2. **Success rate calculation**: Compare funded vs. total applications
3. **Keyword analysis**: Identify hot research areas from funded grants
4. **Agency comparison**: Compare funding levels across sources
5. **Timeline planning**: Align proposals with funding cycles

## Anti-patterns

| Mistake | Solution |
|---------|----------|
| Unsourced claims | Cite all data with dates |
| Stale data | Use most recent available |
| Single source | Cross-reference multiple sources |
| Vague projections | State assumptions explicitly |
| Missing context | Explain methodology limitations |

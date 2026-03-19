---
name: literature-review
description: 'Conduct systematic literature reviews for research. Use when: writing grant background sections, synthesizing research findings, performing systematic reviews, identifying research gaps, building evidence for proposals, creating annotated bibliographies.'
---

# Literature Review

## Overview

Conduct systematic, comprehensive literature reviews following rigorous academic methodology. Search multiple databases, synthesize findings thematically, verify citations, and generate professional output documents for grant proposals and research papers.

## When to Use

- Writing the background section of grant proposals
- Conducting systematic reviews for publication
- Synthesizing current knowledge on a topic
- Identifying research gaps for proposals
- Building evidence base for significance statements
- Creating annotated bibliographies
- Performing meta-analyses or scoping reviews

## Core Workflow

### Phase 1: Planning and Scoping

#### Define Research Question (PICO Framework)

```markdown
## Research Question

**Population**: Who/what is being studied?
**Intervention**: What treatment/exposure/approach?
**Comparison**: Against what alternative?
**Outcome**: What results are measured?

Example:
"What is the efficacy of machine learning approaches (I) 
for predicting grant success (O) in NIH R01 applications (P) 
compared to traditional review metrics (C)?"
```

#### Set Search Parameters

```markdown
## Search Parameters

**Date Range**: 2015-2024
**Languages**: English
**Publication Types**: 
- Peer-reviewed articles
- Preprints (arXiv, bioRxiv)
- Systematic reviews
**Exclusions**:
- Editorials, letters, opinion pieces
- Non-English publications
- Abstracts only
```

### Phase 2: Literature Search

#### Database Selection by Domain

| Domain | Primary Databases |
|--------|-------------------|
| Biomedical | PubMed, PMC, Embase |
| General Science | Web of Science, Scopus |
| Preprints | arXiv, bioRxiv, medRxiv |
| AI/ML | Semantic Scholar, ACM DL |
| Social Science | JSTOR, SSRN |
| Multidisciplinary | Google Scholar |

#### Search Strategy Template

```markdown
## Search Strategy

### Database: PubMed
**Date Searched**: [Date]
**Search String**:
```
("machine learning" OR "artificial intelligence" OR "deep learning")
AND ("grant" OR "funding" OR "proposal")
AND ("prediction" OR "success" OR "outcome")
AND 2015:2024[pdat]
```
**Results**: [N] articles
**Filters Applied**: English, Journal Article

### Database: [Second database]
[Repeat structure]
```

#### Search Commands

```python
# PubMed search via Entrez
from Bio import Entrez

Entrez.email = "your@email.com"

def search_pubmed(query, max_results=100):
    """Search PubMed and return PMIDs."""
    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=max_results,
        sort="relevance"
    )
    results = Entrez.read(handle)
    return results["IdList"]

# Semantic Scholar API
import requests

def search_semantic_scholar(query, limit=100):
    """Search Semantic Scholar."""
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,authors,year,abstract,citationCount"
    }
    response = requests.get(url, params=params)
    return response.json()
```

### Phase 3: Screening and Selection

#### PRISMA Flow Diagram

```
┌─────────────────────────────────────────────┐
│     Records identified from databases       │
│                  (n = XXX)                  │
├─────────────────────────────────────────────┤
│ Database 1: n =                             │
│ Database 2: n =                             │
│ Database 3: n =                             │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│    Records after duplicates removed         │
│                  (n = XXX)                  │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│         Records screened (title)            │
│                  (n = XXX)                  │
├─────────────────────────────────────────────┤
│    Records excluded: n =                    │
│    (Not relevant to topic)                  │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│        Records screened (abstract)          │
│                  (n = XXX)                  │
├─────────────────────────────────────────────┤
│    Records excluded: n =                    │
│    (Did not meet inclusion criteria)        │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│       Full-text articles assessed           │
│                  (n = XXX)                  │
├─────────────────────────────────────────────┤
│    Full-text excluded: n =                  │
│    Reasons:                                 │
│    - Wrong population: n =                  │
│    - Wrong outcome: n =                     │
│    - No data available: n =                 │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│        Studies included in review           │
│                  (n = XXX)                  │
└─────────────────────────────────────────────┘
```

### Phase 4: Data Extraction

#### Extraction Template

```markdown
## Study: [First Author et al., Year]

**Citation**: [Full citation]
**DOI**: [DOI]
**Study Design**: [RCT/Cohort/Cross-sectional/etc.]

### Population
- Sample size: n =
- Characteristics:

### Methods
- Approach:
- Key variables:

### Key Findings
- Primary outcome:
- Secondary outcomes:
- Effect sizes:

### Quality Assessment
- Risk of bias: [Low/Medium/High]
- Limitations noted:

### Relevance to Our Research
- [How this informs our work]
```

### Phase 5: Thematic Synthesis

#### Synthesis Structure (NOT study-by-study)

```markdown
## Results

### Theme 1: [Major Finding Area]

Multiple studies have examined [topic], with converging evidence 
suggesting [synthesis]. Author et al. (2020) demonstrated [finding], 
which was corroborated by [Author 2021; Author 2022]. However, 
[contrasting evidence] was reported by [Author 2023], who found 
[different result] in [different population/context].

The methodological approaches varied considerably, with [N] studies 
using [method A] and [N] studies employing [method B]. Despite these 
differences, the overall pattern suggests [synthetic conclusion].

### Theme 2: [Second Finding Area]
[Continue thematic synthesis...]

### Theme 3: [Third Finding Area]
[Continue thematic synthesis...]
```

### Phase 6: Gap Analysis

```markdown
## Research Gaps

### Methodological Gaps
1. Limited use of [methodology] in this domain
2. Insufficient sample sizes in [context]
3. Lack of longitudinal studies

### Knowledge Gaps
1. Unknown whether [relationship] holds in [context]
2. Mechanisms underlying [phenomenon] not established
3. No studies examining [specific population]

### Translational Gaps
1. Findings not validated in real-world settings
2. Implementation barriers not addressed
3. Cost-effectiveness unknown

## How This Proposal Addresses These Gaps
[Connect to your proposed research]
```

## Citation Management

### Citation Format Templates

**APA 7th Edition**:
```
Author, A. A., & Author, B. B. (Year). Title of article. 
Journal Name, Volume(Issue), Page–Page. https://doi.org/xxxxx
```

**Nature Style**:
```
Author, A.A. & Author, B.B. Title of article. Journal Name 
Volume, Page–Page (Year).
```

**Vancouver (NIH preferred)**:
```
Author AA, Author BB. Title of article. Journal Name. 
Year;Volume(Issue):Page-Page. doi: xxxxx
```

### Citation Verification

```python
def verify_doi(doi):
    """Verify DOI resolves correctly."""
    import requests
    url = f"https://doi.org/{doi}"
    response = requests.head(url, allow_redirects=True)
    return response.status_code == 200

def format_citation(metadata, style="apa"):
    """Format citation from metadata."""
    authors = ", ".join(metadata["authors"])
    year = metadata["year"]
    title = metadata["title"]
    journal = metadata["journal"]
    # Format according to style
    pass
```

## Grant Proposal Integration

### Background Section Template

```markdown
## Background and Significance

### Current State of Knowledge
[Synthesize literature establishing the context]

### Critical Gap
"Despite significant progress in [area], a critical gap remains 
in our understanding of [specific gap]. Specifically, [cite 
supporting evidence for the gap]."

### How This Proposal Fills the Gap
"The proposed research will address this gap by [approach], 
building on preliminary findings that [evidence]."

### Impact
"Successful completion of this work will [outcomes], with 
implications for [broader impact]."
```

## Anti-patterns

| Mistake | Solution |
|---------|----------|
| Study-by-study summaries | Synthesize thematically |
| Uncritical acceptance | Assess quality and bias |
| Missing recent literature | Search within last 6 months |
| Citation errors | Verify all DOIs |
| Bias in selection | Document inclusion criteria |
| No gap identification | Explicitly state what's missing |

## Quality Assessment Tools

| Study Type | Assessment Tool |
|------------|-----------------|
| RCTs | Cochrane Risk of Bias (RoB 2) |
| Observational | Newcastle-Ottawa Scale |
| Systematic reviews | AMSTAR 2 |
| Diagnostic studies | QUADAS-2 |
| Qualitative | CASP Checklist |

## Integration with Grant System

Use aggregated grant data to:

1. **Identify funded research**: What topics have been funded recently?
2. **Find gaps**: What areas lack funding despite literature need?
3. **Track trends**: How are research priorities shifting?
4. **Support significance**: Cite funded grants as evidence of importance

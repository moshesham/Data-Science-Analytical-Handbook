# Data Science Analytical Interview Preparation Handbook

![CI](https://github.com/moshesham/Data-Science-Analytical-Handbook/actions/workflows/ci.yml/badge.svg)
![HTML Validate](https://github.com/moshesham/Data-Science-Analytical-Handbook/actions/workflows/html-validate.yml/badge.svg)
![Markdown Links](https://github.com/moshesham/Data-Science-Analytical-Handbook/actions/workflows/markdown-links-only.yml/badge.svg)
![Notebooks to Markdown](https://github.com/moshesham/Data-Science-Analytical-Handbook/actions/workflows/notebooks-to-markdown.yml/badge.svg)

A comprehensive, open-source interview preparation handbook for data science analytical roles, with a focused track for Meta. Covers the full interview process: statistics, SQL, Python, A/B testing, product sense, behavioral, and hands-on projects.

## ?? Live Site

**[? Data Science Analytical Handbook](https://moshesham.github.io/Data-Science-Analytical-Handbook/)**

## 📁 Repository Content and Structure

This repository is organized into the following sections:

### Core Content

| Section | Location | Description |
|---------|----------|-------------|
| **Main Handbook** | [`Data-Science-Analytical-Interview-Preparation-Handbook.MD`](https://moshesham.github.io/Data-Science-Analytical-Handbook/) | Comprehensive guide to Meta's data science interview process |
| **Jekyll Pages** | [`_pages/`](_pages/) | Web-ready content for GitHub Pages site |
| **Hands-On Projects** | [`Analytical-HandsOn-Projects/`](Analytical-HandsOn-Projects/) | Practical data analysis projects |
| **Simulations** | [`Simulations/`](Simulations/) | Interactive statistics notebooks |

### Supplementary Materials

| Resource | Location | Description |
|----------|----------|-------------|
| **21-Day Prep Guide** | [`supplementary/21-day-prep-guide.md`](supplementary/21-day-prep-guide.md) | Structured 3-week interview preparation plan |
| **Advanced SQL Patterns** | [`supplementary/Advanced-SQL-Patterns+Techniques.md`](supplementary/Advanced-SQL-Patterns+Techniques.md) | Expert-level SQL patterns and practice problems |
| **Statistics Examples** | [`supplementary/statistics-probability-example-questions.md`](supplementary/statistics-probability-example-questions.md) | Statistics and probability practice questions |
| **Behavioral Interview** | [`supplementary/behavioral-mock-interview.md`](supplementary/behavioral-mock-interview.md) | STAR method practice with sample answers |
| **Key Insights (Meta)** | [`supplementary/key-insights-tips-meta.md`](supplementary/key-insights-tips-meta.md) | Meta-specific advice and common pitfalls |
| **SQL Cheat Sheet** | [`supplementary/sql-cheat-sheet.md`](supplementary/sql-cheat-sheet.md) | Quick-reference SQL guide |
| **Statistics Cheat Sheet** | [`supplementary/statistics-cheat-sheet.md`](supplementary/statistics-cheat-sheet.md) | Quick-reference statistics guide |
| **2026 Analytics Challenge** | [`supplementary/2026-new-year-challenge.md`](supplementary/2026-new-year-challenge.md) | 8-week cohort-based curriculum with datasets |

### Best Practices (Data Engineering)

10 deep-dive modules covering the full data engineering stack:

| Module | Location |
|--------|----------|
| Strategy & Architecture | [`Best-Practices/Deep_Dive/1_Strategy+Architecture.md`](Best-Practices/Deep_Dive/1_Strategy+Architecture.md) |
| Data Architecture | [`Best-Practices/Deep_Dive/2_Data_Architecture.md`](Best-Practices/Deep_Dive/2_Data_Architecture.md) |
| Data Governance | [`Best-Practices/Deep_Dive/3_Data_Governance.md`](Best-Practices/Deep_Dive/3_Data_Governance.md) |
| Version Control | [`Best-Practices/Deep_Dive/4_Version_Control.md`](Best-Practices/Deep_Dive/4_Version_Control.md) |
| Data Quality Management | [`Best-Practices/Deep_Dive/5_Data_Quality_Management.md`](Best-Practices/Deep_Dive/5_Data_Quality_Management.md) |
| Data Storage Management | [`Best-Practices/Deep_Dive/6_Data_Storage_Management.md`](Best-Practices/Deep_Dive/6_Data_Storage_Management.md) |
| ETL Processing Frameworks | [`Best-Practices/Deep_Dive/7_ETL_Processing_Frameworks.md`](Best-Practices/Deep_Dive/7_ETL_Processing_Frameworks.md) |
| Orchestration & Workflow | [`Best-Practices/Deep_Dive/8_Orchestration_Workflow_Fundamentals.md`](Best-Practices/Deep_Dive/8_Orchestration_Workflow_Fundamentals.md) |
| Data Transformation | [`Best-Practices/Deep_Dive/9_Transformation_Fundamentals.md`](Best-Practices/Deep_Dive/9_Transformation_Fundamentals.md) |
| Data Acquisition & Ingestion | [`Best-Practices/Deep_Dive/Data_Acquisition_and_Ingestion.md`](Best-Practices/Deep_Dive/Data_Acquisition_and_Ingestion.md) |

## ??? Tools & Integrations

### MCP Server (AI-assisted prep)

An MCP server is available at [`mcp-server/`](mcp-server/) and separately at [ds-interview-mcp-server](https://github.com/moshesham/ds-interview-mcp-server). It integrates with Claude Desktop and VS Code to provide:

- Quiz generation (SQL, statistics, Python, A/B testing)
- SQL validation and optimization
- A/B test design and result analysis
- Case study and mock interview generation

See [`claude-skills-mcp-config.json`](claude-skills-mcp-config.json) for VS Code configuration.

### Streamlit App (local)

A companion Product Analytics app lives in [`streamlit_app/`](streamlit_app/). Run it locally:

```bash
pip install -r streamlit_app/Product_Analytics/requirements.txt
cd streamlit_app/Product_Analytics
streamlit run streamlit_app.py
# Open http://localhost:8501
```

### Local Jekyll Development

```bash
# Using Docker (recommended)
docker-compose up
# Visit http://localhost:4000
```

## ?? How to Use This Material

1. **Pick your level:** Use the Learning Paths table above to find your starting point.
2. **Follow the 21-Day Guide:** [`supplementary/21-day-prep-guide.md`](supplementary/21-day-prep-guide.md) gives a day-by-day structured plan.
3. **Master foundational topics:** Statistics ? SQL ? Python ? A/B Testing in [`_pages/foundational_knowledge/`](_pages/foundational_knowledge/).
4. **Practice SQL:** Work through [`supplementary/Advanced-SQL-Patterns+Techniques.md`](supplementary/Advanced-SQL-Patterns+Techniques.md) and the curated [`_pages/interview_preparation/sql-interview-problems.md`](_pages/interview_preparation/sql-interview-problems.md).
5. **Build portfolio projects:** Complete the hands-on projects in [`Analytical-HandsOn-Projects/`](Analytical-HandsOn-Projects/).
6. **Run interactive simulations:** Explore [`Simulations/`](Simulations/) for statistics practice with real code.
7. **Prepare for behavioral:** Review [`supplementary/behavioral-mock-interview.md`](supplementary/behavioral-mock-interview.md) with STAR stories.
8. **Join the 2026 Challenge:** 8-week cohort curriculum at [`supplementary/2026-new-year-challenge.md`](supplementary/2026-new-year-challenge.md).

## ?? Contributing

Contributions are welcome! If you find errors, want to add practice problems, or improve explanations, please open an issue or submit a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## ?? License

See [LICENSE](LICENSE) for details.

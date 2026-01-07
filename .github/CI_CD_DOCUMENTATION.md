# CI/CD Documentation

This document describes the continuous integration and continuous deployment (CI/CD) setup for the Data Science Analytical Handbook project.

## Table of Contents

- [Overview](#overview)
- [Workflows](#workflows)
- [Security](#security)
- [Automation](#automation)
- [Developer Setup](#developer-setup)
- [Troubleshooting](#troubleshooting)

## Overview

The project uses GitHub Actions for CI/CD with the following key features:

- **Automated Testing**: Python linting, formatting checks, notebook validation
- **Security Scanning**: CodeQL analysis for Python and JavaScript
- **Dependency Management**: Automated dependency updates via Dependabot
- **Documentation**: Automated Jekyll site deployment and HTML validation
- **Quality Gates**: Markdown link checking, code formatting verification
- **Automation**: Auto-labeling PRs, stale issue management

## Workflows

### Main CI Workflow (`ci.yml`)

**Triggers**: Push and pull requests to `main` and `workflow-fix` branches

**Jobs**:
1. **python-quality**: Runs Python linting and formatting checks
   - `isort` - Import sorting
   - `black` - Code formatting
   - `flake8` - Linting (strict mode for critical issues, warnings mode for suggestions)
   - `nbval` - Jupyter notebook validation

2. **markdown-links**: Validates all markdown links in the repository

3. **streamlit-smoke**: Smoke test for the Streamlit app
   - Starts the Streamlit app
   - Verifies it responds to HTTP requests

4. **summary**: Generates a summary of all job results

**Features**:
- Concurrency control to prevent duplicate runs
- Smart caching for Python virtualenvs and npm packages
- Timeout protection (20 min for Python jobs, 15 min for markdown, 10 min for Streamlit)
- Artifact retention (7 days)
- Python 3.11 for consistency

### CodeQL Security Scanning (`codeql.yml`)

**Triggers**: 
- Push to `main`
- Pull requests
- Weekly schedule (Mondays at 6 AM UTC)
- Manual dispatch

**Purpose**: Automated security vulnerability scanning for Python and JavaScript code

**Features**:
- Security and quality queries
- Automated alerts for vulnerabilities
- Results visible in the Security tab

### Dependabot (`dependabot.yml`)

**Configuration**: `.github/dependabot.yml`

**Managed Dependencies**:
- GitHub Actions (weekly updates)
- Python packages in root directory (weekly updates)
- Python packages in Streamlit app (weekly updates)
- Ruby/Bundler (Jekyll dependencies, weekly updates)

**Features**:
- Automatic PR creation for updates
- Labels applied automatically
- Major version updates ignored by default (to prevent breaking changes)
- Limit of 5 open PRs per ecosystem

### Jekyll Deployment (`jekyll-gh-pages.yml`)

**Triggers**: Push to `main`, manual dispatch

**Purpose**: Builds and deploys the Jekyll site to GitHub Pages

**Features**:
- Automated GitHub Pages deployment
- Concurrency control to prevent deployment conflicts

### HTML Validation (`html-validate.yml`)

**Triggers**: 
- Pull requests affecting markdown, HTML, or Jekyll config
- Manual dispatch

**Purpose**: Validates generated HTML from Jekyll site

**Features**:
- Builds Jekyll site
- Runs html-validate with custom rules
- Uploads validation report
- Displays summary in job output

### Notebooks to Markdown (`notebooks-to-markdown.yml`)

**Triggers**: 
- Push to `main` with notebook changes
- Pull requests with notebook changes
- Manual dispatch

**Purpose**: Converts Jupyter notebooks to Markdown for easier viewing

**Features**:
- Automatic conversion using nbconvert
- Commits converted files to repository (on push to main only)
- Uploads artifacts (30 day retention)
- Skip CI tag to prevent infinite loops

### PR Auto-Labeling (`pr-labeler.yml`)

**Triggers**: Pull request opened, synchronized, or reopened

**Purpose**: Automatically labels PRs based on changed files

**Labels Applied**:
- `documentation` - Markdown and doc files
- `python` - Python code and requirements
- `notebooks` - Jupyter notebooks
- `ci-cd` - Workflow and Docker files
- `jekyll` - Jekyll templates and configs
- `streamlit` - Streamlit app files
- `config` - Configuration files

### Stale Issue Management (`stale.yml`)

**Triggers**: Daily at 1 AM UTC, manual dispatch

**Purpose**: Manages inactive issues and pull requests

**Configuration**:
- **Issues**: 60 days until stale, 7 days until closed
- **Pull Requests**: 45 days until stale, 14 days until closed
- **Exempt Labels**: `pinned`, `security`, `help-wanted`, `good-first-issue`, `work-in-progress`, `wip`

### Issue Summarization (`summary.yml`)

**Triggers**: New issues opened

**Purpose**: Uses AI to generate a summary of new issues

**Features**:
- Automatic AI-generated summary
- Posted as a comment on the issue
- Continues even if AI fails

## Security

### Security Policy

See [SECURITY.md](../SECURITY.md) for:
- Supported versions
- How to report vulnerabilities
- Security response process

### CodeQL Analysis

- **Languages**: Python, JavaScript
- **Schedule**: Weekly on Mondays
- **Queries**: Security and quality queries
- **Results**: Available in Security tab

### Dependabot Security Updates

Dependabot automatically:
- Scans for known vulnerabilities
- Creates PRs for security updates
- Prioritizes security fixes

## Automation

### Pull Request Template

Location: `.github/PULL_REQUEST_TEMPLATE.md`

Helps contributors provide:
- Description of changes
- Type of change
- Related issues
- Testing performed
- Checklist for best practices

### Issue Templates

Location: `.github/ISSUE_TEMPLATE/`

**Available Templates**:
1. **Bug Report** (`bug_report.yml`)
   - What happened
   - Expected behavior
   - Steps to reproduce
   - Additional context

2. **Feature Request** (`feature_request.yml`)
   - Problem description
   - Proposed solution
   - Alternatives considered
   - Additional context

### Auto-Labeling

PRs are automatically labeled based on files changed:
- Makes it easier to filter and review PRs
- Helps identify the scope of changes

## Developer Setup

### Pre-commit Hooks

**Installation**:
```bash
pip install pre-commit
pre-commit install
```

**What it does**:
- Runs automated checks before each commit
- Formats code with `black`
- Sorts imports with `isort`
- Runs `flake8` linting
- Checks for common issues (trailing whitespace, large files, etc.)
- Cleans notebook outputs

**Manual run**:
```bash
pre-commit run --all-files
```

### Local Development

**Python Setup**:
```bash
python -m venv .venv-dev
source .venv-dev/bin/activate  # On Windows: .venv-dev\Scripts\activate
pip install -r requirements-dev.txt
```

**Run checks locally**:
```bash
# Format code
black .
isort --profile black .

# Run linting
flake8 .

# Test notebooks
pytest --nbval
```

**Streamlit App**:
```bash
python -m venv .venv-streamlit
source .venv-streamlit/bin/activate
pip install -r streamlit_app/Product_Analytics/requirements.txt
streamlit run streamlit_app/Product_Analytics/streamlit_app.py
```

## Troubleshooting

### CI Failures

**Python quality checks failing**:
- Run `black .` and `isort --profile black .` to auto-fix formatting
- Check `flake8` output for specific issues
- Ensure you're using Python 3.11

**Markdown link checks failing**:
- Check if external links are down temporarily
- Review `.markdown-link-check.json` for ignored patterns
- Some sites block automated checkers

**Notebook validation failing**:
- Clear notebook outputs: `nbstripout notebook.ipynb`
- Re-run notebook cells to ensure they execute
- Check for notebook-specific issues in test output

**Streamlit smoke test failing**:
- Check `streamlit.log` artifact for errors
- Verify requirements.txt includes all dependencies
- Test locally: `streamlit run streamlit_app/Product_Analytics/streamlit_app.py`

### Workflow Issues

**Workflow not running**:
- Check if branch is in trigger configuration
- Verify file paths match path filters
- Check workflow permissions

**Cache not working**:
- Cache keys changed? Check if dependency files modified
- Caches expire after 7 days of no use
- Try clearing cache in repository settings

**Dependabot PRs failing**:
- Check if updated dependency has breaking changes
- Review CI logs for specific failures
- May need to update code to work with new version

## Best Practices

1. **Before pushing**:
   - Run pre-commit hooks
   - Test changes locally
   - Ensure all CI checks pass

2. **Pull Requests**:
   - Use the PR template
   - Link related issues
   - Keep changes focused and small
   - Respond to review comments

3. **Security**:
   - Never commit secrets or API keys
   - Review Dependabot PRs promptly
   - Address CodeQL findings

4. **Documentation**:
   - Update docs when changing functionality
   - Keep README.md current
   - Document breaking changes

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Dependabot Documentation](https://docs.github.com/en/code-security/dependabot)
- [CodeQL Documentation](https://codeql.github.com/docs/)
- [Pre-commit Documentation](https://pre-commit.com/)

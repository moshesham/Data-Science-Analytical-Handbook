# GitHub Actions Workflow Status

This page provides an overview of all GitHub Actions workflows in this repository.

## Active Workflows

### Continuous Integration

| Workflow | Status | Description |
|----------|--------|-------------|
| [CI](.github/workflows/ci.yml) | ![CI](https://github.com/moshesham/Data-Science-Analytical-Handbook/actions/workflows/ci.yml/badge.svg) | Main CI pipeline - Python quality checks, markdown links, Streamlit smoke test |
| [CodeQL](.github/workflows/codeql.yml) | ![CodeQL](https://github.com/moshesham/Data-Science-Analytical-Handbook/actions/workflows/codeql.yml/badge.svg) | Security vulnerability scanning for Python and JavaScript |
| [HTML Validate](.github/workflows/html-validate.yml) | ![HTML Validate](https://github.com/moshesham/Data-Science-Analytical-Handbook/actions/workflows/html-validate.yml/badge.svg) | Validates generated HTML from Jekyll |
| [Markdown Links](.github/workflows/markdown-links-only.yml) | ![Markdown Links](https://github.com/moshesham/Data-Science-Analytical-Handbook/actions/workflows/markdown-links-only.yml/badge.svg) | Manual workflow to check all markdown links |

### Deployment

| Workflow | Status | Description |
|----------|--------|-------------|
| [Jekyll GitHub Pages](.github/workflows/jekyll-gh-pages.yml) | ![Jekyll](https://github.com/moshesham/Data-Science-Analytical-Handbook/actions/workflows/jekyll-gh-pages.yml/badge.svg) | Builds and deploys the Jekyll site to GitHub Pages |
| [Notebooks to Markdown](.github/workflows/notebooks-to-markdown.yml) | ![Notebooks](https://github.com/moshesham/Data-Science-Analytical-Handbook/actions/workflows/notebooks-to-markdown.yml/badge.svg) | Converts Jupyter notebooks to Markdown |

### Automation

| Workflow | Status | Description |
|----------|--------|-------------|
| [PR Labeler](.github/workflows/pr-labeler.yml) | - | Automatically labels pull requests based on changed files |
| [Stale Issues](.github/workflows/stale.yml) | - | Manages stale issues and pull requests |
| [Issue Summary](.github/workflows/summary.yml) | - | AI-powered summarization of new issues |

## Workflow Triggers

### On Push/Pull Request
- CI workflow runs on all pushes and PRs to `main` and `workflow-fix`
- HTML validation runs on PRs that change markdown, HTML, or Jekyll config
- Jekyll deployment runs on pushes to `main`
- Notebooks to Markdown runs when notebook files change

### Scheduled
- **CodeQL**: Weekly on Mondays at 6:00 AM UTC
- **Stale Issues**: Daily at 1:00 AM UTC

### Manual
- All workflows support `workflow_dispatch` for manual triggering
- Use the "Actions" tab → Select workflow → "Run workflow"

## Recent Runs

Visit the [Actions tab](https://github.com/moshesham/Data-Science-Analytical-Handbook/actions) to see:
- Recent workflow runs
- Detailed logs
- Artifacts and reports
- Workflow timing and performance

## Troubleshooting

If a workflow fails:

1. **Check the logs**: Click on the failed workflow run to see detailed logs
2. **Review the error**: Most errors will show specific file and line numbers
3. **Run locally**: Try to reproduce the issue on your local machine
4. **Check documentation**: See [CI/CD Documentation](CI_CD_DOCUMENTATION.md) for common issues

### Common Issues

- **Python quality checks**: Run `black .` and `isort --profile black .` to fix formatting
- **Markdown links**: Some external sites may be temporarily down or block automated checkers
- **Notebook validation**: Ensure notebooks execute without errors
- **Cache issues**: Workflows use caching; sometimes clearing the cache helps

## Monitoring

### Security Alerts

Security alerts from CodeQL and Dependabot are available in the [Security tab](https://github.com/moshesham/Data-Science-Analytical-Handbook/security).

### Dependabot

Dependabot automatically creates PRs for:
- GitHub Actions updates
- Python package updates
- Ruby/Jekyll dependency updates

See open [Dependabot PRs](https://github.com/moshesham/Data-Science-Analytical-Handbook/pulls?q=is%3Aopen+is%3Apr+author%3Aapp%2Fdependabot).

## Configuration Files

| File | Purpose |
|------|---------|
| `.github/workflows/*.yml` | Workflow definitions |
| `.github/dependabot.yml` | Dependabot configuration |
| `.github/labeler.yml` | PR auto-labeling rules |
| `.pre-commit-config.yaml` | Pre-commit hook configuration |
| `.flake8` | Python linting configuration |
| `.htmlvalidate.json` | HTML validation rules |
| `.markdown-link-check.json` | Markdown link checker configuration |

## Metrics

To view workflow performance metrics:
1. Go to [Insights](https://github.com/moshesham/Data-Science-Analytical-Handbook/pulse) → Actions
2. See workflow run times, success rates, and trends

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [CI/CD Best Practices](CI_CD_DOCUMENTATION.md)
- [Contributing Guidelines](../CONTRIBUTING.md)

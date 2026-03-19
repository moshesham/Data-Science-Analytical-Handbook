---
name: dependency-auditor
description: 'Dependency and license review for Python projects. Use when: auditing requirements.txt, checking for vulnerabilities, reviewing licenses, updating dependencies, managing version constraints.'
---

# Dependency Auditor

## When to Use

- Reviewing `requirements.txt` for security issues
- Checking dependency licenses for compatibility
- Updating outdated packages
- Resolving dependency conflicts
- Adding new dependencies safely

## Security Auditing

### Using pip-audit

```bash
# Install pip-audit
pip install pip-audit

# Audit current environment
pip-audit

# Audit requirements file
pip-audit -r requirements.txt

# Output as JSON for CI
pip-audit --format json -o audit-results.json
```

### Using safety

```bash
# Install safety
pip install safety

# Check dependencies
safety check -r requirements.txt

# With API key for full database
safety check --key $SAFETY_API_KEY -r requirements.txt
```

### GitHub Actions Integration

```yaml
- name: Security audit
  run: |
    pip install pip-audit
    pip-audit -r requirements.txt --strict
```

## License Compliance

### Checking Licenses

```bash
# Install pip-licenses
pip install pip-licenses

# List all licenses
pip-licenses --format=markdown

# Check for problematic licenses
pip-licenses --fail-on="GPL;AGPL"

# Output as JSON
pip-licenses --format=json -o licenses.json
```

### Common License Categories

| License | Commercial Use | Copyleft |
|---------|---------------|----------|
| MIT | ✅ | No |
| Apache-2.0 | ✅ | No |
| BSD-3-Clause | ✅ | No |
| GPL-3.0 | ⚠️ Careful | Yes |
| AGPL-3.0 | ⚠️ Careful | Yes (network) |

### Safe Licenses for This Project

```
MIT
Apache-2.0
BSD-2-Clause
BSD-3-Clause
ISC
Python-2.0
PSF-2.0
```

## Version Management

### Version Constraint Patterns

```txt
# Exact (reproducible but no security updates)
requests==2.31.0

# Compatible release (recommended)
requests~=2.31.0  # >=2.31.0, <2.32.0

# Minimum with ceiling
requests>=2.31.0,<3.0.0

# Avoid: no upper bound
requests>=2.31.0  # Risky
```

### Update Strategy

```bash
# Check for outdated packages
pip list --outdated

# Update a specific package
pip install --upgrade requests

# Generate updated requirements
pip freeze > requirements.txt
```

### Using pip-tools

```bash
# Install pip-tools
pip install pip-tools

# Define abstract requirements in requirements.in
# Then compile to pinned requirements.txt
pip-compile requirements.in

# Update all
pip-compile --upgrade requirements.in
```

## Dependency Review Checklist

For each new dependency:

1. **Purpose**: Does it solve a real need?
2. **Maintenance**: Last commit < 6 months? Active maintainers?
3. **Popularity**: Sufficient downloads/stars?
4. **License**: Compatible with project license?
5. **Security**: Any known vulnerabilities?
6. **Size**: Reasonable dependency footprint?
7. **Alternatives**: Is there a lighter option?

## requirements.txt Best Practices

```txt
# requirements.txt

# Core dependencies (pinned for reproducibility)
requests==2.31.0
beautifulsoup4==4.12.2
playwright==1.40.0

# Database
psycopg2-binary==2.9.9
pgvector==0.2.4

# AI/ML (careful with large packages)
openai==1.6.0

# Development (separate file: requirements-dev.txt)
# pytest==7.4.3
# black==23.12.0
```

## Anti-patterns

- **Unpinned versions**: `requests` instead of `requests==2.31.0`
- **No dev separation**: Mix test tools with production deps
- **Giant packages**: Bringing in pandas for one function
- **Ignoring CVEs**: Not running security audits in CI
- **License ignorance**: Using GPL in proprietary code
- **Stale dependencies**: Not updating for years

## CI Integration

```yaml
name: Dependency Audit

on:
  schedule:
    - cron: '0 0 * * 1'  # Weekly
  pull_request:
    paths:
      - 'requirements*.txt'

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Security audit
        run: |
          pip install pip-audit
          pip-audit -r requirements.txt
      
      - name: License check
        run: |
          pip install pip-licenses
          pip-licenses --fail-on="GPL;AGPL"
```

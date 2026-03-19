---
name: ci-cd-pipeline-builder
description: 'GitHub Actions workflow design and hardening. Use when: creating CI/CD pipelines, securing workflows, optimizing build times, adding tests to pipelines, fixing workflow failures, working with .github/workflows/.'
---

# CI/CD Pipeline Builder

## When to Use

- Creating or modifying `.github/workflows/*.yml`
- Hardening workflow security
- Optimizing CI/CD build times
- Adding test stages to pipelines
- Debugging failing workflows
- Setting up matrix builds

## Workflow Structure

### Basic Python Workflow

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run tests
        run: pytest --cov=src tests/
```

### Matrix Builds

```yaml
jobs:
  test:
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
        os: [ubuntu-latest, macos-latest]
      fail-fast: false
    runs-on: ${{ matrix.os }}
```

## Security Hardening

### Pin Actions to SHA

```yaml
# Bad - mutable tag
- uses: actions/checkout@v4

# Good - immutable SHA
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
```

### Minimal Permissions

```yaml
permissions:
  contents: read
  pull-requests: write  # Only if needed

jobs:
  deploy:
    permissions:
      contents: read
      id-token: write  # For OIDC auth
```

### Secret Management

```yaml
env:
  # Never echo secrets
  DATABASE_URL: ${{ secrets.DATABASE_URL }}

steps:
  - name: Connect to DB
    run: |
      # Use --quiet flags
      psql "$DATABASE_URL" --quiet -c "SELECT 1"
```

### Prevent Script Injection

```yaml
# Bad - injectable
- run: echo "Hello ${{ github.event.issue.title }}"

# Good - use environment variable
- env:
    ISSUE_TITLE: ${{ github.event.issue.title }}
  run: echo "Hello $ISSUE_TITLE"
```

## Build Optimization

### Caching Dependencies

```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.11'
    cache: 'pip'
    cache-dependency-path: requirements.txt
```

### Cache Docker Layers

```yaml
- uses: docker/build-push-action@v5
  with:
    context: .
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

### Conditional Jobs

```yaml
jobs:
  changes:
    outputs:
      src: ${{ steps.filter.outputs.src }}
    steps:
      - uses: dorny/paths-filter@v3
        id: filter
        with:
          filters: |
            src:
              - 'src/**'

  test:
    needs: changes
    if: needs.changes.outputs.src == 'true'
```

## Database Testing

```yaml
services:
  postgres:
    image: pgvector/pgvector:pg16
    env:
      POSTGRES_PASSWORD: postgres
    ports:
      - 5432:5432
    options: >-
      --health-cmd pg_isready
      --health-interval 10s
      --health-timeout 5s
      --health-retries 5

steps:
  - name: Run migrations
    env:
      DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test
    run: psql "$DATABASE_URL" -f database/schema.sql
```

## Anti-patterns

- **Unpinned actions**: Use SHA, not tags
- **Overly broad permissions**: Use minimal required
- **No caching**: Wasted build minutes
- **Secrets in logs**: Use masking and quiet flags
- **No fail-fast**: Matrix builds should fail fast in CI
- **Missing timeouts**: Add `timeout-minutes` to jobs

## Debugging

```yaml
- name: Debug
  if: failure()
  run: |
    echo "::group::Environment"
    env | sort
    echo "::endgroup::"
```

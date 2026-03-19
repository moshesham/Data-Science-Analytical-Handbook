# Workflow Patterns

## Recommended Jobs

- `lint`: fast style and static checks
- `test`: unit and integration tests
- `build`: image or package build
- `security`: dependency and config scans

## Python CI Skeleton

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: pip
      - run: pip install -r requirements.txt
      - run: pytest
```

## Grant App Notes

- Run schema checks before ingestion tests
- Keep scheduled ingest workflows isolated from PR validation
- Fail fast for setup errors, not flaky network calls

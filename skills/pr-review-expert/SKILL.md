---
name: pr-review-expert
description: 'Structured pull request review for code quality. Use when: reviewing PRs for ingestion code, schema changes, database migrations, Python code review, providing actionable feedback on pull requests.'
---

# PR Review Expert

## When to Use

- Reviewing pull requests for `src/ingestion/` changes
- Evaluating database schema modifications
- Checking Python code quality
- Providing structured, actionable PR feedback
- Reviewing test coverage for new features

## Review Framework

### Priority Levels

| Level | Label | Action Required | Examples |
|-------|-------|-----------------|----------|
| 🔴 | Blocker | Must fix before merge | Security issue, data loss risk, broken tests |
| 🟡 | Important | Should fix, can follow up | Missing tests, poor error handling |
| 🟢 | Suggestion | Nice to have | Style preference, minor optimization |
| 💬 | Question | Clarification needed | Design intent, edge case handling |

### Review Sections

Structure every review with these sections:

```markdown
## Summary
One paragraph describing what this PR does and its impact.

## 🔴 Blockers
- Issue description with file:line reference
- Why it's a blocker
- Suggested fix

## 🟡 Important Issues
- Issue with context
- Recommendation

## 🟢 Suggestions
- Optional improvements

## ✅ What's Good
- Positive observations to reinforce good patterns
```

## Ingestion Code Review

### Key Areas for `src/ingestion/`

1. **Error Handling**
```python
# ❌ Silent failures
try:
    data = fetch_grants()
except Exception:
    pass

# ✅ Explicit handling with logging
try:
    data = fetch_grants()
except RequestException as e:
    logger.error(f"Failed to fetch grants: {e}")
    raise IngestionError(f"Grant fetch failed: {e}") from e
```

2. **Data Validation**
```python
# ❌ Trust external data
grant_id = response['id']

# ✅ Validate and sanitize
grant_id = response.get('id')
if not grant_id or not isinstance(grant_id, str):
    raise ValidationError("Invalid grant ID")
```

3. **Idempotency**
```python
# ❌ Duplicate on re-run
db.insert(grant)

# ✅ Upsert pattern
db.upsert(grant, on_conflict='external_id')
```

## Schema Change Review

### Migration Checklist

- [ ] Backward compatible (can rollback?)
- [ ] Includes rollback script
- [ ] New columns nullable or have defaults
- [ ] Indexes added for new query patterns
- [ ] No breaking changes to existing columns
- [ ] Migration tested on copy of production data

### Schema Review Points

```sql
-- ❌ Breaking change
ALTER TABLE grants DROP COLUMN old_field;

-- ✅ Deprecate first
ALTER TABLE grants ADD COLUMN deprecated_old_field BOOLEAN DEFAULT true;
-- Then remove in future migration
```

## Python Code Quality

### Style Checks

- Type hints on public functions
- Docstrings on modules and public classes
- Consistent naming (snake_case)
- No magic numbers (use constants)

### Testing Requirements

- Unit tests for new functions
- Integration tests for ingestion sources
- Edge case coverage
- Mocked external services

```python
# Required test patterns
def test_happy_path():
    """Normal operation succeeds."""
    
def test_empty_response():
    """Handles empty data gracefully."""
    
def test_malformed_data():
    """Rejects invalid input with clear error."""
    
def test_network_failure():
    """Retries on transient failures."""
```

## PR Size Guidelines

| Size | Lines Changed | Review Strategy |
|------|---------------|-----------------|
| Small | < 100 | Single reviewer, quick turnaround |
| Medium | 100-500 | Careful review, may need discussion |
| Large | 500+ | Split if possible, pair review |

## Review Response Template

```markdown
## PR Review: #{number} - {title}

### Summary
{What this PR accomplishes}

### Review

🔴 **Blocker** - {file}#L{line}
> {code snippet}
{Issue}: {explanation}
**Suggestion**: {fix}

🟡 **Important** - {file}#L{line}
{Issue and recommendation}

🟢 **Suggestion**
{Optional improvement}

### Testing
- [ ] Unit tests pass
- [ ] New tests added for new code
- [ ] Manually verified {scenario}

### Decision
{Approve / Request Changes / Comment}
```

## Anti-patterns in Reviews

- **Drive-by nits**: Only style comments, no substance
- **No positive feedback**: Demoralizing for authors
- **Vague concerns**: "This seems wrong" without explanation
- **Blocking on preferences**: Not blockers, just opinions
- **Missing context**: Reviewing code without understanding purpose

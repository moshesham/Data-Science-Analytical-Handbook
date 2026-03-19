# Indexing Guide

## Start With Query Patterns

Add indexes only after identifying common filters, joins, and sorts.

## Typical Index Choices

- B-tree for equality and range filters
- GIN for `jsonb` and full-text search
- HNSW or IVF for vector similarity
- Partial indexes for sparse columns

## Grant Data Examples

```sql
CREATE INDEX idx_opportunities_source ON opportunities (source);
CREATE INDEX idx_opportunities_deadline ON opportunities (closes_at) WHERE closes_at IS NOT NULL;
CREATE INDEX idx_opportunities_payload ON opportunities USING gin (raw_payload);
```

## Review Checklist

- Does the index support a real query?
- Is the column selective enough?
- Does the write cost justify the read gain?
- Can a composite index replace multiple single-column indexes?

# Schema Patterns

## Core Tables

Recommended fields for ingestion-backed entities:

- `id UUID PRIMARY KEY`
- `external_id TEXT UNIQUE NOT NULL`
- `source TEXT NOT NULL`
- `created_at TIMESTAMPTZ DEFAULT NOW()`
- `updated_at TIMESTAMPTZ DEFAULT NOW()`

## Modeling Guidance

- Store raw payloads separately from normalized records
- Use lookup tables for controlled vocabularies
- Prefer nullable additions over breaking column changes
- Add check constraints for numeric ranges and date logic

## Grant-Oriented Example

```sql
CREATE TABLE opportunities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  external_id TEXT NOT NULL UNIQUE,
  source TEXT NOT NULL,
  title TEXT NOT NULL,
  posted_at TIMESTAMPTZ,
  closes_at TIMESTAMPTZ,
  raw_payload JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

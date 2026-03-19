---
name: database-designer
description: 'PostgreSQL and pgvector schema design. Use when: designing database schemas, adding vector embeddings, optimizing queries, creating indexes, planning migrations, working with schema.sql or schema_v2.sql.'
---

# Database Designer

## When to Use

- Designing or modifying `database/schema.sql` or `database/schema_v2.sql`
- Adding pgvector support for semantic search
- Creating indexes for search performance
- Planning schema migrations
- Optimizing slow queries

## Schema Design Principles

### Table Structure

```sql
-- Standard table with audit fields
CREATE TABLE grants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    external_id VARCHAR(255) UNIQUE NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    amount_min NUMERIC(15, 2),
    amount_max NUMERIC(15, 2),
    deadline TIMESTAMPTZ,
    source VARCHAR(100) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    CONSTRAINT valid_amount CHECK (amount_min <= amount_max)
);
```

### pgvector Setup

```sql
-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Add embedding column (OpenAI ada-002 = 1536 dims)
ALTER TABLE grants ADD COLUMN embedding vector(1536);

-- Create HNSW index for fast similarity search
CREATE INDEX grants_embedding_idx ON grants 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);
```

### Semantic Search Query

```sql
-- Find similar grants using cosine similarity
SELECT id, title, 
       1 - (embedding <=> $1::vector) AS similarity
FROM grants
WHERE embedding IS NOT NULL
ORDER BY embedding <=> $1::vector
LIMIT 10;
```

## Indexing Strategy

### B-tree Indexes (Exact Matches)

```sql
-- For filtering by source
CREATE INDEX idx_grants_source ON grants(source);

-- For deadline queries
CREATE INDEX idx_grants_deadline ON grants(deadline) 
WHERE deadline IS NOT NULL;
```

### GIN Indexes (Full-text Search)

```sql
-- Full-text search on title and description
ALTER TABLE grants ADD COLUMN search_vector tsvector;

CREATE INDEX idx_grants_search ON grants USING gin(search_vector);

-- Trigger to update search vector
CREATE OR REPLACE FUNCTION update_search_vector()
RETURNS TRIGGER AS $$
BEGIN
    NEW.search_vector := 
        setweight(to_tsvector('english', COALESCE(NEW.title, '')), 'A') ||
        setweight(to_tsvector('english', COALESCE(NEW.description, '')), 'B');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### Composite Indexes

```sql
-- For common filter + sort patterns
CREATE INDEX idx_grants_source_deadline 
ON grants(source, deadline DESC);
```

## Migration Best Practices

1. **Use transactions**: Wrap migrations in `BEGIN/COMMIT`
2. **Add columns nullable first**: Then backfill, then add constraint
3. **Create indexes concurrently**: `CREATE INDEX CONCURRENTLY`
4. **Version your schemas**: Name files with timestamps

```sql
-- migrations/20240315_add_embeddings.sql
BEGIN;

ALTER TABLE grants ADD COLUMN IF NOT EXISTS embedding vector(1536);

CREATE INDEX CONCURRENTLY IF NOT EXISTS grants_embedding_idx 
ON grants USING hnsw (embedding vector_cosine_ops);

COMMIT;
```

## Query Optimization

### EXPLAIN ANALYZE

```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM grants 
WHERE source = 'grants.gov' 
AND deadline > NOW()
ORDER BY deadline;
```

### Common Optimizations

- Add missing indexes for WHERE/JOIN columns
- Use `LIMIT` with `ORDER BY` to enable index scan
- Partition large tables by date or source
- Use connection pooling (PgBouncer)

## Anti-patterns

- **UUID as string**: Use native UUID type
- **Missing NOT NULL**: Always specify constraints
- **No foreign keys**: Enforce referential integrity
- **SERIAL vs UUID**: Use UUID for distributed systems
- **Missing updated_at trigger**: Always track modifications

# Migration Checklist

Before applying a schema change:

- Confirm the change is backward compatible when possible
- Add new columns as nullable or with safe defaults
- Backfill large datasets in batches
- Create indexes concurrently when supported
- Include rollback or mitigation notes
- Test against representative data volume
- Verify application code can handle both old and new states

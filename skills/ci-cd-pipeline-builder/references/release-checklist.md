# Release Checklist

Before shipping workflow changes:

- Validate YAML syntax
- Confirm triggers match intended events
- Verify caches use the right dependency files
- Ensure services have health checks
- Check artifact retention and naming
- Test rollback path for deploy workflows
- Confirm logs are sufficient for failure diagnosis

# Scrape Checklist

Before merging scraper changes:

- Verify selectors on at least two representative pages
- Handle empty states and missing fields
- Add request pacing or retry strategy
- Confirm browser context is closed in all paths
- Capture enough logging for production failures
- Validate parsed fields before storing them
- Document assumptions about pagination and filtering

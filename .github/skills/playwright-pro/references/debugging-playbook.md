# Debugging Playbook

## When a Scrape Fails

1. Capture a screenshot.
2. Save the page HTML.
3. Log the current URL and title.
4. Record whether the failure was navigation, selector, or parsing.
5. Re-run with headed mode if needed.

## Minimal Debug Snippet

```python
await page.screenshot(path='debug/failure.png', full_page=True)
html = await page.content()
print(await page.title())
print(page.url)
```

## Common Failure Modes

- Consent banners block clicks
- Shadow DOM hides elements
- Data loads after XHR, not initial HTML
- Bot protection changes DOM shape
- Pagination requires scroll or button clicks

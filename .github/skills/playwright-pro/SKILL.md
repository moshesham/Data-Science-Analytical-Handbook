---
name: playwright-pro
description: 'Browser automation and scraping with Playwright. Use when: building scrapers, debugging web automation, handling dynamic content, managing browser sessions, implementing retry logic for flaky scrapes, capturing screenshots.'
---

# Playwright Pro

## When to Use

- Writing or debugging browser automation in `src/scraper.py`
- Handling dynamic JavaScript-rendered pages
- Implementing robust scraping with retry logic
- Managing browser contexts and sessions
- Debugging element selectors or page interactions

## Core Practices

### Browser Setup

```python
from playwright.sync_api import sync_playwright

def create_browser_context():
    """Create a configured browser context with stealth settings."""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=True,
        args=['--no-sandbox', '--disable-dev-shm-usage']
    )
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    )
    return context
```

### Reliable Element Selection

1. **Prefer data attributes**: `[data-testid="grant-title"]`
2. **Use text content**: `page.get_by_text("Apply Now")`
3. **Avoid fragile XPath**: Complex paths break on minor DOM changes
4. **Use role selectors**: `page.get_by_role("button", name="Submit")`

### Retry Logic Pattern

```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
async def scrape_with_retry(page, url):
    """Scrape with exponential backoff retry."""
    await page.goto(url, wait_until='networkidle')
    await page.wait_for_selector('.grant-listing', timeout=30000)
    return await page.content()
```

### Handling Dynamic Content

```python
async def wait_for_content(page):
    """Wait for dynamic content to load."""
    # Wait for network idle
    await page.wait_for_load_state('networkidle')
    
    # Wait for specific element
    await page.wait_for_selector('.results-loaded')
    
    # Handle infinite scroll
    while await page.is_visible('.load-more'):
        await page.click('.load-more')
        await page.wait_for_timeout(1000)
```

### Error Handling

```python
from playwright.sync_api import TimeoutError as PlaywrightTimeout

try:
    await page.click('button.submit', timeout=5000)
except PlaywrightTimeout:
    # Take screenshot for debugging
    await page.screenshot(path='debug/timeout_error.png')
    raise
```

## Anti-patterns

- **Hardcoded timeouts**: Use `wait_for_*` methods instead
- **No error screenshots**: Always capture state on failure
- **Ignoring rate limits**: Implement polite delays between requests
- **Session leaks**: Always close browser contexts in finally blocks
- **Synchronous code in async context**: Use proper async/await patterns

## Debugging Tips

1. Run with `headless=False` to watch automation
2. Use `page.pause()` to stop and inspect
3. Enable trace recording: `context.tracing.start(screenshots=True)`
4. Check network tab for failed requests

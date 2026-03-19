# Selector Strategies

Use selectors in this order of preference:

1. Stable test ids or data attributes
2. ARIA roles with accessible names
3. Visible text for user-facing controls
4. Short CSS selectors scoped to a stable container
5. XPath only as a last resort

## Good Patterns

```python
page.get_by_test_id('grant-card')
page.get_by_role('button', name='Apply')
page.locator('[data-source="grants-gov"] .grant-row')
```

## Fragile Patterns

```python
page.locator('div > div:nth-child(3) > span > a')
page.locator('//div[7]/table/tr[4]/td[2]')
```

## Review Checklist

- Selector survives minor layout changes
- Selector is unique on the page
- Selector is readable to future maintainers
- Selector does not depend on generated class names
- Selector can be retried safely

Title: HTML validation — `/21_Day-Prep-Guide/index.html` (errorCount: 17)

Description
-----------
`html-validate` reported 17 errors in `/21_Day-Prep-Guide/index.html`.

Top issues observed
- `doctype-style` — DOCTYPE should be uppercase.
- `no-raw-characters` — raw `&` instances need escaping.
- `wcag/h63` — multiple `<th>` elements missing a valid `scope` attribute (accessibility issue).

Suggested fixes
- Update DOCTYPE in the base layout to `<!DOCTYPE html>`.
- Add `scope="col"` or `scope="row"` to header cells produced by the table renderer. If tables are generated from markdown, add an HTML table template or post-process to add scopes.
- Escape raw ampersands in navigation and titles.

Where to look
- Tables and table headers in this page appear to be generated from markdown or raw HTML inside repo pages. Search for the page source under the repo (e.g., `21_Day-Prep-Guide.md` or the `html_source/Archive/` folder) and the site layout templates.

Notes
- This issue is suitable for template-level fixes (preferred) so the same change applies to other pages.

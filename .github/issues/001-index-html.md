Title: HTML validation — `/index.html` (errorCount: 2)

Description
-----------
html-validate found 2 errors in the generated `_site/index.html`.

Top issues
- `doctype-style` (severity: error) — DOCTYPE should be uppercase. Template currently emits `<!doctype html>`; change to `<!DOCTYPE html>` in the base layout.
- `no-raw-characters` (severity: error) — Raw `&` detected (e.g., in navigation links). Escape as `&amp;` or ensure the generator escapes characters.

Suggested fix
- Edit the Jekyll base layout (likely `_layouts/default.html` or similar) to ensure the DOCTYPE is uppercase.
- Inspect the sidebar / navigation content generation and escape raw ampersands or sanitize titles that include `&`.

Notes
- `html-validate-report.json` contains the full message objects and context. See repo root for the full JSON report.

Title: HTML validation — site-wide patterns and remediation guidance

Description
-----------
This issue captures recurring site-wide HTML validation problems that should be fixed centrally in the Jekyll templates or the content pipeline.

Recurring rule categories (summary)
- `doctype-style`: Ensure the site base layout uses `<!DOCTYPE html>` (uppercase).
- `no-raw-characters`: Escape ampersands and other raw characters in navigation and content.
- `wcag/h63`: Add `scope` attributes to table header (`<th>`) elements generated from markdown or templates.
- `no-inline-style`: Remove inline `style` attributes in generated HTML; prefer CSS classes.
- `void-style`: Ensure void elements are output with HTML5 syntax `<img>`, `<hr>` (no self-closing slash).
- `valid-id`: Ensure IDs begin with a letter (adjust slugify settings or prefix IDs).

High-level plan
1. Update base layout(s) and any table/heading partials to fix doctype, void-style, and scope.
2. Configure markdown or HTML sanitizer step to escape raw characters or run content through a sanitizer/filter before rendering.
3. Add an `html-validate` CI job artifact upload so PRs produce an actionable JSON report.
4. Iteratively fix top N offending pages (issues created separately) after templates are improved.

How to run locally
1. Build site:

   ```powershell
   docker compose -f docker-compose.yml run --rm jekyll jekyll build
   ```

2. Run validator (example using Node image):

   ```powershell
   docker run --rm -v ${PWD}:/workdir -w /workdir node:20-slim bash -c "npm install -g html-validate@8 && html-validate -f json _site > html-validate-report.json"
   ```

Next steps
- After templates are updated, rebuild `_site` and re-run the validator. The issue list per-file will shrink.

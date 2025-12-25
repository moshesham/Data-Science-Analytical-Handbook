# Comprehensive Implementation Master Plan

## Overview
This document outlines the step-by-step execution plan to transform the *Data Science Analytical Handbook* from a collection of markdown files into a fully interactive, structured, and user-friendly static website hosted on GitHub Pages. It incorporates all tasks identified in the `CONTENT_REVIEW_PLAN.md`.

**Core Philosophy:** "Static Infrastructure, Dynamic Experience." We will use Jekyll's build-time features (Liquid, Data files) and client-side JavaScript to emulate dynamic app features without a backend.

**Repository Strategy:** We will proceed with a **Monorepo** structure initially to unify the brand and simplify maintenance. We will structure folders (`Best-Practices`, `Projects`) so they *can* be split into separate repositories later if needed, but for now, they will be integrated into the main site for better discoverability.

---

## Phase 0: Housekeeping & Quick Wins (Immediate Actions)
**Goal:** Fix immediate quality issues, typos, and file naming conventions to establish a clean baseline.

### 0.1 File Renaming & Cleanup
*   **Task:** Rename files for better SEO and clarity.
*   **Actions:**
    1.  `Simulations/Hands-On-Statitistics.ipynb` → `Simulations/Hands-On-Statistics.ipynb` (Fix Typo).
    2.  `_pages/foundational_knowledge/1.md` → `_pages/foundational_knowledge/1-statistics-probability.md`.
    3.  `_pages/foundational_knowledge/3.md` → `_pages/foundational_knowledge/3-python-analysis.md`.
    4.  Update all internal links referencing these files.

### 0.2 Initial Content Stubs
*   **Task:** Create placeholder files for missing content to ensure navigation links work.
*   **Actions:**
    1.  Create `supplementary/sql-cheat-sheet.md`.
    2.  Create `supplementary/statistics-cheat-sheet.md`.
    3.  Create `_pages/interview_preparation/interview-day-checklist.md`.

---

## Phase 1: Infrastructure & Metadata Standardization (The Foundation)
**Goal:** Establish a consistent data structure across all content to enable advanced filtering, sorting, and navigation.

### 1.1 Standardize Front Matter
*   **Task:** Audit and update the YAML front matter of every `.md` file.
*   **Schema:**
    ```yaml
    ---
    layout: page
    title: "Page Title"
    permalink: /path/to/page/
    nav_order: 1
    parent: "Category Name" (Optional)
    difficulty: "Beginner" | "Intermediate" | "Advanced"
    estimated_time: "15 mins"
    tags: [SQL, Python, Strategy]
    track: "Product Analytics" | "Data Engineering" | "Interview Prep"
    ---
    ```
*   **Action:** Update all pages to include `estimated_time` and `difficulty`.

### 1.2 Data-Driven Navigation
*   **Task:** Move navigation logic out of `_includes/sidebar.html` and into a data file.
*   **Action:**
    1.  Create `_data/navigation.yml`.
    2.  Define the menu structure (nested items) to support expandable sub-menus.
    3.  Rewrite `_includes/sidebar.html` to iterate through `site.data.navigation`.

### 1.3 Search Functionality
*   **Task:** Enable site-wide search.
*   **Action:**
    1.  Implement `lunr.js` or `simple-jekyll-search` for client-side search.
    2.  Add a search bar to the sidebar or header.

---

## Phase 2: Content Restructuring & Learning Tracks (The Structure)
**Goal:** Allow users to consume content by "Goal" (Track) or "Skill" rather than just file folder structure.

### 2.1 Implement Learning Tracks
*   **Task:** Create dedicated landing pages for different user personas.
*   **Action:**
    1.  Create `_data/tracks.yml` defining tracks (e.g., "The 21-Day Sprint", "Deep Dive Engineering", "Product Strategy").
    2.  Create `_pages/tracks/index.md` as a dashboard.
    3.  Integrate `Best-Practices/` content into the "Data Engineering" track.

### 2.2 Skills Matrix & Progress Tracking
*   **Task:** Create a "Tag Cloud" and simple progress tracking.
*   **Action:**
    1.  Create `_pages/skills.md` to list content by tag.
    2.  Implement a simple "Mark as Complete" button using `localStorage` (Client-side only) to track progress across sessions.

---

## Phase 3: Interactivity & Tools (The "No-Backend" Features)
**Goal:** Replace static reading with active doing.

### 3.1 Interactive Calculators (JavaScript)
*   **Task:** Port utility logic to client-side JS.
*   **Action:**
    1.  Create `_pages/tools/sample-size-calculator.md`.
    2.  Embed HTML forms and JavaScript to calculate A/B test sample sizes.

### 3.2 Interactive Quizzes
*   **Task:** Add knowledge checks at the end of chapters.
*   **Action:**
    1.  Create `_data/quizzes.yml`.
    2.  Create `_includes/quiz_widget.html`.
    3.  Add quizzes to SQL and Python pages.

### 3.3 Simulation Visualizations
*   **Task:** Visualize probability concepts.
*   **Action:**
    1.  Create `_pages/simulations/distributions.md`.
    2.  Use **Chart.js** to render interactive Normal/Binomial distributions.

---

## Phase 4: Content Expansion & Gap Filling
**Goal:** Address the "Sparse" and "Incomplete" areas identified in the review.

### 4.1 Expand Core Pages
*   **Task:** Flesh out placeholders.
*   **Action:**
    1.  **Conclusion:** Expand `_pages/conclusion.md` with career growth advice.
    2.  **Appendix:** Convert `_pages/appendix.md` to a "Data Science Glossary" (Terms A-Z).
    3.  **Real World Distributions:** Complete `supplementary/real-world-data-distributions.md` with the visualizations from Phase 3.3.
    4.  **Statistics:** Expand `1-statistics-probability.md` with worked examples.

### 4.2 Create Cheat Sheets & Checklists
*   **Task:** Create high-value reference materials.
*   **Action:**
    1.  **SQL Cheat Sheet:** Fill `supplementary/sql-cheat-sheet.md` with JOINs, Window Functions, etc.
    2.  **Stats Cheat Sheet:** Fill `supplementary/statistics-cheat-sheet.md` with formulas.
    3.  **Interview Checklist:** Fill `_pages/interview_preparation/interview-day-checklist.md`.

---

## Phase 5: Project & Notebook Integration
**Goal:** Showcase the "Hands-On" aspect effectively.

### 5.1 Notebook Rendering strategy
*   **Task:** Display `.ipynb` files natively in the static site.
*   **Action:**
    1.  Set up GitHub Action to convert notebooks to Markdown.
    2.  Ensure `Simulations/Hands-On-Statistics.ipynb` renders correctly.

### 5.2 New Hands-On Projects
*   **Task:** Create new project repositories/folders.
*   **Action:**
    1.  **Customer Churn:** Create `Analytical-HandsOn-Projects/Customer_Churn_Project/` (Notebook + Data).
    2.  **Cohort Analysis:** Create `Analytical-HandsOn-Projects/Cohort_Analysis_Project/`.
    3.  **A/B Testing:** Create `Analytical-HandsOn-Projects/AB_Test_Project/`.

### 5.3 Streamlit App Integration
*   **Task:** Link to external app.
*   **Action:**
    1.  Deploy `streamlit_app/` to Streamlit Cloud.
    2.  Add "Live App" link in the Handbook's navigation.

---

## Phase 6: Quality Assurance & Deployment
**Goal:** Ensure stability.

### 6.1 CI/CD Maintenance
*   **Task:** Keep the workflows green.
*   **Action:**
    1.  Monitor `html-validate` as we add new JS widgets.
    2.  Monitor `markdown-link-check` as we reorganize folders.

### 6.2 SEO & Analytics
*   **Task:** Make the site discoverable.
*   **Action:**
    1.  Configure `jekyll-seo-tag`.
    2.  Add Google Analytics.

---

## Execution Roadmap (Next Steps)

1.  **Immediate:** Execute **Phase 0** (Renames & Stubs).
2.  **Short Term:** Execute **Phase 1.2** (Navigation Refactor).
3.  **Mid Term:** Build the "Sample Size Calculator" (Phase 3.1).
4.  **Long Term:** Write missing content (Phase 4).

---
layout: default
title: "Analytical Engineering"
permalink: /analytical-engineering/
difficulty: "Intermediate"
estimated_time: "45 mins"
tags: [Analytical Engineering, dbt, Warehousing, Data Modeling, Quality]
track: "Analytical Engineering"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <span>Analytical Engineering</span>
</div>

<div class="header">
  <h1>Analytical Engineering</h1>
  <p>Build reliable, versioned, tested analytics datasets (the bridge between Data Engineering and Analytics).</p>
</div>

<div class="section">

  <div class="card">
    <h3>What is Analytical Engineering?</h3>
    <p>Analytical Engineering focuses on turning raw data into trustworthy analytics tables—clean, documented, and tested—so analysts and data scientists can move fast without re-solving data quality and definition problems in every query.</p>
    <ul>
      <li><strong>Inputs:</strong> raw/staging tables from ETL/ELT</li>
      <li><strong>Outputs:</strong> curated dimensions/facts, metric layers, semantic definitions</li>
      <li><strong>Tooling patterns:</strong> SQL-first transforms, version control, automated tests, CI</li>
    </ul>
  </div>

  <div class="card">
    <h3>Core Deliverables (What You Actually Build)</h3>
    <ul>
      <li><strong>Staging models:</strong> typed columns, standardized naming, deduplication, light cleaning.</li>
      <li><strong>Intermediate models:</strong> reusable logic (sessionization, attribution, cohort tables).</li>
      <li><strong>Marts:</strong> business-ready facts/dimensions with clear grains and stable keys.</li>
      <li><strong>Quality gates:</strong> uniqueness, not-null, referential integrity, freshness, volume anomalies.</li>
      <li><strong>Documentation:</strong> source-to-metric lineage and definitions that match stakeholder language.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Step-by-Step Tutorial: From Raw Orders to an Analytics Fact</h3>
    <p><strong>Goal:</strong> create a trustworthy <code>fact_orders</code> in Postgres with deduplication, incremental loading, and checks.</p>

    <p><strong>Step 1 — Define the grain and keys</strong></p>
    <ul>
      <li><strong>Grain:</strong> one row per <code>order_id</code></li>
      <li><strong>Primary key:</strong> <code>order_id</code></li>
      <li><strong>Foreign keys:</strong> <code>user_id</code> references <code>dim_users(user_id)</code></li>
    </ul>

    <p><strong>Step 2 — Stage raw data (dedupe + type safety)</strong></p>
    <pre><code>-- stg_orders: keep latest record per order_id
WITH ranked AS (
  SELECT
    r.*,
    ROW_NUMBER() OVER (
      PARTITION BY r.order_id
      ORDER BY r.updated_at DESC, r.ingested_at DESC
    ) AS rn
  FROM raw_orders r
)
SELECT
  order_id,
  user_id,
  amount::numeric(12,2) AS amount,
  updated_at::timestamptz AS updated_at
FROM ranked
WHERE rn = 1;</code></pre>

    <p><strong>Step 3 — Build the fact table (idempotent upsert)</strong></p>
    <pre><code>INSERT INTO analytics.fact_orders (order_id, user_id, amount, updated_at)
SELECT order_id, user_id, amount, updated_at
FROM analytics.stg_orders
ON CONFLICT (order_id) DO UPDATE
SET
  user_id = EXCLUDED.user_id,
  amount = EXCLUDED.amount,
  updated_at = EXCLUDED.updated_at
WHERE analytics.fact_orders.updated_at IS DISTINCT FROM EXCLUDED.updated_at;</code></pre>

    <p><strong>Step 4 — Add quality checks (run in CI)</strong></p>
    <pre><code>-- Primary key uniqueness
  SELECT COUNT(*) AS rows, COUNT(DISTINCT order_id) AS distinct_order_ids
  FROM analytics.fact_orders;

  -- No null keys
  SELECT COUNT(*) AS null_order_id
  FROM analytics.fact_orders
  WHERE order_id IS NULL;

  -- Referential integrity
  SELECT COUNT(*) AS orphan_orders
  FROM analytics.fact_orders o
  LEFT JOIN analytics.dim_users u ON o.user_id = u.user_id
  WHERE o.user_id IS NOT NULL AND u.user_id IS NULL;</code></pre>

    <p><strong>Step 5 — Publish definitions</strong></p>
    <ul>
      <li>What is <code>amount</code>? Gross? Net of refunds? In what currency?</li>
      <li>What is an “order”? Does it include cancelled orders?</li>
      <li>What timestamp do we use for “order date”? created vs paid vs shipped?</li>
    </ul>
  </div>

  <div class="card">
    <h3>Deep Dive Pages</h3>
    <ul>
      <li><a href="{{ '/analytical-engineering/advanced-sql-postgres/' | relative_url }}">Advanced SQL (Postgres) for Analytical Engineering</a></li>
    </ul>
  </div>

</div>

<div class="navigation-buttons">
  <a href="{{ '/foundational-knowledge/' | relative_url }}">Previous: Foundational Knowledge</a>
  <a href="{{ '/analytical-engineering/advanced-sql-postgres/' | relative_url }}">Next: Advanced SQL (Postgres)</a>
</div>

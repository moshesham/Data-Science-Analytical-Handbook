---
layout: default
title: "Advanced SQL (Postgres) for Analytical Engineering"
permalink: /analytical-engineering/advanced-sql-postgres/
difficulty: "Advanced"
estimated_time: "90 mins"
tags: [SQL, Postgres, Analytical Engineering, Modeling, Quality, Incremental]
track: "Analytical Engineering"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/analytical-engineering/' | relative_url }}">Analytical Engineering</a> <span>&gt;</span>
  <span>Advanced SQL (Postgres)</span>
</div>

<div class="header">
  <h1>Advanced SQL (Postgres) for Analytical Engineering</h1>
  <p>Production-grade SQL patterns for reliable analytics datasets: layered modeling, idempotent loads, de-duplication, SCD2, QA checks, and performance.</p>
</div>

<div class="section">

  <div class="card">
    <h3>Analytical Engineering Mental Model</h3>
    <ul>
      <li><strong>Contract:</strong> define grains, keys, and metric definitions.</li>
      <li><strong>Layering:</strong> <code>raw</code> → <code>staging</code> → <code>intermediate</code> → <code>marts</code> (facts/dims).</li>
      <li><strong>Idempotent builds:</strong> re-running should converge to the same truth.</li>
      <li><strong>Quality gates:</strong> tests run every build; failures block deploy.</li>
      <li><strong>Performance:</strong> indexes, pre-aggregation, and avoiding join fanout.</li>
    </ul>
  </div>

  <div class="card">
    <h3>1) Postgres Power Tools (Worth Memorizing)</h3>
    <ul>
      <li><strong><code>COUNT(*) FILTER (WHERE ...)</code>:</strong> clean conditional aggregation.</li>
      <li><strong><code>DISTINCT ON</code>:</strong> fastest readable “latest per key” pattern.</li>
      <li><strong><code>INSERT ... ON CONFLICT</code>:</strong> practical upsert for idempotent loads.</li>
      <li><strong><code>IS DISTINCT FROM</code>:</strong> NULL-safe comparisons in updates/joins.</li>
      <li><strong><code>generate_series</code>:</strong> create date spines for complete time series.</li>
      <li><strong><code>EXPLAIN (ANALYZE, BUFFERS)</code>:</strong> diagnose scans vs indexes and row estimates.</li>
    </ul>
  </div>

  <div class="card">
    <h3>2) Tutorial: Build a Trustworthy Orders Mart (End-to-End)</h3>
    <p><strong>Scenario:</strong> You ingest <code>raw_orders</code> and want a stable <code>analytics.fact_orders</code> used by analysts.</p>

    <p><strong>Step 0 — Table conventions</strong></p>
    <ul>
      <li><strong>raw:</strong> append-only, may contain duplicates and schema drift.</li>
      <li><strong>staging:</strong> typed, standardized names, deduplicated.</li>
      <li><strong>mart:</strong> business-ready columns, keys, and constraints.</li>
    </ul>

    <p><strong>Step 1 — Staging: latest record wins</strong></p>
    <pre><code>-- stg_orders: one row per order_id
CREATE SCHEMA IF NOT EXISTS analytics;

CREATE OR REPLACE VIEW analytics.stg_orders AS
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
  status::text AS status,
  created_at::timestamptz AS created_at,
  updated_at::timestamptz AS updated_at
FROM ranked
WHERE rn = 1;</code></pre>

    <p><strong>Step 2 — Mart table: constraints are part of data quality</strong></p>
    <pre><code>CREATE TABLE IF NOT EXISTS analytics.fact_orders (
  order_id   text PRIMARY KEY,
  user_id    text,
  amount     numeric(12,2) NOT NULL,
  status     text NOT NULL,
  created_at timestamptz NOT NULL,
  updated_at timestamptz NOT NULL
);

CREATE INDEX IF NOT EXISTS fact_orders_user_id_idx ON analytics.fact_orders(user_id);
CREATE INDEX IF NOT EXISTS fact_orders_created_at_idx ON analytics.fact_orders(created_at);</code></pre>

    <p><strong>Step 3 — Idempotent upsert load</strong></p>
    <pre><code>INSERT INTO analytics.fact_orders (order_id, user_id, amount, status, created_at, updated_at)
SELECT order_id, user_id, amount, status, created_at, updated_at
FROM analytics.stg_orders
ON CONFLICT (order_id) DO UPDATE
SET
  user_id    = EXCLUDED.user_id,
  amount     = EXCLUDED.amount,
  status     = EXCLUDED.status,
  created_at = EXCLUDED.created_at,
  updated_at = EXCLUDED.updated_at
WHERE analytics.fact_orders.updated_at IS DISTINCT FROM EXCLUDED.updated_at;</code></pre>

    <p><strong>Step 4 — Watermarking (incremental)</strong></p>
    <p>In Postgres you usually keep the watermark in an orchestration system (Airflow, Dagster) or a control table.</p>
    <pre><code>CREATE TABLE IF NOT EXISTS analytics.job_control (
  job_name text PRIMARY KEY,
  last_success_ts timestamptz NOT NULL
);

-- Example: read watermark
SELECT last_success_ts
FROM analytics.job_control
WHERE job_name = 'orders_mart';</code></pre>

    <p><strong>Step 5 — Tests you can run as queries (CI gates)</strong></p>
    <pre><code>-- 1) PK uniqueness (should match)
SELECT COUNT(*) AS rows, COUNT(DISTINCT order_id) AS distinct_order_ids
FROM analytics.fact_orders;

-- 2) No negative amounts (example business rule)
SELECT COUNT(*) AS bad_rows
FROM analytics.fact_orders
WHERE amount &lt; 0;

-- 3) Valid statuses (example enum-like rule)
SELECT status, COUNT(*)
FROM analytics.fact_orders
GROUP BY 1
HAVING status NOT IN ('created','paid','shipped','refunded','cancelled');</code></pre>
  </div>

  <div class="card">
    <h3>3) SCD Type 2 in Postgres (Practical Pattern)</h3>
    <p><strong>Goal:</strong> keep history for changing attributes (e.g., user plan).</p>
    <p><strong>Table:</strong> <code>dim_user_plan(user_id, plan, valid_from, valid_to, is_current)</code></p>

    <p><strong>Step-by-step:</strong> identify changes → expire current → insert new current. Wrap in a transaction in real jobs.</p>
    <pre><code>-- Find changed users
WITH current_dim AS (
  SELECT * FROM analytics.dim_user_plan WHERE is_current = true
), changes AS (
  SELECT s.user_id, s.plan
  FROM analytics.stg_user_plan s
  LEFT JOIN current_dim d
    ON s.user_id = d.user_id
  WHERE d.user_id IS NULL OR s.plan IS DISTINCT FROM d.plan
)
SELECT * FROM changes;</code></pre>

    <pre><code>-- Expire current rows for changed users
UPDATE analytics.dim_user_plan d
SET valid_to = NOW(), is_current = false
WHERE is_current = true
  AND EXISTS (
    SELECT 1
    FROM analytics.stg_user_plan s
    WHERE s.user_id = d.user_id
      AND s.plan IS DISTINCT FROM d.plan
  );</code></pre>

    <pre><code>-- Insert new current rows
INSERT INTO analytics.dim_user_plan (user_id, plan, valid_from, valid_to, is_current)
SELECT s.user_id, s.plan, NOW(), NULL, true
FROM analytics.stg_user_plan s
LEFT JOIN analytics.dim_user_plan d
  ON s.user_id = d.user_id AND d.is_current = true
WHERE d.user_id IS NULL OR s.plan IS DISTINCT FROM d.plan;</code></pre>
  </div>

  <div class="card">
    <h3>4) Time Series Completeness With a Date Spine</h3>
    <p><strong>Problem:</strong> charts lie when missing days disappear. Use a date spine and LEFT JOIN.</p>
    <pre><code>WITH spine AS (
  SELECT d::date AS day
  FROM generate_series(date '2025-01-01', date '2025-01-31', interval '1 day') AS t(d)
), daily AS (
  SELECT date_trunc('day', created_at)::date AS day, COUNT(*) AS orders
  FROM analytics.fact_orders
  GROUP BY 1
)
SELECT s.day, COALESCE(d.orders, 0) AS orders
FROM spine s
LEFT JOIN daily d USING (day)
ORDER BY s.day;</code></pre>
  </div>

  <div class="card">
    <h3>5) Avoiding Join Fanout (A Silent Analytics Killer)</h3>
    <p><strong>Rule:</strong> if you join facts to a dimension, the dimension side should be unique on the join key.</p>

    <p><strong>Detect non-unique dimension keys:</strong></p>
    <pre><code>SELECT user_id, COUNT(*)
FROM analytics.dim_users
GROUP BY 1
HAVING COUNT(*) &gt; 1
ORDER BY 2 DESC
LIMIT 50;</code></pre>

    <p><strong>Fix:</strong> dedupe the dimension to one row per key (e.g., latest wins) before joining.</p>
    <pre><code>WITH dim_users_latest AS (
  SELECT DISTINCT ON (user_id)
    user_id,
    country,
    updated_at
  FROM analytics.dim_users
  ORDER BY user_id, updated_at DESC
)
SELECT o.order_id, u.country
FROM analytics.fact_orders o
LEFT JOIN dim_users_latest u ON o.user_id = u.user_id;</code></pre>
  </div>

  <div class="card">
    <h3>6) Performance Notes (Postgres)</h3>
    <ul>
      <li><strong>Indexes:</strong> index join keys and common time filters; validate with <code>EXPLAIN (ANALYZE)</code>.</li>
      <li><strong>Large tables:</strong> consider partitioning by date for very large facts (range partitions).</li>
      <li><strong>Materialized views:</strong> good for expensive aggregates used repeatedly; refresh on schedule.</li>
      <li><strong>Vacuum/analyze:</strong> keep stats fresh so the planner chooses good plans.</li>
    </ul>
  </div>

</div>

<div class="navigation-buttons">
  <a href="{{ '/analytical-engineering/' | relative_url }}">Back: Analytical Engineering</a>
  <a href="{{ '/foundational_knowledge/2-SQL/' | relative_url }}">Next: SQL Fundamentals</a>
</div>

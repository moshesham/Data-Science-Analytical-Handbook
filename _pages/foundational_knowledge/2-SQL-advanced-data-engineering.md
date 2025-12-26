---
layout: default
title: "Advanced SQL for Data Engineering"
permalink: /foundational_knowledge/2-SQL/advanced/
difficulty: "Advanced"
estimated_time: "75 mins"
tags: [SQL, Data Engineering, ETL, Warehousing, Incremental Loads]
track: "Foundational Knowledge"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Foundational Knowledge & Skills</a> <span>&gt;</span>
  <a href="{{ '/foundational_knowledge/2-SQL/' | relative_url }}">SQL & Data Manipulation</a> <span>&gt;</span>
  <span>Advanced SQL for Data Engineering</span>
</div>

<div class="header">
  <h1>Advanced SQL for Data Engineering</h1>
  <p>Complex operations used in real pipelines: incremental loads, deduplication, SCD2, data quality checks, and performance patterns.</p>
</div>

<div class="section">

  <div class="card">
    <h3>How Data Engineering SQL Differs From Interview SQL</h3>
    <ul>
      <li><strong>Idempotency:</strong> running the same job twice should not double-count.</li>
      <li><strong>Incremental vs full refresh:</strong> compute only what changed (watermarks/partitions).</li>
      <li><strong>Schema discipline:</strong> stable keys, well-defined grains, and explicit type casting.</li>
      <li><strong>Quality gates:</strong> null checks, referential integrity, and anomaly detection queries.</li>
      <li><strong>Operational concerns:</strong> late-arriving data, backfills, and partition management.</li>
    </ul>
  </div>

  <div class="card">
    <h3>1) Incremental Loads With Watermarks</h3>
    <p><strong>Goal:</strong> load only new/updated rows since the last successful run.</p>
    <p><strong>Step-by-step:</strong> (1) read watermark (max processed timestamp), (2) filter source, (3) upsert into target, (4) advance watermark when successful.</p>

    <pre><code>-- Assume a control table that stores the last successful processed timestamp
-- job_control(job_name, last_success_ts)

WITH params AS (
  SELECT last_success_ts
  FROM job_control
  WHERE job_name = 'orders_incremental'
), staged AS (
  SELECT o.*
  FROM raw_orders o
  CROSS JOIN params p
  WHERE o.updated_at &gt; p.last_success_ts
)
SELECT COUNT(*) AS rows_to_process
FROM staged;</code></pre>

    <p><strong>Upsert (Postgres):</strong> prefer <code>INSERT ... ON CONFLICT ... DO UPDATE</code>. (Postgres 15+ also supports <code>MERGE</code>, but <code>ON CONFLICT</code> is widely used.)</p>
    <pre><code>-- Pre-req: analytics.orders(order_id) must be UNIQUE or PRIMARY KEY
INSERT INTO analytics.orders (order_id, user_id, amount, updated_at)
SELECT order_id, user_id, amount, updated_at
FROM staged
ON CONFLICT (order_id) DO UPDATE
SET
  user_id = EXCLUDED.user_id,
  amount = EXCLUDED.amount,
  updated_at = EXCLUDED.updated_at
WHERE analytics.orders.updated_at IS DISTINCT FROM EXCLUDED.updated_at;</code></pre>

    <p><strong>Notes:</strong> pick a stable key (e.g., <code>order_id</code>), and make sure <code>updated_at</code> is trustworthy.</p>
  </div>

  <div class="card">
    <h3>2) De-duplication in Staging (Latest Wins)</h3>
    <p><strong>Problem:</strong> raw sources often contain duplicates (retries, CDC artifacts). You need a deterministic rule.</p>

    <p><strong>Step-by-step:</strong> (1) partition by business key, (2) order by ingestion/update time, (3) keep row_number=1.</p>
    <pre><code>WITH ranked AS (
  SELECT
    r.*,
    ROW_NUMBER() OVER (
      PARTITION BY r.order_id
      ORDER BY r.updated_at DESC, r.ingested_at DESC
    ) AS rn
  FROM raw_orders r
)
SELECT *
FROM ranked
WHERE rn = 1;</code></pre>
  </div>

  <div class="card">
    <h3>3) SCD Type 2 (Slowly Changing Dimension)</h3>
    <p><strong>Use case:</strong> you want historical truth (e.g., user plan changes over time) rather than overwriting.</p>

    <p><strong>Target table pattern:</strong> <code>(user_id, plan, valid_from, valid_to, is_current)</code></p>
    <p><strong>Step-by-step idea:</strong></p>
    <ul>
      <li>Identify changed records vs current dimension (compare attributes).</li>
      <li>Expire current rows (<code>valid_to = load_ts</code>, <code>is_current = false</code>).</li>
      <li>Insert new current rows (<code>valid_from = load_ts</code>, <code>valid_to = NULL</code>, <code>is_current = true</code>).</li>
    </ul>

    <pre><code>-- 1) Find changes vs the current dimension row
WITH current_dim AS (
  SELECT * FROM dim_user_plan WHERE is_current = true
), changes AS (
  SELECT s.user_id, s.plan
  FROM staged_user_plan s
  LEFT JOIN current_dim d
    ON s.user_id = d.user_id
  WHERE d.user_id IS NULL OR s.plan &lt;&gt; d.plan
)
SELECT * FROM changes;</code></pre>

    <p><strong>Tip:</strong> in warehouses that support it, implement SCD2 with two statements (expire + insert) inside a transaction.</p>
  </div>

  <div class="card">
    <h3>4) Building Fact Tables: Star Schema Mindset</h3>
    <p><strong>Rule:</strong> facts should have a clear grain and foreign keys to dimensions.</p>
    <pre><code>-- Example: daily_user_activity_fact at user-day grain
WITH events_clean AS (
  SELECT
    user_id,
    date_trunc('day', event_ts) AS day,
    event_name
  FROM events
  WHERE user_id IS NOT NULL
)
SELECT
  user_id,
  day,
  COUNT(*) AS events,
  COUNT(*) FILTER (WHERE event_name = 'purchase') AS purchases
FROM events_clean
GROUP BY 1, 2;</code></pre>
    <p><strong>Postgres note:</strong> <code>FILTER</code> is supported and is usually cleaner than <code>SUM(CASE WHEN ...)</code>.</p>
  </div>

  <div class="card">
    <h3>5) Data Quality Checks You Can Run in SQL</h3>
    <p>These checks are commonly automated in pipeline validation steps.</p>

    <p><strong>Null rate check:</strong></p>
    <pre><code>SELECT
  COUNT(*) AS rows,
  SUM(CASE WHEN user_id IS NULL THEN 1 ELSE 0 END) AS null_user_id
FROM analytics.orders;</code></pre>

    <p><strong>Uniqueness check (primary key):</strong></p>
    <pre><code>SELECT
  COUNT(*) AS rows,
  COUNT(DISTINCT order_id) AS distinct_order_ids
FROM analytics.orders;</code></pre>

    <p><strong>Referential integrity (anti-join):</strong></p>
    <pre><code>SELECT COUNT(*) AS orphan_orders
FROM analytics.orders o
LEFT JOIN analytics.users u
  ON o.user_id = u.user_id
WHERE u.user_id IS NULL;</code></pre>

    <p><strong>Anomaly check (day-over-day volume):</strong></p>
    <pre><code>WITH daily AS (
  SELECT date_trunc('day', order_ts) AS day, COUNT(*) AS orders
  FROM analytics.orders
  GROUP BY 1
)
SELECT
  day,
  orders,
  LAG(orders) OVER (ORDER BY day) AS prev_orders,
  CASE
    WHEN LAG(orders) OVER (ORDER BY day) IS NULL THEN NULL
    WHEN LAG(orders) OVER (ORDER BY day) = 0 THEN NULL
    ELSE orders::float / LAG(orders) OVER (ORDER BY day)
  END AS ratio_vs_prev
FROM daily
ORDER BY day;</code></pre>
  </div>

  <div class="card">
    <h3>6) Performance Patterns (Warehouses)</h3>
    <ul>
      <li><strong>Partition pruning:</strong> filter on partition columns (e.g., <code>event_date</code>) to scan less data.</li>
      <li><strong>Pre-aggregate:</strong> aggregate large fact tables before joining to wide dimensions.</li>
      <li><strong>Avoid accidental fanout:</strong> validate join key uniqueness on the dimension side.</li>
      <li><strong>Materialize heavy steps:</strong> use intermediate tables/materialized views for recurring expensive CTEs.</li>
      <li><strong>Choose correct grain:</strong> store raw + curated layers; don’t force analytics queries to parse messy raw data.</li>
    </ul>
  </div>

</div>

<div class="navigation-buttons">
  <a href="{{ '/foundational_knowledge/2-SQL/' | relative_url }}">Back: SQL & Data Manipulation</a>
  <a href="{{ '/foundational_knowledge/3/' | relative_url }}">Next: Programming (Python/R) for Data Analysis</a>
</div>

---
layout: default
title: "SQL & Data Manipulation"
permalink: /foundational_knowledge/2-SQL/
difficulty: "Intermediate"
estimated_time: "60 mins"
tags: [SQL, Data Manipulation, Query Optimization]
track: "Foundational Knowledge"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Foundational Knowledge & Skills</a> <span>&gt;</span>
  <span>SQL & Data Manipulation</span>
</div>

<div class="header">
  <h1>SQL & Data Manipulation</h1>
  <p>Core SQL syntax, advanced techniques, query optimization, and data cleaning with SQL.</p>
</div>

<div class="section">
  <div class="card">
    <h3>Want the Data Engineering version?</h3>
    <p>Go deeper on incremental loads, deduplication, SCD2, and data quality checks:</p>
    <p><a href="{{ '/foundational_knowledge/2-SQL/advanced/' | relative_url }}" class="button">Advanced SQL for Data Engineering →</a></p>
  </div>
</div>

<div class="section">
  
  <div class="card">
    <h3>What Can You Expect?</h3>
    <p>You can expect SQL coding questions that involve:</p>
    <ul>
      <li>Writing complex queries, joining tables, aggregating data</li>
      <li>Using window functions and optimizing query performance</li>
      <li>Analyzing a large dataset or solving a business problem using SQL</li>
    </ul>
  </div>

  <div class="card">
    <h3>How to Prep</h3>
    <ul>
      <li>Practice writing SQL queries regularly and focus on efficiency.</li>
      <li>Be prepared to explain your code and its logic.</li>
      <li><strong>Resources:</strong>
        <ul>
          <li><a href="https://sqlzoo.net/" target="_blank">SQLZOO</a></li>
          <li><a href="https://www.hackerrank.com/domains/sql" target="_blank">HackerRank SQL</a></li>
          <li><a href="https://leetcode.com/problemset/database/" target="_blank">LeetCode Database</a></li>
          <li><a href="https://platform.stratascratch.com/coding" target="_blank">StrataScratch</a></li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="card">
    <h3>Key SQL Concepts</h3>
    <ul>
      <li><strong>SELECT, FROM, WHERE:</strong> Basic query structure.</li>
      <li><strong>JOINs (INNER, LEFT, RIGHT, FULL):</strong> Combining data from multiple tables.</li>
      <li><strong>GROUP BY and Aggregate Functions (COUNT, SUM, AVG, MIN, MAX):</strong> Summarizing data.</li>
      <li><strong>Window Functions (ROW_NUMBER, RANK, LAG, LEAD):</strong> Performing calculations across rows related to the current row.</li>
      <li><strong>Subqueries and CTEs (Common Table Expressions):</strong> Creating reusable query blocks.</li>
    </ul>
  </div>

  <div class="card">
    <h3>SQL Concepts, Explained (With Examples)</h3>

    <h4>1) Filtering: <code>WHERE</code> vs <code>HAVING</code></h4>
    <ul>
      <li><strong><code>WHERE</code> filters rows</strong> before aggregation.</li>
      <li><strong><code>HAVING</code> filters groups</strong> after <code>GROUP BY</code>.</li>
    </ul>
    <pre><code>-- WHERE filters raw rows
SELECT user_id, SUM(amount) AS total
FROM Orders
WHERE order_date &gt;= '2025-01-01' AND order_date &lt; '2025-02-01'
GROUP BY 1;

-- HAVING filters aggregated groups
SELECT user_id, SUM(amount) AS total
FROM Orders
GROUP BY 1
HAVING SUM(amount) &gt;= 100;</code></pre>

    <h4>2) JOIN types (what they return)</h4>
    <ul>
      <li><strong>INNER JOIN:</strong> only matching keys on both sides.</li>
      <li><strong>LEFT JOIN:</strong> keep all left rows; unmatched right is NULL.</li>
      <li><strong>FULL OUTER JOIN:</strong> keep all rows from both sides (not available everywhere).</li>
    </ul>
    <pre><code>-- LEFT JOIN + ON clause filtering (keeps users with zero orders)
SELECT
  u.user_id,
  COUNT(o.order_id) AS orders_in_jan
FROM Users u
LEFT JOIN Orders o
  ON u.user_id = o.user_id
 AND o.order_date &gt;= '2025-01-01'
 AND o.order_date &lt;  '2025-02-01'
GROUP BY 1;</code></pre>

    <h4>3) Null handling: <code>COALESCE</code> and NULL-safe math</h4>
    <pre><code>SELECT
  user_id,
  COALESCE(SUM(amount), 0) AS total_spend
FROM Orders
GROUP BY 1;</code></pre>

    <h4>4) Set logic: <code>UNION ALL</code> vs <code>UNION</code></h4>
    <ul>
      <li><strong><code>UNION ALL</code> keeps duplicates</strong> (faster, preferred unless you need de-dup).</li>
      <li><strong><code>UNION</code> removes duplicates</strong> (extra sort/dedup cost).</li>
    </ul>
  </div>

  <div class="card">
    <h3>Interview-Grade SQL: Mental Model</h3>
    <ul>
      <li><strong>Start from grain:</strong> What is one row in the final output? (user-day, order, session, etc.)</li>
      <li><strong>Separate concerns:</strong> Use CTEs to isolate <em>filtering</em>, <em>joining</em>, <em>aggregation</em>, and <em>windowing</em>.</li>
      <li><strong>Be explicit about time:</strong> Use half-open intervals (<code>&gt;= start</code> and <code>&lt; next_day/month</code>) to avoid boundary bugs.</li>
      <li><strong>Know your dialect:</strong> Date functions and percentiles differ. This handbook assumes <strong>Postgres</strong> unless stated otherwise.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Postgres Quick Reference (High-Value in Interviews)</h3>
    <ul>
      <li><strong>Date bucketing:</strong> <code>date_trunc('day'|'week'|'month', ts)</code></li>
      <li><strong>Half-open time filters:</strong> <code>ts &gt;= '2025-01-01' AND ts &lt; '2025-02-01'</code></li>
      <li><strong>Conditional aggregation:</strong> <code>COUNT(*) FILTER (WHERE ...)</code> or <code>SUM(CASE WHEN ... THEN 1 ELSE 0 END)</code></li>
      <li><strong>De-dupe shortcut:</strong> <code>DISTINCT ON (key) ... ORDER BY key, updated_at DESC</code></li>
      <li><strong>Upsert:</strong> <code>INSERT ... ON CONFLICT (key) DO UPDATE</code></li>
      <li><strong>NULL-safe comparison:</strong> <code>IS DISTINCT FROM</code></li>
    </ul>

    <p><strong><code>DISTINCT ON</code> example (latest row per user):</strong></p>
    <pre><code>SELECT DISTINCT ON (user_id)
  user_id,
  plan,
  updated_at
FROM user_profiles
ORDER BY user_id, updated_at DESC;</code></pre>
  </div>

  <div class="card">
    <h3>Core Patterns You Will Be Asked</h3>
    <ul>
      <li><strong>Conditional aggregation:</strong> multiple metrics in one pass using <code>SUM(CASE WHEN ... THEN 1 ELSE 0 END)</code>.</li>
      <li><strong>Top-N per group:</strong> <code>ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)</code> then filter to <code>rn &lt;= N</code>.</li>
      <li><strong>De-duplication:</strong> keep latest record per entity with <code>ROW_NUMBER()</code> and <code>QUALIFY</code> (if supported) or a wrapping CTE.</li>
      <li><strong>Retention:</strong> cohort on first event, compute period offsets, pivot/aggregate to a retention table.</li>
      <li><strong>Funnels:</strong> step completion counts per user/session, then aggregate conversion between steps.</li>
      <li><strong>Rolling metrics:</strong> 7-day rolling average/sum using window frames.</li>
    </ul>

    <p><strong>Conditional aggregation template:</strong></p>
    <pre><code>SELECT
  date_trunc('day', event_ts) AS day,
  COUNT(DISTINCT user_id) AS dau,
  SUM(CASE WHEN event_name = 'purchase' THEN 1 ELSE 0 END) AS purchases,
  COUNT(DISTINCT CASE WHEN event_name = 'purchase' THEN user_id END) AS purchasing_users
FROM events
WHERE event_ts &gt;= '2025-01-01' AND event_ts &lt; '2025-02-01'
GROUP BY 1
ORDER BY 1;</code></pre>
  </div>

  <div class="card">
    <h3>Window Functions: Practical Recipes</h3>
    <p><strong>1) Latest record per user (de-dupe):</strong></p>
    <pre><code>WITH ranked AS (
  SELECT
    u.*,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY updated_at DESC) AS rn
  FROM user_profiles u
)
SELECT *
FROM ranked
WHERE rn = 1;</code></pre>

    <p><strong>2) Top 3 items per store by revenue:</strong></p>
    <pre><code>WITH store_item AS (
  SELECT store_id, item_id, SUM(revenue) AS rev
  FROM sales
  GROUP BY 1, 2
), ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY rev DESC) AS rn
  FROM store_item
)
SELECT store_id, item_id, rev
FROM ranked
WHERE rn &lt;= 3
ORDER BY store_id, rn;</code></pre>

    <p><strong>3) 7-day rolling DAU (window frame):</strong></p>
    <pre><code>WITH daily AS (
  SELECT
    date_trunc('day', event_ts) AS day,
    COUNT(DISTINCT user_id) AS dau
  FROM events
  GROUP BY 1
)
SELECT
  day,
  dau,
  AVG(dau) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS dau_7d_avg
FROM daily
ORDER BY day;</code></pre>
  </div>

  <div class="card">
    <h3>Step-by-Step Walkthrough: "Total Spend for Jan 2023 Signups"</h3>
    <p><strong>Problem:</strong> Given <code>Users(user_id, signup_date)</code> and <code>Orders(order_id, user_id, order_date, amount)</code>, compute total spend per user <em>for users who signed up in Jan 2023</em>.</p>

    <p><strong>Step 1 — Decide the output grain:</strong> one row per <code>user_id</code>.</p>
    <p><strong>Step 2 — Filter users by signup month:</strong> use a half-open interval to avoid end-of-month edge cases.</p>
    <p><strong>Step 3 — Join to orders:</strong> decide whether you want to keep users with zero orders. In most product analytics, you do.</p>
    <p><strong>Step 4 — Aggregate:</strong> sum amount per user.</p>

    <pre><code>WITH jan_signups AS (
  SELECT user_id
  FROM Users
  WHERE signup_date &gt;= '2023-01-01'
    AND signup_date &lt;  '2023-02-01'
)
SELECT
  u.user_id,
  COALESCE(SUM(o.amount), 0) AS total_spent
FROM jan_signups u
LEFT JOIN Orders o
  ON u.user_id = o.user_id
GROUP BY 1
ORDER BY 1;</code></pre>

    <p><strong>Common follow-up questions:</strong></p>
    <ul>
      <li>If you only want spend <em>within January</em>, add an order_date filter (in the <code>ON</code> clause if keeping zero-order users).</li>
      <li>If <code>Orders</code> has refunds/chargebacks, define whether to net them out or filter them.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Step-by-Step Walkthrough: Top-N Per Group (Classic Window Question)</h3>
    <p><strong>Problem:</strong> “For each <code>store_id</code>, return the top 2 <code>item_id</code> by revenue.”</p>
    <p><strong>Step 1 — Aggregate to the ranking grain:</strong> store-item.</p>
    <p><strong>Step 2 — Rank within each store:</strong> <code>ROW_NUMBER()</code> with a deterministic tie-breaker if needed.</p>
    <p><strong>Step 3 — Filter to top N:</strong> <code>rn &lt;= 2</code>.</p>
    <pre><code>WITH store_item AS (
  SELECT
    store_id,
    item_id,
    SUM(revenue) AS rev
  FROM sales
  GROUP BY 1, 2
), ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY rev DESC, item_id) AS rn
  FROM store_item
)
SELECT store_id, item_id, rev
FROM ranked
WHERE rn &lt;= 2
ORDER BY store_id, rn;</code></pre>
  </div>

  <div class="card">
    <h3>NULLs, Duplicates, and Counting Correctly</h3>
    <ul>
      <li><strong><code>COUNT(*)</code> vs <code>COUNT(col)</code>:</strong> <code>COUNT(col)</code> ignores NULLs.</li>
      <li><strong>LEFT JOIN filter trap:</strong> filtering on right-table columns in <code>WHERE</code> turns it into an INNER JOIN; move those conditions into the <code>ON</code> clause when you truly want a LEFT JOIN.</li>
      <li><strong>Distinct counting with conditions:</strong> use <code>COUNT(DISTINCT CASE WHEN ... THEN id END)</code>.</li>
      <li><strong>Many-to-many joins:</strong> beware silent row multiplication; aggregate before joining when appropriate.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Query Performance & Readability (What Interviewers Notice)</h3>
    <ul>
      <li><strong>Filter early:</strong> reduce data before big joins/aggregations.</li>
      <li><strong>Project early:</strong> select only needed columns in CTEs (especially for wide tables).</li>
      <li><strong>Use <code>EXPLAIN</code> (if available):</strong> talk through join order, scans vs indexes, and cardinality.</li>
      <li><strong>Prefer deterministic ordering:</strong> if you use <code>ROW_NUMBER()</code>, ensure tie-breakers in <code>ORDER BY</code>.</li>
      <li><strong>Consistent style:</strong> one expression per line, uppercase keywords, and clear CTE names.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Example SQL Problem</h3>
    <p>Given two tables: <code>Users</code> (user_id, signup_date) and <code>Orders</code> (order_id, user_id, order_date, amount), write a query to find the total amount spent by each user who signed up in January 2023.</p>
    
    <pre><code>SELECT
  u.user_id,
  SUM(o.amount) AS total_spent
FROM Users u
JOIN Orders o
  ON u.user_id = o.user_id
WHERE u.signup_date &gt;= '2023-01-01'
  AND u.signup_date &lt;  '2023-02-01'
GROUP BY 1
ORDER BY 1;</code></pre>
  </div>

  <div class="card">
    <h3>Mini Practice Set (With Solutions)</h3>

    <p><strong>1) Daily new users:</strong> For <code>Users(user_id, signup_ts)</code>, return signup day and count of users.</p>
    <pre><code>SELECT
  date_trunc('day', signup_ts) AS signup_day,
  COUNT(*) AS new_users
FROM Users
GROUP BY 1
ORDER BY 1;</code></pre>

    <p><strong>2) Users with no orders (anti-join):</strong> For <code>Users</code> and <code>Orders</code>, list users who never ordered.</p>
    <pre><code>SELECT u.user_id
FROM Users u
LEFT JOIN Orders o
  ON u.user_id = o.user_id
WHERE o.user_id IS NULL;</code></pre>

    <p><strong>3) First purchase date per user:</strong></p>
    <pre><code>SELECT
  user_id,
  MIN(order_date) AS first_order_date
FROM Orders
GROUP BY 1;</code></pre>

    <p><strong>4) Top 1 most recent order per user:</strong></p>
    <pre><code>WITH ranked AS (
  SELECT
    o.*,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY order_date DESC, order_id DESC) AS rn
  FROM Orders o
)
SELECT *
FROM ranked
WHERE rn = 1;</code></pre>
  </div>

</div>

<div class="section">
  <h2>Test Your Knowledge</h2>
  {% include quiz_widget.html quiz_id="sql_basics" %}
</div>

<div class="navigation-buttons">
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Previous: Statistics & Probability</a>
  <a href="{{ '/foundational_knowledge/2-SQL/advanced/' | relative_url }}">Next: Advanced SQL for Data Engineering</a>
</div>

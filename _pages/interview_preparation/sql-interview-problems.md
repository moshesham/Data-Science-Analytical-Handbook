---
layout: default
title: "SQL Interview Problems"
permalink: /interview-preparation/sql-interview-problems/
difficulty: "Mixed"
estimated_time: "90 mins"
tags: [SQL, Interview, Practice, Postgres]
track: "Interview Preparation"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/interview-preparation/' | relative_url }}">Interview Preparation</a> <span>&gt;</span>
  <span>SQL Interview Problems</span>
</div>

<div class="header">
  <h1>SQL Interview Problems</h1>
  <p>15 curated problems covering patterns you'll see in FAANG interviews. All solutions in Postgres.</p>
</div>

<div class="section">

  <div class="card">
    <h3>How to Use This Page</h3>
    <ul>
      <li><strong>Difficulty:</strong> 🟢 Easy (5 min) | 🟡 Medium (10-15 min) | 🔴 Hard (20+ min)</li>
      <li><strong>Approach:</strong> Try each problem for 10 minutes before looking at the solution</li>
      <li><strong>Focus:</strong> Understand the pattern, not just the answer</li>
      <li><strong>All solutions use Postgres syntax</strong></li>
    </ul>
  </div>

  <div class="card">
    <h3>Pattern Cheat Sheet</h3>
    <table>
      <tr>
        <th>Pattern</th>
        <th>When to Use</th>
        <th>Key Technique</th>
      </tr>
      <tr>
        <td>Ranking</td>
        <td>"Top N per group"</td>
        <td><code>ROW_NUMBER() OVER (PARTITION BY ...)</code></td>
      </tr>
      <tr>
        <td>Running Totals</td>
        <td>"Cumulative sum", "running balance"</td>
        <td><code>SUM() OVER (ORDER BY ...)</code></td>
      </tr>
      <tr>
        <td>Gaps & Islands</td>
        <td>"Consecutive days", "streaks"</td>
        <td><code>date - ROW_NUMBER()</code></td>
      </tr>
      <tr>
        <td>Cohort Analysis</td>
        <td>"Retention by signup month"</td>
        <td><code>date_trunc</code> + self-join</td>
      </tr>
      <tr>
        <td>Funnel Analysis</td>
        <td>"Conversion rates between steps"</td>
        <td>Conditional aggregation or self-join</td>
      </tr>
      <tr>
        <td>Year-over-Year</td>
        <td>"Compare to same period last year"</td>
        <td><code>LAG() OVER (ORDER BY year)</code></td>
      </tr>
    </table>
  </div>

</div>

<div class="section">
  <h2>🟢 Easy Problems</h2>

  <div class="card">
    <h3>Problem 1: Second Highest Salary</h3>
    <p><strong>Difficulty:</strong> 🟢 Easy | <strong>Pattern:</strong> Ranking</p>
    
    <p><strong>Table:</strong> <code>employees</code></p>
    <pre><code>| id | name    | salary |
|----|---------|--------|
| 1  | Alice   | 100000 |
| 2  | Bob     | 80000  |
| 3  | Charlie | 80000  |
| 4  | Diana   | 120000 |</code></pre>
    
    <p><strong>Question:</strong> Find the second highest salary. If there's a tie for first, return the next distinct salary. Return NULL if no second highest exists.</p>
    
    <details>
    <summary>💡 Hint</summary>
    <p>Use <code>DENSE_RANK()</code> to handle ties, or use <code>DISTINCT</code> with <code>OFFSET</code>.</p>
    </details>
    
    <details>
    <summary>✅ Solution</summary>
    
    <h4>Approach 1: DENSE_RANK</h4>
    <pre><code>WITH ranked AS (
  SELECT 
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM employees
)
SELECT salary AS second_highest_salary
FROM ranked
WHERE rnk = 2
LIMIT 1;</code></pre>
    
    <h4>Approach 2: OFFSET (cleaner)</h4>
    <pre><code>SELECT DISTINCT salary AS second_highest_salary
FROM employees
ORDER BY salary DESC
OFFSET 1
LIMIT 1;</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| second_highest_salary |
|-----------------------|
| 100000                |</code></pre>
    <p>(Diana has 120000, Alice has 100000 = second highest)</p>
    
    <h4>Edge Case:</h4>
    <p>If all employees have the same salary, this returns empty. Wrap in a subquery with <code>COALESCE</code> if you need to return NULL explicitly.</p>
    </details>
  </div>

  <div class="card">
    <h3>Problem 2: Duplicate Emails</h3>
    <p><strong>Difficulty:</strong> 🟢 Easy | <strong>Pattern:</strong> Aggregation</p>
    
    <p><strong>Table:</strong> <code>users</code></p>
    <pre><code>| id | email           |
|----|-----------------|
| 1  | a@example.com   |
| 2  | b@example.com   |
| 3  | a@example.com   |</code></pre>
    
    <p><strong>Question:</strong> Find all duplicate emails.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>SELECT email
FROM users
GROUP BY email
HAVING COUNT(*) > 1;</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| email         |
|---------------|
| a@example.com |</code></pre>
    </details>
  </div>

  <div class="card">
    <h3>Problem 3: Customers Who Never Ordered</h3>
    <p><strong>Difficulty:</strong> 🟢 Easy | <strong>Pattern:</strong> LEFT JOIN + NULL check</p>
    
    <p><strong>Tables:</strong></p>
    <pre><code>customers            orders
| id | name  |       | id | customer_id |
|----|-------|       |----|-------------|
| 1  | Alice |       | 1  | 2           |
| 2  | Bob   |       | 2  | 2           |
| 3  | Carol |</code></pre>
    
    <p><strong>Question:</strong> Find customers who have never placed an order.</p>
    
    <details>
    <summary>✅ Solution</summary>
    
    <h4>Approach 1: LEFT JOIN</h4>
    <pre><code>SELECT c.name
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.id IS NULL;</code></pre>
    
    <h4>Approach 2: NOT EXISTS (often faster)</h4>
    <pre><code>SELECT name
FROM customers c
WHERE NOT EXISTS (
  SELECT 1 FROM orders o WHERE o.customer_id = c.id
);</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| name  |
|-------|
| Alice |
| Carol |</code></pre>
    </details>
  </div>

</div>

<div class="section">
  <h2>🟡 Medium Problems</h2>

  <div class="card">
    <h3>Problem 4: Department Top 3 Salaries</h3>
    <p><strong>Difficulty:</strong> 🟡 Medium | <strong>Pattern:</strong> Ranking + Top N per Group</p>
    
    <p><strong>Tables:</strong></p>
    <pre><code>employees                       departments
| id | name    | salary | dept_id |   | id | name    |
|----|---------|--------|---------|   |----|---------|
| 1  | Alice   | 100000 | 1       |   | 1  | Sales   |
| 2  | Bob     | 80000  | 1       |   | 2  | Eng     |
| 3  | Charlie | 90000  | 1       |
| 4  | Diana   | 120000 | 1       |
| 5  | Eve     | 95000  | 2       |
| 6  | Frank   | 85000  | 2       |</code></pre>
    
    <p><strong>Question:</strong> Find the top 3 earners in each department. Include ties.</p>
    
    <details>
    <summary>💡 Hint</summary>
    <p>Use <code>DENSE_RANK()</code> to handle ties (vs <code>ROW_NUMBER()</code> which breaks ties arbitrarily).</p>
    </details>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>WITH ranked AS (
  SELECT 
    d.name AS department,
    e.name AS employee,
    e.salary,
    DENSE_RANK() OVER (
      PARTITION BY e.dept_id 
      ORDER BY e.salary DESC
    ) AS rnk
  FROM employees e
  JOIN departments d ON e.dept_id = d.id
)
SELECT department, employee, salary
FROM ranked
WHERE rnk <= 3
ORDER BY department, salary DESC;</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| department | employee | salary |
|------------|----------|--------|
| Sales      | Diana    | 120000 |
| Sales      | Alice    | 100000 |
| Sales      | Charlie  | 90000  |
| Eng        | Eve      | 95000  |
| Eng        | Frank    | 85000  |</code></pre>
    
    <h4>Why DENSE_RANK?</h4>
    <ul>
      <li><code>ROW_NUMBER</code>: 1, 2, 3, 4... (arbitrary tie-breaker)</li>
      <li><code>RANK</code>: 1, 1, 3, 4... (skips after ties)</li>
      <li><code>DENSE_RANK</code>: 1, 1, 2, 3... (no skips) ← Use for "top N"</li>
    </ul>
    </details>
  </div>

  <div class="card">
    <h3>Problem 5: Running Total</h3>
    <p><strong>Difficulty:</strong> 🟡 Medium | <strong>Pattern:</strong> Window Functions</p>
    
    <p><strong>Table:</strong> <code>transactions</code></p>
    <pre><code>| id | user_id | amount | txn_date   |
|----|---------|--------|------------|
| 1  | 1       | 100    | 2025-01-01 |
| 2  | 1       | 200    | 2025-01-02 |
| 3  | 1       | -50    | 2025-01-03 |
| 4  | 2       | 300    | 2025-01-01 |</code></pre>
    
    <p><strong>Question:</strong> Calculate the running balance for each user, ordered by date.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>SELECT 
  user_id,
  txn_date,
  amount,
  SUM(amount) OVER (
    PARTITION BY user_id 
    ORDER BY txn_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_balance
FROM transactions
ORDER BY user_id, txn_date;</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| user_id | txn_date   | amount | running_balance |
|---------|------------|--------|-----------------|
| 1       | 2025-01-01 | 100    | 100             |
| 1       | 2025-01-02 | 200    | 300             |
| 1       | 2025-01-03 | -50    | 250             |
| 2       | 2025-01-01 | 300    | 300             |</code></pre>
    
    <h4>Note:</h4>
    <p><code>ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW</code> is the default for <code>SUM() OVER (ORDER BY ...)</code>, but being explicit is clearer.</p>
    </details>
  </div>

  <div class="card">
    <h3>Problem 6: Consecutive Login Days</h3>
    <p><strong>Difficulty:</strong> 🟡 Medium | <strong>Pattern:</strong> Gaps and Islands</p>
    
    <p><strong>Table:</strong> <code>logins</code></p>
    <pre><code>| user_id | login_date |
|---------|------------|
| 1       | 2025-01-01 |
| 1       | 2025-01-02 |
| 1       | 2025-01-03 |
| 1       | 2025-01-05 |
| 1       | 2025-01-06 |
| 2       | 2025-01-01 |</code></pre>
    
    <p><strong>Question:</strong> Find users who logged in for 3+ consecutive days.</p>
    
    <details>
    <summary>💡 Hint</summary>
    <p>The "gaps and islands" trick: <code>login_date - ROW_NUMBER()</code> produces the same value for consecutive dates.</p>
    </details>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>WITH login_groups AS (
  SELECT 
    user_id,
    login_date,
    login_date - (ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date))::int AS grp
  FROM logins
),
streaks AS (
  SELECT 
    user_id,
    grp,
    COUNT(*) AS streak_length,
    MIN(login_date) AS streak_start,
    MAX(login_date) AS streak_end
  FROM login_groups
  GROUP BY user_id, grp
)
SELECT DISTINCT user_id
FROM streaks
WHERE streak_length >= 3;</code></pre>
    
    <h4>How it works:</h4>
    <pre><code>| user_id | login_date | row_num | date - row_num (grp) |
|---------|------------|---------|----------------------|
| 1       | 2025-01-01 | 1       | 2024-12-31           |
| 1       | 2025-01-02 | 2       | 2024-12-31           | ← Same group!
| 1       | 2025-01-03 | 3       | 2024-12-31           | ← Same group!
| 1       | 2025-01-05 | 4       | 2025-01-01           | ← New group
| 1       | 2025-01-06 | 5       | 2025-01-01           |</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| user_id |
|---------|
| 1       |</code></pre>
    </details>
  </div>

  <div class="card">
    <h3>Problem 7: Month-over-Month Growth</h3>
    <p><strong>Difficulty:</strong> 🟡 Medium | <strong>Pattern:</strong> LAG</p>
    
    <p><strong>Table:</strong> <code>monthly_revenue</code></p>
    <pre><code>| month      | revenue |
|------------|---------|
| 2025-01-01 | 10000   |
| 2025-02-01 | 12000   |
| 2025-03-01 | 11000   |</code></pre>
    
    <p><strong>Question:</strong> Calculate the month-over-month growth rate as a percentage.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>SELECT 
  month,
  revenue,
  LAG(revenue) OVER (ORDER BY month) AS prev_revenue,
  ROUND(
    (revenue - LAG(revenue) OVER (ORDER BY month)) * 100.0 
    / NULLIF(LAG(revenue) OVER (ORDER BY month), 0),
    2
  ) AS growth_pct
FROM monthly_revenue;</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| month      | revenue | prev_revenue | growth_pct |
|------------|---------|--------------|------------|
| 2025-01-01 | 10000   | NULL         | NULL       |
| 2025-02-01 | 12000   | 10000        | 20.00      |
| 2025-03-01 | 11000   | 12000        | -8.33      |</code></pre>
    
    <h4>Note:</h4>
    <p><code>NULLIF(..., 0)</code> prevents division by zero if previous revenue was 0.</p>
    </details>
  </div>

  <div class="card">
    <h3>Problem 8: Cohort Retention</h3>
    <p><strong>Difficulty:</strong> 🟡 Medium | <strong>Pattern:</strong> Cohort Analysis</p>
    
    <p><strong>Tables:</strong></p>
    <pre><code>users                    activity
| user_id | signup_date |   | user_id | activity_date |
|---------|-------------|   |---------|---------------|
| 1       | 2025-01-15  |   | 1       | 2025-01-16    |
| 2       | 2025-01-20  |   | 1       | 2025-02-10    |
| 3       | 2025-02-05  |   | 2       | 2025-01-25    |
                            | 3       | 2025-02-06    |
                            | 3       | 2025-03-10    |</code></pre>
    
    <p><strong>Question:</strong> Calculate Day-30 retention rate by signup month cohort.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>WITH cohorts AS (
  SELECT 
    user_id,
    date_trunc('month', signup_date) AS cohort_month
  FROM users
),
retained AS (
  SELECT DISTINCT 
    c.user_id,
    c.cohort_month
  FROM cohorts c
  JOIN activity a ON c.user_id = a.user_id
  WHERE a.activity_date >= (
    SELECT signup_date FROM users WHERE user_id = c.user_id
  ) + INTERVAL '30 days'
)
SELECT 
  c.cohort_month,
  COUNT(DISTINCT c.user_id) AS total_users,
  COUNT(DISTINCT r.user_id) AS retained_users,
  ROUND(
    COUNT(DISTINCT r.user_id) * 100.0 / COUNT(DISTINCT c.user_id),
    2
  ) AS retention_rate
FROM cohorts c
LEFT JOIN retained r USING (user_id, cohort_month)
GROUP BY c.cohort_month
ORDER BY c.cohort_month;</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| cohort_month | total_users | retained_users | retention_rate |
|--------------|-------------|----------------|----------------|
| 2025-01-01   | 2           | 1              | 50.00          |
| 2025-02-01   | 1           | 1              | 100.00         |</code></pre>
    </details>
  </div>

</div>

<div class="section">
  <h2>🔴 Hard Problems</h2>

  <div class="card">
    <h3>Problem 9: Median Salary by Department</h3>
    <p><strong>Difficulty:</strong> 🔴 Hard | <strong>Pattern:</strong> Percentile</p>
    
    <p><strong>Table:</strong> <code>employees</code></p>
    <pre><code>| id | dept | salary |
|----|------|--------|
| 1  | A    | 100    |
| 2  | A    | 200    |
| 3  | A    | 300    |
| 4  | B    | 150    |
| 5  | B    | 250    |</code></pre>
    
    <p><strong>Question:</strong> Find the median salary for each department.</p>
    
    <details>
    <summary>💡 Hint</summary>
    <p>Postgres has <code>PERCENTILE_CONT(0.5)</code> for median.</p>
    </details>
    
    <details>
    <summary>✅ Solution</summary>
    
    <h4>Approach 1: PERCENTILE_CONT (Postgres)</h4>
    <pre><code>SELECT 
  dept,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary
FROM employees
GROUP BY dept;</code></pre>
    
    <h4>Approach 2: ROW_NUMBER (universal)</h4>
    <pre><code>WITH ranked AS (
  SELECT 
    dept,
    salary,
    ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary) AS rn,
    COUNT(*) OVER (PARTITION BY dept) AS cnt
  FROM employees
)
SELECT 
  dept,
  AVG(salary) AS median_salary
FROM ranked
WHERE rn IN (FLOOR((cnt + 1) / 2.0), CEIL((cnt + 1) / 2.0))
GROUP BY dept;</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| dept | median_salary |
|------|---------------|
| A    | 200           |
| B    | 200           |</code></pre>
    </details>
  </div>

  <div class="card">
    <h3>Problem 10: Find the Quiet Students</h3>
    <p><strong>Difficulty:</strong> 🔴 Hard | <strong>Pattern:</strong> Window Functions + Complex Logic</p>
    
    <p><strong>Tables:</strong></p>
    <pre><code>students              exams
| id | name  |        | exam_id | student_id | score |
|----|-------|        |---------|------------|-------|
| 1  | Alice |        | 1       | 1          | 90    |
| 2  | Bob   |        | 1       | 2          | 85    |
| 3  | Carol |        | 1       | 3          | 80    |
                       | 2       | 1          | 70    |
                       | 2       | 2          | 75    |
                       | 2       | 3          | 80    |</code></pre>
    
    <p><strong>Question:</strong> Find students who never scored the highest OR lowest in any exam.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>WITH exam_ranks AS (
  SELECT 
    student_id,
    exam_id,
    score,
    RANK() OVER (PARTITION BY exam_id ORDER BY score DESC) AS high_rank,
    RANK() OVER (PARTITION BY exam_id ORDER BY score ASC) AS low_rank
  FROM exams
),
extremes AS (
  SELECT DISTINCT student_id
  FROM exam_ranks
  WHERE high_rank = 1 OR low_rank = 1
)
SELECT s.id, s.name
FROM students s
WHERE s.id NOT IN (SELECT student_id FROM extremes)
  AND EXISTS (SELECT 1 FROM exams e WHERE e.student_id = s.id);  -- Must have taken exams</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| id | name |
|----|------|
| 2  | Bob  |</code></pre>
    <p>Bob never scored highest (90) or lowest (70/80) in any exam.</p>
    </details>
  </div>

  <div class="card">
    <h3>Problem 11: Product Price at a Given Date</h3>
    <p><strong>Difficulty:</strong> 🔴 Hard | <strong>Pattern:</strong> Point-in-Time Lookup</p>
    
    <p><strong>Table:</strong> <code>price_changes</code> (SCD Type 2)</p>
    <pre><code>| product_id | new_price | change_date |
|------------|-----------|-------------|
| 1          | 10        | 2025-01-01  |
| 1          | 15        | 2025-01-15  |
| 1          | 12        | 2025-02-01  |
| 2          | 20        | 2025-01-10  |</code></pre>
    
    <p><strong>Question:</strong> Find the price of each product on 2025-01-20. If no price change before that date, return 0.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>WITH latest_price AS (
  SELECT 
    product_id,
    new_price,
    ROW_NUMBER() OVER (
      PARTITION BY product_id 
      ORDER BY change_date DESC
    ) AS rn
  FROM price_changes
  WHERE change_date <= '2025-01-20'
)
SELECT 
  p.product_id,
  COALESCE(l.new_price, 0) AS price
FROM (SELECT DISTINCT product_id FROM price_changes) p
LEFT JOIN latest_price l 
  ON p.product_id = l.product_id AND l.rn = 1;</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| product_id | price |
|------------|-------|
| 1          | 15    |  -- Changed to 15 on Jan 15
| 2          | 20    |  -- Changed to 20 on Jan 10</code></pre>
    </details>
  </div>

  <div class="card">
    <h3>Problem 12: Friends Who Watched Same Movie</h3>
    <p><strong>Difficulty:</strong> 🔴 Hard | <strong>Pattern:</strong> Self-Join + Graph</p>
    
    <p><strong>Tables:</strong></p>
    <pre><code>friendships              watches
| user_id | friend_id |   | user_id | movie_id |
|---------|-----------|   |---------|----------|
| 1       | 2         |   | 1       | 100      |
| 1       | 3         |   | 2       | 100      |
| 2       | 3         |   | 3       | 100      |
                          | 1       | 200      |
                          | 3       | 200      |</code></pre>
    
    <p><strong>Question:</strong> For each movie, count how many pairs of friends both watched it.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>WITH friend_pairs AS (
  -- Normalize friendships (both directions)
  SELECT user_id, friend_id FROM friendships
  UNION
  SELECT friend_id, user_id FROM friendships
)
SELECT 
  w1.movie_id,
  COUNT(*) / 2 AS friend_pairs  -- Divide by 2 since we count both directions
FROM watches w1
JOIN watches w2 
  ON w1.movie_id = w2.movie_id 
  AND w1.user_id < w2.user_id  -- Avoid counting (A,B) and (B,A)
JOIN friend_pairs f 
  ON (w1.user_id = f.user_id AND w2.user_id = f.friend_id)
GROUP BY w1.movie_id;</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| movie_id | friend_pairs |
|----------|--------------|
| 100      | 3            |  -- (1,2), (1,3), (2,3)
| 200      | 1            |  -- (1,3)</code></pre>
    </details>
  </div>

  <div class="card">
    <h3>Problem 13: Funnel Conversion Rates</h3>
    <p><strong>Difficulty:</strong> 🔴 Hard | <strong>Pattern:</strong> Funnel Analysis</p>
    
    <p><strong>Table:</strong> <code>events</code></p>
    <pre><code>| user_id | event_type | event_time          |
|---------|------------|---------------------|
| 1       | view       | 2025-01-01 10:00:00 |
| 1       | add_cart   | 2025-01-01 10:05:00 |
| 1       | purchase   | 2025-01-01 10:10:00 |
| 2       | view       | 2025-01-01 11:00:00 |
| 2       | add_cart   | 2025-01-01 11:05:00 |
| 3       | view       | 2025-01-01 12:00:00 |</code></pre>
    
    <p><strong>Question:</strong> Calculate the conversion rate at each step of the funnel: view → add_cart → purchase.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>WITH funnel AS (
  SELECT 
    user_id,
    MAX(CASE WHEN event_type = 'view' THEN 1 ELSE 0 END) AS viewed,
    MAX(CASE WHEN event_type = 'add_cart' THEN 1 ELSE 0 END) AS added_cart,
    MAX(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchased
  FROM events
  GROUP BY user_id
)
SELECT 
  SUM(viewed) AS views,
  SUM(added_cart) AS add_carts,
  SUM(purchased) AS purchases,
  ROUND(SUM(added_cart) * 100.0 / NULLIF(SUM(viewed), 0), 2) AS view_to_cart_pct,
  ROUND(SUM(purchased) * 100.0 / NULLIF(SUM(added_cart), 0), 2) AS cart_to_purchase_pct,
  ROUND(SUM(purchased) * 100.0 / NULLIF(SUM(viewed), 0), 2) AS overall_conversion_pct
FROM funnel;</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| views | add_carts | purchases | view_to_cart_pct | cart_to_purchase_pct | overall_conversion_pct |
|-------|-----------|-----------|------------------|----------------------|------------------------|
| 3     | 2         | 1         | 66.67            | 50.00                | 33.33                  |</code></pre>
    </details>
  </div>

  <div class="card">
    <h3>Problem 14: Active User Retention (DAU/MAU Ratio)</h3>
    <p><strong>Difficulty:</strong> 🔴 Hard | <strong>Pattern:</strong> Rolling Window</p>
    
    <p><strong>Table:</strong> <code>daily_active</code></p>
    <pre><code>| user_id | active_date |
|---------|-------------|
| 1       | 2025-01-01  |
| 1       | 2025-01-02  |
| ...     | ...         |</code></pre>
    
    <p><strong>Question:</strong> Calculate the DAU/MAU ratio for each day. MAU = unique users active in the past 30 days.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>WITH daily_stats AS (
  SELECT 
    active_date,
    COUNT(DISTINCT user_id) AS dau
  FROM daily_active
  GROUP BY active_date
),
mau_calc AS (
  SELECT 
    d1.active_date,
    COUNT(DISTINCT d2.user_id) AS mau
  FROM daily_active d1
  JOIN daily_active d2 
    ON d2.active_date BETWEEN d1.active_date - INTERVAL '29 days' AND d1.active_date
  GROUP BY d1.active_date
)
SELECT 
  ds.active_date,
  ds.dau,
  mc.mau,
  ROUND(ds.dau * 100.0 / NULLIF(mc.mau, 0), 2) AS stickiness_pct
FROM daily_stats ds
JOIN mau_calc mc ON ds.active_date = mc.active_date
ORDER BY ds.active_date;</code></pre>
    
    <h4>Interpretation:</h4>
    <ul>
      <li><strong>Stickiness</strong> (DAU/MAU) shows how often monthly users engage daily</li>
      <li>20-25% = healthy consumer app</li>
      <li>50%+ = power user product (enterprise SaaS)</li>
    </ul>
    </details>
  </div>

  <div class="card">
    <h3>Problem 15: Recommend Friends of Friends</h3>
    <p><strong>Difficulty:</strong> 🔴 Hard | <strong>Pattern:</strong> Graph Traversal</p>
    
    <p><strong>Table:</strong> <code>friendships</code></p>
    <pre><code>| user_id | friend_id |
|---------|-----------|
| 1       | 2         |
| 1       | 3         |
| 2       | 4         |
| 3       | 4         |
| 3       | 5         |</code></pre>
    
    <p><strong>Question:</strong> For user 1, recommend users who are friends of friends but not already friends. Rank by number of mutual friends.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>WITH all_friends AS (
  -- Normalize friendships (bidirectional)
  SELECT user_id, friend_id FROM friendships
  UNION
  SELECT friend_id, user_id FROM friendships
),
user_friends AS (
  -- User 1's direct friends
  SELECT friend_id FROM all_friends WHERE user_id = 1
),
friends_of_friends AS (
  -- Friends of user 1's friends
  SELECT 
    af.friend_id AS recommended_user,
    af.user_id AS mutual_friend
  FROM all_friends af
  WHERE af.user_id IN (SELECT friend_id FROM user_friends)  -- Start from user 1's friends
    AND af.friend_id != 1  -- Not user 1
    AND af.friend_id NOT IN (SELECT friend_id FROM user_friends)  -- Not already friends
)
SELECT 
  recommended_user,
  COUNT(DISTINCT mutual_friend) AS mutual_friends
FROM friends_of_friends
GROUP BY recommended_user
ORDER BY mutual_friends DESC;</code></pre>
    
    <h4>Answer:</h4>
    <pre><code>| recommended_user | mutual_friends |
|------------------|----------------|
| 4                | 2              |  -- Friends with both 2 and 3
| 5                | 1              |  -- Friends with just 3</code></pre>
    </details>
  </div>

</div>

<div class="section">
  <div class="card">
    <h3>✅ SQL Interview Checklist</h3>
    <p>Before your interview, confirm you can:</p>
    <ul>
      <li>☐ Solve "Top N per group" with <code>ROW_NUMBER</code> / <code>DENSE_RANK</code></li>
      <li>☐ Calculate running totals with <code>SUM() OVER</code></li>
      <li>☐ Identify consecutive sequences (gaps and islands)</li>
      <li>☐ Build a cohort retention analysis</li>
      <li>☐ Calculate MoM / YoY growth with <code>LAG</code></li>
      <li>☐ Handle point-in-time lookups (SCD2)</li>
      <li>☐ Explain the difference between <code>WHERE</code> and <code>HAVING</code></li>
      <li>☐ Know when to use <code>LEFT JOIN</code> vs <code>NOT EXISTS</code></li>
    </ul>
  </div>
</div>

<div class="navigation-buttons">
  <a href="{{ '/interview-preparation/technical-skills/' | relative_url }}">Previous: Technical Skills</a>
  <a href="{{ '/interview-preparation/analytical-execution/' | relative_url }}">Next: Analytical Execution</a>
</div>

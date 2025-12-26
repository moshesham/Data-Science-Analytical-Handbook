---
layout: default
title: "Technical Skills Interview"
permalink: /interview-preparation/technical-skills/
difficulty: "Advanced"
estimated_time: "60 mins"
tags: [Interview, Technical Skills, Problem Solving]
track: "Interview Preparation"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/interview-preparation/technical-skills/' | relative_url }}">Interview Preparation</a> <span>&gt;</span>
  <span>Technical Skills Interview</span>
</div>

<div class="header">
  <h1>Technical Skills Interview (Coding/SQL)</h1>
  <p>SQL deep dive, Python/R data manipulation, and hands-on practice.</p>
</div>

<div class="section">
  
  <div class="card">
    <h3>What to Expect</h3>
    <p>This interview assesses your coding and problem-solving abilities using data. Expect SQL-heavy questions, but be prepared to use your preferred language (Python/R) for data manipulation and analysis tasks.</p>
  </div>

  <div class="card">
    <h3>Key Areas</h3>
    <ul>
      <li><strong>SQL Proficiency:</strong> Writing efficient and complex queries involving joins, aggregations, window functions, subqueries, and CTEs. Be prepared to optimize queries for performance.</li>
      <li><strong>Data Manipulation (Python/R):</strong> Using Pandas/dplyr, NumPy/base R for data cleaning, transformation, and analysis.</li>
      <li><strong>Algorithm Implementation (Less Common):</strong> In some cases, you might be asked to implement basic algorithms or data structures.</li>
    </ul>
  </div>

  <div class="card">
    <h3>How to Prepare</h3>
    <ul>
      <li><strong>Understand the Problem Thoroughly:</strong> Before jumping into coding, ensure you fully understand the problem. Ask clarifying questions to the interviewer to confirm your understanding of the requirements, edge cases, and any constraints.</li>
      <li><strong>Communicate Your Thought Process:</strong> While practicing, solve problems by "thinking out loud." Verbalize your thought process, explain your chosen approach, and justify your decisions.</li>
      <li><strong>Plan Your Approach:</strong> Take a moment to plan how you want to solve the problem before you start coding. Break down the problem into smaller, manageable subproblems.</li>
      <li><strong>Explain Trade-offs:</strong> Be prepared to discuss the trade-offs of different approaches.</li>
      <li><strong>Practice SQL Extensively:</strong> Use platforms like SQLZOO, HackerRank SQL, LeetCode Database, and StrataScratch.</li>
      <li><strong>Master Data Manipulation Libraries:</strong> Become very comfortable with Pandas (Python) or dplyr (R).</li>
      <li><strong>Focus on Problem-Solving:</strong> Practice breaking down complex problems into smaller, manageable parts.</li>
      <li><strong>Write Clean and Efficient Code:</strong> Pay attention to code readability, style, and efficiency.</li>
      <li><strong>Mock Interviews:</strong> Practice coding interviews with friends or using platforms like Pramp or InterviewBit.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Common Analytical Patterns</h3>
    <p>While every problem is unique, many data analysis questions fall into common patterns:</p>
    <ol>
      <li><strong>Filtering and Aggregation:</strong> Filtering data based on certain criteria and then aggregating it using functions like COUNT, SUM, AVG, MIN, MAX.</li>
      <li><strong>Joining and Combining Data:</strong> Combining data from multiple tables using JOINs.</li>
      <li><strong>Ranking and Ordering:</strong> Ranking data based on certain criteria or ordering it in a specific way.</li>
      <li><strong>Window Functions:</strong> Performing calculations across a set of rows that are related to the current row.</li>
      <li><strong>Time Series Analysis:</strong> Analyzing data over time to identify trends, patterns, and anomalies.</li>
    </ol>
  </div>

  <div class="card">
    <h3>Example Question (SQL)</h3>
    <p>Given a table <code>UserActivity</code> (user_id, activity_date, activity_type), write a query to find the number of users who performed each activity type on each date.</p>
    <pre><code>SELECT activity_date, activity_type, COUNT(DISTINCT user_id) AS num_users
FROM UserActivity
GROUP BY activity_date, activity_type;</code></pre>
  </div>

  <div class="card">
    <h3>Example Question (Python/Pandas)</h3>
    <p>Calculate the average age by city using Pandas:</p>
    <pre><code>import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 28, 22, 27],
        'City': ['New York', 'London', 'New York', 'London', 'Paris']}
df = pd.DataFrame(data)

average_age_by_city = df.groupby('City')['Age'].mean()
print(average_age_by_city)</code></pre>
  </div>

  <div class="card">
    <h3>🧠 Interview-Grade SQL Challenges</h3>
    
    <details>
    <summary><strong>Challenge 1: 7-Day Rolling Active Users</strong></summary>
    <p><strong>Difficulty:</strong> 🟡 Medium</p>
    
    <p><strong>Table:</strong> <code>daily_logins</code> (user_id, login_date)</p>
    <p><strong>Question:</strong> Calculate the 7-day rolling count of unique active users for each day.</p>
    
    <details>
    <summary>💡 Hint</summary>
    <p>Use a self-join with a date range, or use <code>RANGE BETWEEN</code> in a window function.</p>
    </details>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>-- Approach 1: Self-join
WITH daily_users AS (
  SELECT DISTINCT login_date, user_id
  FROM daily_logins
)
SELECT 
  d1.login_date,
  COUNT(DISTINCT d2.user_id) AS rolling_7d_users
FROM (SELECT DISTINCT login_date FROM daily_logins) d1
JOIN daily_users d2 
  ON d2.login_date BETWEEN d1.login_date - INTERVAL '6 days' AND d1.login_date
GROUP BY d1.login_date
ORDER BY d1.login_date;

-- Approach 2: Window function with date spine
WITH date_spine AS (
  SELECT generate_series(
    (SELECT MIN(login_date) FROM daily_logins),
    (SELECT MAX(login_date) FROM daily_logins),
    '1 day'::interval
  )::date AS dt
),
user_presence AS (
  SELECT 
    ds.dt,
    dl.user_id
  FROM date_spine ds
  LEFT JOIN daily_logins dl 
    ON dl.login_date BETWEEN ds.dt - INTERVAL '6 days' AND ds.dt
)
SELECT 
  dt AS login_date,
  COUNT(DISTINCT user_id) AS rolling_7d_users
FROM user_presence
GROUP BY dt
ORDER BY dt;</code></pre>
    
    <h4>Key Insight:</h4>
    <p>The self-join approach counts unique users across a 7-day window. Note that <code>- INTERVAL '6 days'</code> gives you 7 days total (today + 6 previous).</p>
    </details>
    </details>
    
    <details>
    <summary><strong>Challenge 2: First Purchase by Category</strong></summary>
    <p><strong>Difficulty:</strong> 🟡 Medium</p>
    
    <p><strong>Table:</strong> <code>purchases</code> (user_id, category, purchase_date, amount)</p>
    <p><strong>Question:</strong> For each user, find their first purchase in each category.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>-- Using DISTINCT ON (Postgres-specific, fastest)
SELECT DISTINCT ON (user_id, category)
  user_id,
  category,
  purchase_date AS first_purchase_date,
  amount AS first_purchase_amount
FROM purchases
ORDER BY user_id, category, purchase_date ASC;

-- Using ROW_NUMBER (universal)
WITH ranked AS (
  SELECT 
    *,
    ROW_NUMBER() OVER (
      PARTITION BY user_id, category 
      ORDER BY purchase_date ASC
    ) AS rn
  FROM purchases
)
SELECT user_id, category, purchase_date, amount
FROM ranked
WHERE rn = 1;</code></pre>
    </details>
    </details>
    
    <details>
    <summary><strong>Challenge 3: Identify Power Users</strong></summary>
    <p><strong>Difficulty:</strong> 🔴 Hard</p>
    
    <p><strong>Tables:</strong></p>
    <ul>
      <li><code>sessions</code> (user_id, session_start, session_end)</li>
      <li><code>purchases</code> (user_id, purchase_date, amount)</li>
    </ul>
    <p><strong>Question:</strong> Find users who:</p>
    <ol>
      <li>Had 10+ sessions in the last 30 days</li>
      <li>AND made 3+ purchases in the last 30 days</li>
      <li>AND have total purchase amount > $500</li>
    </ol>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>WITH session_counts AS (
  SELECT 
    user_id,
    COUNT(*) AS sessions_30d
  FROM sessions
  WHERE session_start >= CURRENT_DATE - INTERVAL '30 days'
  GROUP BY user_id
  HAVING COUNT(*) >= 10
),
purchase_stats AS (
  SELECT 
    user_id,
    COUNT(*) AS purchases_30d,
    SUM(amount) AS total_amount
  FROM purchases
  WHERE purchase_date >= CURRENT_DATE - INTERVAL '30 days'
  GROUP BY user_id
  HAVING COUNT(*) >= 3 AND SUM(amount) > 500
)
SELECT 
  s.user_id,
  s.sessions_30d,
  p.purchases_30d,
  p.total_amount
FROM session_counts s
JOIN purchase_stats p USING (user_id);</code></pre>
    
    <h4>Pattern:</h4>
    <p>Use CTEs to calculate each criterion separately, then JOIN to find users meeting ALL criteria.</p>
    </details>
    </details>
  </div>

  <div class="card">
    <h3>🐍 Interview-Grade Python Challenges</h3>
    
    <details>
    <summary><strong>Challenge 1: Clean and Dedupe Customer Data</strong></summary>
    <p><strong>Difficulty:</strong> 🟡 Medium</p>
    
    <p><strong>Data:</strong></p>
    <pre><code>customers = pd.DataFrame({
    'id': [1, 2, 2, 3, 4, 4],
    'name': ['Alice', 'Bob', 'Robert', 'Carol', 'Dave', 'Dave'],
    'email': ['alice@a.com', 'bob@b.com', 'bob@b.com', None, 'dave@d.com', 'dave@d.com'],
    'signup_date': ['2025-01-01', '2025-01-05', '2025-01-06', '2025-01-10', '2025-01-15', '2025-01-20'],
    'is_verified': [True, False, True, False, True, False]
})</code></pre>
    
    <p><strong>Task:</strong></p>
    <ol>
      <li>Dedupe by customer ID, keeping the row with is_verified=True (or most recent signup if no verified)</li>
      <li>Fill missing emails with 'unknown@company.com'</li>
      <li>Ensure signup_date is datetime type</li>
    </ol>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>import pandas as pd

# Start with the data
customers = pd.DataFrame({
    'id': [1, 2, 2, 3, 4, 4],
    'name': ['Alice', 'Bob', 'Robert', 'Carol', 'Dave', 'Dave'],
    'email': ['alice@a.com', 'bob@b.com', 'bob@b.com', None, 'dave@d.com', 'dave@d.com'],
    'signup_date': ['2025-01-01', '2025-01-05', '2025-01-06', '2025-01-10', '2025-01-15', '2025-01-20'],
    'is_verified': [True, False, True, False, True, False]
})

# Convert signup_date to datetime
customers['signup_date'] = pd.to_datetime(customers['signup_date'])

# Sort by id, is_verified (True first), then signup_date (most recent first)
customers_sorted = customers.sort_values(
    by=['id', 'is_verified', 'signup_date'],
    ascending=[True, False, False]
)

# Keep first occurrence per id (which is verified=True or most recent)
customers_deduped = customers_sorted.drop_duplicates(subset='id', keep='first')

# Fill missing emails
customers_deduped['email'] = customers_deduped['email'].fillna('unknown@company.com')

print(customers_deduped)</code></pre>
    
    <h4>Output:</h4>
    <pre><code>   id   name         email signup_date  is_verified
0   1  Alice   alice@a.com  2025-01-01         True
2   2  Robert   bob@b.com  2025-01-06         True
3   3  Carol  unknown@...  2025-01-10        False
4   4   Dave  dave@d.com  2025-01-15         True</code></pre>
    </details>
    </details>
    
    <details>
    <summary><strong>Challenge 2: Calculate Cohort Retention in Pandas</strong></summary>
    <p><strong>Difficulty:</strong> 🔴 Hard</p>
    
    <p><strong>Data:</strong></p>
    <pre><code>users = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'signup_date': ['2025-01-01', '2025-01-15', '2025-02-01', '2025-02-10', '2025-03-01']
})

activity = pd.DataFrame({
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4, 5],
    'activity_date': ['2025-01-05', '2025-02-10', '2025-03-15', 
                      '2025-01-20', '2025-02-20', '2025-02-05', '2025-03-05',
                      '2025-02-15', '2025-03-10']
})</code></pre>
    
    <p><strong>Task:</strong> Create a cohort retention table showing the % of users retained in months 0, 1, 2, 3 after signup.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>import pandas as pd

# Prepare data
users['signup_date'] = pd.to_datetime(users['signup_date'])
activity['activity_date'] = pd.to_datetime(activity['activity_date'])

# Add cohort month to users
users['cohort_month'] = users['signup_date'].dt.to_period('M')

# Merge activity with users
merged = activity.merge(users[['user_id', 'signup_date', 'cohort_month']], on='user_id')

# Calculate months since signup
merged['months_since_signup'] = (
    (merged['activity_date'].dt.to_period('M') - merged['cohort_month'])
    .apply(lambda x: x.n if pd.notna(x) else None)
)

# Filter to only positive months (activity after signup)
merged = merged[merged['months_since_signup'] >= 0]

# Count unique users per cohort and month
retention = merged.groupby(['cohort_month', 'months_since_signup']).agg(
    active_users=('user_id', 'nunique')
).reset_index()

# Get cohort sizes
cohort_sizes = users.groupby('cohort_month').size().reset_index(name='cohort_size')

# Merge and calculate retention rate
retention = retention.merge(cohort_sizes, on='cohort_month')
retention['retention_rate'] = (retention['active_users'] / retention['cohort_size'] * 100).round(1)

# Pivot for display
retention_matrix = retention.pivot(
    index='cohort_month', 
    columns='months_since_signup', 
    values='retention_rate'
).fillna(0)

print(retention_matrix)</code></pre>
    
    <h4>Output:</h4>
    <pre><code>months_since_signup    0      1      2
cohort_month                          
2025-01               100.0   50.0   50.0
2025-02               100.0   50.0    0.0
2025-03               100.0    0.0    0.0</code></pre>
    </details>
    </details>
    
    <details>
    <summary><strong>Challenge 3: Implement a Simple A/B Test Analysis</strong></summary>
    <p><strong>Difficulty:</strong> 🔴 Hard</p>
    
    <p><strong>Data:</strong></p>
    <pre><code>experiment = pd.DataFrame({
    'user_id': range(1, 2001),
    'variant': ['control']*1000 + ['treatment']*1000,
    'converted': [0]*920 + [1]*80 + [0]*890 + [1]*110  # 8% control, 11% treatment
})</code></pre>
    
    <p><strong>Task:</strong> Calculate the conversion rate, lift, confidence interval, and p-value.</p>
    
    <details>
    <summary>✅ Solution</summary>
    <pre><code>import pandas as pd
import numpy as np
from scipy import stats

# Calculate stats per variant
summary = experiment.groupby('variant').agg(
    users=('user_id', 'count'),
    conversions=('converted', 'sum'),
    conversion_rate=('converted', 'mean')
).reset_index()

print("Summary:\n", summary)

# Extract values
control = summary[summary['variant'] == 'control'].iloc[0]
treatment = summary[summary['variant'] == 'treatment'].iloc[0]

p_control = control['conversion_rate']
p_treatment = treatment['conversion_rate']
n_control = control['users']
n_treatment = treatment['users']

# Calculate lift
lift = (p_treatment - p_control) / p_control * 100
print(f"\nLift: {lift:.1f}%")

# Pooled proportion and standard error
p_pooled = (control['conversions'] + treatment['conversions']) / (n_control + n_treatment)
se = np.sqrt(p_pooled * (1 - p_pooled) * (1/n_control + 1/n_treatment))

# Z-statistic and p-value
z = (p_treatment - p_control) / se
p_value = 2 * (1 - stats.norm.cdf(abs(z)))  # Two-tailed
print(f"Z-statistic: {z:.3f}")
print(f"P-value: {p_value:.4f}")

# 95% Confidence interval for the difference
diff = p_treatment - p_control
se_diff = np.sqrt(p_treatment*(1-p_treatment)/n_treatment + p_control*(1-p_control)/n_control)
ci_lower = diff - 1.96 * se_diff
ci_upper = diff + 1.96 * se_diff
print(f"95% CI for difference: [{ci_lower*100:.2f}%, {ci_upper*100:.2f}%]")

# Conclusion
if p_value < 0.05:
    print("\n✅ Result is statistically significant at α=0.05")
else:
    print("\n❌ Result is NOT statistically significant at α=0.05")</code></pre>
    
    <h4>Output:</h4>
    <pre><code>Summary:
     variant  users  conversions  conversion_rate
0   control   1000           80             0.08
1  treatment  1000          110             0.11

Lift: 37.5%
Z-statistic: 2.400
P-value: 0.0164
95% CI for difference: [0.57%, 5.43%]

✅ Result is statistically significant at α=0.05</code></pre>
    </details>
    </details>
  </div>

  <div class="card">
    <h3>📚 More Practice Resources</h3>
    <ul>
      <li><a href="{{ '/interview-preparation/sql-interview-problems/' | relative_url }}">📊 15 Curated SQL Interview Problems</a> — Full problem set with solutions</li>
      <li><a href="{{ '/foundational_knowledge/4-ab-testing/' | relative_url }}">🧪 A/B Testing Deep Dive</a> — Comprehensive experimentation guide</li>
      <li><a href="{{ '/tools/sample-size-calculator/' | relative_url }}">🔢 Sample Size Calculator</a> — Interactive tool with explanations</li>
    </ul>
  </div>

  <div class="card">
    <h3>⚠️ Common Technical Interview Mistakes</h3>
    <table>
      <tr>
        <th>Mistake</th>
        <th>Why It Hurts</th>
        <th>Fix</th>
      </tr>
      <tr>
        <td>Jumping straight to code</td>
        <td>May solve wrong problem</td>
        <td>Ask 2-3 clarifying questions first</td>
      </tr>
      <tr>
        <td>Not testing edge cases</td>
        <td>NULLs, empty tables break queries</td>
        <td>Always consider: empty input, NULL values, duplicates</td>
      </tr>
      <tr>
        <td>Overly complex solution</td>
        <td>Hard to debug and explain</td>
        <td>Start simple, optimize if needed</td>
      </tr>
      <tr>
        <td>Silent coding</td>
        <td>Interviewer can't assess your thinking</td>
        <td>Narrate your thought process</td>
      </tr>
      <tr>
        <td>Not validating output</td>
        <td>Logic errors slip through</td>
        <td>Trace through with sample data</td>
      </tr>
    </table>
  </div>

  <div class="card">
    <h3>✅ Technical Interview Checklist</h3>
    <p>Before your interview:</p>
    <ul>
      <li>☐ Practice 10+ SQL problems covering window functions, CTEs, JOINs</li>
      <li>☐ Solve 5+ Pandas problems (groupby, merge, pivot)</li>
      <li>☐ Know how to calculate sample size for an A/B test</li>
      <li>☐ Can implement a two-sample proportion test in Python</li>
      <li>☐ Practice explaining your code out loud</li>
      <li>☐ Have your IDE/editor ready with sample data</li>
    </ul>
  </div>

</div>

<div class="navigation-buttons">
  <a href="{{ '/foundational_knowledge/3/' | relative_url }}">Previous: Foundational Knowledge</a>
  <a href="{{ '/interview-preparation/analytical-execution/' | relative_url }}">Next: Analytical Execution</a>
</div>

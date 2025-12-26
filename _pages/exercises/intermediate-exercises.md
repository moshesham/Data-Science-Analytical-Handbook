---
layout: page
title: "Intermediate Exercises"
permalink: /exercises/intermediate/
nav_order: 2
parent: "Exercises"
difficulty: "Intermediate"
estimated_time: "3-4 hours"
tags: [Exercises, Practice, Intermediate, Step-by-Step]
track: "Interview Success Blueprint"
---

# Intermediate Exercises: Step-by-Step Problem Solving

These exercises build on foundational knowledge with more complex scenarios. Each problem includes detailed explanations to help you understand not just *what* to do, but *why*.

---

## 📊 Statistics Exercises

### Exercise S4: Hypothesis Testing by Hand

**Problem:** A/B test for a checkout page redesign. You want to know if the new design increases conversion rate.

**Data:**
| Group | Visitors | Conversions | Conversion Rate |
|-------|----------|-------------|-----------------|
| Control (Old) | 5,000 | 150 | 3.0% |
| Treatment (New) | 5,000 | 185 | 3.7% |

**Question:** At α = 0.05, is the new design significantly better? Perform a two-proportion z-test step by step.

<details>
<summary>💡 Hint</summary>
Calculate pooled proportion, standard error, z-statistic, then compare to critical value.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: State the Hypotheses**
```
H₀: p_treatment = p_control (no difference)
H₁: p_treatment > p_control (treatment is better)

This is a one-tailed test since we're testing if new is BETTER.
```

**Step 2: Calculate Sample Proportions**
```
p̂_control = 150/5000 = 0.030 (3.0%)
p̂_treatment = 185/5000 = 0.037 (3.7%)

Observed difference = 0.037 - 0.030 = 0.007 (0.7 percentage points)
```

**Step 3: Calculate Pooled Proportion**
Under H₀, we assume both groups have the same true proportion:
```
p̂_pooled = (successes in both) / (total in both)
p̂_pooled = (150 + 185) / (5000 + 5000)
p̂_pooled = 335 / 10000 = 0.0335
```

**Step 4: Calculate Standard Error**
```
SE = √[p̂_pooled × (1 - p̂_pooled) × (1/n₁ + 1/n₂)]
SE = √[0.0335 × 0.9665 × (1/5000 + 1/5000)]
SE = √[0.0335 × 0.9665 × 0.0004]
SE = √[0.00001295]
SE = 0.00360
```

**Step 5: Calculate Z-Statistic**
```
z = (p̂_treatment - p̂_control) / SE
z = (0.037 - 0.030) / 0.00360
z = 0.007 / 0.00360
z = 1.944
```

**Step 6: Find Critical Value and p-value**
For α = 0.05, one-tailed test:
- Critical z = 1.645
- Our z = 1.944 > 1.645

p-value: P(Z > 1.944) ≈ 0.026

**Step 7: Make Decision**
```
z = 1.944 > z_critical = 1.645
p-value = 0.026 < α = 0.05

→ REJECT H₀
```

**Answer:** Yes, the new design shows a statistically significant improvement (z = 1.94, p = 0.026). The 0.7 percentage point lift is unlikely due to chance alone.

**But wait - is it practically significant?**
- Relative lift: (3.7% - 3.0%) / 3.0% = 23% improvement
- With 5000 monthly visitors: 35 additional conversions
- Calculate ROI to determine business value

**Key Takeaway:** Statistical significance ≠ practical significance. Always consider effect size and business impact.
</details>

---

### Exercise S5: Conditional Probability (Bayes' Theorem)

**Problem:** A fraud detection system has these characteristics:
- 0.5% of transactions are actually fraudulent
- When a transaction IS fraud, the system flags it 95% of the time (sensitivity)
- When a transaction is NOT fraud, the system incorrectly flags it 3% of the time (false positive rate)

**Question:** If a transaction is flagged as fraud, what's the probability it's actually fraudulent?

<details>
<summary>💡 Hint</summary>
Use Bayes' Theorem. The answer is NOT 95%!
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Define the Events**
```
F = Transaction is fraud
¬F = Transaction is not fraud
+ = System flags as fraud
- = System doesn't flag
```

**Step 2: Extract Given Information**
```
P(F) = 0.005 (0.5% fraud rate)
P(¬F) = 0.995 (99.5% legitimate)
P(+|F) = 0.95 (sensitivity - correctly catch fraud)
P(+|¬F) = 0.03 (false positive rate)
```

**Step 3: We Want P(F|+)**
Probability transaction is fraud GIVEN it was flagged.

Bayes' Theorem:
```
P(F|+) = P(+|F) × P(F) / P(+)
```

**Step 4: Calculate P(+) - Total Probability of Being Flagged**
```
P(+) = P(+|F) × P(F) + P(+|¬F) × P(¬F)
P(+) = 0.95 × 0.005 + 0.03 × 0.995
P(+) = 0.00475 + 0.02985
P(+) = 0.0346
```

**Step 5: Apply Bayes' Theorem**
```
P(F|+) = P(+|F) × P(F) / P(+)
P(F|+) = 0.95 × 0.005 / 0.0346
P(F|+) = 0.00475 / 0.0346
P(F|+) = 0.137 = 13.7%
```

**Step 6: Interpret the Result**

Even with 95% sensitivity and only 3% false positive rate, only ~14% of flagged transactions are actually fraud!

**Why?** Base rate (prior probability) matters!
- For every 10,000 transactions:
  - 50 are fraud, system catches 47.5 (95%)
  - 9,950 are legit, system wrongly flags 298.5 (3%)
  - Total flagged: 346
  - True positives: 47.5 / 346 = 13.7%

**Answer:** Only 13.7% of flagged transactions are actually fraudulent.

**Key Takeaway:** When the base rate is low, even a good classifier will have many false positives. This is the "base rate fallacy."

**Practical Implication:** You might need a human review stage for flagged transactions rather than automatic blocking.
</details>

---

### Exercise S6: Simpson's Paradox

**Problem:** Hospital comparison data:

**Treatment Success Rates - Simple View:**
| Hospital | Patients | Recovered | Success Rate |
|----------|----------|-----------|--------------|
| Hospital A | 1000 | 750 | 75% |
| Hospital B | 1000 | 700 | 70% |

Hospital A looks better! But look at the breakdown by patient condition:

**Breakdown by Severity:**
| Hospital | Mild Patients | Mild Recovered | Severe Patients | Severe Recovered |
|----------|---------------|----------------|-----------------|------------------|
| Hospital A | 900 | 720 (80%) | 100 | 30 (30%) |
| Hospital B | 100 | 85 (85%) | 900 | 615 (68%) |

**Question:** Which hospital is actually better? Explain the paradox.

<details>
<summary>💡 Hint</summary>
Compare success rates within each severity group, not overall.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Verify the Overall Numbers**
Hospital A:
- Total recovered: 720 + 30 = 750
- Success rate: 750/1000 = 75% ✓

Hospital B:
- Total recovered: 85 + 615 = 700
- Success rate: 700/1000 = 70% ✓

**Step 2: Compare Within Each Severity Group**

**Mild Patients:**
- Hospital A: 720/900 = 80%
- Hospital B: 85/100 = **85%** ← B is better!

**Severe Patients:**
- Hospital A: 30/100 = 30%
- Hospital B: 615/900 = **68%** ← B is better!

**Step 3: Explain the Paradox**

Hospital B is better for BOTH mild AND severe patients, yet has a lower overall rate!

How? Hospital B treats mostly severe patients (900 vs 100), while Hospital A treats mostly mild patients (900 vs 100).

Since severe patients have lower success rates overall, Hospital B's overall rate is dragged down despite being better at treating both types.

**Step 4: Visualize the Paradox**
```
Hospital A composition: 90% mild, 10% severe
Hospital B composition: 10% mild, 90% severe

Hospital A's advantage comes from treating "easier" cases.
```

**Answer:** Hospital B is actually better at treating patients in both severity categories. The overall rate favors Hospital A only because A treats a higher proportion of mild (easier) cases. This is Simpson's Paradox.

**Key Takeaway:** Always stratify by confounding variables before comparing groups. Aggregate statistics can be misleading when group compositions differ.

**Real-world examples:**
- College admission rates by gender vs. by department
- Batting averages by year vs. combined
- Drug effectiveness across subgroups
</details>

---

## 💻 SQL Exercises

### Exercise Q4: Window Functions Basics

**Schema:**
```sql
CREATE TABLE daily_sales (
    sale_date DATE,
    product_id INTEGER,
    revenue DECIMAL(10,2)
);
```

**Question:** For each day, show the daily revenue alongside:
1. Running total of revenue
2. 7-day moving average
3. Day-over-day change

<details>
<summary>💡 Hint</summary>
Use SUM() OVER, AVG() OVER with frame clauses, and LAG().
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Aggregate to Daily Level**
```sql
WITH daily_totals AS (
    SELECT 
        sale_date,
        SUM(revenue) AS daily_revenue
    FROM daily_sales
    GROUP BY sale_date
)
SELECT * FROM daily_totals ORDER BY sale_date;
```

**Step 2: Add Running Total**
```sql
WITH daily_totals AS (
    SELECT 
        sale_date,
        SUM(revenue) AS daily_revenue
    FROM daily_sales
    GROUP BY sale_date
)
SELECT 
    sale_date,
    daily_revenue,
    SUM(daily_revenue) OVER (ORDER BY sale_date) AS running_total
FROM daily_totals
ORDER BY sale_date;
```

**Understanding the Window:**
```
SUM() OVER (ORDER BY sale_date)

This means: For each row, sum all rows from the start up to current row.
Default frame: RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
```

**Step 3: Add 7-Day Moving Average**
```sql
AVG(daily_revenue) OVER (
    ORDER BY sale_date 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
) AS moving_avg_7d
```

**Understanding the Frame:**
```
ROWS BETWEEN 6 PRECEDING AND CURRENT ROW

This includes: current row + 6 previous rows = 7 days total
```

**Step 4: Add Day-over-Day Change**
```sql
daily_revenue - LAG(daily_revenue, 1) OVER (ORDER BY sale_date) AS dod_change
```

**Complete Solution:**
```sql
WITH daily_totals AS (
    SELECT 
        sale_date,
        SUM(revenue) AS daily_revenue
    FROM daily_sales
    GROUP BY sale_date
)
SELECT 
    sale_date,
    daily_revenue,
    SUM(daily_revenue) OVER (
        ORDER BY sale_date
    ) AS running_total,
    ROUND(AVG(daily_revenue) OVER (
        ORDER BY sale_date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ), 2) AS moving_avg_7d,
    daily_revenue - LAG(daily_revenue, 1) OVER (
        ORDER BY sale_date
    ) AS dod_change,
    ROUND(
        (daily_revenue - LAG(daily_revenue, 1) OVER (ORDER BY sale_date)) * 100.0 
        / NULLIF(LAG(daily_revenue, 1) OVER (ORDER BY sale_date), 0)
    , 1) AS dod_pct_change
FROM daily_totals
ORDER BY sale_date;
```

**Sample Output:**
| sale_date | daily_revenue | running_total | moving_avg_7d | dod_change | dod_pct_change |
|-----------|---------------|---------------|---------------|------------|----------------|
| 2024-01-01 | 1000.00 | 1000.00 | 1000.00 | NULL | NULL |
| 2024-01-02 | 1200.00 | 2200.00 | 1100.00 | 200.00 | 20.0 |
| 2024-01-03 | 800.00 | 3000.00 | 1000.00 | -400.00 | -33.3 |

**Key Takeaway:** Window functions let you calculate across rows without collapsing them (unlike GROUP BY).
</details>

---

### Exercise Q5: Cohort Retention Query

**Schema:**
```sql
CREATE TABLE user_actions (
    user_id INTEGER,
    action_type VARCHAR(50),
    action_date DATE
);
```

**Question:** Build a monthly retention cohort analysis. For users who signed up each month, what percentage returned in months 1, 2, 3, etc.?

<details>
<summary>💡 Hint</summary>
First find each user's signup month, then calculate the month number of each action relative to signup.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Find Each User's First Action (Signup Month)**
```sql
WITH user_cohorts AS (
    SELECT 
        user_id,
        DATE_TRUNC('month', MIN(action_date)) AS cohort_month
    FROM user_actions
    GROUP BY user_id
)
SELECT * FROM user_cohorts LIMIT 5;
```

**Step 2: Calculate Month Number for Each Action**
```sql
WITH user_cohorts AS (
    SELECT 
        user_id,
        DATE_TRUNC('month', MIN(action_date)) AS cohort_month
    FROM user_actions
    GROUP BY user_id
),
user_activities AS (
    SELECT 
        a.user_id,
        c.cohort_month,
        DATE_TRUNC('month', a.action_date) AS activity_month,
        -- Calculate months since signup
        EXTRACT(YEAR FROM AGE(
            DATE_TRUNC('month', a.action_date), 
            c.cohort_month
        )) * 12 + 
        EXTRACT(MONTH FROM AGE(
            DATE_TRUNC('month', a.action_date), 
            c.cohort_month
        )) AS month_number
    FROM user_actions a
    JOIN user_cohorts c ON a.user_id = c.user_id
)
SELECT DISTINCT user_id, cohort_month, activity_month, month_number
FROM user_activities
ORDER BY cohort_month, user_id, month_number;
```

**Step 3: Count Unique Users Per Cohort-Month Combination**
```sql
WITH user_cohorts AS (
    SELECT 
        user_id,
        DATE_TRUNC('month', MIN(action_date)) AS cohort_month
    FROM user_actions
    GROUP BY user_id
),
user_activities AS (
    SELECT DISTINCT
        a.user_id,
        c.cohort_month,
        (DATE_PART('year', DATE_TRUNC('month', a.action_date)) - 
         DATE_PART('year', c.cohort_month)) * 12 +
        (DATE_PART('month', DATE_TRUNC('month', a.action_date)) - 
         DATE_PART('month', c.cohort_month)) AS month_number
    FROM user_actions a
    JOIN user_cohorts c ON a.user_id = c.user_id
),
cohort_sizes AS (
    SELECT 
        cohort_month,
        COUNT(DISTINCT user_id) AS cohort_size
    FROM user_cohorts
    GROUP BY cohort_month
),
retention_counts AS (
    SELECT 
        cohort_month,
        month_number,
        COUNT(DISTINCT user_id) AS users_retained
    FROM user_activities
    GROUP BY cohort_month, month_number
)
SELECT 
    r.cohort_month,
    c.cohort_size,
    r.month_number,
    r.users_retained,
    ROUND(100.0 * r.users_retained / c.cohort_size, 1) AS retention_pct
FROM retention_counts r
JOIN cohort_sizes c ON r.cohort_month = c.cohort_month
WHERE r.month_number <= 6  -- First 6 months
ORDER BY r.cohort_month, r.month_number;
```

**Step 4: Pivot to Retention Matrix Format (Optional)**
```sql
-- Pivoted view for visualization
SELECT 
    cohort_month,
    cohort_size,
    MAX(CASE WHEN month_number = 0 THEN retention_pct END) AS month_0,
    MAX(CASE WHEN month_number = 1 THEN retention_pct END) AS month_1,
    MAX(CASE WHEN month_number = 2 THEN retention_pct END) AS month_2,
    MAX(CASE WHEN month_number = 3 THEN retention_pct END) AS month_3,
    MAX(CASE WHEN month_number = 4 THEN retention_pct END) AS month_4,
    MAX(CASE WHEN month_number = 5 THEN retention_pct END) AS month_5,
    MAX(CASE WHEN month_number = 6 THEN retention_pct END) AS month_6
FROM (/* previous query */) retention_data
GROUP BY cohort_month, cohort_size
ORDER BY cohort_month;
```

**Sample Output:**
| cohort_month | cohort_size | month_0 | month_1 | month_2 | month_3 |
|--------------|-------------|---------|---------|---------|---------|
| 2024-01-01 | 1000 | 100.0 | 45.2 | 32.1 | 28.5 |
| 2024-02-01 | 1200 | 100.0 | 48.3 | 35.7 | 30.2 |
| 2024-03-01 | 950 | 100.0 | 42.1 | 30.5 | NULL |

**Key Takeaway:** Cohort analysis requires: (1) defining cohorts, (2) calculating time periods, (3) counting unique users, (4) calculating percentages.
</details>

---

### Exercise Q6: Self-Join for Sequential Analysis

**Schema:**
```sql
CREATE TABLE page_views (
    session_id VARCHAR(50),
    user_id INTEGER,
    page_name VARCHAR(100),
    view_time TIMESTAMP,
    view_order INTEGER  -- Order within session
);
```

**Question:** Find the most common page-to-page transitions. What pages do users visit immediately after the homepage?

<details>
<summary>💡 Hint</summary>
Self-join the table to pair each page with the next page in the sequence.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Understand the Self-Join Pattern**
We need to pair each row with the "next" row in the same session.

**Step 2: Use LEAD() Function (Easier Approach)**
```sql
WITH page_sequences AS (
    SELECT 
        session_id,
        user_id,
        page_name AS from_page,
        LEAD(page_name) OVER (
            PARTITION BY session_id 
            ORDER BY view_order
        ) AS to_page
    FROM page_views
)
SELECT * FROM page_sequences WHERE to_page IS NOT NULL;
```

**Step 3: Filter to Homepage as Starting Page**
```sql
WITH page_sequences AS (
    SELECT 
        session_id,
        user_id,
        page_name AS from_page,
        LEAD(page_name) OVER (
            PARTITION BY session_id 
            ORDER BY view_order
        ) AS to_page
    FROM page_views
)
SELECT 
    to_page AS page_after_homepage,
    COUNT(*) AS transition_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS pct_of_homepage_exits
FROM page_sequences
WHERE from_page = 'homepage'
  AND to_page IS NOT NULL
GROUP BY to_page
ORDER BY transition_count DESC;
```

**Step 4: Alternative Using Self-Join**
```sql
-- Self-join approach (more generalizable)
SELECT 
    a.page_name AS from_page,
    b.page_name AS to_page,
    COUNT(*) AS transition_count
FROM page_views a
JOIN page_views b 
    ON a.session_id = b.session_id
    AND a.view_order = b.view_order - 1  -- Sequential pages
WHERE a.page_name = 'homepage'
GROUP BY a.page_name, b.page_name
ORDER BY transition_count DESC;
```

**Complete Solution with Full Transition Matrix:**
```sql
WITH page_sequences AS (
    SELECT 
        session_id,
        page_name AS from_page,
        LEAD(page_name) OVER (
            PARTITION BY session_id 
            ORDER BY view_order
        ) AS to_page
    FROM page_views
),
transition_counts AS (
    SELECT 
        from_page,
        to_page,
        COUNT(*) AS transitions
    FROM page_sequences
    WHERE to_page IS NOT NULL
    GROUP BY from_page, to_page
),
from_totals AS (
    SELECT 
        from_page,
        SUM(transitions) AS total_from
    FROM transition_counts
    GROUP BY from_page
)
SELECT 
    t.from_page,
    t.to_page,
    t.transitions,
    ROUND(100.0 * t.transitions / f.total_from, 1) AS pct_of_exits
FROM transition_counts t
JOIN from_totals f ON t.from_page = f.from_page
ORDER BY t.from_page, t.transitions DESC;
```

**Sample Output:**
| from_page | to_page | transitions | pct_of_exits |
|-----------|---------|-------------|--------------|
| homepage | product_list | 4521 | 45.2 |
| homepage | search | 2103 | 21.0 |
| homepage | login | 1876 | 18.8 |
| homepage | cart | 892 | 8.9 |

**Key Takeaway:** LEAD/LAG are preferred for sequential analysis, but self-joins work when you need more complex conditions.
</details>

---

## 🐍 Python Exercises

### Exercise P3: Multi-Step Data Analysis

**Problem:** You have sales data with columns: `date`, `product`, `region`, `quantity`, `unit_price`.

Write code to:
1. Calculate total revenue per product per region
2. Find the top product in each region
3. Calculate the contribution percentage of each product to its region's total

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Load and Prepare Data**
```python
import pandas as pd

# Load data
df = pd.read_csv('sales_data.csv')
df['date'] = pd.to_datetime(df['date'])

# Calculate revenue
df['revenue'] = df['quantity'] * df['unit_price']

print(df.head())
```

**Step 2: Revenue per Product per Region**
```python
product_region_revenue = (
    df
    .groupby(['region', 'product'])
    ['revenue']
    .sum()
    .reset_index()
    .rename(columns={'revenue': 'total_revenue'})
)

print(product_region_revenue)
```

**Step 3: Find Top Product per Region**
```python
# Method 1: Using idxmax
top_products = (
    product_region_revenue
    .loc[
        product_region_revenue
        .groupby('region')['total_revenue']
        .idxmax()
    ]
)

# Method 2: Sort and take first
top_products = (
    product_region_revenue
    .sort_values('total_revenue', ascending=False)
    .groupby('region')
    .first()
    .reset_index()
)

print("Top product in each region:")
print(top_products)
```

**Step 4: Calculate Contribution Percentage**
```python
# Calculate region totals
region_totals = (
    product_region_revenue
    .groupby('region')['total_revenue']
    .sum()
    .reset_index()
    .rename(columns={'total_revenue': 'region_total'})
)

# Merge and calculate percentage
product_contribution = product_region_revenue.merge(
    region_totals, on='region'
)
product_contribution['contribution_pct'] = (
    product_contribution['total_revenue'] / 
    product_contribution['region_total'] * 100
).round(1)

print(product_contribution)
```

**Complete Solution:**
```python
import pandas as pd

def analyze_sales(filepath):
    # Load and prepare
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    df['revenue'] = df['quantity'] * df['unit_price']
    
    # Product-region aggregation
    product_region = (
        df.groupby(['region', 'product'])
        .agg(
            total_revenue=('revenue', 'sum'),
            units_sold=('quantity', 'sum'),
            avg_price=('unit_price', 'mean')
        )
        .reset_index()
    )
    
    # Region totals for percentage
    region_totals = (
        product_region.groupby('region')['total_revenue']
        .transform('sum')
    )
    
    product_region['contribution_pct'] = (
        (product_region['total_revenue'] / region_totals * 100)
        .round(1)
    )
    
    # Rank products within each region
    product_region['rank_in_region'] = (
        product_region.groupby('region')['total_revenue']
        .rank(ascending=False, method='dense')
        .astype(int)
    )
    
    # Top products
    top_products = product_region[product_region['rank_in_region'] == 1]
    
    return {
        'full_analysis': product_region,
        'top_products': top_products
    }

# Run analysis
results = analyze_sales('sales_data.csv')
print("=== Full Analysis ===")
print(results['full_analysis'])
print("\n=== Top Products per Region ===")
print(results['top_products'])
```

**Key Takeaway:** Use `.transform()` to add group-level calculations back to individual rows.
</details>

---

## 🎯 Practice Checklist

After completing these exercises, you should be able to:

- [ ] Perform and interpret hypothesis tests
- [ ] Apply Bayes' Theorem correctly
- [ ] Recognize and explain Simpson's Paradox
- [ ] Write window functions with proper frame clauses
- [ ] Build cohort retention queries
- [ ] Use self-joins and LEAD/LAG for sequential analysis
- [ ] Create multi-step pandas analysis pipelines
- [ ] Calculate percentages within groups

---

## 📈 Next Steps

Ready for real-world complexity? Move on to:
- [Advanced Exercises](/exercises/advanced/) - Complex scenarios, system design

Or practice specific topics:
- [SQL Interview Problems](/interview-preparation/sql-interview-problems/)
- [A/B Testing Deep Dive](/foundational_knowledge/4-ab-testing/)

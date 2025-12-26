---
layout: page
title: "Beginner Exercises"
permalink: /exercises/beginner/
nav_order: 1
parent: "Exercises"
difficulty: "Beginner"
estimated_time: "2-3 hours"
tags: [Exercises, Practice, Beginner, Step-by-Step]
track: "Data Science Foundations"
---

# Beginner Exercises: Step-by-Step Problem Solving

Welcome to the beginner exercises! Each problem includes detailed step-by-step solutions to help you build confidence and understand the reasoning behind each answer.

---

## 📊 Statistics Exercises

### Exercise S1: Mean vs Median Decision

**Problem:** You're analyzing salaries at a small company. Here are the salaries:
- Employee 1: $45,000
- Employee 2: $48,000
- Employee 3: $52,000
- Employee 4: $55,000
- Employee 5: $58,000
- CEO: $450,000

**Question:** Should you report mean or median salary? Calculate both and explain your choice.

<details>
<summary>💡 Hint</summary>
Think about what happens to the mean when there's an extreme value.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Calculate the Mean**
```
Sum of all salaries:
$45,000 + $48,000 + $52,000 + $55,000 + $58,000 + $450,000 = $708,000

Mean = $708,000 ÷ 6 = $118,000
```

**Step 2: Calculate the Median**
```
First, order the values (already ordered):
$45,000, $48,000, $52,000, $55,000, $58,000, $450,000

With 6 values, median is average of 3rd and 4th values:
Median = ($52,000 + $55,000) ÷ 2 = $53,500
```

**Step 3: Compare and Decide**
- Mean salary: $118,000
- Median salary: $53,500

The mean ($118,000) is much higher than what 5 out of 6 employees actually earn!

**Answer:** Report the **median ($53,500)** because the CEO's salary is an outlier that skews the mean upward. The median better represents what a "typical" employee earns.

**Key Takeaway:** Use median when data has outliers or is skewed. Use mean when data is roughly symmetric.
</details>

---

### Exercise S2: Standard Deviation Interpretation

**Problem:** Two pizza delivery companies report their delivery times:

| Company | Mean Time | Standard Deviation |
|---------|-----------|-------------------|
| FastPizza | 25 minutes | 3 minutes |
| QuickBite | 25 minutes | 12 minutes |

**Question:** You have an important meeting in 35 minutes. Which company should you order from? Why?

<details>
<summary>💡 Hint</summary>
Think about what standard deviation tells you about consistency.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Understand What Standard Deviation Means**

Standard deviation measures *spread* - how much individual values typically deviate from the mean.
- Small SD = values cluster close to mean (consistent)
- Large SD = values spread far from mean (inconsistent)

**Step 2: Analyze FastPizza (SD = 3 min)**

Using the 68-95-99.7 rule:
- 68% of deliveries: 25 ± 3 = 22 to 28 minutes
- 95% of deliveries: 25 ± 6 = 19 to 31 minutes
- 99.7% of deliveries: 25 ± 9 = 16 to 34 minutes

Almost all deliveries arrive within 34 minutes ✅

**Step 3: Analyze QuickBite (SD = 12 min)**

Using the 68-95-99.7 rule:
- 68% of deliveries: 25 ± 12 = 13 to 37 minutes
- 95% of deliveries: 25 ± 24 = 1 to 49 minutes

About 16% of deliveries take longer than 37 minutes! ❌

**Step 4: Make the Decision**

With 35 minutes available:
- FastPizza: ~99.7% chance of arriving on time
- QuickBite: ~80% chance of arriving on time

**Answer:** Order from **FastPizza**. Despite having the same mean, FastPizza's lower standard deviation means much more consistent (reliable) delivery times.

**Key Takeaway:** When reliability matters, prefer lower variance even if the mean is the same.
</details>

---

### Exercise S3: Probability with Dice

**Problem:** You roll two fair six-sided dice.

**Questions:**
1. What is the probability of getting a sum of 7?
2. What is the probability of getting a sum of 12?
3. Why are these probabilities different?

<details>
<summary>💡 Hint</summary>
List out all the ways to get each sum.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Count Total Outcomes**
```
Die 1 can show: 1, 2, 3, 4, 5, or 6 (6 options)
Die 2 can show: 1, 2, 3, 4, 5, or 6 (6 options)

Total possible outcomes = 6 × 6 = 36
```

**Step 2: Find Ways to Get Sum of 7**
```
(1, 6) → 1 + 6 = 7 ✓
(2, 5) → 2 + 5 = 7 ✓
(3, 4) → 3 + 4 = 7 ✓
(4, 3) → 4 + 3 = 7 ✓
(5, 2) → 5 + 2 = 7 ✓
(6, 1) → 6 + 1 = 7 ✓

Ways to get 7: 6
```

**Step 3: Calculate Probability of Sum = 7**
```
P(sum = 7) = favorable outcomes / total outcomes
P(sum = 7) = 6 / 36 = 1/6 ≈ 16.67%
```

**Step 4: Find Ways to Get Sum of 12**
```
(6, 6) → 6 + 6 = 12 ✓

Ways to get 12: 1
```

**Step 5: Calculate Probability of Sum = 12**
```
P(sum = 12) = 1 / 36 ≈ 2.78%
```

**Step 6: Explain the Difference**

The sum of 7 is more likely because there are more combinations that produce it. 7 is in the "middle" of possible sums (2 to 12), while 12 requires both dice to show their maximum value.

**Answer:**
1. P(sum = 7) = 6/36 = 1/6 ≈ 16.67%
2. P(sum = 12) = 1/36 ≈ 2.78%
3. Sum of 7 has 6 times more favorable outcomes than sum of 12

**Key Takeaway:** When counting outcomes, list them systematically to avoid missing any.
</details>

---

## 💻 SQL Exercises

### Exercise Q1: Basic SELECT with WHERE

**Schema:**
```sql
-- employees table
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary INTEGER,
    hire_date DATE
);
```

**Sample Data:**
| employee_id | name | department | salary | hire_date |
|-------------|------|------------|--------|-----------|
| 1 | Alice | Engineering | 85000 | 2020-03-15 |
| 2 | Bob | Marketing | 65000 | 2019-07-22 |
| 3 | Carol | Engineering | 92000 | 2018-11-01 |
| 4 | David | Sales | 55000 | 2021-01-10 |
| 5 | Eva | Marketing | 70000 | 2020-06-30 |

**Question:** Write a query to find all employees in the Engineering department who earn more than $80,000. Order by salary descending.

<details>
<summary>💡 Hint</summary>
You'll need WHERE with two conditions connected by AND.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Start with Basic SELECT**
```sql
SELECT *
FROM employees
```
This returns all columns and all rows.

**Step 2: Add Department Filter**
```sql
SELECT *
FROM employees
WHERE department = 'Engineering'
```
This filters to only Engineering employees.

**Step 3: Add Salary Filter**
```sql
SELECT *
FROM employees
WHERE department = 'Engineering'
  AND salary > 80000
```
Now we have both conditions.

**Step 4: Add Ordering**
```sql
SELECT *
FROM employees
WHERE department = 'Engineering'
  AND salary > 80000
ORDER BY salary DESC
```

**Final Answer:**
```sql
SELECT employee_id, name, department, salary, hire_date
FROM employees
WHERE department = 'Engineering'
  AND salary > 80000
ORDER BY salary DESC;
```

**Result:**
| employee_id | name | department | salary | hire_date |
|-------------|------|------------|--------|-----------|
| 3 | Carol | Engineering | 92000 | 2018-11-01 |
| 1 | Alice | Engineering | 85000 | 2020-03-15 |

**Key Takeaway:** Build queries incrementally - add one clause at a time and verify results.
</details>

---

### Exercise Q2: GROUP BY with COUNT

**Schema:**
```sql
-- orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount DECIMAL(10,2),
    status VARCHAR(20)
);
```

**Sample Data:**
| order_id | customer_id | order_date | total_amount | status |
|----------|-------------|------------|--------------|--------|
| 1 | 101 | 2024-01-15 | 150.00 | completed |
| 2 | 102 | 2024-01-16 | 89.50 | completed |
| 3 | 101 | 2024-01-17 | 225.00 | completed |
| 4 | 103 | 2024-01-18 | 45.00 | cancelled |
| 5 | 101 | 2024-01-19 | 180.00 | pending |
| 6 | 102 | 2024-01-20 | 310.00 | completed |

**Question:** For each customer, find the number of orders and total amount spent. Only include customers with more than 1 order.

<details>
<summary>💡 Hint</summary>
You'll need GROUP BY, COUNT, SUM, and HAVING (not WHERE for filtering groups).
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Understand the Goal**
We need to:
- Group orders by customer
- Count orders per customer
- Sum amounts per customer
- Filter to customers with > 1 order

**Step 2: Basic Grouping**
```sql
SELECT customer_id
FROM orders
GROUP BY customer_id
```
This gives us unique customers.

**Step 3: Add Aggregations**
```sql
SELECT 
    customer_id,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_spent
FROM orders
GROUP BY customer_id
```

**Step 4: Filter Groups with HAVING**

⚠️ Common mistake: Using WHERE to filter after GROUP BY.

WHERE filters *before* grouping.
HAVING filters *after* grouping.

```sql
SELECT 
    customer_id,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1
```

**Final Answer:**
```sql
SELECT 
    customer_id,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1
ORDER BY total_spent DESC;
```

**Result:**
| customer_id | order_count | total_spent |
|-------------|-------------|-------------|
| 101 | 3 | 555.00 |
| 102 | 2 | 399.50 |

**Key Takeaway:** Use WHERE before GROUP BY, HAVING after GROUP BY.
</details>

---

### Exercise Q3: Simple JOIN

**Schema:**
```sql
-- customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- orders table (from previous exercise)
```

**Question:** List all orders with customer names. Include order_id, customer name, order_date, and total_amount.

<details>
<summary>💡 Hint</summary>
Join customers and orders on customer_id.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Identify the Tables and Keys**
- `customers` table has `customer_id` (primary key)
- `orders` table has `customer_id` (foreign key)
- These are the columns we'll join on

**Step 2: Write the Basic JOIN**
```sql
SELECT *
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
```

**Step 3: Select Specific Columns**
```sql
SELECT 
    orders.order_id,
    customers.name AS customer_name,
    orders.order_date,
    orders.total_amount
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
```

**Step 4: Use Table Aliases for Readability**

**Final Answer:**
```sql
SELECT 
    o.order_id,
    c.name AS customer_name,
    o.order_date,
    o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
ORDER BY o.order_date;
```

**Join Types Quick Reference:**
- `JOIN` (or `INNER JOIN`): Only matching rows from both tables
- `LEFT JOIN`: All rows from left table, matching from right
- `RIGHT JOIN`: All rows from right table, matching from left
- `FULL OUTER JOIN`: All rows from both tables

**Key Takeaway:** Always specify which table each column comes from when joining.
</details>

---

## 🐍 Python Exercises

### Exercise P1: Loading and Inspecting Data

**Problem:** You have a CSV file with e-commerce data. Write Python code to:
1. Load the data into a pandas DataFrame
2. Display the first 5 rows
3. Check for missing values
4. Get summary statistics

<details>
<summary>💡 Hint</summary>
Use pd.read_csv(), .head(), .isnull().sum(), and .describe()
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Import pandas**
```python
import pandas as pd
```

**Step 2: Load the Data**
```python
# Load CSV file into DataFrame
df = pd.read_csv('ecommerce_data.csv')

# Check the shape (rows, columns)
print(f"Dataset shape: {df.shape}")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
```

**Step 3: Display First 5 Rows**
```python
# Preview the data
print(df.head())

# Alternative: see last 5 rows
# print(df.tail())

# See column names and types
print(df.info())
```

**Step 4: Check for Missing Values**
```python
# Count missing values per column
missing = df.isnull().sum()
print("Missing values per column:")
print(missing)

# As percentage
missing_pct = (df.isnull().sum() / len(df) * 100).round(2)
print("\nMissing percentage:")
print(missing_pct)
```

**Step 5: Get Summary Statistics**
```python
# Numeric columns summary
print(df.describe())

# Include non-numeric columns
print(df.describe(include='all'))
```

**Complete Code:**
```python
import pandas as pd

# Load data
df = pd.read_csv('ecommerce_data.csv')

# Basic info
print(f"Shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())

# Check missing values
print(f"\nMissing values:")
print(df.isnull().sum())

# Summary statistics
print(f"\nSummary statistics:")
print(df.describe())
```

**Output Example:**
```
Shape: (1000, 8)

First 5 rows:
   order_id  customer_id  product  quantity  price    date
0         1          101   Laptop         1  999.0  2024-01-15
1         2          102    Mouse         2   25.0  2024-01-15
...

Missing values:
order_id       0
customer_id    0
product        5
quantity       0
price         12
date           0

Summary statistics:
       order_id  customer_id  quantity    price
count   1000.0       1000.0    1000.0    988.0
mean     500.5        150.2       2.3    125.4
...
```

**Key Takeaway:** Always start by understanding your data's shape, types, and missing values before analysis.
</details>

---

### Exercise P2: Filtering and Grouping

**Problem:** Using the e-commerce DataFrame, write code to:
1. Filter to orders from January 2024
2. Group by product and calculate total revenue (quantity × price)
3. Sort by revenue descending

<details>
<summary>💡 Hint</summary>
Use boolean filtering with dates, then .groupby() with .agg()
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Convert Date Column**
```python
# Ensure date is datetime type
df['date'] = pd.to_datetime(df['date'])

# Verify the conversion
print(df['date'].dtype)  # Should show: datetime64[ns]
```

**Step 2: Filter to January 2024**
```python
# Create boolean mask for January 2024
jan_2024 = (df['date'].dt.year == 2024) & (df['date'].dt.month == 1)

# Apply filter
jan_orders = df[jan_2024]

print(f"January 2024 orders: {len(jan_orders)}")
```

**Alternative filtering methods:**
```python
# Using string comparison (if date is string)
jan_orders = df[df['date'].str.startswith('2024-01')]

# Using between
start = '2024-01-01'
end = '2024-01-31'
jan_orders = df[(df['date'] >= start) & (df['date'] <= end)]
```

**Step 3: Calculate Revenue**
```python
# Add revenue column
jan_orders['revenue'] = jan_orders['quantity'] * jan_orders['price']
```

**Step 4: Group by Product**
```python
# Group and aggregate
product_revenue = jan_orders.groupby('product').agg({
    'revenue': 'sum',
    'order_id': 'count'  # Number of orders
}).rename(columns={'order_id': 'order_count'})

# Sort by revenue
product_revenue = product_revenue.sort_values('revenue', ascending=False)

print(product_revenue)
```

**Complete Code:**
```python
import pandas as pd

# Load and prepare data
df = pd.read_csv('ecommerce_data.csv')
df['date'] = pd.to_datetime(df['date'])

# Filter to January 2024
jan_2024_mask = (df['date'].dt.year == 2024) & (df['date'].dt.month == 1)
jan_orders = df[jan_2024_mask].copy()

# Calculate revenue
jan_orders['revenue'] = jan_orders['quantity'] * jan_orders['price']

# Group by product and calculate totals
product_summary = (
    jan_orders
    .groupby('product')
    .agg(
        total_revenue=('revenue', 'sum'),
        total_quantity=('quantity', 'sum'),
        order_count=('order_id', 'count')
    )
    .sort_values('total_revenue', ascending=False)
    .reset_index()
)

print(product_summary)
```

**Output Example:**
```
    product  total_revenue  total_quantity  order_count
0    Laptop       15984.00              16           16
1   Monitor        8550.00              30           25
2  Keyboard        1250.00              50           42
3     Mouse         750.00              30           28
```

**Key Takeaway:** Always use .copy() when filtering to avoid SettingWithCopyWarning.
</details>

---

## 🎯 Practice Checklist

After completing these exercises, you should be able to:

- [ ] Calculate and interpret mean, median, and mode
- [ ] Understand and explain standard deviation
- [ ] Calculate basic probabilities
- [ ] Write SELECT queries with WHERE, AND, OR
- [ ] Use GROUP BY with COUNT, SUM, AVG
- [ ] Join two tables on a common key
- [ ] Load and inspect DataFrames in pandas
- [ ] Filter and group data in pandas

---

## 📈 Next Steps

Ready for more challenging exercises? Move on to:
- [Intermediate Exercises](/exercises/intermediate/) - More complex SQL, multi-step analysis
- [Advanced Exercises](/exercises/advanced/) - Real-world scenarios, optimization

Or return to foundational concepts:
- [Statistics & Probability Fundamentals](/foundational_knowledge/1/)
- [SQL & Data Manipulation](/foundational_knowledge/2-SQL/)
- [Python Programming](/foundational_knowledge/3/)

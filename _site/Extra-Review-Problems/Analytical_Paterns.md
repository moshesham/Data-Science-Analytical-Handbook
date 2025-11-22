# Mastering SQL: Analytical Patterns for LeetCode and Beyond
*A Comprehensive Guide to SQL Problem-Solving Patterns*

## Table of Contents
1. Introduction
2. The Core Process
3. Specific Analytical Patterns and Techniques
   - 3.1 Common PostgreSQL Syntax
4. Common LeetCode Problems by Pattern
5. Tips and Practice Recommendations
6. Additional Topics and Resources

## 1. Introduction

This guide provides a structured approach to solving SQL problems, moving beyond simple syntax and focusing on the underlying analytical patterns. By understanding these patterns, you can tackle a wide range of SQL challenges more effectively. Remember, SQL isn't just about writing queries; it's about translating business problems into logical steps.

## 2. The Core Process

### Core Analytical Task
- Before writing any SQL, understand exactly what the problem asks you to analyze or find
- Identify if it's a straightforward question or needs breaking down
- Look for keywords and focus on the intent

### Data Relationships
- Identify relevant tables and their relationships
- Determine necessary joins
- Identify unique identifiers linking tables
- Understand the underlying data model

### SQL Techniques
- Choose specific techniques based on analytical intent
- Consider: aggregations, filtering, self-joins
- Match the right tool to the analytical task

### CTEs For Structure
- Consider using Common Table Expressions (CTEs)
- Break down queries into logical, manageable parts
- Improve query structure and readability
- Consider CTEs even for seemingly simple queries

### Execution Plan
- Develop logical progression for problem-solving
- Start with a plan before coding
- Essential for complex problems

## 3. Specific Analytical Patterns and Techniques

### 3.1 Common PostgreSQL Syntax

This section details common syntax in PostgreSQL, especially for functions related to aggregation, date manipulation, and window functions. These are often used in complex analytical SQL queries.

#### A. Aggregation Functions (PostgreSQL)

**Basic Aggregates:**
- `COUNT(expression)`: Returns the number of rows where expression is not NULL. `COUNT(*)` counts all rows.
- `SUM(expression)`: Returns the sum of all values of the expression.
- `AVG(expression)`: Returns the average of all values of the expression.
- `MIN(expression)`: Returns the minimum of all values of the expression.
- `MAX(expression)`: Returns the maximum of all values of the expression.

**Grouping:**
- `GROUP BY`: Groups rows that have the same values in specified columns into summary rows.
- `HAVING`: A clause for filtering groups based on aggregated values. It's used with `GROUP BY`.

**Handling NULLs in Aggregates:**
- `COALESCE(value1, value2, ...)`: Returns the first non-NULL value from the list. Often used to handle NULLs in calculations.
- `NULLIF(value1, value2)`: Returns NULL if `value1` equals `value2`, otherwise returns `value1`.

**Example of Aggregation Functions:**
```sql
SELECT
    department_id,
    COUNT(*) AS employee_count,
    AVG(COALESCE(salary, 0)) AS avg_salary,
    MAX(salary) AS max_salary
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 10;
```

#### B. Common Date Manipulation Functions (PostgreSQL)

**Extracting Date Components:**
- `EXTRACT(part FROM timestamp)`: Extracts specific components like YEAR, MONTH, DAY, HOUR, etc., from a timestamp.
- `date_part('part', timestamp)`: Similar to EXTRACT, but uses string arguments for the part.

**Date Arithmetic:**
- `timestamp +/- interval`: Adds or subtracts an interval from a timestamp (e.g., timestamp + INTERVAL '1 day').

**Date Truncation:**
- `DATE_TRUNC('unit', timestamp)`: Truncates a timestamp to a specific unit (e.g., DATE_TRUNC('month', timestamp)).

**Formatting Dates:**
- `TO_CHAR(timestamp, 'format')`: Converts a timestamp to a string using a specified format.

**Example of Date Functions:**
```sql
SELECT
   EXTRACT(YEAR FROM order_date) AS order_year,
   DATE_TRUNC('month', order_date) AS order_month,
   COUNT(*)
FROM orders
WHERE order_date > CURRENT_DATE - INTERVAL '1 year'
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY order_year;
```

#### C. Window Functions (PostgreSQL)

**Ranking Functions:**
- `RANK() OVER (PARTITION BY ... ORDER BY ...)`: Assigns ranks within a partition, with gaps for ties.
- `DENSE_RANK() OVER (PARTITION BY ... ORDER BY ...)`: Assigns ranks within a partition, no gaps for ties.
- `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)`: Assigns unique row numbers within a partition.

**Analytical Functions:**
- `LAG(expression, offset, default) OVER (PARTITION BY ... ORDER BY ...)`: Accesses a row at a given offset before the current row.
- `LEAD(expression, offset, default) OVER (PARTITION BY ... ORDER BY ...)`: Accesses a row at a given offset after the current row.

**Aggregate Window Functions:**
- `SUM() OVER (PARTITION BY ... ORDER BY ...)`: A running sum, calculated in a window.
- `AVG() OVER (PARTITION BY ... ORDER BY ...)`: A running average, calculated in a window.

**Example of Window Functions:**
```sql
SELECT
   order_id,
   customer_id,
   order_date,
   order_amount,
   RANK() OVER (PARTITION BY customer_id ORDER BY order_date) as customer_order_rank,
   SUM(order_amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS customer_running_total,
   LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) as previous_order_date
FROM orders;
```

### Pattern Examples

#### A. Aggregation and Grouping
Analytical Intent: To summarize data over groups

**Example (184 - Department Highest Salary):**
```sql
WITH MaxSalaries AS (
  SELECT DepartmentId, MAX(COALESCE(Salary, 0)) AS MaxSalary
  FROM Employee
  GROUP BY DepartmentId
)
SELECT d.Name AS Department,
       e.Name AS Employee,
       e.Salary
FROM Employee e
JOIN MaxSalaries ms
  ON e.DepartmentId = ms.DepartmentId
  AND COALESCE(e.Salary, 0) = ms.MaxSalary
JOIN Department d ON e.DepartmentId = d.Id;
```

#### B. Filtering and Selection
Analytical Intent: Retrieve specific subsets based on conditions

**Example (183 - Customers Who Never Order):**
```sql
WITH OrderedCustomers AS (
  SELECT CustomerId FROM Orders
)
SELECT Name
FROM Customers
WHERE Id NOT IN (
  SELECT COALESCE(CustomerId, 0)
  FROM OrderedCustomers
);
```

#### C. Self-Joins
Analytical Intent: Compare rows within a single table

**Example (180 - Consecutive Numbers):**
```sql
WITH LaggedLogs AS (
  SELECT
    Id,
    Num,
    LAG(Num, 1, NULL) OVER (ORDER BY Id) AS prev_num1,
    LAG(Num, 2, NULL) OVER (ORDER BY Id) AS prev_num2
  FROM Logs
)
SELECT DISTINCT Num
FROM LaggedLogs
WHERE Num = prev_num1
  AND Num = prev_num2
  AND Num IS NOT NULL;
```

#### D. Ranking and Ordering
Analytical Intent: Find relative position of records

**Example (176 - Second Highest Salary):**
```sql
WITH RankedSalaries AS (
  SELECT
    Salary,
    DENSE_RANK() OVER (
      ORDER BY COALESCE(Salary, 0) DESC
    ) as rank_num
  FROM Employee
)
SELECT
  CASE
    WHEN (SELECT COUNT(*) FROM RankedSalaries) < 2 THEN NULL
    ELSE (SELECT Salary FROM RankedSalaries WHERE rank_num = 2)
  END AS SecondHighestSalary
FROM (SELECT 1 as dummy_column) as dummy_table;
```

## 4. Common LeetCode SQL Problems by Pattern

### Pattern-Based Quick Reference

| Pattern & Problem | Difficulty | Key Concepts | Common Pitfalls |
|------------------|------------|--------------|-----------------|
| **Aggregation** ||||
| 184 - Dept Highest Salary | Medium | GROUP BY, MAX | NULL handling |
| 185 - Dept Top 3 Salaries | Hard | Window funcs | Duplicates |
| 262 - Trips and Users | Hard | Multi-join | Date filtering |
| **Filtering** ||||
| 183 - Customers No Orders | Easy | NOT IN | NULL in subquery |
| 196 - Delete Duplicates | Easy | Self-JOIN | Row deletion |
| 1251 - Avg Selling Price | Easy | JOIN | Date ranges |
| **Self-Joins** ||||
| 180 - Consecutive Numbers | Medium | LAG | Row sequence |
| 197 - Rising Temperature | Easy | Self-JOIN | Date compare |
| 1270 - Manager Hierarchy | Medium | Multi-join | Recursion |
| **Ranking** ||||
| 176 - Second High Salary | Medium | DENSE_RANK | NULL result |
| 177 - Nth High Salary | Medium | ROW_NUMBER | Variable N |
| 178 - Rank Scores | Medium | DENSE_RANK | Tie handling |

## 5. Tips and Practice Recommendations

### Pattern Recognition Tips

**Aggregation Problems:**
- Look for: "highest," "average," "total"
- Consider NULL handling in aggregations
- Watch for grouping requirements

**Filtering Problems:**
- Keywords: "never," "not in," "exclude"
- Consider date range conditions
- Watch for multiple conditions

**Self-Join Problems:**
- Look for consecutive values
- Consider hierarchical relationships
- Watch for row comparisons

**Ranking Problems:**
- Keywords: "nth highest," "top k"
- Consider tie handling
- Watch for NULL values

### Practice Strategy

**Start Simple:**
- Begin with easy problems in each pattern
- Master basic patterns before combinations
- Practice NULL handling consistently

**Build Complexity:**
- Move to medium difficulty
- Combine multiple patterns
- Focus on performance optimization

**Review and Reflect:**
- Document common mistakes
- Create pattern templates
- Build a personal problem-solving framework

### Common Mistakes to Avoid

**Technical Mistakes:**
- Forgetting NULL handling
- Incorrect join conditions
- Missing edge cases

**Logical Mistakes:**
- Misinterpreting requirements
- Overlooking business rules
- Incorrect aggregation logic

**Performance Mistakes:**
- Unnecessary subqueries
- Inefficient joins
- Missing indexes consideration

## 6. Additional Topics and Resources

### Advanced SQL Concepts

**Subqueries and CTEs:**
- Explore different types of subqueries and when to use each
- Delve into advanced CTE use cases, such as recursive queries

**Performance Tuning:**
- Learn about query optimization techniques
- Consider indexes, explain plans, and query profiling

**Advanced Joins:**
- Practice different types of joins, like LEFT JOIN, RIGHT JOIN, FULL JOIN
- Learn the nuances of join conditions and when to use them

**Data Modeling:**
- Explore database schema designs
- Learn about normalization and denormalization

**String Manipulation:**
- Deepen your understanding of various string functions


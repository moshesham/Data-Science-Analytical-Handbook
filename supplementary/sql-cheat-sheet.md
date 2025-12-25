---
layout: page
title: "SQL Cheat Sheet"
permalink: /supplementary/sql-cheat-sheet/
nav_order: 10
parent: "Supplementary Materials"
difficulty: "Beginner"
estimated_time: "25 mins"
tags: [SQL, Reference, Cheat Sheet]
track: "Reference"
---

# SQL Cheat Sheet

## Basic SELECT Patterns

### Simple SELECT
```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

### SELECT with Aggregation
```sql
SELECT COUNT(*), AVG(price), SUM(quantity)
FROM products
WHERE category = 'electronics';
```

## JOIN Types

### INNER JOIN
```sql
SELECT a.name, b.order_date
FROM customers a
INNER JOIN orders b ON a.customer_id = b.customer_id;
```

### LEFT JOIN
```sql
SELECT a.name, b.order_date
FROM customers a
LEFT JOIN orders b ON a.customer_id = b.customer_id;
```

### RIGHT JOIN
```sql
SELECT a.name, b.order_date
FROM customers a
RIGHT JOIN orders b ON a.customer_id = b.customer_id;
```

### FULL OUTER JOIN
```sql
SELECT a.name, b.order_date
FROM customers a
FULL OUTER JOIN orders b ON a.customer_id = b.customer_id;
```

## Window Functions

### ROW_NUMBER()
```sql
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) as rank
FROM employees;
```

### RANK() and DENSE_RANK()
```sql
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) as rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank
FROM employees;
```

### LAG() and LEAD()
```sql
SELECT month, revenue,
       LAG(revenue) OVER (ORDER BY month) as prev_revenue,
       LEAD(revenue) OVER (ORDER BY month) as next_revenue
FROM monthly_revenue;
```

## Aggregation Patterns

### GROUP BY with HAVING
```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

### ROLLUP and CUBE
```sql
SELECT department, job_title, AVG(salary)
FROM employees
GROUP BY ROLLUP(department, job_title);
```

## Date/Time Functions

### Common Date Functions
```sql
-- Extract year/month/day
SELECT EXTRACT(YEAR FROM order_date) as year,
       EXTRACT(MONTH FROM order_date) as month
FROM orders;

-- Date arithmetic
SELECT order_date,
       order_date + INTERVAL '30 days' as due_date
FROM orders;
```

## String Manipulation

### Common String Functions
```sql
SELECT UPPER(name), LOWER(email),
       CONCAT(first_name, ' ', last_name) as full_name,
       SUBSTRING(name, 1, 3) as short_name
FROM users;
```

## NULL Handling

### COALESCE and NULLIF
```sql
SELECT name,
       COALESCE(phone, 'No phone') as contact_phone,
       NULLIF(status, 'inactive') as active_status
FROM customers;
```

## Subquery Patterns

### Scalar Subquery
```sql
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

### EXISTS Subquery
```sql
SELECT name
FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

## CTE (Common Table Expression)

### WITH Clause
```sql
WITH monthly_sales AS (
    SELECT DATE_TRUNC('month', order_date) as month,
           SUM(amount) as total_sales
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
)
SELECT month, total_sales,
       LAG(total_sales) OVER (ORDER BY month) as prev_month_sales
FROM monthly_sales;
```

## Performance Optimization Tips

1. **Use EXPLAIN PLAN** to analyze query execution
2. **Index frequently queried columns**
3. **Avoid SELECT *** in production
4. **Use LIMIT for large result sets**
5. **Prefer JOINs over subqueries when possible**
6. **Use UNION ALL instead of UNION when duplicates are not an issue**

## Common Patterns

### Pivot Table Equivalent
```sql
SELECT department,
       SUM(CASE WHEN job_title = 'Manager' THEN 1 ELSE 0 END) as managers,
       SUM(CASE WHEN job_title = 'Developer' THEN 1 ELSE 0 END) as developers
FROM employees
GROUP BY department;
```

### Running Totals
```sql
SELECT order_date, amount,
       SUM(amount) OVER (ORDER BY order_date) as running_total
FROM orders;
```

### Percentiles
```sql
SELECT name, salary,
       PERCENT_RANK() OVER (ORDER BY salary) as percentile
FROM employees;
```
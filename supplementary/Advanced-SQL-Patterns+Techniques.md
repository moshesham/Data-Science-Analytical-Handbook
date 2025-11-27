# Advanced SQL Patterns and Techniques
*Extended Guide for Complex SQL Problems*

## 1. Advanced Window Function Patterns

### Introduction to Complex Windows
Window functions are powerful tools for analyzing data across rows. This section explores advanced patterns that go beyond basic window functions.

### Frame Specifications
#### ROWS vs RANGE
```sql
-- ROWS example: exactly 3 previous rows
SUM(amount) OVER (
    ORDER BY transaction_date
    ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
)

-- RANGE example: all rows within 3 days
SUM(amount) OVER (
    ORDER BY transaction_date
    RANGE BETWEEN INTERVAL '3' DAY PRECEDING AND CURRENT ROW
)
```

### Gap and Island Detection
A common pattern for finding consecutive sequences or gaps in data.

```sql
-- Finding gaps in sequential IDs
WITH numbered AS (
  SELECT 
    id,
    ROW_NUMBER() OVER (ORDER BY id) as rn
  FROM sequences
),
gaps AS (
  SELECT 
    id,
    id - rn as grp
  FROM numbered
)
SELECT 
  MIN(id) as gap_start,
  MAX(id) as gap_end,
  COUNT(*) - 1 as gap_size
FROM gaps
GROUP BY grp
HAVING COUNT(*) > 1;
```

### Running Totals with Reset Conditions
```sql
-- Running total that resets each month
SELECT 
  transaction_date,
  amount,
  SUM(amount) OVER (
    PARTITION BY DATE_TRUNC('month', transaction_date)
    ORDER BY transaction_date
  ) as monthly_running_total
FROM transactions;
```

### Percentile Analysis
```sql
-- Complex percentile calculations
SELECT 
  product_id,
  price,
  PERCENT_RANK() OVER (ORDER BY price) as price_percentile,
  CASE 
    WHEN PERCENT_RANK() OVER (ORDER BY price) <= 0.25 THEN 'Budget'
    WHEN PERCENT_RANK() OVER (ORDER BY price) <= 0.75 THEN 'Mid-Range'
    ELSE 'Premium'
  END as price_category
FROM products;
```

## 2. Real-World Data Quality Patterns

### Fuzzy Matching Techniques

#### Using Similarity Functions
```sql
-- Comprehensive fuzzy matching
WITH similarity_metrics AS (
  SELECT 
    a.customer_id as id1,
    b.customer_id as id2,
    similarity(a.name, b.name) as name_sim,
    similarity(
      regexp_replace(a.email, '@.*$', ''),
      regexp_replace(b.email, '@.*$', '')
    ) as email_sim,
    levenshtein(
      regexp_replace(a.phone, '[^0-9]', ''),
      regexp_replace(b.phone, '[^0-9]', '')
    ) as phone_distance
  FROM customers a
  JOIN customers b ON a.customer_id < b.customer_id
)
SELECT *
FROM similarity_metrics
WHERE (name_sim > 0.8 AND email_sim > 0.7)
   OR (name_sim > 0.7 AND phone_distance < 2);
```

### Data Consistency Checks
```sql
-- Comprehensive data validation
WITH validation_checks AS (
  SELECT
    table_name,
    column_name,
    COUNT(*) as total_rows,
    COUNT(column_name) as non_null_rows,
    COUNT(DISTINCT column_name) as unique_values,
    MIN(column_name) as min_value,
    MAX(column_name) as max_value,
    AVG(CASE 
      WHEN column_name ~ '^[0-9]+$' 
      THEN column_name::numeric 
      ELSE NULL 
    END) as avg_numeric_value
  FROM information_schema.columns c
  JOIN your_table t ON true
  GROUP BY table_name, column_name
)
SELECT *
FROM validation_checks
WHERE non_null_rows < total_rows
   OR unique_values = 1;
```

## 3. Time Series Analysis Patterns

### Period-over-Period Analysis

#### Complex Comparisons
```sql
WITH daily_metrics AS (
  SELECT
    date,
    SUM(revenue) as revenue,
    LAG(SUM(revenue), 1) OVER (ORDER BY date) as prev_day,
    LAG(SUM(revenue), 7) OVER (ORDER BY date) as prev_week,
    LAG(SUM(revenue), 30) OVER (ORDER BY date) as prev_month
  FROM sales
  GROUP BY date
),
growth_metrics AS (
  SELECT
    date,
    revenue,
    (revenue - prev_day) / NULLIF(prev_day, 0) * 100 as daily_growth,
    (revenue - prev_week) / NULLIF(prev_week, 0) * 100 as weekly_growth,
    (revenue - prev_month) / NULLIF(prev_month, 0) * 100 as monthly_growth
  FROM daily_metrics
)
SELECT *
FROM growth_metrics
WHERE ABS(daily_growth) > 20  -- Significant daily changes
   OR ABS(weekly_growth) > 50;  -- Significant weekly changes
```

### Seasonal Analysis
```sql
-- Detecting seasonality
WITH monthly_sales AS (
  SELECT
    DATE_TRUNC('month', date) as month,
    SUM(revenue) as revenue
  FROM sales
  GROUP BY DATE_TRUNC('month', date)
),
seasonal_indices AS (
  SELECT
    EXTRACT(month FROM month) as month_num,
    AVG(revenue) as avg_revenue,
    AVG(revenue) OVER () as global_avg,
    AVG(revenue) / NULLIF(AVG(revenue) OVER (), 0) as seasonal_index
  FROM monthly_sales
  GROUP BY EXTRACT(month FROM month)
)
SELECT *
FROM seasonal_indices
ORDER BY month_num;
```

## 4. Performance Optimization Patterns

### Query Plan Analysis

#### Identifying Bottlenecks
```sql
EXPLAIN ANALYZE
SELECT 
  c.customer_id,
  c.name,
  COUNT(o.order_id) as order_count,
  SUM(o.total_amount) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 10;
```

### Index Design Patterns
```sql
-- Composite index for range + equality predicates
CREATE INDEX idx_orders_customer_date ON orders (
  customer_id,  -- equality predicate first
  order_date    -- range predicate second
);

-- Covering index for common query
CREATE INDEX idx_orders_summary ON orders (
  customer_id,
  order_date,
  total_amount
) INCLUDE (order_id);  -- included for covering
```

### Materialized Views
```sql
-- Creating an efficient materialized view
CREATE MATERIALIZED VIEW mv_customer_summary AS
SELECT 
  customer_id,
  COUNT(*) as order_count,
  SUM(total_amount) as total_spent,
  MAX(order_date) as last_order_date
FROM orders
GROUP BY customer_id
WITH DATA;

-- Create unique index for efficient refreshes
CREATE UNIQUE INDEX idx_mv_customer_summary 
ON mv_customer_summary (customer_id);

-- Refresh strategy
REFRESH MATERIALIZED VIEW CONCURRENTLY mv_customer_summary;
```

### Common Performance Patterns

#### Before Optimization
```sql
-- Inefficient query
SELECT 
  p.product_name,
  COUNT(DISTINCT o.customer_id) as unique_customers,
  SUM(oi.quantity * oi.unit_price) as total_revenue
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
LEFT JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY p.product_id, p.product_name;
```

#### After Optimization
```sql
-- Optimized version
WITH order_metrics AS (
  SELECT 
    oi.product_id,
    COUNT(DISTINCT o.customer_id) as unique_customers,
    SUM(oi.quantity * oi.unit_price) as total_revenue
  FROM order_items oi
  JOIN orders o ON oi.order_id = o.order_id
  WHERE o.order_date >= CURRENT_DATE - INTERVAL '1 year'
  GROUP BY oi.product_id
)
SELECT 
  p.product_name,
  COALESCE(om.unique_customers, 0) as unique_customers,
  COALESCE(om.total_revenue, 0) as total_revenue
FROM products p
LEFT JOIN order_metrics om ON p.product_id = om.product_id;
```

### Best Practices Checklist
1. Always analyze query plans with `EXPLAIN ANALYZE`
2. Design indexes based on query patterns
3. Consider materialized views for expensive calculations
4. Use CTEs for better readability and optimization
5. Minimize the number of joins when possible
6. Use covering indexes for frequent queries
7. Regularly update statistics with `ANALYZE`
8. Monitor and maintain materialized view refresh schedules


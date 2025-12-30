# 📊 2026 Analytics Challenge - Sample Datasets

This folder contains sample datasets for the 2026 Analytics Challenge. These datasets are designed to help you practice SQL, Pandas, and statistical analysis without the friction of finding or downloading external data.

## 📁 Dataset Inventory

| File | Description | Use In |
|------|-------------|--------|
| `customers.csv` | Customer master data with signup dates | Week 1, Week 2 |
| `orders.csv` | Order transactions with dates and amounts | Week 1, Week 2, Week 5 |
| `products.csv` | Product catalog with categories and pricing | Week 1, Week 5, Week 7 |
| `order_items.csv` | Line-item details for orders | Week 1, Week 5, Week 7 |
| `users.csv` | Users with referral relationships (self-join practice) | Week 1 |
| `user_activity.csv` | User login/purchase events for cohort analysis | Week 2, Week 7 |
| `daily_metrics.csv` | Daily active users and engagement metrics | Week 2, Week 5, Week 6 |
| `monthly_revenue.csv` | Monthly aggregated revenue data | Week 2, Week 6 |

## 🚀 Quick Start

### Using DuckDB (Zero Setup - Recommended)

```python
import duckdb

# Load all tables into DuckDB
con = duckdb.connect()
con.execute("CREATE TABLE customers AS SELECT * FROM 'data/customers.csv'")
con.execute("CREATE TABLE orders AS SELECT * FROM 'data/orders.csv'")
con.execute("CREATE TABLE products AS SELECT * FROM 'data/products.csv'")

# Run SQL queries directly
result = con.execute("""
    SELECT c.name, COUNT(o.order_id) as order_count
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.name
    ORDER BY order_count DESC
""").fetchdf()
print(result)
```

### Using Pandas

```python
import pandas as pd

customers = pd.read_csv('data/customers.csv')
orders = pd.read_csv('data/orders.csv')
products = pd.read_csv('data/products.csv')

# Quick exploration
print(customers.info())
print(orders.describe())
```

### Using Polars (Week 5 Modern Track)

```python
import polars as pl

customers = pl.read_csv('data/customers.csv')
orders = pl.read_csv('data/orders.csv')

# Lazy evaluation for performance
result = (
    orders.lazy()
    .group_by('customer_id')
    .agg(pl.col('amount').sum().alias('total_revenue'))
    .collect()
)
print(result)
```

## 📋 Schema Details

### customers.csv
| Column | Type | Description |
|--------|------|-------------|
| customer_id | INT | Primary key |
| name | TEXT | Customer name |
| signup_date | DATE | Account creation date |
| email | TEXT | Email address |
| country | TEXT | Country of residence |

### orders.csv
| Column | Type | Description |
|--------|------|-------------|
| order_id | INT | Primary key |
| customer_id | INT | Foreign key to customers |
| order_date | DATE | Order placement date |
| amount | DECIMAL | Order total |
| status | TEXT | completed/cancelled/pending |

### products.csv
| Column | Type | Description |
|--------|------|-------------|
| product_id | INT | Primary key |
| product_name | TEXT | Product name |
| category | TEXT | Top-level category |
| subcategory | TEXT | Sub-category |
| unit_price | DECIMAL | List price |
| cost | DECIMAL | Product cost |

### order_items.csv
| Column | Type | Description |
|--------|------|-------------|
| order_item_id | INT | Primary key |
| order_id | INT | Foreign key to orders |
| product_id | INT | Foreign key to products |
| quantity | INT | Units ordered |
| unit_price | DECIMAL | Price at time of order |

### users.csv
| Column | Type | Description |
|--------|------|-------------|
| user_id | INT | Primary key |
| name | TEXT | User name |
| referred_by_user_id | INT | Self-referencing FK (nullable) |
| signup_date | DATE | Registration date |

### user_activity.csv
| Column | Type | Description |
|--------|------|-------------|
| user_id | INT | Foreign key to users |
| signup_date | DATE | User's signup date |
| activity_date | DATE | Date of activity |
| event_type | TEXT | login/purchase |

### daily_metrics.csv
| Column | Type | Description |
|--------|------|-------------|
| dt | DATE | Metric date |
| dau | INT | Daily active users |
| new_users | INT | New signups that day |
| returning_users | INT | Returning users that day |
| sessions | INT | Total sessions |
| avg_session_duration_sec | INT | Average session length |

### monthly_revenue.csv
| Column | Type | Description |
|--------|------|-------------|
| month | DATE | First day of month |
| revenue | DECIMAL | Total revenue |
| orders | INT | Order count |
| avg_order_value | DECIMAL | Average order value |
| new_customers | INT | New customer orders |
| returning_customers | INT | Returning customer orders |

## 🎯 Practice Problems by Dataset

### Week 1 (SQL Fundamentals)
- **customers + orders**: Find customers with 3+ orders in December
- **users**: Self-join to find referral chains
- **products + order_items**: Calculate revenue by category

### Week 2 (Window Functions)
- **daily_metrics**: 7-day rolling average of DAU
- **orders**: Rank customers by spending
- **user_activity**: Build a cohort retention matrix

### Week 5 (Pandas/Polars)
- **orders**: Clean and explore, handle edge cases
- **order_items + products**: Merge and analyze margins
- **daily_metrics**: Visualize trends over time

### Week 7 (Analytical Engineering)
- Build a staging → mart pipeline with these tables
- Create data quality tests
- Handle date spine for missing days

## 🔗 External Datasets

For the capstone project (Week 8) and additional practice, consider these public datasets:

- [Inside Airbnb](http://insideairbnb.com/get-the-data/) - NYC listings
- [UCI Online Retail II](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II) - E-commerce transactions
- [Google BigQuery Public Datasets](https://cloud.google.com/bigquery/public-data) - Various large datasets
- [Kaggle Datasets](https://www.kaggle.com/datasets) - Thousands of options

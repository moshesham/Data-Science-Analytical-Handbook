# Cohort Analysis Project

This folder hosts a hands-on cohort analysis project aligned with **Week 2** of the [2026 Analytics Challenge](../../supplementary/2026-new-year-challenge.md).

## 🎯 Learning Objectives

By completing this project, you will be able to:
- Define user cohorts based on signup date or first action
- Calculate retention rates across time periods (D1, D7, D30, monthly)
- Build cohort retention matrices using SQL window functions
- Create retention heatmap visualizations
- Interpret retention curves to identify product/feature issues

## 📂 Project Contents

| File | Description |
|------|-------------|
| `Cohort_Analysis.ipynb` | Main analysis notebook (in progress) |
| `data/` | User activity data for analysis |
| `README.md` | This file |

## 🔧 Skills Practiced

- **SQL:** Window functions (ROW_NUMBER, LAG), date arithmetic, cohort labeling
- **Python:** Pandas pivot tables, groupby, Seaborn heatmaps
- **Product Sense:** Understanding what retention means for different product types
- **Visualization:** Creating publication-quality retention heatmaps

## 📊 Free Dataset Suggestions

| Dataset | Description | Link |
|---------|-------------|------|
| UCI Online Retail II | Invoice-level e-commerce data with customer IDs | [UCI ML](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II) |
| Brazilian E-Commerce (Olist) | Orders with customer IDs and timestamps | [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| Challenge Sample Data | User activity data included with the 2026 challenge | [Local](../../supplementary/challenge-2026/data/user_activity.csv) |

## 🚀 Getting Started

1. **Load the sample data** from `../../supplementary/challenge-2026/data/user_activity.csv`
2. **Define cohorts:** Group users by their signup month
3. **Calculate retention:** For each cohort, what % were active in month 1, 2, 3...?
4. **Visualize:** Create a heatmap where rows = cohorts, columns = months since signup

## 📈 Example SQL (Cohort Retention Matrix)

```sql
WITH cohorts AS (
  SELECT 
    user_id,
    DATE_TRUNC('month', signup_date) AS cohort_month
  FROM user_activity
  GROUP BY user_id, DATE_TRUNC('month', signup_date)
),
activity AS (
  SELECT 
    user_id,
    DATE_TRUNC('month', activity_date) AS activity_month
  FROM user_activity
  GROUP BY user_id, DATE_TRUNC('month', activity_date)
)
SELECT 
  cohort_month,
  EXTRACT(MONTH FROM AGE(activity_month, cohort_month)) AS month_number,
  COUNT(DISTINCT c.user_id) AS active_users
FROM cohorts c
JOIN activity a ON c.user_id = a.user_id
GROUP BY cohort_month, month_number
ORDER BY cohort_month, month_number;
```

## 🆕 2026 Enhancements

This project now includes:
- **Visual SQL:** Immediately visualize window function outputs
- **Polars comparison:** See how to build cohorts in Polars vs Pandas
- **Interpretation guide:** Common retention patterns and what they mean

## 📖 Related Resources

- [2026 Analytics Challenge - Week 2](../../supplementary/2026-new-year-challenge.md#week-2-sql-mastery--window-functions--ctes)
- [Advanced SQL Patterns](../../supplementary/Advanced-SQL-Patterns+Techniques.md)

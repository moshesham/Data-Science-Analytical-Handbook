# Customer Churn Project

This folder hosts a customer churn prediction project aligned with **Week 5-6** of the [2026 Analytics Challenge](../../supplementary/2026-new-year-challenge.md).

## 🎯 Learning Objectives

By completing this project, you will be able to:
- Perform exploratory data analysis on customer behavior data
- Engineer features that predict churn (usage patterns, tenure, demographics)
- Build and evaluate classification models (logistic regression, tree-based models)
- Interpret model results and communicate actionable insights
- Understand ethical considerations in churn prediction

## 📂 Project Contents

| File | Description |
|------|-------------|
| `Customer_Churn.ipynb` | Main analysis notebook (in progress) |
| `data/` | Customer data with churn labels |
| `README.md` | This file |

## 🔧 Skills Practiced

- **Python/Pandas:** Data cleaning, feature engineering, EDA
- **Machine Learning:** Classification, model evaluation (AUC, precision, recall)
- **Statistics:** Understanding feature importance, correlation analysis
- **Product Sense:** Translating model outputs to business recommendations
- **Ethics:** Considering bias and fairness in churn models

## 📊 Free Dataset Suggestions

| Dataset | Description | Link |
|---------|-------------|------|
| IBM Telco Customer Churn | Classic churn dataset with demographics and usage | [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) |
| Cell2Cell Churn | Larger dataset with more features | [Kaggle](https://www.kaggle.com/datasets/ktisha/cell2cell) |

## 🚀 Getting Started

1. **Download the IBM Telco dataset** from Kaggle
2. **Explore the data:** What features are available? What's the churn rate?
3. **Feature engineering:** Create tenure buckets, usage ratios, etc.
4. **Build models:** Start with logistic regression, then try Random Forest
5. **Evaluate:** Use AUC, precision-recall curves, confusion matrix
6. **Interpret:** Which features matter most? What can the business do?

## 💡 Key Questions to Answer

1. What is the overall churn rate? Is the data imbalanced?
2. Which customer segments have the highest churn risk?
3. What are the top 5 predictors of churn?
4. If we could only intervene with 10% of at-risk customers, who should we target?
5. What interventions would you recommend based on the analysis?

## 🆕 2026 Enhancements

This project now includes:
- **Polars comparison:** Build the same EDA pipeline in both Pandas and Polars
- **AI-assisted interpretation:** Use LLMs to help explain model coefficients
- **Ethical considerations:** Discussion of bias in churn models

## 📖 Related Resources

- [2026 Analytics Challenge - Week 5](../../supplementary/2026-new-year-challenge.md#week-5-python-pandas--polars-for-analysis)
- [2026 Analytics Challenge - Week 6](../../supplementary/2026-new-year-challenge.md#week-6-product-metrics--case-studies)

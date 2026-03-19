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
| `Customer_Churn.ipynb` | Complete end-to-end analysis notebook (9 sections) |
| `data/` | Auto-created on first run; caches the downloaded CSV |
| `README.md` | This file |

## 📓 What's in the Notebook

| Section | Content |
|---------|---------|
| **0. Setup & Data Loading** | Auto-downloads IBM Telco CSV from GitHub; falls back to realistic synthetic data |
| **1. Data Cleaning** | Fix `TotalCharges` dtype, drop `customerID`, encode target |
| **2. EDA** | 6 charts: churn distribution, tenure, monthly charges, contract type, internet service, correlation heatmap |
| **3. Feature Engineering** | 30+ features: binary encoding, NumServices, HasFullProtection, ChargePerService, TenureBucket, one-hot encoding |
| **4. Model Building** | 3 pipelines: Logistic Regression, Random Forest, Gradient Boosting |
| **5. Evaluation & Threshold Tuning** | ROC + PR curves, confusion matrix, optimal F1 threshold |
| **6. Feature Importance** | Built-in MDI importance + permutation importance on validation set |
| **7. Risk Scoring & ROI** | Customer risk tiers (Low/Medium/High) + retention campaign ROI model |
| **8. Business Recommendations** | Executive summary, key findings, interventions, ethics, next steps |
| **9. Polars Comparison** | Same EDA in Polars with side-by-side code + Lazy API example |

## 🚀 Quick Results Preview

Typical performance on the IBM Telco dataset (may vary slightly):

| Model | ROC AUC | PR AUC | F1 (optimal threshold) |
|-------|---------|--------|------------------------|
| Logistic Regression | ~0.84 | ~0.63 | ~0.62 |
| Random Forest | ~0.84 | ~0.65 | ~0.63 |
| Gradient Boosting | ~0.84 | ~0.64 | ~0.62 |

## 🔧 Skills Practiced

- **Python/Pandas:** Data cleaning, feature engineering, EDA
- **Machine Learning:** Classification, model evaluation (AUC, precision, recall)
- **Statistics:** Understanding feature importance, correlation analysis
- **Product Sense:** Translating model outputs to business recommendations
- **Ethics:** Considering bias and fairness in churn models

## 📊 Dataset

The notebook **automatically** tries to download the IBM Telco Customer Churn CSV from a public GitHub mirror:

```
https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv
```

If the download fails (no internet, firewall, etc.) it falls back to a **statistically representative synthetic dataset** with the same 21-column schema, ~7 043 rows, and ~26.5% churn rate — so you can run the full notebook offline with realistic results.

| Dataset | Description | Link |
|---------|-------------|------|
| IBM Telco Customer Churn | Classic dataset — auto-downloaded by notebook | [Kaggle mirror](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) |
| Cell2Cell Churn | Larger dataset for further challenge | [Kaggle](https://www.kaggle.com/datasets/ktisha/cell2cell) |

## 🚀 Getting Started

1. **Open the notebook** — `Customer_Churn.ipynb`
2. **Run all cells** — data loads automatically (no manual download needed)
3. **Follow the sections** in order; each builds on the previous
4. **Answer the challenge questions** at the end of the notebook

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

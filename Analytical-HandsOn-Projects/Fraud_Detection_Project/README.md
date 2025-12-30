# Fraud Detection Project

This folder hosts a fraud detection project aligned with the [2026 Analytics Challenge](../../supplementary/2026-new-year-challenge.md).

## 🎯 Learning Objectives

By completing this project, you will be able to:
- Handle severely imbalanced classification problems
- Engineer features from transaction data (aggregates, velocity, ratios)
- Build and tune tree-based models for fraud detection
- Evaluate models using appropriate metrics (PR-AUC, recall@k)
- Understand the business trade-off between false positives and false negatives

## 📂 Project Contents

| File | Description |
|------|-------------|
| `Fraud_Detection.ipynb` | Main analysis notebook (in progress) |
| `data/` | Anonymized transaction data |
| `README.md` | This file |

## 🔧 Skills Practiced

- **Python:** Pandas, scikit-learn, imbalanced-learn
- **Machine Learning:** Class imbalance handling (SMOTE, class weights, threshold tuning)
- **Statistics:** Precision-recall trade-offs, AUC interpretation
- **Business Sense:** Cost-benefit analysis of fraud detection thresholds

## 📊 Free Dataset Suggestions

| Dataset | Description | Link |
|---------|-------------|------|
| Credit Card Fraud | 284k transactions, 492 frauds (~0.17%) | [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) |
| IEEE-CIS Fraud | Richer feature set, larger dataset | [Kaggle](https://www.kaggle.com/c/ieee-fraud-detection/data) |

## 🚀 Getting Started

1. **Download the Credit Card Fraud dataset** (it's anonymized PCA features)
2. **Explore the imbalance:** What % of transactions are fraudulent?
3. **Engineer features:** Time-based aggregates, rolling statistics
4. **Handle imbalance:** Try SMOTE, undersampling, class weights
5. **Build models:** Random Forest, XGBoost, or LightGBM
6. **Tune thresholds:** Optimize for business costs, not just accuracy

## 💡 Key Questions to Answer

1. At what threshold do we catch 90% of fraud? What's the false positive rate?
2. If each false positive costs $10 to investigate and each missed fraud costs $500, what's the optimal threshold?
3. Which features are most predictive of fraud?
4. How would you monitor this model in production?

## 📈 Example: Precision-Recall Analysis

```python
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

# Get predictions
y_scores = model.predict_proba(X_test)[:, 1]

# Calculate precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_test, y_scores)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(recall, precision, linewidth=2)
plt.xlabel('Recall (Fraud Detection Rate)')
plt.ylabel('Precision (% of flagged that are fraud)')
plt.title('Precision-Recall Curve: Fraud Detection')
plt.axhline(y=0.5, color='r', linestyle='--', label='50% Precision')
plt.axvline(x=0.9, color='g', linestyle='--', label='90% Recall')
plt.legend()
```

## 🆕 2026 Enhancements

This project now includes:
- **Cost-benefit analysis framework:** Calculate optimal threshold based on business costs
- **Production monitoring guide:** How to detect model drift
- **Ethical considerations:** Fairness in fraud detection

## 📖 Related Resources

- [2026 Analytics Challenge](../../supplementary/2026-new-year-challenge.md)
- [Statistics Cheat Sheet](../../supplementary/statistics-cheat-sheet.md)

# Fraud Detection Project (Placeholder)

Detect anomalous or fraudulent transactions.

## Planned contents
- Notebook: class imbalance handling, feature engineering (aggregates, ratios), model (tree/boosting), evaluation (PR AUC, ROC, recall@k)
- Data: anonymized transactions under `data/`
- Plots: precision-recall, feature importance, threshold vs recall
- Guardrails: false-positive cost considerations

## Free dataset suggestions
- [Credit Card Fraud (Kaggle)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) — anonymized transactions with severe class imbalance
- [IEEE-CIS Fraud (Kaggle)](https://www.kaggle.com/c/ieee-fraud-detection/data) — richer feature set (larger; can downsample)

## Next steps
1) Add dataset to `data/` (e.g., transactions with labels 0/1 and numeric/categorical features).
2) Create `Fraud_Detection.ipynb` with modeling and threshold tuning.
3) Export via CI to `notebooks_md/Fraud_Detection_Project/` (auto from workflow).

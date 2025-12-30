# A/B Testing Project

This folder hosts an end-to-end A/B testing project aligned with **Week 4** of the [2026 Analytics Challenge](../../supplementary/2026-new-year-challenge.md).

## 🎯 Learning Objectives

By completing this project, you will be able to:
- Design a complete experiment with hypothesis, metrics, and sample size calculation
- Analyze A/B test results including lift, confidence intervals, and p-values
- Detect Sample Ratio Mismatch (SRM) using chi-squared tests
- Navigate trade-offs when success metrics and guardrails conflict
- **New for 2026:** Understand when to use Multi-Armed Bandits vs traditional A/B tests

## 📂 Project Contents

| File | Description |
|------|-------------|
| `AB_Test.ipynb` | Main analysis notebook (in progress) |
| `data/` | Synthetic or anonymized test data |
| `README.md` | This file |

## 🔧 Skills Practiced

- **Statistics:** Power analysis, sample size calculation, hypothesis testing
- **Python:** scipy.stats, pandas, visualization with matplotlib/seaborn
- **Product Sense:** Defining success/guardrail metrics, interpreting edge cases
- **Communication:** Presenting go/no-go recommendations to stakeholders

## 📊 Free Dataset Suggestions

| Dataset | Description | Link |
|---------|-------------|------|
| Cookie Cats A/B Test | Mobile game level gate test (retention) | [Kaggle](https://www.kaggle.com/datasets/erikbruin/cookie-cats) |
| Udacity A/B Test | Enrollment funnel conversion test | [Kaggle](https://www.kaggle.com/datasets/zhangluyuan/ab-testing) |

## 🚀 Getting Started

1. **Download a dataset** from the suggestions above or use synthetic data
2. **Open the notebook** in Jupyter or Google Colab
3. **Follow the analysis framework:**
   - Hypothesis formulation
   - Sample size calculation
   - Data validation (check for SRM)
   - Statistical testing
   - Guardrail analysis
   - Recommendation

## 🆕 2026 Enhancements

This project now includes:
- **Multi-Armed Bandit comparison:** When to use MAB vs A/B
- **Peeking simulation:** Visualize why early stopping inflates false positives
- **AI-augmented design review:** Use LLMs to critique your experiment design

## 📖 Related Resources

- [2026 Analytics Challenge - Week 4](../../supplementary/2026-new-year-challenge.md#week-4-ab-testing--experimentation)
- [Statistics Cheat Sheet](../../supplementary/statistics-cheat-sheet.md)
- [Trustworthy Online Experiments (Book)](https://www.goodreads.com/book/show/48570077-trustworthy-online-controlled-experiments)

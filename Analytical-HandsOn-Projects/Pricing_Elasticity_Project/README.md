# Pricing Elasticity Project

This folder hosts a pricing elasticity analysis project aligned with the [2026 Analytics Challenge](../../supplementary/2026-new-year-challenge.md) capstone.

## 🎯 Learning Objectives

By completing this project, you will be able to:
- Estimate price elasticity of demand using regression analysis
- Understand and calculate cross-price elasticity
- Build demand curves and simulate revenue impact of price changes
- Account for confounding variables (promotions, seasonality, competition)
- Communicate pricing recommendations to business stakeholders

## 📂 Project Contents

| File | Description |
|------|-------------|
| `Pricing_Elasticity.ipynb` | Main analysis notebook (in progress) |
| `data/` | Historical price and sales data |
| `README.md` | This file |

## 🔧 Skills Practiced

- **Statistics:** Regression analysis, log-log models, causal inference basics
- **Python:** Pandas, statsmodels, scikit-learn
- **Visualization:** Demand curves, revenue surfaces, elasticity comparisons
- **Business Sense:** Pricing strategy, revenue optimization

## 📊 Free Dataset Suggestions

| Dataset | Description | Link |
|---------|-------------|------|
| UCI Online Retail II | Quantity, unit price, timestamps | [UCI ML](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II) |
| Brazilian E-Commerce (Olist) | Prices, order items, categories | [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| Challenge Sample Data | Products with prices and costs | [Local](../../supplementary/challenge-2026/data/products.csv) |

## 🚀 Getting Started

1. **Load pricing data** with price, quantity, and ideally variation over time
2. **Explore correlations:** How does quantity change with price?
3. **Estimate elasticity:** Use log-log regression
4. **Control for confounders:** Add promotions, seasonality as controls
5. **Simulate scenarios:** What happens to revenue at different prices?

## 📈 Key Concepts

### Price Elasticity Formula

$$\text{Elasticity} = \frac{\% \Delta \text{Quantity}}{\% \Delta \text{Price}}$$

- **Elasticity > 1 (elastic):** Price increase reduces revenue
- **Elasticity < 1 (inelastic):** Price increase increases revenue
- **Elasticity = 1 (unit elastic):** Revenue unchanged

### Log-Log Regression for Elasticity

```python
import statsmodels.api as sm
import numpy as np

# Log-transform price and quantity
df['log_price'] = np.log(df['price'])
df['log_quantity'] = np.log(df['quantity'])

# Regression: log(Q) = α + β*log(P) + controls
X = df[['log_price', 'is_promotion', 'month']]
X = sm.add_constant(X)
y = df['log_quantity']

model = sm.OLS(y, X).fit()
print(model.summary())

# The coefficient on log_price IS the elasticity
elasticity = model.params['log_price']
print(f"Price Elasticity: {elasticity:.2f}")
```

## 💡 Key Questions to Answer

1. What is the price elasticity for different product categories?
2. Which products are most/least price sensitive?
3. If we raise prices by 10%, what's the expected revenue impact?
4. Are there segments (customer types, regions) with different elasticities?

## 🆕 2026 Enhancements

This project now includes:
- **Revenue simulation tool:** Interactive price-revenue scenario modeling
- **Cross-elasticity analysis:** How does changing Product A's price affect Product B's sales?
- **AI-assisted interpretation:** Use LLMs to explain elasticity to non-technical stakeholders

## 📖 Related Resources

- [2026 Analytics Challenge - Week 6](../../supplementary/2026-new-year-challenge.md#week-6-product-metrics--case-studies)
- [Statistics Cheat Sheet](../../supplementary/statistics-cheat-sheet.md)

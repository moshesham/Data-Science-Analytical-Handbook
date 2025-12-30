# Demand Forecasting Project

This folder hosts a demand forecasting project aligned with the [2026 Analytics Challenge](../../supplementary/2026-new-year-challenge.md) capstone.

## 🎯 Learning Objectives

By completing this project, you will be able to:
- Analyze time series data for trends, seasonality, and anomalies
- Engineer features for forecasting (lags, rolling averages, calendar events)
- Build and compare forecasting models (ARIMA, Prophet, LightGBM)
- Evaluate forecast accuracy using appropriate metrics (MAPE, RMSE)
- Translate forecasts into inventory/supply chain recommendations

## 📂 Project Contents

| File | Description |
|------|-------------|
| `Demand_Forecasting.ipynb` | Main analysis notebook (in progress) |
| `data/` | Historical sales/demand data |
| `README.md` | This file |

## 🔧 Skills Practiced

- **Python:** Pandas time series, statsmodels, Prophet, scikit-learn
- **Statistics:** Time series decomposition, stationarity testing
- **Visualization:** Trend lines, seasonality plots, forecast intervals
- **Business Sense:** Inventory optimization, safety stock calculations

## 📊 Free Dataset Suggestions

| Dataset | Description | Link |
|---------|-------------|------|
| Store Item Demand | 5-year daily store-item sales | [Kaggle](https://www.kaggle.com/c/demand-forecasting-kernels-only/data) |
| M5 Forecasting | Walmart daily unit sales with calendar | [Kaggle](https://www.kaggle.com/competitions/m5-forecasting-accuracy/data) |
| Rossmann Stores | European drug store sales | [Kaggle](https://www.kaggle.com/c/rossmann-store-sales/data) |

## 🚀 Getting Started

1. **Download a dataset** from the suggestions above
2. **Explore the time series:** Plot trends, check for seasonality
3. **Decompose:** Use STL or classical decomposition
4. **Build baseline:** Simple moving average or naive forecast
5. **Build models:** Compare ARIMA, Prophet, and ML approaches
6. **Evaluate:** Use time-based cross-validation, not random splits!

## 📈 Example: Seasonality Decomposition

```python
from statsmodels.tsa.seasonal import STL
import matplotlib.pyplot as plt

# Decompose time series
stl = STL(df['sales'], period=7)  # Weekly seasonality
result = stl.fit()

# Plot components
fig, axes = plt.subplots(4, 1, figsize=(12, 10))
result.observed.plot(ax=axes[0], title='Observed')
result.trend.plot(ax=axes[1], title='Trend')
result.seasonal.plot(ax=axes[2], title='Seasonal')
result.resid.plot(ax=axes[3], title='Residual')
plt.tight_layout()
```

## 🆕 2026 Enhancements

This project now includes:
- **Polars for data prep:** Fast data loading and aggregation
- **AI-assisted feature ideas:** Use LLMs to brainstorm calendar/event features
- **Business recommendations:** Template for presenting to stakeholders

## 📖 Related Resources

- [2026 Analytics Challenge - Week 8 Capstone](../../supplementary/2026-new-year-challenge.md#week-8-capstone--storytelling)
- [Statistics Cheat Sheet](../../supplementary/statistics-cheat-sheet.md)

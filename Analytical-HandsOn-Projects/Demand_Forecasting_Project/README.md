# Demand Forecasting Project (Placeholder)

Forecast weekly demand for a retail/product line.

## Planned contents
- Notebook: ingestion, EDA, feature engineering (seasonality/holidays), baseline vs ML forecast (ARIMA/Prophet/LightGBM)
- Data: sample weekly sales CSV under `data/`
- Plots: seasonality decomposition, accuracy metrics, forecast horizon charts
- Business readout: inventory/supply implications

## Free dataset suggestions
- [Store Item Demand Forecasting (Kaggle)](https://www.kaggle.com/c/demand-forecasting-kernels-only/data) — 5-year daily store-item sales
- [M5 Forecasting (Kaggle)](https://www.kaggle.com/competitions/m5-forecasting-accuracy/data) — Walmart daily unit sales with calendar/events

## Next steps
1) Add dataset to `data/` (e.g., weekly sales with store, sku, date, units).
2) Create `Demand_Forecasting.ipynb` covering EDA, model comparison, backtesting.
3) Export via CI to `notebooks_md/Demand_Forecasting_Project/` (auto from workflow).

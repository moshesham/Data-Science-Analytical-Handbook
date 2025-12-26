# Pricing Elasticity Project (Placeholder)

Estimate price elasticity and simulate revenue impact.

## Planned contents
- Notebook: data prep, elasticity estimation (log-log regression), cross-elasticity, scenario simulation
- Data: historical price/units promotions under `data/`
- Plots: demand curves, elasticity vs category, revenue surfaces
- Business readout: recommended price moves and risks

## Free dataset suggestions
- [UCI Online Retail II](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II) — includes quantity, unit price, timestamps
- [Brazilian E-Commerce (Olist) on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — prices, order items, categories

## Next steps
1) Add dataset to `data/` (price, units, promos, category, date) in `data/`.
2) Create `Pricing_Elasticity.ipynb` with modeling + scenarios.
3) Export via CI to `notebooks_md/Pricing_Elasticity_Project/` (auto from workflow).

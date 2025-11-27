# Streamlit Product Analytics App

This directory contains an interactive Streamlit application for exploring product analytics concepts covered in the handbook.

## About

This app is a companion tool to the Data Science Analytical Handbook, providing interactive simulations and visualizations for:
- Statistical concepts
- A/B testing scenarios
- Data distributions
- Product metrics analysis

## Running the App

This app is **not part of the Jekyll site** and must be run separately.

### Prerequisites

```bash
pip install -r Product_Analytics/requirements.txt
```

### Launch

```bash
cd streamlit_app/Product_Analytics
streamlit run streamlit_app.py
```

The app will open in your default web browser at `http://localhost:8501`

## Note

The Streamlit app is excluded from the Jekyll build process (see `_config.yml`). It's designed to be run locally or deployed separately if needed.

## Deployment (Optional)

To deploy this app to Streamlit Cloud:
1. Create a Streamlit Cloud account at https://streamlit.io/cloud
2. Connect your GitHub repository
3. Point to `streamlit_app/Product_Analytics/streamlit_app.py` as the main file
4. Deploy!

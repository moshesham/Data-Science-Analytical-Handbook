# main.py
import streamlit as st
from st_pages import Page, show_pages



# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("streamlit_app/Product_Analytics/pages/home.py", "Home", "🏠"),
        Page("streamlit_app/Product_Analytics/pages/2_probability.py", "Probability Overview", "📊"),
        Page("streamlit_app/Product_Analytics/pages/2_1_Combinatorics.py", "Combinatorics", "🧮"),
        Page("streamlit_app/Product_Analytics/pages/3_descriptive_statistics.py", "Descriptive Statistics", "📊"),
        Page("streamlit_app/Product_Analytics/pages/4_data_visualization.py", "Data Visualization", "📊"),
        Page("streamlit_app/Product_Analytics/pages/5_hypothesis_testing.py", "Hypothesis Testing", "🤔"),
        Page("streamlit_app/Product_Analytics/pages/6_ab_testing.py", "A/B Testing", "🆎"),
        Page("streamlit_app/Product_Analytics/pages/7_survival_analysis.py", "Survival Analysis", "⏳"),


    ]
)

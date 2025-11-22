# Home.py
import streamlit as st
def main():
    # Header Section
    st.title("Welcome to the Product Analytics Handbook")
    st.write("This interactive platform is designed to help you learn and practice key concepts in product analytics. Use the navigation bar on the left to explore the various topics.")
    
    st.markdown("""
        ### Overview

        This handbook will guide you through key areas in product analytics, with focus on:

        **Fundamentals:**
            - **Probability:** Understand the basics of probability, including distributions and statistical inference.
            - **Descriptive Statistics:** Learn how to summarize and describe data using central tendency, dispersion, and other measures.
            - **Data Visualization:** Explore effective techniques for visualizing data to gain insights and communicate findings.
            - **Data Quality and Validation:** Understand the importance of data quality and how to ensure data accuracy.
            - **KRIs and KPIs Metrics:** Learn how to define, design, and implement effective Key Risk Indicators (KRIs) and Key Performance Indicators (KPIs).
            - **Effective Communication:** Learn how to effectively communicate data insights to stakeholders.

        **Advanced Topics:**
            - **Hypothesis Testing:** Learn how to design and conduct A/B tests and other hypothesis tests.
            - **Time Series Analysis:** Learn how to analyze data over time to identify trends and patterns.
            - **A/B Testing:** Explore the process of designing, running, and interpreting A/B tests for product optimization.

        **Applications:**
            - **Survival Analysis:** Understand how to analyze time-to-event data, such as customer churn.
            - **Churn Analysis:** Learn how to identify factors contributing to customer churn and develop strategies to reduce it.
            - **Marketing Analytics:** Understand how to analyze marketing campaigns and measure their effectiveness.
            - **Fraud Risk Analysis:** Learn how to use data to detect and prevent fraud.
            - **Supply Chain Analysis:** Explore how to optimize supply chain operations using data analysis.
            - **Economic Demand Forecasting:** Learn how to forecast demand for products and services.

        ### How to Use This Handbook

        1.  **Navigation:** Use the sidebar to navigate to different topics.
        2.  **Theory:** Each section starts with theoretical concepts to provide background.
        3.  **Interactive Demos:** Practice with interactive elements to better understand each concept.
        4.  **Real-world Applications:** Understand how these concepts are used in real product scenarios.

         ### Next Steps

        Begin exploring the various sections using the sidebar navigation. For the best flow start with `Data Fundamentals` page.
        """)
    
    st.markdown("## Getting Started")
    st.markdown("To begin your journey, navigate to the `Data Fundamentals` page. From there, continue through the different topics in order for the most comprehensive experience.")

    st.markdown("## About the Project")
    st.markdown("This project is designed to be an interactive platform for learning the key concepts of Product Analytics. It is meant to be an interactive learning tool with practical examples and real world applications to enhance your knowledge.")

    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
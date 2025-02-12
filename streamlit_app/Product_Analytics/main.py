# Home.py
import streamlit as st
def main():
    # Header Section
    st.title("Welcome to the Product Analytics Handbook")
    st.write("This interactive platform is designed to help you learn and practice key concepts in product analytics. Use the navigation bar on the left to explore the various topics.")
    
    st.markdown("""
        ### Overview

        This handbook will guide you through key areas in product analytics, with focus on:
            - **Statistics Fundamentals:** Understand descriptive statistics, distributions, and hypothesis testing.
            - **Visualization Techniques:** Learn how to effectively visualize data for exploratory analysis and communication.
            - **A/B Testing:** Explore the process of designing, running, and interpreting A/B tests.
            - **Data Analysis:** Learn how to apply core concepts for effective product analysis.

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
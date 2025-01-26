# main.py
import streamlit as st
from st_pages import Page, show_pages, add_page_title

# Add your main page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("streamlit_app/Product_Analytics/pages/home.py", "Home", "🏠"),
        Page("streamlit_app/Product_Analytics/pages/3_descriptive_statistics.py", "Descriptive Statistics", "📊"),
        Page("streamlit_app/Product_Analytics/pages/4_data_visualization.py", "Data Visualization", "📊"),
        Page("streamlit_app/Product_Analytics/pages/5_hypothesis_testing.py", "Hypothesis Testing", "🤔"),
        Page("streamlit_app/Product_Analytics/pages/6_ab_testing.py", "A/B Testing", "🆎"),
    ]
)


# Define the mapping between HTML section IDs and Streamlit page file names
# pages_config = [
#     {"type": "page", "file": "Home.py", "name": "Home", "icon": "🏠"},
#      # Foundational Skills
#     {"type": "section", "name": "Foundational Skills", "icon": "🧠"},
#     {"type": "page", "file": "pages/2_data_fundamentals.py", "name": "Data Fundamentals", "icon": "🗂️", "in_section": True},
#      {"type": "section", "name": "Statistics and Probability", "icon": "📊"},
#     {"type": "page", "file": "pages/2_1_statistics_probability.py", "name": "Statistics and Probability", "icon": "📊", "in_section": True},
#     {"type": "section", "name": "SQL and Data Manipulation", "icon": "🗄️"},
#     {"type": "page", "file": "pages/2_2_sql_data_manipulation.py", "name": "SQL and Data Manipulation", "icon": "🗄️", "in_section": True},
#    {"type": "section", "name": "Programming for Data Analysis", "icon": "🐍"},
#     {"type": "page", "file": "pages/2_3_programming_data_analysis.py", "name": "Programming for Data Analysis", "icon": "🐍", "in_section": True},
#     # Core Techniques
#     {"type": "section", "name": "Core Analysis Techniques", "icon": "📊"},
#       {"type": "page", "file": "pages/3_1_data_exploration.py", "name": "Data Exploration", "icon": "🔍", "in_section": True},
#       {"type": "page", "file": "pages/3_2_experimentation.py", "name": "Experimentation", "icon": "🧪", "in_section": True},
#     {"type": "page", "file": "pages/3_3_cohort_analysis.py", "name": "Cohort Analysis", "icon": "👥", "in_section": True},
#     {"type": "page", "file": "pages/3_4_segmentation.py", "name": "Segmentation", "icon": "🧩", "in_section": True},
#      {"type": "page", "file": "pages/3_5_funnel_analysis.py", "name": "Funnel Analysis", "icon": "🧮", "in_section": True},
#      {"type": "page", "file": "pages/3_6_time_series.py", "name": "Time Series Analysis", "icon": "⏳", "in_section": True},
#    # Communication and Presentation Skills
#     {"type": "section", "name": "Communication and Presentation", "icon": "🗣️"},
#      {"type": "page", "file": "pages/4_1_data_visualization.py", "name": "Data Visualization", "icon": "📊", "in_section": True},
#      {"type": "page", "file": "pages/4_2_storytelling_data.py", "name": "Storytelling with Data", "icon": "✍️", "in_section": True},
#      {"type": "page", "file": "pages/4_3_presentation_skills.py", "name": "Presentation Skills", "icon": "🎤", "in_section": True},
#     # Interview Practice
#     {"type": "section", "name": "Interview Practice", "icon": "🧑‍💻"},
#     {"type": "page", "file": "pages/5_1_technical_skills_interview.py", "name": "Technical Interviews", "icon": "💻", "in_section": True},
#      {"type": "page", "file": "pages/5_2_analytical_execution_interview.py", "name": "Analytical Interviews", "icon": "🤔", "in_section": True},
#     {"type": "page", "file": "pages/5_3_product_sense_interview.py", "name": "Product Sense Interviews", "icon": "💡", "in_section": True},
#       {"type": "page", "file": "pages/5_4_behavioral_interview.py", "name": "Behavioral Interviews", "icon": "🎭", "in_section": True},
#     # Resources
#     {"type": "section", "name": "Additional Resources and Practice", "icon": "📚"},
#      {"type": "page", "file": "pages/5_resources_practice.py", "name": "Resources and Practice", "icon": "📚", "in_section": True},
#     # Conclusion
#     {"type": "section", "name": "Conclusion", "icon": "🏁"},
#     {"type": "page", "file": "pages/7_conclusion.py", "name": "Conclusion", "icon": "🏁", "in_section": True},
#       #Appendix
#     {"type": "section", "name": "Appendix", "icon": "📝"},
#      {"type": "page", "file": "pages/8_1_glossary.py", "name": "Glossary of Terms", "icon": "📖", "in_section": True},
#     {"type": "page", "file": "pages/8_2_cheatsheets.py", "name": "Cheatsheets", "icon": "📑", "in_section": True}
# ]

# Generate Streamlit files with base style


# # Header Section
# st.title("Welcome to the Product Analytics Handbook")
# st.write("This interactive platform is designed to help you learn and practice key concepts in product analytics. Use the navigation bar on the left to explore the various topics.")

# st.markdown("""
#     ### Overview

#     This handbook will guide you through key areas in product analytics, with focus on:
#         - **Statistics Fundamentals:** Understand descriptive statistics, distributions, and hypothesis testing.
#         - **Visualization Techniques:** Learn how to effectively visualize data for exploratory analysis and communication.
#         - **A/B Testing:** Explore the process of designing, running, and interpreting A/B tests.
#         - **Data Analysis:** Learn how to apply core concepts for effective product analysis.

#     ### How to Use This Handbook

#     1.  **Navigation:** Use the sidebar to navigate to different topics.
#     2.  **Theory:** Each section starts with theoretical concepts to provide background.
#     3.  **Interactive Demos:** Practice with interactive elements to better understand each concept.
#     4.  **Real-world Applications:** Understand how these concepts are used in real product scenarios.

#       ### Next Steps

#     Begin exploring the various sections using the sidebar navigation. For the best flow start with `Data Fundamentals` page.
#     """)

# st.markdown("## Getting Started")
# st.markdown("To begin your journey, navigate to the `Data Fundamentals` page. From there, continue through the different topics in order for the most comprehensive experience.")

# st.markdown("## About the Project")
# st.markdown("This project is designed to be an interactive platform for learning the key concepts of Product Analytics. It is meant to be an interactive learning tool with practical examples and real world applications to enhance your knowledge.")

# hide_streamlit_style = """
#     <style>
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     </style>
#     """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
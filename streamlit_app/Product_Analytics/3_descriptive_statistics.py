# pages/3_descriptive_statistics.py
import streamlit as st
import pandas as pd
import numpy as np

# from scipy import stats
# import seaborn as sns
import matplotlib.pyplot as plt
from utils import data_utils, stats_utils, viz_utils, style_utils  # Import utility functions

def main():
    # Page Configuration
    st.set_page_config(
        page_title="Descriptive Statistics",
        page_icon="📊",
        layout="wide"
    )

    # Header Section
    st.title("Descriptive Statistics")
    st.write("Explore the fundamentals of summarizing data using descriptive statistics. This section covers measures of central tendency, dispersion, percentiles, and data distributions.")

    # Theory Section
    with st.expander("📖 Theoretical Concepts"):
      st.markdown("""
        Descriptive statistics provide a concise summary of the main features of a dataset. Key concepts include measures of central tendency (mean, median, mode), measures of dispersion (range, variance, standard deviation, IQR), and percentiles. Understanding data distributions (histograms, skewness, kurtosis) is also crucial. These tools help you understand the spread and central tendency of your data.

        ### Measures of Central Tendency
        -   **Mean:** The average of all values. Sensitive to outliers. Formula: μ = Σx / n
        -   **Median:** The middle value when data is sorted. Robust to outliers.
        -   **Mode:** The most frequent value.

        ### Measures of Dispersion
        -   **Range:** The difference between the maximum and minimum values.
        -   **Variance:** Average squared deviation from the mean. Formula: σ² = Σ(x - μ)² / n
        -   **Standard Deviation:** Square root of the variance. Formula: σ = √σ²
        -   **IQR:** Interquartile Range (Q3 - Q1), the range of the middle 50% of the data

        ### Percentiles and Quantiles
        -   **Percentiles:** Divide data into 100 equal parts.
        -   **Quantiles:** Divide data into equal parts (e.g., quartiles into 4).

        ### Data Distributions
        -   **Histograms:** Show the frequency distribution of data.
        -   **Skewness:** Measures asymmetry of the distribution
        -   **Kurtosis:** Measures the "tailedness" of the distribution.

        **Further Reading:**
        - [Descriptive Statistics (Wikipedia)](https://en.wikipedia.org/wiki/Descriptive_statistics)
        - [Measures of Central Tendency (Khan Academy)](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/a/mean-median-and-mode-review)
        - [Measures of Dispersion (Khan Academy)](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/a/calculating-standard-deviation-step-by-step)
         - [Percentiles (Wikipedia)](https://en.wikipedia.org/wiki/Percentile)
        """)


    # Interactive Demo Section
    st.header("🔄 Interactive Demo")
    st.write("Use the controls below to generate synthetic data and see how different statistical measures are calculated and visualized. Experiment with different data distributions and sample sizes to see their effect on key statistics and the resulting visualizations.")
    # Synthetic data generation (using utils)
    sample_size = st.slider("Sample Size", min_value=100, max_value=5000, value=1000, step=100,
                            help="Adjust the sample size to see how it affects the visualizations.")
    data_type = st.selectbox("Data Distribution", ["Normal", "Right-Skewed", "Left-Skewed"], index = 0,
                            help="Select the type of data distribution you want to generate.")
    comparison = st.checkbox("Compare Distributions", help="Enable to compare different data distributions against each other.")

    if st.button("Generate Data"):
        with st.spinner('Generating data and calculating statistics...'):
          if data_type == "Normal":
              data = data_utils.generate_normal_data(sample_size=sample_size)
          elif data_type == "Right-Skewed":
              data = data_utils.generate_right_skewed_data(sample_size=sample_size)
          elif data_type == "Left-Skewed":
              data = data_utils.generate_left_skewed_data(sample_size=sample_size)
          else:
              data = []
              st.error("Error: Unknown data type.")

          if data is not []:
              # Calculate and display descriptive statistics
              summary_data = stats_utils.calculate_descriptive_stats(data)
              st.subheader("Descriptive Statistics Table")
              st.write("Here's the table showing the descriptive statistics for the generated data.")
              st.dataframe(pd.DataFrame(summary_data, index = [data_type]).transpose().style.background_gradient(cmap='viridis', axis=1))
              st.write("Observe how different measures like Mean, Median, and Standard Deviation change based on the data type.")


              # Plotting histograms and boxplots
              if comparison:
                 data_sets_comparison = {
                    f"{data_type}": data,
                    "Normal": data_utils.generate_normal_data(sample_size=sample_size),
                    "Right-Skewed": data_utils.generate_right_skewed_data(sample_size=sample_size),
                     "Left-Skewed": data_utils.generate_left_skewed_data(sample_size=sample_size)
                 }

                 st.subheader("Data Distribution Comparison")
                 st.write("The following graphs compare the distribution for your data with a normal, right and left skewed distributions")
                 col1, col2 = st.columns(2)
                 with col1:
                    fig_hist = viz_utils.plot_multiple_histograms(data_sets_comparison, title="Histogram Comparison", xlabel="Value", ylabel="Frequency")
                    st.pyplot(fig_hist)
                    st.write("Histograms display the frequency of each value in the datasets. Observe how the shape of the histogram reflects the underlying distribution.")
                 with col2:
                     fig_box = viz_utils.plot_multiple_boxplots(data_sets_comparison, title="Boxplot Comparison", ylabel="Value")
                     st.pyplot(fig_box)
                     st.write("Boxplots summarize the distribution by showing the median (center line), quartiles (box edges), and outliers (points outside the whiskers).")


              else:
                st.subheader("Data Distribution Visualization")
                st.write("Here are the histogram and boxplot visualizations for the selected data type:")
                col1, col2 = st.columns(2)
                with col1:
                  fig_hist = viz_utils.plot_histogram(data, title=f"Histogram of {data_type} data", xlabel="Value", ylabel="Frequency")
                  st.pyplot(fig_hist)
                  st.write("The histogram shows the frequency distribution of the generated data. The shape, skewness, and spread of the data are important to note.")
                with col2:
                  fig_box = viz_utils.plot_boxplot(data, title=f"Boxplot of {data_type} data", ylabel="Value")
                  st.pyplot(fig_box)
                  st.write("The boxplot summarizes the data distribution by displaying the median, quartiles, and outliers.")

    # Practice Section
    st.header("💪 Practice Exercise")
    st.write("Calculate descriptive statistics for the given dataset. Use the data generation tool above to create a sample dataset and observe the statistics in the summary table.")
    exercise_data = st.text_area("Enter Data (Comma Separated)", value="10, 12, 15, 18, 20, 20, 25, 100",
                                help="Enter comma separated numerical values to calculate the descriptive statistics.")

    if st.button("Calculate Statistics for Exercise"):
        try:
             exercise_data = [float(x.strip()) for x in exercise_data.split(",")]
             exercise_summary = stats_utils.calculate_descriptive_stats(exercise_data)
             st.subheader("Exercise Output")
             st.write("Here are the descriptive statistics for the data you entered. Observe how these statistics relate to the provided visualization of a similar distribution.")
             st.dataframe(pd.DataFrame(exercise_summary, index = ["User Data"]).transpose().style.background_gradient(cmap='viridis', axis=1))
        except ValueError:
            st.error("Invalid input. Please enter comma-separated numbers.")
        except Exception as e:
            st.error(f"An error occurred: {e}")


    # Real-world Application
    st.header("🌍 Real-world Application")
    st.write("In product analytics, descriptive statistics are used to understand user engagement, identify trends, and detect anomalies. For example, calculating the mean session duration can help in understanding user behavior. The median is useful to understand the 'typical' user as it is less sensitive to extreme outliers. Standard deviation shows the variability in user engagement. Using the IQR can help us remove outliers to analyze only users in a given range of engagement.")

    # Knowledge Check
    st.header("✅ Knowledge Check")
    st.write("Test your understanding with the following quiz questions:")
    # Multiple Choice Quiz (radio buttons)
    st.subheader("Quiz: Multiple Choice")
    quiz_questions = [
        {
            "question": "Which measure is most affected by outliers?",
            "options": ["Mean", "Median", "Mode", "IQR"],
            "answer": "Mean"
        },
         {
            "question": "Which measure provides the range of the middle 50% of data?",
            "options": ["Standard Deviation", "Variance", "Range", "IQR"],
            "answer": "IQR"
        },
         {
           "question": "What measure indicates the spread of the data around the mean?",
           "options": ["Median", "Mode", "Variance", "Standard Deviation"],
            "answer": "Standard Deviation"
        }
    ]

    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i + 1}. {question['question']}**")
        user_answer = st.radio(f"Options for question {i+1}", options=question["options"], key=f"radio_{i}")

        if st.button(f"Check answer for {i+1}"):
             if user_answer == question["answer"]:
                st.success("Correct!")
             else:
                st.error(f"Incorrect. The correct answer is: {question['answer']}")

if __name__ == "__main__":
    main()
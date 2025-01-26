# pages/4_data_visualization.py
import streamlit as st
import pandas as pd
import numpy as np
from utils import data_utils, stats_utils, viz_utils, style_utils  # Import utility functions

def main():
    # Page Configuration
    st.set_page_config(
        page_title="Data Visualization",
        page_icon="📊",
        layout="wide"
    )

    # Header Section
    st.title("Data Visualization")
    st.write("Explore different data visualization techniques and their applications in product analytics.")


    # Theory Section
    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
        Data visualization is a critical component of effective data analysis. It allows for complex data to be represented in a digestible format. This section covers different visualization techniques and their applications in product analytics.

        ### Key Visualization Techniques
        - Histograms and Boxplots: to display data distribution.
        - Scatter plots with regression: to show correlations between numerical data.
        - Heatmaps: to show correlation matrices.
         - Density Plots: to show a smooth distribution of data

        **Further Reading:**
        - [Data Visualization (Wikipedia)](https://en.wikipedia.org/wiki/Data_visualization)
        - [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
        - [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

        """)


    # Interactive Demo Section
    st.header("🔄 Interactive Demo")
    st.write("Select the type of data visualization and explore it's different parameters.")

    viz_type = st.selectbox("Visualization Type", ["Histogram", "Boxplot", "Distribution Comparison", "Correlation Heatmap", "Scatter Plot with Regression", "Time Series Plot"], index=0,
                             help="Choose the type of visualization to explore.")

    if viz_type == "Histogram":
        st.subheader("Histogram Visualization")
        sample_size = st.slider("Sample Size", min_value=100, max_value=5000, value=1000, step=100, help="Set the sample size for the data.")
        data_type = st.selectbox("Data Distribution", ["Normal", "Right-Skewed", "Left-Skewed"], index = 0, help="Choose the type of distribution.")
        if st.button("Generate and Plot Histogram", help="Generate a histogram with the selected data type and sample size"):
           with st.spinner("Generating and plotting the data..."):
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
                    fig = viz_utils.plot_histogram(data, title = f"Histogram of {data_type} data")
                    st.pyplot(fig)
                    st.write("The histogram displays the distribution of a single dataset. The shape, skewness, and spread of the data are important to note.")

    elif viz_type == "Boxplot":
          st.subheader("Boxplot Visualization")
          sample_size = st.slider("Sample Size", min_value=100, max_value=5000, value=1000, step=100, help="Set the sample size for the data.")
          data_type = st.selectbox("Data Distribution", ["Normal", "Right-Skewed", "Left-Skewed"], index = 0, help="Choose the type of distribution.")
          if st.button("Generate and Plot Boxplot", help="Generate a boxplot with the selected data type and sample size."):
           with st.spinner("Generating and plotting the data..."):
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
                    fig = viz_utils.plot_boxplot(data, title=f"Boxplot of {data_type} data")
                    st.pyplot(fig)
                    st.write("The boxplot summarizes the data distribution by displaying the median, quartiles, and outliers.")

    elif viz_type == "Distribution Comparison":
        st.subheader("Distribution Comparison")
        sample_size = st.slider("Sample Size", min_value=100, max_value=5000, value=1000, step=100, help="Set the sample size for all the datasets used.")
        if st.button("Generate and Plot Distribution Comparison", help="Generate and compare the normal, right and left skewed distributions."):
             with st.spinner("Generating and plotting the data..."):
                  data_sets_comparison = {
                         "Normal": data_utils.generate_normal_data(sample_size=sample_size),
                         "Right-Skewed": data_utils.generate_right_skewed_data(sample_size=sample_size),
                          "Left-Skewed": data_utils.generate_left_skewed_data(sample_size=sample_size)
                     }
                  fig = viz_utils.plot_distribution_comparison(data_sets_comparison, title ="Distribution Comparison Plot")
                  st.pyplot(fig)
                  st.write("The density plot displays the estimated probability density of the different datasets.")
    elif viz_type == "Correlation Heatmap":
        st.subheader("Correlation Heatmap")
        st.write("Upload a CSV to generate a correlation heatmap. Ensure that numerical columns are present.")
        uploaded_file = st.file_uploader("Upload CSV", type=["csv"], help="Upload a CSV file with numerical data.")
        if uploaded_file is not None:
           try:
                df = pd.read_csv(uploaded_file)
                numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
                if not numerical_cols:
                    st.error("No numerical columns found in the uploaded CSV.")
                else:
                    annot = st.checkbox("Show Annotations", value=True, help="Check to display correlation values on the heatmap.")
                    corr_matrix = df[numerical_cols].corr()
                    fig = viz_utils.plot_correlation_heatmap(corr_matrix, title="Correlation Heatmap", annot = annot)
                    st.pyplot(fig)
                    st.write("The heatmap displays the correlation coefficients between different columns. Values close to 1 or -1 indicate strong positive or negative correlation, respectively. Values close to zero indicate little to no linear correlation.")
           except Exception as e:
                st.error(f"Error processing the file: {e}")

    elif viz_type == "Scatter Plot with Regression":
        st.subheader("Scatter Plot with Regression")
        st.write("Enter two comma separated lists of numerical values for X and Y below to visualize a scatter plot with a regression line.")
        x_values = st.text_area("Enter X Values (Comma Separated)", value="1,2,3,4,5",
                            help="Enter comma separated values for X.")
        y_values = st.text_area("Enter Y Values (Comma Separated)", value="2,4,1,3,5",
                            help="Enter comma separated values for Y.")
        if st.button("Generate and Plot Scatter", help="Generate a scatter plot with the given X and Y values."):
            try:
                  x = [float(x.strip()) for x in x_values.split(",")]
                  y = [float(y.strip()) for y in y_values.split(",")]

                  if len(x) != len(y):
                      st.error("The number of x values must match the number of y values.")
                  else:
                    fig = viz_utils.plot_scatter_with_regression(np.array(x), np.array(y),
                                                    title="Scatter Plot with Regression", xlabel="X Variable", ylabel="Y Variable")
                    st.pyplot(fig)
                    st.write("The scatter plot shows the relationship between X and Y variables. The line shows the linear regression between the two variables.")

            except ValueError:
                st.error("Invalid input. Please enter comma-separated numbers.")
            except Exception as e:
                 st.error(f"An error occured: {e}")
    elif viz_type == "Time Series Plot":
         st.subheader("Time Series Plot")
         periods = st.slider("Number of Periods", min_value=50, max_value=1000, value=365, step=50,
                                help="Set the number of periods (e.g., days) to generate.")
         trend = st.slider("Trend", min_value=-1.0, max_value=1.0, value = 0.1, step =0.1,
                           help="Set the trend component")
         seasonality_amplitude = st.slider("Seasonality Amplitude", min_value=0.0, max_value=50.0, value= 10.0, step = 5.0,
                           help="Set the seasonal component")
         noise_scale = st.slider("Noise Scale", min_value=0.0, max_value=20.0, value=5.0, step = 1.0,
                           help="Set the scale of random noise.")
         if st.button("Generate and Plot Time Series", help="Generate a time series plot with a specified trend, seasonality and noise"):
             with st.spinner("Generating and plotting time series data..."):
                time_series_df = data_utils.generate_time_series_data(periods=periods, trend = trend, seasonality_amplitude=seasonality_amplitude, noise_scale = noise_scale)

                fig, ax = plt.subplots()
                ax.plot(time_series_df['date'], time_series_df['value'])
                ax.set_title("Time Series Data")
                ax.set_xlabel("Date")
                ax.set_ylabel("Value")
                plt.xticks(rotation=45) # Rotate x-axis labels for better readability
                st.pyplot(fig)
                st.write("The time series plot shows the data points over time. Observe the trend, seasonality, and the noise. ")
    # Real-world Application
    st.header("🌍 Real-world Application")
    st.write("Data visualization is key for exploratory data analysis, identifying patterns, and communicating insights. Histograms and box plots can help you understand the distribution of a single variable, while scatter plots and correlation heatmaps show the relationships between two or more variables. Time series plots help visualize trends and seasonality in data over time.")



if __name__ == "__main__":
    main()
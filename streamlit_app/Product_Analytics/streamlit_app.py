import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from stats_utils import (
    calculate_mean,
    calculate_median,
    calculate_mode,
    calculate_variance,
    calculate_std_dev,
    plot_histogram
)

# --- DATA ACQUISITION ---
st.header("Data Acquisition")


# Use st.cache_data to cache the data loading and preprocessing
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df



uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = load_data(uploaded_file)  # Load data using the cached function
    st.write("### Raw Data")
    st.dataframe(df.head())

    # --- EXPLORATORY DATA ANALYSIS ---
    st.header("Exploratory Data Analysis")
    # Select a numeric column for analysis
    numeric_columns = df.select_dtypes(include=["number"]).columns
    selected_column = st.selectbox("Select a numeric column", numeric_columns)

    if selected_column:
        column_data = df[selected_column]

        # If a numeric column is selected, proceed with calculations and visualization
        df.dropna(subset=[selected_column], inplace=True)

        # --- CALCULATIONS ---
        st.subheader("Calculations")
        mean = calculate_mean(column_data)
        median = calculate_median(column_data)
        mode = calculate_mode(column_data)
        variance = calculate_variance(column_data)
        std_dev = calculate_std_dev(column_data)

        st.write(f"Mean: {mean}")
        st.write(f"Median: {median}")
        st.write(f"Mode: {mode}")
        st.write(f"Variance: {variance}")
        st.write(f"Standard Deviation: {std_dev}")

        # --- VISUALIZATION ---
        st.subheader("Visualization")

        # Plot a histogram
        fig = plot_histogram(column_data)
        st.pyplot(fig)

    # --- BAR CHART EXPLANATION ---
    st.header("Creating Bar Charts with Matplotlib")
    st.write(
        """
        Bar charts are used to compare different categories or groups of data.
        Here's an example of how to create a simple bar chart using Matplotlib:
        """
    )

    # Example Matplotlib code for a bar chart
    with st.echo():
        # Sample data
        categories = ['A', 'B', 'C', 'D']
        values = [10, 15, 7, 12]

        # Create the bar chart
        plt.figure()  # Create a new figure
        plt.bar(categories, values)

        # Add labels and title
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.title("Simple Bar Chart")

        # Show the plot
        st.pyplot(plt)
        plt.close()  # Close the figure to free memory

    # --- INTERACTIVE BAR CHART CREATION ---
    st.header("Interactive Bar Chart Creation")
    st.write("Experiment with the settings below to create your own bar chart:")

    # Data selection
    x_column = st.selectbox("Select X-axis column", df.columns)
    y_column = st.selectbox("Select Y-axis column", df.columns)

    # Chart type
    chart_type = st.selectbox("Select chart type", ["bar", "barh"])

    # Colors
    color = st.color_picker("Select bar color", "#1f77b4")

    # Labels and titles
    x_label = st.text_input("Enter X-axis label", x_column)
    y_label = st.text_input("Enter Y-axis label", y_column)
    title = st.text_input("Enter chart title", "Interactive Bar Chart")

    # Create the visualization
    try:
        # Create a new figure for the interactive chart
        plt.figure()

        # Get the data
        categories = df[x_column].tolist()
        values = df[y_column].tolist()

        # Create the bar chart
        if chart_type == "bar":
            plt.bar(categories, values, color=color)
        else:  # horizontal bar chart
            plt.barh(categories, values, color=color)

        # Add labels and title
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

        # Rotate x-axis labels if it's a vertical bar chart
        if chart_type == "bar":
            plt.xticks(rotation=45)

        # Display the plot in Streamlit
        st.pyplot(plt)

        # Close the figure to free memory
        plt.close()

    except Exception as e:
        st.error(f"Error creating chart: {str(e)}")
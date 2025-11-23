from io import StringIO
from typing import Optional

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# --- Helper Functions ---


def generate_example_data():
    np.random.seed(42)
    n = 1000
    data = pd.DataFrame(
        {
            "SessionDuration": np.random.randn(n),  # More descriptive names
            "PurchaseAmount": np.random.randn(n) * 2 + 1,
            "ProductRating": np.random.exponential(scale=2, size=n),
            "UserCategory": np.random.choice(["New", "Returning", "VIP"], size=n),
            "DeviceType": np.random.choice(["Mobile", "Desktop"], size=n),
            "Date": pd.date_range("2023-01-01", periods=n, freq="D"),
            "DailyClicks": np.cumsum(np.random.randn(n)) + 50,
            "UserGroup": np.random.choice(["GroupX", "GroupY", "GroupZ"], size=n),
            "ExperimentGroup": np.random.choice(["Control", "Treatment"], size=n),
        }
    )
    data["MarketingSpend"] = data["SessionDuration"] * 0.5 + np.random.randn(n) * 0.5
    return data


def load_data(data_source: str) -> Optional[pd.DataFrame]:
    """Loads data, handles errors, and returns None if loading fails."""
    if data_source == "Use Example Dataset":
        return generate_example_data()
    elif data_source == "Upload CSV":
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file)
                df.dropna(
                    subset=df.select_dtypes(include=np.number).columns, inplace=True
                )
                return df
            except Exception as e:
                st.error(f"Error reading CSV: {e}")
                return None
        return None
    elif data_source == "Paste CSV Data":
        csv_data = st.text_area("Paste your CSV data here:", height=200)
        if csv_data:
            try:
                df = pd.read_csv(StringIO(csv_data))
                df.dropna(
                    subset=df.select_dtypes(include=np.number).columns, inplace=True
                )
                return df
            except Exception as e:
                st.error(f"Error reading CSV data: {e}")
                return None
        return None
    return None


# --- Main Page Function ---


def data_visualization_page():
    st.set_page_config(page_title="Data Visualization", page_icon="📊", layout="wide")

    st.title("Data Visualization: Actionable Insights Through Visuals")
    st.write(
        "Master data visualization to explore, analyze, and communicate data effectively."
    )

    with st.expander("📖 Theoretical Concepts and Best Practices"):
        st.markdown(
            """
        (Same theoretical content as before - no changes needed here)
        ... (rest of the theory section, including the detailed table) ...
        """
        )
        st.markdown(
            """
                Effective data visualization transforms data into visual representations, revealing patterns and insights.

                **Guiding Principles:**

                1.  **Know Your Audience and Purpose:** Tailor visualizations to the audience and goal (exploration, presentation, etc.).
                2.  **Choose the Right Chart Type:**  Match the chart to the data and the message (see table below).
                3.  **Simplify:** Remove clutter. Every element should have a purpose.
                4.  **Use Color Strategically:** Highlight key data, use consistent schemes, and consider colorblindness.
                5.  **Label Clearly:** Axes, titles, legends, and data points (when appropriate) should be informative.
                6.  **Tell a Story:** Guide the viewer's eye. Use annotations and captions.
                7.  **Provide Context:** Include units, data sources, and relevant explanations.
                8. **Accessibility:** consider user with disabilities

                **Chart Types and Their Uses:**
                """
        )

        chart_types_data = {
            "Chart Type": [
                "Histogram",
                "Box Plot",
                "Density Plot",
                "Scatter Plot",
                "Line Chart",
                "Bar Chart",
                "Stacked Bar Chart",
                "Heatmap",
                "Violin Plot",
                "Pie Chart",
                "Area Chart",
                "Scatter Plot Matrix",
                "3D Scatter Plot",
                "Bubble Chart",
                "Funnel Chart",
            ],
            "Data Types": [
                "Numerical (Continuous or Discrete)",
                "Numerical, (Optional) Categorical",
                "Numerical (Continuous)",
                "Numerical (Two Variables)",
                "Time Series (Numerical vs. Time)",
                "Categorical, (Optional) Numerical",
                "Categorical, Numerical",
                "Numerical (Multiple), Categorical (2D Grid)",
                "Numerical, (Optional) Categorical",
                "Categorical (Proportions)",
                "Time Series (Numerical vs. Time)",
                "Numerical (Multiple)",
                "Numerical (Three Variables)",
                "Numerical (Three Variables), (Optional) Categorical",
                "Numerical (Sequential Stages)",
            ],
            "Best Use Cases in Product Analytics": [
                "Distribution of a *single* metric (session duration, purchase amount). Identify central tendency, spread, skewness, outliers.",
                "Compare distributions across groups (A/B tests, user segments).  Show median, quartiles, outliers.",
                "Smoothed distribution. Good for comparing shapes.",
                "Relationship between two metrics (marketing spend vs. new users). Identify correlations, clusters, outliers.",
                "Trends over time (daily active users, weekly revenue). Identify seasonality, overall trends, sudden changes.",
                "Compare values across categories (users per country, revenue per product).",
                "Show composition of a whole across categories (revenue breakdown by product category *and* region).",
                "Correlation matrix (relationships between metrics) OR values across a 2D grid (user activity by day/hour).",
                "Compare distributions across groups, showing more detail than box plots.",
                "Show parts of a whole. *Use sparingly*; bar charts are often better. Only use with few categories.",
                "Show cumulative values over time (total revenue, total users).",
                "Explore pairwise relationships between *multiple* numerical variables.",
                "Visualize the relationship between three numerical variables.",
                "Similar to a scatter plot, but adds a third dimension represented by the size of the bubbles. Useful for comparing three variables and group.",
                "Visualize the flow of users or items through a series of stages, identifying drop-off points.",
            ],
            "Code Example (Plotly)": [
                "`px.histogram(data, x='SessionDuration', nbins=50)`",
                "`px.box(data, x='UserCategory', y='DailyClicks')`",
                "`px.histogram(data, x='ProductRating', marginal='rug', histnorm='probability_density')`",
                "`px.scatter(data, x='MarketingSpend', y='PurchaseAmount', trendline='ols')`",
                "`px.line(data, x='Date', y='DailyClicks')`",
                "`px.bar(data, x='DeviceType', y='SessionDuration')`",
                "`px.bar(data, x='UserGroup', y='PurchaseAmount', color='DeviceType')`",
                "`px.imshow(data.corr(), text_auto=True)` OR `px.imshow(data[['Date', 'UserGroup', 'SessionDuration']].pivot('Date', 'UserGroup', 'SessionDuration'))`",  # Fixed example
                "`px.violin(data, x='ExperimentGroup', y='PurchaseAmount', box=True, points='all')`",
                "`px.pie(data, names='DeviceType', values='SessionDuration')`",
                "`px.area(data, x='Date', y='DailyClicks')`",  # Example - needs cumulative data
                "`px.scatter_matrix(data, dimensions=['SessionDuration', 'PurchaseAmount', 'ProductRating'])`",
                "`px.scatter_3d(data, x='SessionDuration', y='PurchaseAmount', z='ProductRating', color='UserCategory')`",
                "`px.scatter(data, x='SessionDuration', y='PurchaseAmount', size='ProductRating', color='UserCategory')`",
                "`data = dict(number=[1000, 800, 500, 200], stage=['Website Visits', 'Sign-ups', 'Trial Starts', 'Purchases']); fig = px.funnel(data, x='number', y='stage')`",
            ],
        }

        chart_types_df = pd.DataFrame(chart_types_data)
        st.dataframe(chart_types_df, use_container_width=True)
        st.markdown(
            """
        **Further Reading:** (Same excellent links, plus Plotly)
            *   [Data Visualization (Wikipedia)](https://en.wikipedia.org/wiki/Data_visualization)
            *   [Seaborn Documentation](https://seaborn.pydata.org/)
            *   [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
            *   [Fundamentals of Data Visualization by Claus Wilke](https://clauswilke.com/dataviz/)
            *   [The Visual Display of Quantitative Information by Edward Tufte](https://www.edwardtufte.com/tufte/books_vdqi)
            *   [Plotly Python Documentation](https://plotly.com/python/)
        """
        )

    st.header("🔄 Interactive Demo")
    st.write(
        "Select a visualization and explore its parameters. Use the example dataset or upload your own."
    )

    data_source = st.radio(
        "Data Source:",
        ["Use Example Dataset", "Upload CSV", "Paste CSV Data"],
        horizontal=True,
    )
    data = load_data(data_source)

    if data is None:
        st.info("Please select or upload data to continue.")
        st.stop()

    numerical_cols = data.select_dtypes(include=np.number).columns.tolist()
    if not numerical_cols:
        st.warning(
            "No numerical columns found. Many visualizations require numerical data."
        )

    viz_type = st.selectbox(
        "Visualization Type",
        [
            "Histogram",
            "Box Plot",
            "Density Plot",
            "Scatter Plot",
            "Line Chart",
            "Bar Chart",
            "Heatmap",
            "Violin Plot",
            "Scatter Plot Matrix",
            "3D Scatter Plot",
            "Bubble Chart",
            "Funnel Chart",
        ],
        index=0,
    )

    # --- Visualization Sections (using Plotly for interactivity) ---

    if viz_type == "Histogram":
        st.subheader("Histogram")
        col = st.selectbox("Select Column:", numerical_cols)
        nbins = st.slider(
            "Number of Bins:", min_value=5, max_value=100, value=30, step=5
        )
        show_density = st.checkbox("Show Density Curve (KDE)", value=False)

        # Unique key for the button
        if st.button("Plot Histogram", key="histogram_button"):
            fig = px.histogram(
                data,
                x=col,
                nbins=nbins,
                title=f"Histogram of {col}",
                marginal="rug" if not show_density else "box",
                opacity=0.7,
            )
            if show_density:
                fig.update_traces(histnorm="probability density")
            st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Box Plot":
        st.subheader("Box Plot")
        col = st.selectbox("Select Column:", numerical_cols)
        group_col = st.selectbox(
            "Group By (Optional):",
            ["None"] + list(data.select_dtypes(include="object").columns),
        )

        if st.button("Plot Box Plot", key="boxplot_button"):
            fig = px.box(
                data,
                x=group_col if group_col != "None" else None,
                y=col,
                title=f"Box Plot of {col}"
                + (f" by {group_col}" if group_col != "None" else ""),
                points="all",
            )
            st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Density Plot":
        st.subheader("Density Plot")
        col = st.selectbox("Select Column:", numerical_cols)
        if st.button("Plot Density Plot", key="density_button"):
            fig = px.histogram(
                data,
                x=col,
                title=f"Density Plot of {col}",
                marginal="rug",
                histnorm="probability density",
            )
            st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Scatter Plot":
        st.subheader("Scatter Plot")
        if len(numerical_cols) < 2:
            st.error("At least two numerical columns are required.")
        else:
            x_col = st.selectbox("Select X-axis Column:", numerical_cols, index=0)
            y_col = st.selectbox(
                "Select Y-axis Column:",
                numerical_cols,
                index=1 if len(numerical_cols) > 1 else 0,
            )
            color_col = st.selectbox(
                "Color by (Optional):", ["None"] + list(data.columns), index=0
            )
            trendline = st.selectbox("Trendline:", ["None", "ols", "lowess"])

            if st.button("Plot Scatter Plot", key="scatter_button"):
                fig = px.scatter(
                    data,
                    x=x_col,
                    y=y_col,
                    color=color_col if color_col != "None" else None,
                    title=f"Scatter Plot of {x_col} vs. {y_col}",
                    trendline=trendline if trendline != "None" else None,
                    opacity=0.7,
                )
                st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Line Chart":
        st.subheader("Line Chart")
        date_cols = data.select_dtypes(
            include=["datetime", "datetimetz"]
        ).columns.tolist()
        if not date_cols:
            st.error("No date/time column found.")
        else:
            time_col = st.selectbox("Select Time Column:", date_cols)
            value_col = st.selectbox("Select Value Column:", numerical_cols)
            agg_func = st.selectbox(
                "Aggregation Function:", ["sum", "mean", "median", "count"], index=0
            )
            if st.button("Plot Line Chart", key="line_button"):
                plot_data = (
                    data.groupby(time_col)[value_col].agg(agg_func).reset_index()
                )
                plot_data = plot_data.sort_values(by=time_col)
                fig = px.line(
                    plot_data,
                    x=time_col,
                    y=value_col,
                    title=f"Line Chart of {value_col} over Time",
                )
                st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Bar Chart":
        st.subheader("Bar Chart")
        cat_cols = st.multiselect(
            "Select Category Column(s):", data.select_dtypes(include="object").columns
        )
        num_col = st.selectbox(
            "Select Value Column (Optional - for aggregation):",
            ["None"] + list(data.select_dtypes(include=np.number).columns),
        )
        orientation = st.radio(
            "Orientation:", ["Vertical", "Horizontal"], horizontal=True
        )
        # 'orient' variable unused; orientation is checked inline when needed

        if st.button("Plot Bar Chart", key="bar_button"):  # UNIQUE KEY
            if not cat_cols:
                st.error("Please select at least one category column.")
                st.stop()

            if num_col != "None":
                agg_func = st.selectbox(
                    "Aggregation Function:",
                    ["sum", "mean", "count", "median", "min", "max"],
                    index=0,
                )
                agg_functions = {
                    "sum": "sum",
                    "mean": "mean",
                    "count": "count",
                    "median": "median",
                    "min": "min",
                    "max": "max",
                }
                agg_data = (
                    data.groupby(cat_cols)[num_col]
                    .agg(agg_functions[agg_func])
                    .reset_index()
                )

                if len(cat_cols) == 1:
                    fig = px.bar(
                        agg_data,
                        x=cat_cols[0],
                        y=num_col,
                        title=f"{agg_func.capitalize()} of {num_col} by {cat_cols[0]}",
                        orientation="v" if orientation == "Vertical" else "h",
                        color=(
                            cat_cols[0]
                            if len(agg_data[cat_cols[0]].unique()) <= 10
                            else None
                        ),
                    )
                else:
                    agg_data["combined_categories"] = (
                        agg_data[cat_cols].astype(str).agg(" - ".join, axis=1)
                    )
                    fig = px.bar(
                        agg_data,
                        x="combined_categories",
                        y=num_col,
                        title=f"{agg_func.capitalize()} of {num_col} by {', '.join(cat_cols)}",
                        orientation="v" if orientation == "Vertical" else "h",
                        color=(
                            "combined_categories"
                            if len(agg_data["combined_categories"].unique()) <= 10
                            else None
                        ),
                    )
                    fig.update_xaxes(tickangle=-45)
                st.plotly_chart(fig, use_container_width=True)

            else:
                if len(cat_cols) == 1:
                    counts = data[cat_cols[0]].value_counts().reset_index()
                    counts.columns = [cat_cols[0], "Count"]
                    fig = px.bar(
                        counts,
                        x=cat_cols[0],
                        y="Count",
                        title=f"Counts of {cat_cols[0]}",
                        orientation="v" if orientation == "Vertical" else "h",
                        color=(
                            cat_cols[0]
                            if len(counts[cat_cols[0]].unique()) <= 10
                            else None
                        ),
                    )
                else:
                    counts = data.groupby(cat_cols).size().reset_index(name="Count")
                    counts["combined_categories"] = (
                        counts[cat_cols].astype(str).agg(" - ".join, axis=1)
                    )
                    fig = px.bar(
                        counts,
                        x="combined_categories",
                        y="Count",
                        title=f"Count by {', '.join(cat_cols)}",
                        orientation="v" if orientation == "Vertical" else "h",
                        color=(
                            "combined_categories"
                            if len(counts["combined_categories"].unique()) <= 10
                            else None
                        ),
                    )
                    fig.update_xaxes(tickangle=-45)
                st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Heatmap":
        st.subheader("Correlation Heatmap")
        st.write("Visualize the correlation between numerical columns.")
        if st.button("Generate Heatmap", key="heatmap_button"):  # Unique Key
            if len(numerical_cols) < 2:
                st.error("At least two numerical columns are required.")
            else:
                corr_matrix = data[numerical_cols].corr()
                fig = px.imshow(
                    corr_matrix,
                    text_auto=".2f",
                    aspect="auto",
                    color_continuous_scale="RdBu_r",
                    title="Correlation Heatmap",
                )
                fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
                st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Violin Plot":
        st.subheader("Violin Plot")
        x_col = st.selectbox(
            "Select X-axis (Categorical):",
            ["None"] + list(data.select_dtypes(include="object").columns),
        )
        y_col = st.selectbox("Select Y-axis (Numerical):", numerical_cols)

        if st.button("Plot Violin Plot", key="violin_button"):  # Unique Key
            fig = px.violin(
                data,
                x=x_col if x_col != "None" else None,
                y=y_col,
                title=f"Violin Plot of {y_col}"
                + (f" by {x_col}" if x_col != "None" else ""),
                box=True,
                points="all",
            )
            st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Scatter Plot Matrix":
        st.subheader("Scatter Plot Matrix")
        st.write("Visualize pairwise relationships between multiple numerical columns.")
        cols = st.multiselect("Select Numerical Columns:", numerical_cols)
        if st.button(
            "Generate Scatter Plot Matrix", key="scatter_matrix_button"
        ):  # Unique Key
            if len(cols) < 2:
                st.error("Please select at least two numerical columns.")
            else:
                fig = px.scatter_matrix(
                    data, dimensions=cols, title="Scatter Plot Matrix"
                )
                st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "3D Scatter Plot":
        st.subheader("3D Scatter Plot")
        if len(numerical_cols) < 3:
            st.error("At least three numerical columns are required.")
        else:
            x_col = st.selectbox("Select X-axis Column:", numerical_cols, index=0)
            y_col = st.selectbox(
                "Select Y-axis Column:",
                numerical_cols,
                index=1 if len(numerical_cols) > 1 else 0,
            )
            z_col = st.selectbox(
                "Select Z-axis Column:",
                numerical_cols,
                index=2 if len(numerical_cols) > 2 else 0,
            )
            color_col = st.selectbox(
                "Color by (Optional):", ["None"] + list(data.columns), index=0
            )

            if st.button("Plot 3D Scatter Plot", key="3d_scatter_button"):  # Unique Key
                fig = px.scatter_3d(
                    data,
                    x=x_col,
                    y=y_col,
                    z=z_col,
                    color=color_col if color_col != "None" else None,
                    title=f"3D Scatter Plot of {x_col}, {y_col}, and {z_col}",
                )
                st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Bubble Chart":
        st.subheader("Bubble Chart")
        if len(numerical_cols) < 3:
            st.error(
                "At least three numerical columns are required for a Bubble Chart."
            )
        else:
            x_col = st.selectbox("Select X-axis Column:", numerical_cols, index=0)
            y_col = st.selectbox(
                "Select Y-axis Column:",
                numerical_cols,
                index=1 if len(numerical_cols) > 1 else 0,
            )
            size_col = st.selectbox(
                "Select Size Column:",
                numerical_cols,
                index=2 if len(numerical_cols) > 2 else 0,
            )
            color_col = st.selectbox(
                "Color by (Optional):", ["None"] + list(data.columns), index=0
            )

            if st.button(
                "Generate Bubble Chart", key="bubble_chart_button"
            ):  # Unique Key
                fig = px.scatter(
                    data,
                    x=x_col,
                    y=y_col,
                    size=size_col,
                    color=color_col if color_col != "None" else None,
                    title=f"Bubble Chart of {x_col} and {y_col} by size {size_col}",
                )
                st.plotly_chart(fig, use_container_width=True)

    elif viz_type == "Funnel Chart":
        st.subheader("Funnel Chart")
        st.write("Visualize the flow of users/items through a series of stages.")

        num_stages = st.number_input(
            "Number of Stages:", min_value=2, max_value=10, value=4, step=1
        )
        stages = []
        values = []
        for i in range(num_stages):
            stage = st.text_input(f"Stage {i+1} Name:", value=f"Stage {i+1}")
            value = st.number_input(
                f"Value for {stage}:", min_value=0, value=1000 - (i * 100), step=10
            )
            stages.append(stage)
            values.append(value)

        if st.button("Generate Funnel Chart", key="funnel_chart_button"):  # Unique key
            funnel_data = pd.DataFrame({"stage": stages, "value": values})
            fig = px.funnel(funnel_data, x="value", y="stage", title="Funnel Chart")
            st.plotly_chart(fig, use_container_width=True)

    # --- Practice Exercises ---
    st.header("💪 Practice Exercises")
    st.markdown(
        """
    1.  **Distribution Exploration:**  Create a histogram of a numerical column. Experiment with bin sizes. What's the distribution's shape, center, and spread?
    2.  **Correlation Analysis:** Create a scatter plot of two numerical columns.  Is there a positive, negative, or no correlation?  Add a trendline.
    3.  **Group Comparison:** If your dataset has a categorical column, create a box plot (or violin plot) of a numerical column, grouped by category.  Are there differences between groups?
    4.  **Time Series Analysis:** If your data has a timestamp, create a line chart.  Identify trends or seasonality. Try different aggregations (daily, weekly, monthly).
    5.  **Funnel Analysis:** Create a funnel chart for a user journey (e.g., visit -> signup -> purchase). Identify drop-off points.
    6.  **Dashboard Design:** Recreate a simplified version of the interactive dashboard below using your data (or the example data).
    """
    )

    # --- Real-world Application: Interactive Dashboard ---
    st.header("🌍 Real-world Application: Interactive Product Analytics Dashboard")
    st.write(
        "This dashboard demonstrates how visualizations combine to provide a comprehensive view.  It's a simplified example."
    )

    # UNIQUE KEY for the dashboard button:
    if st.button("Generate Dashboard", key="dashboard_button"):
        st.subheader("User Engagement Dashboard")

        # --- KPI Cards ---
        col1, col2, col3 = st.columns(3)
        with col1:
            try:
                total_users = data["UserCategory"].nunique()  # Example
                st.metric("Total Users", total_users)
            except KeyError:
                st.metric("Total Users", "N/A")

        with col2:
            try:
                avg_session = data["SessionDuration"].mean()
                st.metric("Avg. Session Duration", f"{avg_session:.2f}")
            except KeyError:
                st.metric("Avg. Session Duration", "N/A")

        with col3:
            try:
                conversion_rate = (
                    data["DeviceType"].value_counts(normalize=True)["Mobile"] * 100
                )  # Example
                st.metric("Conversion Rate", f"{conversion_rate:.1f}%")
            except (KeyError, TypeError):
                st.metric("Conversion Rate", "N/A")

        # --- Charts ---
        st.subheader("User Activity Over Time")
        try:
            daily_data = (
                data.groupby("Date")["DailyClicks"].sum().reset_index()
            )  # Example
            fig_time = px.line(
                daily_data,
                x="Date",
                y="DailyClicks",
                title="Daily Active Users (Proxy)",
            )
            st.plotly_chart(fig_time, use_container_width=True)
        except KeyError:
            st.write("Time series plot requires 'Date' and a numerical column.")

        st.subheader("Distribution of Session Durations")
        try:
            fig_hist = px.histogram(
                data,
                x="SessionDuration",
                title="Distribution of Session Durations",
                nbins=30,
                marginal="box",
            )
            st.plotly_chart(fig_hist, use_container_width=True)
        except KeyError:
            st.write("Histogram requires a numerical column (e.g., 'SessionDuration').")

        st.subheader("Users by Category")
        try:
            user_counts = data["UserCategory"].value_counts().reset_index()
            user_counts.columns = ["Category", "Count"]
            fig_bar = px.bar(
                user_counts, x="Category", y="Count", title="Users by Category"
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        except KeyError:
            st.write("Bar chart requires a categorical column (e.g., 'UserCategory').")

        st.subheader("Correlation Heatmap")
        numerical_cols = data.select_dtypes(include=np.number).columns.tolist()
        if len(numerical_cols) >= 2:
            corr_matrix = data[numerical_cols].corr()
            fig_heatmap = px.imshow(
                corr_matrix,
                text_auto=".2f",
                aspect="auto",
                color_continuous_scale="RdBu_r",
                title="Correlation Heatmap",
            )
            st.plotly_chart(fig_heatmap, use_container_width=True)
        else:
            st.write("Not enough numerical columns for a heatmap.")


if __name__ == "__main__":
    data_visualization_page()

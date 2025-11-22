import numpy as np
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# --- Data Generation Functions ---


def generate_demand_data(
    n_periods=365,
    base_demand=100,
    trend_strength=0.1,
    seasonality_strength=0.3,
    noise_level=0.1,
    random_state=42,
):
    """Generates synthetic daily demand data with trend, seasonality, and noise."""
    np.random.seed(random_state)
    time = np.arange(n_periods)
    trend = time * trend_strength * base_demand / n_periods  # Gradual trend over time
    seasonality = np.sin(2 * np.pi * time / 365) * seasonality_strength * base_demand
    noise = np.random.randn(n_periods) * noise_level * base_demand
    demand = base_demand + trend + seasonality + noise
    demand = np.maximum(demand, 10)  # Ensure demand is non-negative and reasonable min
    date_rng = pd.date_range(start="2023-01-01", periods=n_periods)
    df = pd.DataFrame({"Date": date_rng, "Demand": demand})
    df.set_index("Date", inplace=True)
    return df


# --- Forecasting Functions ---


def moving_average_forecast(data, window):
    """Calculates Moving Average forecast."""
    return data["Demand"].rolling(window=window, center=False).mean().shift(1)


def exponential_smoothing_forecast(data, alpha, seasonal=False, seasonal_periods=7):
    """Calculates Exponential Smoothing forecast (Single or Holt-Winters if seasonal=True)."""
    if seasonal:
        model = ExponentialSmoothing(
            data["Demand"],
            seasonal_periods=seasonal_periods,
            seasonal="add",
            trend="add",
            initialization_method="estimated",
        ).fit()
    else:
        model = ExponentialSmoothing(
            data["Demand"], initialization_method="estimated"
        ).fit(
            smoothing_level=alpha
        )  # Single ES
    return model.fittedvalues


def linear_regression_forecast(data, future_periods):
    """Calculates Linear Regression forecast based on time index."""
    model = LinearRegression()
    X = np.array(range(len(data))).reshape(-1, 1)  # Time index as feature
    y = data["Demand"]
    model.fit(X, y)

    future_X = np.array(range(len(data), len(data) + future_periods)).reshape(-1, 1)
    forecast = model.predict(future_X)
    forecast_series = pd.Series(
        forecast,
        index=pd.date_range(
            start=data.index[-1] + pd.Timedelta(days=1), periods=future_periods
        ),
    )
    return forecast_series  # Returns future forecast only


# --- Accuracy Metric Functions ---


def calculate_metrics(actual, forecast):
    """Calculates common forecast accuracy metrics."""
    mae = mean_absolute_error(actual, forecast)
    mse = mean_squared_error(actual, forecast)
    rmse = np.sqrt(mse)
    # MAPE - handling potential division by zero
    actual_non_zero = actual[actual != 0]
    forecast_non_zero = forecast[actual != 0]
    if len(actual_non_zero) > 0:  # Avoid MAPE if all actuals are zero
        mape = (
            np.mean(np.abs((actual_non_zero - forecast_non_zero) / actual_non_zero))
            * 100
        )
    else:
        mape = np.nan  # Or np.inf if you want to indicate infinite percentage error

    metrics = {"MAE": mae, "MSE": mse, "RMSE": rmse, "MAPE (%)": mape}
    return metrics


def main():
    st.set_page_config(
        page_title="Economic Demand Forecasting", page_icon="📈", layout="wide"
    )

    st.title("Economic Demand Forecasting: Predicting Future Trends")
    st.write("Explore various forecasting techniques to predict economic demand.")

    with st.expander("📖 Theoretical Overview"):
        st.markdown(
            """
        Demand forecasting is a critical process in economics and business for predicting future demand for products or services. Accurate forecasts are essential for informed decision-making in areas like production planning, inventory management, budgeting, and resource allocation.

        ### 1. Importance of Demand Forecasting

        *   **Informed Decision-Making:**  Reduces uncertainty and provides a basis for strategic and operational decisions.
        *   **Inventory Optimization:**  Prevents overstocking and stockouts, minimizing costs and maximizing customer service.
        *   **Production Planning:**  Aligns production with anticipated demand, optimizing resource utilization and efficiency.
        *   **Financial Planning:**  Supports budgeting, revenue projections, and financial risk management.
        *   **Supply Chain Management:**  Enables efficient logistics, supplier coordination, and overall supply chain optimization.

        ### 2. Types of Demand Forecasting

        *   **Qualitative Forecasting:** Based on expert opinions, market surveys, and subjective assessments. Useful when historical data is limited or unreliable.
        *   **Quantitative Forecasting:** Relies on historical data and statistical techniques. More objective and suitable when data is available.
            *   **Time Series Forecasting:** Analyzes historical patterns in demand data over time to extrapolate future trends. (Focus of this page)
            *   **Causal Forecasting:** Identifies cause-and-effect relationships between demand and other factors (e.g., price, marketing spend, economic indicators).  (Covered in Regression example).

        ### 3. Time Series Forecasting Techniques

        *   **Moving Average (MA):** Simple and intuitive.  Averages demand over a specific past period (window) to forecast the next period.  Smooths out noise but lags behind trends.
        *   **Exponential Smoothing (ES):**  Assigns exponentially decreasing weights to past observations, giving more importance to recent data.  Can be adapted for trend and seasonality (Holt-Winters).
            *   **Single Exponential Smoothing:** Suitable for data with no trend or seasonality.
            *   **Holt's Double Exponential Smoothing:**  Handles data with trend but no seasonality.
            *   **Holt-Winters Triple Exponential Smoothing:**  Handles data with both trend and seasonality. (Implemented in the interactive demo).

        ### 4. Causal Forecasting - Regression Analysis

        *   **Linear Regression:** Models the relationship between demand (dependent variable) and one or more independent variables (predictors) such as time, price, or marketing expenditure.  Can capture trends and the impact of causal factors.
        *   **Limitations:**  Assumes linear relationships and requires identification of relevant predictors.

        ### 5. Evaluating Forecast Accuracy

        *   **Mean Absolute Error (MAE):** Average absolute difference between forecast and actual values.  Easy to interpret.
        *   **Mean Squared Error (MSE):** Average squared difference.  Penalizes larger errors more heavily.
        *   **Root Mean Squared Error (RMSE):** Square root of MSE.  Same units as the data, easier to interpret than MSE.
        *   **Mean Absolute Percentage Error (MAPE):** Average percentage error.  Scale-independent, easy to compare across datasets, but undefined if actual values are zero.

        **Further Reading:**
            *   [Forecasting: Principles and Practice (Hyndman & Athanasopoulos)](https://otexts.com/fpp3/) - Excellent online textbook on forecasting.
            *   [Demand Forecasting Techniques (Corporate Finance Institute)](https://corporatefinanceinstitute.com/resources/valuation/demand-forecasting/)
            *   [Time Series Analysis (Wikipedia)](https://en.wikipedia.org/wiki/Time_series_analysis) - Background on time series concepts.
        """
        )

    st.header("🧮 Interactive Demand Forecasting Demo")

    forecast_type = st.selectbox(
        "Select Forecasting Method:",
        ["Moving Average", "Exponential Smoothing", "Linear Regression"],
        key="forecast_type_select",
    )

    # --- Data Generation Inputs ---
    st.subheader("1. Generate Demand Data")
    n_periods_demand = st.slider(
        "Number of Days to Simulate:",
        min_value=30,
        max_value=730,
        value=365,
        step=30,
        key="n_periods_demand",
    )
    base_demand_input = st.number_input(
        "Base Daily Demand:",
        min_value=10,
        max_value=500,
        value=100,
        step=10,
        key="base_demand_input",
    )
    trend_strength_input = st.slider(
        "Trend Strength:",
        min_value=-0.2,
        max_value=0.2,
        value=0.1,
        step=0.02,
        key="trend_strength_input",
    )  # Added trend
    seasonality_strength_input = st.slider(
        "Seasonality Strength:",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.05,
        key="seasonality_strength_input",
    )
    noise_level_input = st.slider(
        "Demand Noise Level:",
        min_value=0.0,
        max_value=0.5,
        value=0.1,
        step=0.05,
        key="noise_level_input",
    )

    if st.button("Generate Demand Data", key="generate_data_button"):
        demand_df = generate_demand_data(
            n_periods_demand,
            base_demand_input,
            trend_strength_input,
            seasonality_strength_input,
            noise_level_input,
        )
        st.session_state.demand_data = demand_df  # Store data in session state

    if "demand_data" in st.session_state:
        df_demand = st.session_state.demand_data
        st.subheader("2. Demand Data Visualization")
        st.line_chart(df_demand)

        # --- Forecasting Method Parameters ---
        st.subheader("3. Forecasting Parameters")

        if forecast_type == "Moving Average":
            window_ma = st.slider(
                "Moving Average Window Size:",
                min_value=2,
                max_value=30,
                value=7,
                step=1,
                key="window_ma",
            )
            forecast_series = moving_average_forecast(
                df_demand.copy(), window_ma
            )  # Pass a copy to avoid modifying original df

        elif forecast_type == "Exponential Smoothing":
            alpha_es = st.slider(
                "Smoothing Factor (Alpha):",
                min_value=0.01,
                max_value=0.99,
                value=0.3,
                step=0.05,
                key="alpha_es",
            )
            seasonal_es = st.checkbox(
                "Seasonal Exponential Smoothing (Holt-Winters)", key="seasonal_es_check"
            )
            if seasonal_es:
                seasonal_periods_es = st.number_input(
                    "Seasonal Periods:",
                    min_value=2,
                    max_value=30,
                    value=7,
                    step=1,
                    key="seasonal_periods_es",
                )
                forecast_series = exponential_smoothing_forecast(
                    df_demand.copy(),
                    alpha_es,
                    seasonal=seasonal_es,
                    seasonal_periods=seasonal_periods_es,
                )
            else:
                forecast_series = exponential_smoothing_forecast(
                    df_demand.copy(), alpha_es, seasonal=seasonal_es
                )

        elif forecast_type == "Linear Regression":
            future_periods_lr = st.number_input(
                "Periods to Forecast into the Future:",
                min_value=7,
                max_value=365,
                value=30,
                step=7,
                key="future_periods_lr",
            )
            forecast_series_future = linear_regression_forecast(
                df_demand.copy(), future_periods_lr
            )  # Future forecast
            forecast_series = linear_regression_forecast(
                df_demand.copy(), 0
            )  # In-sample forecast for metrics
            forecast_series.name = "Regression Forecast"  # Needed for concat later

        # --- Perform Forecasting and Display Results ---
        if st.button("Run Forecast", key="run_forecast_button"):
            if (
                forecast_type != "Linear Regression"
            ):  # For MA and ES, forecast is in-sample
                forecast_df = df_demand.copy()
                forecast_df["Forecast"] = forecast_series
            else:  # For LR, forecast_df combines historical and future forecasts
                forecast_df_hist = df_demand.copy()
                forecast_df_hist["Forecast"] = forecast_series
                forecast_df_future = pd.DataFrame({"Forecast": forecast_series_future})
                forecast_df_future.index = forecast_series_future.index
                forecast_df = pd.concat([forecast_df_hist, forecast_df_future])

            st.subheader("4. Forecast vs. Actual Demand")
            st.line_chart(forecast_df[["Demand", "Forecast"]])

            # --- Accuracy Metrics ---
            st.subheader("5. Forecast Accuracy Metrics")
            if forecast_type != "Linear Regression":
                metrics = calculate_metrics(
                    forecast_df["Demand"].dropna(), forecast_df["Forecast"].dropna()
                )  # Drop NAs for metrics
            else:  # For linear regression, calculate metrics only on historical data
                metrics = calculate_metrics(
                    forecast_df_hist["Demand"].dropna(),
                    forecast_df_hist["Forecast"].dropna(),
                )

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("MAE", f"{metrics['MAE']:.2f}")
            with col2:
                st.metric("MSE", f"{metrics['MSE']:.2f}")
            with col3:
                st.metric("RMSE", f"{metrics['RMSE']:.2f}")
            with col4:
                st.metric(
                    "MAPE (%)",
                    f"{metrics['MAPE (%)']:.2f}"
                    if not np.isnan(metrics["MAPE (%)"])
                    else "Undefined (Zeros in Data)",
                )  # Handle NaN MAPE

    st.header("💪 Practice Exercises")
    st.markdown(
        """
    1. **Compare Moving Average with different window sizes.**  Generate demand data and experiment with different window sizes for the Moving Average forecast. Observe how the window size affects the forecast smoothness and responsiveness to changes in demand.
    2. **Explore Exponential Smoothing with different alpha values.**  Test different alpha values (smoothing factors) for Exponential Smoothing.  How does alpha influence the forecast's reaction to recent demand?
    3. **Forecast data with trend and seasonality using Holt-Winters.** Generate data with both trend and seasonality, and apply Holt-Winters Exponential Smoothing. Compare its performance to Single Exponential Smoothing.
    4. **Use Linear Regression for demand forecasting with time as a predictor.** Generate demand data and use Linear Regression to forecast future demand based on the time index. Extend the forecast into future periods.
    5. **Evaluate forecast accuracy metrics for different methods.** For the same dataset, compare the MAE, MSE, RMSE, and MAPE values for Moving Average, Exponential Smoothing, and Linear Regression forecasts. Which method performs best based on these metrics?
    """
    )

    st.header("🌍 Real-world Applications")
    st.markdown(
        """
    Economic demand forecasting is essential in numerous industries and applications:

    *   **Retail and E-commerce:** Predicting sales for inventory planning, promotions, and staffing.
    *   **Manufacturing:** Production scheduling, raw material procurement, capacity planning.
    *   **Supply Chain Management:** Optimizing logistics, warehouse operations, and distribution networks.
    *   **Finance:** Forecasting demand for financial products, predicting market trends.
    *   **Energy:** Predicting electricity demand, natural gas consumption for resource management.
    *   **Healthcare:** Forecasting patient volumes, predicting demand for medical supplies and staff.
    *   **Transportation:** Predicting passenger traffic, freight demand for resource and capacity allocation.
    """
    )

    st.header("✅ Knowledge Check")
    quiz_questions = [
        {
            "question": "Which forecasting method is best suited for data with no trend or seasonality?",
            "options": [
                "Moving Average",
                "Exponential Smoothing (Single)",
                "Holt-Winters Exponential Smoothing",
                "Linear Regression",
            ],
            "answer": "Exponential Smoothing (Single)",
            "solution": "Single Exponential Smoothing is designed for data with a stable level (no trend or seasonality).",
        },
        {
            "question": "What is a key limitation of the Moving Average method?",
            "options": [
                "It is computationally complex.",
                "It is highly sensitive to outliers.",
                "It lags behind trends in the data.",
                "It cannot handle seasonality.",
            ],
            "answer": "It lags behind trends in the data.",
            "solution": "Moving Average averages past values, causing it to be slow in responding to trend changes.",
        },
        {
            "question": "Which Exponential Smoothing method is designed to handle data with both trend and seasonality?",
            "options": [
                "Single Exponential Smoothing",
                "Double Exponential Smoothing",
                "Holt-Winters Exponential Smoothing",
                "Simple Moving Average",
            ],
            "answer": "Holt-Winters Exponential Smoothing",
            "solution": "Holt-Winters (Triple Exponential Smoothing) explicitly models level, trend, and seasonality.",
        },
        {
            "question": "Which forecast accuracy metric is scale-independent and easy to compare across different datasets, but undefined if actual values are zero?",
            "options": [
                "MAE (Mean Absolute Error)",
                "MSE (Mean Squared Error)",
                "RMSE (Root Mean Squared Error)",
                "MAPE (Mean Absolute Percentage Error)",
            ],
            "answer": "MAPE (Mean Absolute Percentage Error)",
            "solution": "MAPE expresses error as a percentage, making it scale-independent, but division by zero is a limitation.",
        },
        {
            "question": "In Exponential Smoothing, what does a higher smoothing factor (alpha) indicate?",
            "options": [
                "More weight is given to past observations.",
                "More weight is given to recent observations.",
                "The forecast will be smoother and less responsive.",
                "The forecast will be less accurate.",
            ],
            "answer": "More weight is given to recent observations.",
            "solution": "Alpha controls the balance between recent and past data. Higher alpha emphasizes recent data.",
        },
        {
            "question": "When is Qualitative forecasting most appropriate?",
            "options": [
                "When you have a lot of historical data.",
                "When you need highly accurate forecasts.",
                "When you have limited or unreliable historical data.",
                "When you need to forecast very short-term demand.",
            ],
            "answer": "When you have limited or unreliable historical data.",
            "solution": "Qualitative methods rely on expert judgment when data is scarce or not useful.",
        },
        {
            "question": "Linear Regression for demand forecasting is an example of:",
            "options": [
                "Time Series Forecasting",
                "Causal Forecasting",
                "Qualitative Forecasting",
                "Moving Average",
            ],
            "answer": "Causal Forecasting",
            "solution": "Regression models the *cause-and-effect* relationship between demand and other factors (like time as a proxy for trend).",
        },
        {
            "question": "Which metric penalizes larger forecast errors more heavily?",
            "options": ["MAE", "RMSE", "MAPE", "All of the above equally"],
            "answer": "RMSE",
            "solution": "RMSE (and MSE) square the errors, so larger errors have a disproportionately bigger impact.",
        },
        {
            "question": "For data with a clear upward trend, which method is generally better than Simple Moving Average?",
            "options": [
                "Single Exponential Smoothing",
                "Moving Average with a larger window",
                "Holt's Double Exponential Smoothing",
                "Qualitative Forecasting",
            ],
            "answer": "Holt's Double Exponential Smoothing",
            "solution": "Holt's method is designed to capture trend, unlike simple MA or Single ES.",
        },
        {
            "question": "If MAPE is 'Undefined (Zeros in Data)', what does this usually mean?",
            "options": [
                "The forecast is perfectly accurate.",
                "There are zero values in the actual demand data.",
                "The MAPE value is extremely high (approaching infinity).",
                "The model failed to converge.",
            ],
            "answer": "There are zero values in the actual demand data.",
            "solution": "MAPE involves division by actual values; zero actuals lead to division by zero and undefined MAPE.",
        },
    ]

    user_answers = []
    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i + 1}. {question['question']}**")
        user_answer = st.radio(
            f"Select an answer:", question["options"], key=f"quiz_{i}"
        )
        user_answers.append(user_answer)

    if st.button("Submit Quiz"):
        correct_count = 0
        for i, (user_answer, question) in enumerate(zip(user_answers, quiz_questions)):
            if user_answer == question["answer"]:
                correct_count += 1

        st.write(
            f"You got {correct_count} out of {len(quiz_questions)} questions correct."
        )

        with st.expander("Show Detailed Solutions"):
            for i, question in enumerate(quiz_questions):
                st.markdown(f"**Question {i+1}:** {question['question']}")
                st.markdown(f"**Your Answer:** {user_answers[i]}")
                st.markdown(f"**Correct Answer:** {question['answer']}")
                st.markdown(f"**Solution:** {question['solution']}")
                if user_answers[i] == question["answer"]:
                    st.success("Correct!")
                else:
                    st.error("Incorrect.")


if __name__ == "__main__":
    main()

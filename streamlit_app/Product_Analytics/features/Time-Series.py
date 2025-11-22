import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
import pmdarima as pm  # For auto_arima

# Function to generate synthetic time series data
def generate_time_series_data(n_periods=200, trend_slope=0.5, seasonality_strength=20, noise_level=10, random_state=42):
    np.random.seed(random_state)
    time = np.arange(n_periods)
    trend = trend_slope * time
    seasonality = seasonality_strength * np.sin(2 * np.pi * time / 12)  # Assume yearly seasonality
    noise = np.random.randn(n_periods) * noise_level
    data = trend + seasonality + noise
    date_rng = pd.date_range(start='2023-01-01', periods=n_periods, freq='M') #monthly data
    df = pd.DataFrame({'Date': date_rng, 'Value': data})
    df.set_index('Date', inplace=True)
    return df


# Function to plot time series decomposition
def plot_decomposition(df, model='additive'):
    decomposition = seasonal_decompose(df['Value'], model=model)
    fig, axes = plt.subplots(4, 1, figsize=(10, 8))
    axes[0].plot(decomposition.observed)
    axes[0].set_title('Observed')
    axes[1].plot(decomposition.trend)
    axes[1].set_title('Trend')
    axes[2].plot(decomposition.seasonal)
    axes[2].set_title('Seasonal')
    axes[3].plot(decomposition.resid)
    axes[3].set_title('Residual')
    plt.tight_layout()
    st.pyplot(fig)
    return decomposition



# Function for ADF test
def adf_test(timeseries):
    result = adfuller(timeseries, autolag='AIC')
    output = pd.Series(result[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in result[4].items():
        output[f'Critical Value ({key})'] = value
    return output

def main():
    st.set_page_config(page_title="Time Series Analysis", page_icon="⏰", layout="wide")

    st.title("Time Series Analysis: Unveiling Patterns in Temporal Data")
    st.write("Explore time series concepts, decomposition, forecasting, and more.")

    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
        Time series analysis deals with data points collected or recorded over time.  It's used to understand patterns, trends, and make predictions.

        ### 1. Key Concepts

        *   **Time Series:**  A sequence of data points indexed in time order.
        *   **Trend:**  The long-term direction of the data (increasing, decreasing, or stable).
        *   **Seasonality:**  Repeating patterns or cycles within a fixed period (e.g., daily, weekly, yearly).
        *   **Cyclicality:**  Fluctuations that are *not* of a fixed frequency (unlike seasonality). Often longer term than seasonal effects.
        *   **Stationarity:**  A time series whose statistical properties (mean, variance, autocorrelation) *do not* change over time. Crucial for many forecasting models.
        *   **Autocorrelation:**  The correlation of a time series with its own past values (lags).
        *   **Partial Autocorrelation:** The correlation of a time series with a lagged version of itself, *after* removing the effects of intermediate lags.

        ### 2. Time Series Decomposition

        *   **Purpose:**  Breaking down a time series into its components (trend, seasonality, residuals).
        *   **Models:**
            *   **Additive Model:**  `y(t) = Trend(t) + Seasonality(t) + Residual(t)` (appropriate when the seasonal variations are relatively *constant* over time).
            *   **Multiplicative Model:** `y(t) = Trend(t) * Seasonality(t) * Residual(t)` (appropriate when the seasonal variations *change* proportionally to the level of the series).

        ### 3. Stationarity Testing

        *   **Importance:** Many time series models assume stationarity.  Non-stationary data needs to be transformed.
        *   **Augmented Dickey-Fuller (ADF) Test:** A statistical test for stationarity.
            *   **Null Hypothesis (H0):** The time series is *non-stationary*.
            *   **Alternative Hypothesis (H1):** The time series is stationary.
            *   **Interpretation:** If the p-value is below a significance level (e.g., 0.05), we reject the null hypothesis and conclude the series is stationary.

        ### 4. Time Series Forecasting

        * **ARIMA (Autoregressive Integrated Moving Average) Models**
            *   **AR (Autoregressive):** Uses past values of the series to predict future values. The 'p' parameter is the order (number of lags) of the AR component.
            *   **I (Integrated):** Represents differencing to make the series stationary. The 'd' parameter is the degree of differencing.
            *   **MA (Moving Average):** Uses past forecast errors to predict future values. The 'q' parameter is the order of the MA component.
        * **SARIMA (Seasonal ARIMA)** Extends ARIMA to handle seasonal data. Includes additional seasonal terms: (P, D, Q, S), where S is the length of the seasonal cycle.
        * **Auto ARIMA**  Automatically searches for the optimal ARIMA parameters (p, d, q) and (P, D, Q, S).

        **Further Reading:**
            *   [Time Series Analysis (Wikipedia)](https://en.wikipedia.org/wiki/Time_series)
            *   [Statsmodels Time Series Analysis Documentation](https://www.statsmodels.org/stable/tsa.html)
            *   [Forecasting: Principles and Practice (Hyndman & Athanasopoulos)](https://otexts.com/fpp3/)
        """)

    st.header("🔄 Interactive Demo")

    # Data source selection
    data_source = st.radio("Choose data source:", ["Generate Synthetic Data", "Upload CSV"])

    if data_source == "Generate Synthetic Data":
        n_periods = st.slider("Number of Periods:", min_value=50, max_value=500, value=200, step=50)
        trend_slope = st.slider("Trend Slope:", min_value=-1.0, max_value=1.0, value=0.1, step=0.05)
        seasonality_strength = st.slider("Seasonality Strength:", min_value=0, max_value=50, value=20, step=5)
        noise_level = st.slider("Noise Level:", min_value=0, max_value=50, value=10, step=5)
        df = generate_time_series_data(n_periods, trend_slope, seasonality_strength, noise_level)

    else:  # Upload CSV
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file, index_col=0, parse_dates=True)
                # Handle common date parsing issues:
                if df.index.inferred_type == "string":  # If not parsed as dates...
                    df.index = pd.to_datetime(df.index, errors='coerce')  # Try to convert
                df.dropna(inplace=True) # Drop any rows that have issues.
                if df.index.isnull().any():
                   st.error("Date parsing failed. Please ensure your CSV has a valid date column as the first column.")
                   df = None

            except Exception as e:
                st.error(f"Error reading the CSV file: {e}")
                df = None
        else:
            df = None


    if df is not None: # only proceed if df is valid
        st.write("Time Series Data:")
        st.dataframe(df)

        # Time Series Plot
        st.subheader("Time Series Plot")
        fig, ax = plt.subplots()
        ax.plot(df['Value'])
        ax.set_xlabel("Date")
        ax.set_ylabel("Value")
        ax.set_title("Time Series Data")
        st.pyplot(fig)

        # Decomposition
        st.subheader("Time Series Decomposition")
        decomposition_model = st.selectbox("Decomposition Model:", ["additive", "multiplicative"])
        decomposition = plot_decomposition(df, model=decomposition_model)

        # Stationarity Test
        st.subheader("Stationarity Test (ADF)")
        adf_result = adf_test(df['Value'])
        st.write(adf_result)
        if adf_result['p-value'] < 0.05:
            st.success("The time series is likely stationary.")
        else:
            st.warning("The time series is likely non-stationary. Consider differencing.")

        # Autocorrelation and Partial Autocorrelation
        st.subheader("Autocorrelation and Partial Autocorrelation")
        lags = st.slider("Number of Lags:", min_value=1, max_value=50, value=20, step=1)
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        plot_acf(df['Value'], lags=lags, ax=axes[0])
        plot_pacf(df['Value'], lags=lags, ax=axes[1])
        st.pyplot(fig)


        # Forecasting
        st.subheader("Time Series Forecasting (ARIMA)")
        train_size = int(len(df) * 0.8)
        train, test = df[0:train_size], df[train_size:]

        model_choice = st.radio("Model Selection:", ["Manual ARIMA", "Auto ARIMA"])

        if model_choice == "Manual ARIMA":
            p = st.number_input("AR Order (p):", min_value=0, value=1, step=1)
            d = st.number_input("Differencing Order (d):", min_value=0, value=0, step=1)
            q = st.number_input("MA Order (q):", min_value=0, value=1, step=1)
            try:
                model = ARIMA(train['Value'], order=(p, d, q))
                model_fit = model.fit()
                st.write(model_fit.summary())
                predictions = model_fit.predict(start=len(train), end=len(df) - 1)

                 # Plot predictions
                fig, ax = plt.subplots()
                ax.plot(train['Value'], label='Train')
                ax.plot(test['Value'], label='Test')
                ax.plot(test.index, predictions, label='Predictions') #Use correct index
                ax.set_xlabel("Date")
                ax.set_ylabel("Value")
                ax.legend()
                st.pyplot(fig)
                #Calculate and show evaluation metrics
                rmse = np.sqrt(mean_squared_error(test['Value'], predictions))
                mae = mean_absolute_error(test['Value'], predictions)
                st.write(f"RMSE: {rmse:.2f}")
                st.write(f"MAE: {mae:.2f}")

            except Exception as e:
                st.error(f"Error fitting ARIMA model: {e}")

        else:  # Auto ARIMA
            try:
                auto_model = pm.auto_arima(train['Value'], seasonal=True, m=12, trace=True, suppress_warnings=True, stepwise=True)
                st.write(auto_model.summary())
                predictions = auto_model.predict(n_periods=len(test))  # Predict for test period

                # Plot
                fig, ax = plt.subplots()
                ax.plot(train['Value'], label='Train')
                ax.plot(test['Value'], label='Test')
                ax.plot(test.index, predictions, label='Predictions') #Use correct index
                ax.set_xlabel("Date")
                ax.set_ylabel("Value")
                ax.legend()
                st.pyplot(fig)

                #Metrics
                rmse = np.sqrt(mean_squared_error(test['Value'], predictions))
                mae = mean_absolute_error(test['Value'], predictions)
                st.write(f"RMSE: {rmse:.2f}")
                st.write(f"MAE: {mae:.2f}")
            except Exception as e:
                st.error(f"Error fitting Auto ARIMA model: {e}")

    st.header("💪 Practice Exercises")
    st.markdown("""
    1.  **Load a time series dataset (e.g., stock prices, weather data).**  Perform time series decomposition and interpret the results.
    2.  **Test a time series for stationarity using the ADF test.**  If it's non-stationary, apply differencing to make it stationary.
    3.  **Analyze the autocorrelation and partial autocorrelation plots of a time series.**  Use the plots to suggest appropriate orders (p, d, q) for an ARIMA model.
    4.  **Build an ARIMA model to forecast future values of a time series.**  Evaluate the model's performance using metrics like RMSE and MAE.
    5.  **Experiment with different values of p, d, and q in an ARIMA model.**  Compare the results and try to find the best-fitting model.
    6. **Use Auto Arima on a dataset** Compare the results of the model with a manual Arima model.
    """)

    st.header("🌍 Real-world Applications")
    st.markdown("""
    Time series analysis is used in a wide range of fields:

    *   **Finance:**  Stock price forecasting, risk management.
    *   **Economics:**  Predicting economic indicators (GDP, inflation, unemployment).
    *   **Sales & Marketing:**  Demand forecasting, sales prediction.
    *   **Operations:**  Inventory management, capacity planning.
    *   **Energy:**  Predicting electricity demand, optimizing energy production.
    *   **Healthcare:**  Tracking disease outbreaks, predicting patient volume.
    *   **Environmental Science:**  Analyzing climate data, predicting weather patterns.
    """)

    st.header("✅ Knowledge Check")
    quiz_questions = [
        {
            "question": "What is the term for a time series whose statistical properties (mean, variance) do not change over time?",
            "options": ["Trend", "Seasonality", "Stationarity", "Autocorrelation"],
            "answer": "Stationarity",
            "solution": "Stationarity is a key assumption for many time series models. A stationary series has constant statistical properties."
        },
        {
            "question": "Which component of a time series represents repeating patterns within a fixed period?",
            "options": ["Trend", "Seasonality", "Cyclicality", "Residual"],
            "answer": "Seasonality",
            "solution": "Seasonality refers to regular, repeating patterns, such as daily, weekly, or yearly cycles."
        },
        {
            "question": "In the Augmented Dickey-Fuller (ADF) test, what does a small p-value (e.g., < 0.05) suggest?",
            "options": ["The time series is non-stationary", "The time series is stationary", "The time series has a strong trend", "The time series has strong seasonality"],
            "answer": "The time series is stationary",
            "solution": "A small p-value in the ADF test leads us to reject the null hypothesis of non-stationarity, suggesting the series is stationary."
        },
        {
            "question": "What does 'ARIMA' stand for in time series modeling?",
            "options": ["Autoregressive Integrated Moving Average", "Autocorrelated Regression Integrated Moving Average", "Autoregressive Integrated Moving Assessment", "Autocorrelated Regression Integrated Moving Assessment"],
            "answer": "Autoregressive Integrated Moving Average",
            "solution": "ARIMA models combine autoregressive (AR), integrated (I), and moving average (MA) components."
        },
        {
            "question": "What is the purpose of differencing a time series?",
            "options": ["To remove seasonality", "To make the series stationary", "To remove the trend", "To add noise"],
            "answer": "To make the series stationary",
            "solution": "Differencing involves subtracting consecutive observations to remove trends and stabilize the mean, helping to achieve stationarity."
        },
        {
            "question": "In an ARIMA(1, 0, 1) model, what does the '1' in the first position represent?",
            "options": ["The order of differencing", "The order of the autoregressive (AR) component", "The order of the moving average (MA) component", "The length of the seasonal cycle"],
            "answer": "The order of the autoregressive (AR) component",
            "solution": "The first number in the ARIMA(p, d, q) notation represents the order of the AR component (the number of lagged values used)."
        },
        {
            "question": "Which of the following is a suitable metric for evaluating the performance of a time series forecasting model?",
            "options": ["Accuracy", "Precision", "Recall", "Root Mean Squared Error (RMSE)"],
            "answer": "Root Mean Squared Error (RMSE)",
            "solution": "RMSE, which measures the average magnitude of the forecast errors, is a common metric for time series forecasting. Accuracy, precision, and recall are typically used for classification problems, not regression."
        },
        {
           "question": "What is the difference between *autocorrelation* and *partial autocorrelation*?",
            "options": ["Autocorrelation measures the correlation with past values, while partial autocorrelation measures the correlation with future values.",
                        "Autocorrelation measures the direct relationship with a lagged value, while partial autocorrelation measures the relationship after removing the effects of intermediate lags.",
                        "Autocorrelation is used for stationary series, while partial autocorrelation is used for non-stationary series.",
                        "There is no difference; they are the same thing."],
            "answer": "Autocorrelation measures the direct relationship with a lagged value, while partial autocorrelation measures the relationship after removing the effects of intermediate lags.",
            "solution": "Partial autocorrelation helps to identify the order of an AR model by isolating the direct relationship between a time series and a specific lag."
        },
        {
            "question": "In time series decomposition, what does the 'residual' component represent?",
            "options": ["The long-term direction of the data", "Repeating patterns within a fixed period", "The randomness or noise in the data after removing trend and seasonality", "Fluctuations that are not of a fixed frequency"],
            "answer": "The randomness or noise in the data after removing trend and seasonality",
            "solution": "The residual component represents the part of the time series that cannot be explained by the trend or seasonal components."
        },
       {
            "question": "Which model is appropriate if seasonal fluctuations increase *proportionally* to the level of the time series?",
            "options":["Additive Decomposition", "Multiplicative Decomposition", "ARIMA", "Auto Arima"],
            "answer": "Multiplicative Decomposition",
            "solution": "A multiplicative model is used when the magnitude of the seasonal pattern changes with the level of the series."

        }

    ]

    user_answers = []
    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i + 1}. {question['question']}**")
        user_answer = st.radio(f"Select an answer:", question["options"], key=f"quiz_{i}")
        user_answers.append(user_answer)

    if st.button("Submit Quiz"):
        correct_count = 0
        for i, (user_answer, question) in enumerate(zip(user_answers, quiz_questions)):
            if user_answer == question["answer"]:
                correct_count += 1

        st.write(f"You got {correct_count} out of {len(quiz_questions)} questions correct.")

        with st.expander("Show Detailed Solutions"):
            for i, question in enumerate(quiz_questions):
                st.markdown(f"**Question {i+1}:** {question['question']}")
                st.markdown(f"**Your Answer:** {user_answers[i]}")
                st.markdown(f"**Correct Answer:** {question['answer']}")
                st.markdown(f"**Solution:** {question['solution']}")
                if user_answers[i] == question['answer']:
                    st.success("Correct!")
                else:
                    st.error("Incorrect.")
if __name__ == "__main__":
    main()

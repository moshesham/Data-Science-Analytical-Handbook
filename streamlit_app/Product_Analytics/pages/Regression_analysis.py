import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, LogisticRegression, PoissonRegressor, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
from scipy.special import expit  # For sigmoid function in logistic regression


def generate_data(regression_type, n_samples=100, noise_level=0.2, random_state=42):
    """Generates synthetic data for different regression types."""
    np.random.seed(random_state)
    X = np.random.rand(n_samples, 1) * 10  # Feature: 0 to 10

    if regression_type == "Linear Regression":
        y = 2 * X.flatten() + 1 + np.random.randn(n_samples) * noise_level * 5 #add more noise
    elif regression_type == "Logistic Regression":
        y = (expit(X.flatten() - 5) > np.random.rand(n_samples)).astype(int) #make it more centered
    elif regression_type == "Poisson Regression":
        y = np.random.poisson(lam=np.exp(X.flatten() / 3), size=n_samples) # link to X
    elif regression_type == "Multivariate Regression":
        X = np.random.rand(n_samples, 3) * 10 # Three features now
        y = 2*X[:,0] + 0.5*X[:,1] - 1*X[:,2] + 1 + np.random.randn(n_samples) * noise_level
    return X, y


def plot_regression(X, y, y_pred, regression_type, feature_names=None):
    """Plots the data and regression line/curve."""
    fig, ax = plt.subplots()

    if regression_type == "Logistic Regression":
        # Sort for a smooth sigmoid curve
        sorted_indices = np.argsort(X.flatten())
        X_sorted = X.flatten()[sorted_indices]
        y_pred_sorted = y_pred[sorted_indices]

        ax.scatter(X, y, color='blue', label='Data')
        ax.plot(X_sorted, y_pred_sorted, color='red', label='Logistic Fit')
        ax.set_xlabel(feature_names[0] if feature_names else 'X')
        ax.set_ylabel('Probability (y)')
    elif regression_type == "Multivariate Regression":
        #Since we can't really visualize >3D, we'll show actual vs predicted
        ax.scatter(y, y_pred)
        ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2) #ideal line
        ax.set_xlabel('Actual Values')
        ax.set_ylabel('Predicted Values')
    else: # Linear and Poisson
        ax.scatter(X, y, color='blue', label='Data')
        ax.plot(X, y_pred, color='red', label='Regression Fit')
        ax.set_xlabel(feature_names[0] if feature_names else 'X')
        ax.set_ylabel('y')

    ax.set_title(f"{regression_type} Results")
    ax.legend()
    st.pyplot(fig)

def main():
    st.set_page_config(page_title="Regression Analysis Beyond Linearity", page_icon="📈", layout="wide")

    st.title("Regression Analysis: Beyond the Basics")
    st.write("Explore different regression models, regularization, and their applications.")

    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
        Regression analysis is a powerful statistical method for understanding and modeling the relationship between a dependent variable (the outcome) and one or more independent variables (predictors or features).  While linear regression is a great starting point, many real-world scenarios require more sophisticated models.

        ### 1. Linear Regression (Review)

        *   **Model:**  Assumes a linear relationship: `y = β₀ + β₁x₁ + ... + βₙxₙ + ε`
        *   **Goal:** Find coefficients (β) that minimize the sum of squared errors.
        *   **Limitations:**  Only models linear relationships; sensitive to outliers.

        ### 2. Logistic Regression

        *   **Use Case:**  Predicting *binary* outcomes (0 or 1, Yes/No, Click/No-Click).
        *   **Model:**  Uses the *sigmoid* (logistic) function to map linear predictions to probabilities: `P(y=1) = 1 / (1 + exp(-(β₀ + β₁x₁ + ... + βₙxₙ)))`
        *   **Interpretation:** Coefficients represent the change in the *log-odds* of the outcome for a one-unit change in the predictor.

        ### 3. Poisson Regression

        *   **Use Case:** Modeling *count* data (non-negative integers: number of events, occurrences).
        *   **Model:** Assumes the outcome follows a Poisson distribution.  Uses a log link function: `log(E[y]) = β₀ + β₁x₁ + ... + βₙxₙ`
        * **Interpretation:** Coefficients represent change in *log of expected count*.

        ### 4. Generalized Linear Models (GLMs)

        *   **Framework:** A flexible generalization of ordinary linear regression.  Connects linear regression, logistic regression, Poisson regression, and others.
        *   **Components:**
            *   **Random Component:**  The probability distribution of the response variable (e.g., Normal, Binomial, Poisson).
            *   **Systematic Component:**  The linear predictor (β₀ + β₁x₁ + ... + βₙxₙ).
            *   **Link Function:**  Connects the random and systematic components (e.g., identity, logit, log).

        ### 5. Regularization

        *   **Problem:**  Overfitting – models that perform well on training data but poorly on new data.
        *   **Solution:**  Regularization adds a penalty term to the loss function, discouraging overly complex models.
        *   **Types:**
            *   **L1 Regularization (Lasso):** Adds the absolute value of the coefficients to the loss function.  Can lead to *feature selection* (some coefficients become zero).
            *   **L2 Regularization (Ridge):** Adds the squared value of the coefficients.  Shrinks coefficients towards zero, but rarely to zero.
            *   **Elastic Net**: Combines L1 and L2 regularization.
        
        ### 6. Multivariate Regression
        * **Description:** Multivariate regression involves modeling the relationship between *multiple* independent variables (predictors) and a *single* dependent variable.  It's an extension of simple linear regression.
        *   **Model:** `y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε`  where x₁, x₂, ..., xₙ are different predictor variables.
        * **Interpretation:** Each coefficient (βᵢ) represents the change in the dependent variable (y) associated with a one-unit change in the corresponding independent variable (xᵢ), *holding all other variables constant*.  This "holding constant" is crucial for interpretation.

        **Further Reading:**
            *   [Generalized Linear Models (Wikipedia)](https://en.wikipedia.org/wiki/Generalized_linear_model)
            *   [Logistic Regression (Wikipedia)](https://en.wikipedia.org/wiki/Logistic_regression)
            *   [Poisson Regression (UCLA Stats)](https://stats.oarc.ucla.edu/r/dae/poisson-regression/)
        """)

    st.header("🔄 Interactive Demo")

    regression_type = st.selectbox("Select a Regression Type:", ["Linear Regression", "Logistic Regression", "Poisson Regression", "Multivariate Regression"])

    n_samples = st.slider("Number of Samples:", min_value=50, max_value=500, value=100, step=50)
    noise_level = st.slider("Noise Level:", min_value=0.0, max_value=1.0, value=0.2, step=0.05)

    X, y = generate_data(regression_type, n_samples, noise_level)

    if regression_type in ["Linear Regression", "Multivariate Regression"]:
        model = LinearRegression()
        if regression_type == "Multivariate Regression":
          feature_names = [f"Feature {i+1}" for i in range(X.shape[1])]
        else:
            feature_names = ['Feature 1']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        st.write(f"Mean Squared Error: {mse:.2f}")
        st.write(f"R-squared: {r2:.2f}")

        # Statsmodels for summary (Linear Regression)
        if regression_type == "Linear Regression":
            X_train_sm = sm.add_constant(X_train)  # Add constant for intercept
            model_sm = sm.OLS(y_train, X_train_sm)
            results = model_sm.fit()
            st.write(results.summary())
        #Multivariate regression
        if regression_type == "Multivariate Regression":
          X_train_sm = sm.add_constant(X_train)  # Add constant for intercept
          model_sm = sm.OLS(y_train, X_train_sm)
          results = model_sm.fit()
          st.write(results.summary())
        #predict on the test set for consistent plotting
        y_pred = model.predict(X)

    elif regression_type == "Logistic Regression":
        model = LogisticRegression()
        feature_names = ['Feature 1']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train)
        y_pred_proba = model.predict_proba(X)[:, 1]  # Probabilities for class 1
        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        st.write(f"Accuracy: {accuracy:.2f}")
        st.write("Confusion Matrix:")
        st.write(confusion_matrix(y_test, y_pred))
        st.write("Classification Report:")
        st.write(classification_report(y_test, y_pred))

        # Statsmodels for summary
        X_train_sm = sm.add_constant(X_train)
        model_sm = sm.Logit(y_train, X_train_sm)
        results = model_sm.fit()
        st.write(results.summary())

        #predict on full set for plot consistency
        y_pred_proba = model.predict_proba(X)[:, 1] #use for plot

    elif regression_type == "Poisson Regression":
        feature_names = ['Feature 1']
        # Scale X for Poisson (avoid convergence issues)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        model = PoissonRegressor()
        model.fit(X_train, y_train)

        #Stats model summary
        X_train_sm = sm.add_constant(X_train)
        model_sm = sm.GLM(y_train, X_train_sm, family=sm.families.Poisson())
        results = model_sm.fit()
        st.write(results.summary())

        y_pred = model.predict(X_scaled)  # Predict on scaled X
        mse = mean_squared_error(y, y_pred)
        st.write(f"Mean Squared Error: {mse:.2f}")  # MSE on original scale

    with st.expander("Show Data"):
        df = pd.DataFrame(X, columns=feature_names)
        df['y'] = y
        st.dataframe(df)

    plot_regression(X, y, y_pred_proba if regression_type == 'Logistic Regression' else y_pred, regression_type, feature_names)


    with st.expander("Regularization Demo"):
        reg_type = st.selectbox("Select Regularization Type:", ["None", "Ridge (L2)", "Lasso (L1)"])
        alpha = st.slider("Regularization Strength (alpha):", min_value=0.01, max_value=10.0, value=1.0, step=0.01)

        # Generate data (using linear data for demonstration)
        X_reg, y_reg = generate_data("Linear Regression", n_samples=100, noise_level=0.5)
        X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)
        #Scale data
        scaler = StandardScaler()
        X_reg_train = scaler.fit_transform(X_reg_train)
        X_reg_test = scaler.transform(X_reg_test)

        if reg_type == "Ridge (L2)":
            model_reg = Ridge(alpha=alpha)
        elif reg_type == "Lasso (L1)":
            model_reg = Lasso(alpha=alpha)
        else:
            model_reg = LinearRegression()  # No regularization

        model_reg.fit(X_reg_train, y_reg_train)
        y_reg_pred = model_reg.predict(X_reg_test)
        mse_reg = mean_squared_error(y_reg_test, y_reg_pred)
        st.write(f"Mean Squared Error ({reg_type}): {mse_reg:.2f}")

        # Display coefficients
        if reg_type != "None":
             st.write("Coefficients:", model_reg.coef_)

        #Visualize performance on whole dataset for comparison
        y_reg_pred_all = model_reg.predict(scaler.transform(X_reg)) # Predict on all (scaled) data
        plot_regression(X_reg, y_reg, y_reg_pred_all, "Linear Regression")

    st.header("💪 Practice Exercises")

    st.markdown("""
    1.  **Predicting House Prices:** You have a dataset with features like square footage, number of bedrooms, location, etc.  Use linear regression to predict house prices.
    2.  **Customer Churn:** Given data on customer behavior (usage, demographics, support interactions), build a logistic regression model to predict churn (whether a customer will cancel their subscription).
    3.  **Website Traffic:** Model the number of daily website visitors using Poisson regression, considering factors like marketing spend, day of the week, and seasonality.
    4.  **Regularization Comparison:** Experiment with different values of alpha for Ridge and Lasso regression on a dataset prone to overfitting.  Compare the coefficients and prediction accuracy.
    5.  **Multivariate Prediction:** Use a dataset with multiple independent variables to make a prediction for a single dependent variable. Compare the results with simple linear regression using only single independent variable.
    """)
    if st.button("Show Answers and Explanations"):
        st.markdown("""
            1.  **Predicting House Prices:**  This is a classic application of linear regression. Use the provided features to train a `LinearRegression` model in scikit-learn.
            2.  **Customer Churn:**  Logistic regression is appropriate here because the outcome (churn) is binary. Use `LogisticRegression` in scikit-learn.  Remember to consider data preprocessing (e.g., handling categorical variables, scaling numerical features).
            3.  **Website Traffic:**  Poisson regression is suitable for count data. Use `PoissonRegressor` in scikit-learn (or `GLM` with `family=sm.families.Poisson()` in statsmodels).
            4.  **Regularization Comparison:**  Create a dataset where some features are highly correlated or irrelevant.  Train `Ridge` and `Lasso` models with varying `alpha` values.  Observe how Lasso can drive some coefficients to zero (feature selection).
            5.  **Multivariate Prediction:** Find any dataset with multiple independent variables (e.g., advertising spend on different channels) to predict a single dependent variable (sales). Compare the accuracy (e.g., R-squared) against a single-variable linear regression. It is also important to interpret the significance of each variable's coefficient.
            """)

    st.header("🌍 Real-world Applications")
    st.markdown("""
    Regression models are used extensively in various fields:

    *   **Finance:** Predicting stock prices, credit risk assessment.
    *   **Marketing:** Customer lifetime value prediction, campaign response modeling.
    *   **Healthcare:** Predicting disease risk, patient readmission rates.
    *   **Operations:** Demand forecasting, inventory management.
    *   **Product Analytics:**  Identifying factors that drive user engagement, predicting user behavior.
    *   **E-commerce**: Predicting customer purchase, recommending items based on purchasing behavior
    """)


    st.header("✅ Knowledge Check")

    quiz_questions = [
      {
            "question": "Which regression model is best suited for predicting binary outcomes (0 or 1)?",
            "options": ["Linear Regression", "Logistic Regression", "Poisson Regression", "Ridge Regression"],
            "answer": "Logistic Regression",
            "solution": "Logistic regression is specifically designed for binary classification problems."
        },
        {
            "question": "What type of data is Poisson regression typically used to model?",
            "options": ["Continuous data", "Binary data", "Count data", "Categorical data"],
            "answer": "Count data",
            "solution": "Poisson regression is used for modeling non-negative integer counts."
        },
        {
            "question": "Which of the following is NOT a component of a Generalized Linear Model (GLM)?",
            "options": ["Random component", "Systematic component", "Link function", "Regularization term"],
            "answer": "Regularization term",
            "solution": "Regularization is a technique to *prevent overfitting*, but it's not a core component of the GLM framework itself.  GLMs have a random component (distribution), systematic component (linear predictor), and a link function."
        },
        {
            "question": "What is the purpose of regularization in regression models?",
            "options": ["To increase model complexity", "To handle missing data", "To prevent overfitting", "To transform the response variable"],
            "answer": "To prevent overfitting",
            "solution": "Regularization adds a penalty to the loss function, discouraging overly complex models that might fit the training data too closely."
        },
        {
            "question": "Which type of regularization can lead to feature selection (setting some coefficients to zero)?",
            "options": ["Ridge (L2)", "Lasso (L1)", "Both Ridge and Lasso", "Neither Ridge nor Lasso"],
            "answer": "Lasso (L1)",
            "solution": "Lasso regularization, due to its L1 penalty, can shrink some coefficients all the way to zero, effectively removing those features from the model."
        },
        {
            "question": "In logistic regression, what does a coefficient represent?",
            "options": ["The change in the outcome variable for a one-unit change in the predictor",
                        "The change in the log-odds of the outcome for a one-unit change in the predictor",
                        "The probability of the outcome being 1",
                        "The odds ratio of the outcome"],
            "answer": "The change in the log-odds of the outcome for a one-unit change in the predictor",
            "solution": "Logistic regression coefficients are interpreted in terms of log-odds, not directly in terms of the probability."
        },
        {
            "question": "What is the purpose of the sigmoid function in logistic regression?",
            "options": ["To linearize the relationship between predictors and the outcome",
                        "To transform the outcome variable to a normal distribution",
                        "To map linear predictions to probabilities between 0 and 1",
                        "To handle count data"],
            "answer": "To map linear predictions to probabilities between 0 and 1",
            "solution": "The sigmoid function 'squashes' the linear combination of predictors into a probability range."
        },
       {
            "question": "In multivariate regression, what does the coefficient β₂ for variable x₂ represent?",
            "options": ["The change in y for a one-unit change in x₂, ignoring other variables.",
                       "The change in y for a one-unit change in x₂, holding all other variables constant.",
                       "The correlation between x₂ and y.",
                       "The variance of x₂."],
            "answer": "The change in y for a one-unit change in x₂, holding all other variables constant.",
            "solution": "The key to multivariate regression interpretation is the concept of holding other variables constant.  It isolates the effect of a single predictor."
        },
        {
            "question": "What distribution does Poisson regression assume for the response variable?",
            "options": ["Normal distribution", "Binomial distribution", "Poisson distribution", "Exponential distribution"],
            "answer": "Poisson distribution",
            "solution": "Poisson regression assumes that the response variable follows a Poisson distribution, which is appropriate for count data."
        },
        {
          "question": "Which type of regression would be MOST appropriate for predicting the number of customer support tickets a company receives in a day?",
          "options": ["Linear Regression", "Logistic Regression", "Poisson Regression", "Ridge Regression"],
          "answer": "Poisson Regression",
          "solution": "Since the number of support tickets is count data, Poisson regression is the most suitable choice."
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

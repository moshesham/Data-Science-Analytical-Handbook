import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (accuracy_score, confusion_matrix, classification_report,
                             precision_score, recall_score, f1_score, roc_auc_score, roc_curve)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline  # Use imblearn's Pipeline
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Load data (replace with your actual data loading)
@st.cache_data
def load_data():
    # Attempt to load from a local path (for development/testing)
    try:
        df = pd.read_csv("telecom_churn.csv")  # Replace with your actual file
    except FileNotFoundError:
        # If the file is not found locally, try loading a sample dataset from a URL
        url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"  # Example public dataset
        try:
            df = pd.read_csv(url)
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return None

    # Basic Preprocessing (adapt as needed for your dataset)
    if 'customerID' in df.columns:
        df.set_index('customerID', inplace=True)
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df.dropna(subset=['TotalCharges'], inplace=True)  # Or impute
    if 'Churn' in df.columns:  # Standardize the target variable
        df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    return df



def preprocess_data(df, preprocessor=None, fit_preprocessor=True):
    """Preprocesses the data, fitting or using a preprocessor."""

    # Identify categorical and numerical features
    categorical_features = df.select_dtypes(include=['object']).columns.tolist()
    numerical_features = df.select_dtypes(include=['number']).columns.tolist()

    # Make sure target variable is not in features
    if 'Churn' in categorical_features:
        categorical_features.remove('Churn')
    if 'Churn' in numerical_features:
        numerical_features.remove('Churn')

    if preprocessor is None:  # Create preprocessor if it doesn't exist
        if fit_preprocessor:
            # Create preprocessing pipelines for numeric and categorical features
            numeric_transformer = Pipeline(steps=[
                ('scaler', StandardScaler())])

            categorical_transformer = Pipeline(steps=[
                ('onehot', OneHotEncoder(handle_unknown='ignore'))]) #handle new categories in test

            # Use ColumnTransformer to apply the transformations to the correct columns
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numeric_transformer, numerical_features),
                    ('cat', categorical_transformer, categorical_features)])

            preprocessor.fit(df) # FIT the preprocessor

    # Now, *transform* the data, whether a preprocessor existed or we just created it
    if len(numerical_features) > 0 and len(categorical_features) > 0:
         X = preprocessor.transform(df)
    elif len(numerical_features) >0: #handle edge case of no categorical features
        X = preprocessor.transform(df[numerical_features]) #Just transform numerical
    else: #handle edge case of no numerical features.
        X = preprocessor.transform(df[categorical_features]) #Just transform categorical

    # Get feature names after one-hot encoding
    try:
      feature_names = list(preprocessor.named_transformers_['cat'].named_steps['onehot'].get_feature_names_out(categorical_features))
      feature_names = numerical_features + feature_names
    except: #handle edge case of only numerical features
      feature_names = numerical_features


    return X, feature_names, preprocessor


def train_model(X_train, y_train, model_name, smote=False):
    """Trains a specified model, optionally with SMOTE."""
    if model_name == "Logistic Regression":
        model = LogisticRegression(random_state=42, solver='liblinear')
        param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100]}
    elif model_name == "Decision Tree":
        model = DecisionTreeClassifier(random_state=42)
        param_grid = {'max_depth': [3, 5, 7, 10, None], 'min_samples_split': [2, 5, 10]}
    elif model_name == "Random Forest":
        model = RandomForestClassifier(random_state=42)
        param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [3, 5, 7, None]}
    elif model_name == "Gradient Boosting":
        model = GradientBoostingClassifier(random_state=42)
        param_grid = {'n_estimators': [50, 100, 200], 'learning_rate': [0.01, 0.1, 0.2], 'max_depth': [3, 5, 7]}
    elif model_name == "SVM":
        model = SVC(random_state=42, probability=True)  # Need probability for ROC AUC
        param_grid = {'C': [0.1, 1, 10], 'gamma': ['scale', 'auto']}
    elif model_name == "Naive Bayes":
        model = GaussianNB()
        param_grid = {}  # Naive Bayes doesn't have many tunable hyperparameters
    else:
        raise ValueError("Invalid model name")

    if smote:
        model = ImbPipeline(steps=[('smote', SMOTE(random_state=42)), ('classifier', model)])

    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='roc_auc', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    return best_model

def evaluate_model(model, X_test, y_test):
    """Evaluates the model and returns metrics."""
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]  # Probabilities for the positive class

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)
    conf_matrix = confusion_matrix(y_test, y_pred)

    metrics = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC AUC": roc_auc,
        "Confusion Matrix": conf_matrix
    }
    return metrics

def plot_roc_curve(model, X_test, y_test):
    """Plots the ROC curve."""
    y_prob = model.predict_proba(X_test)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label=f'AUC = {roc_auc_score(y_test, y_prob):.2f}')
    ax.plot([0, 1], [0, 1], 'k--')
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('ROC Curve')
    ax.legend()
    st.pyplot(fig)


def main():
    st.set_page_config(page_title="Customer Churn Prediction", page_icon="👤", layout="wide")

    st.title("Predicting Customer Churn: A Machine Learning Approach")
    st.write("Analyze customer data, build predictive models, and evaluate their performance.")

    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
        Customer churn (attrition) is a critical metric for businesses, representing the loss of customers. Predicting churn allows companies to take proactive steps to retain customers.

        ### Key Concepts

        *   **Churn:** The event where a customer stops doing business with a company.
        *   **Classification Problem:** Churn prediction is typically framed as a binary classification problem (churn or no churn).
        *   **Evaluation Metrics:**
            *   **Accuracy:** Overall correctness of the model.
            *   **Precision:** Proportion of predicted churners who actually churned.  (True Positives / (True Positives + False Positives))
            *   **Recall:** Proportion of actual churners who were correctly predicted. (True Positives / (True Positives + False Negatives))
            *   **F1 Score:** Harmonic mean of precision and recall.
            *   **ROC AUC:** Area Under the Receiver Operating Characteristic Curve.  Measures the model's ability to distinguish between classes.
            *   **Confusion Matrix:**  A table showing the counts of True Positives, True Negatives, False Positives, and False Negatives.
        *   **Imbalanced Data:** Churn datasets often have an imbalance (more non-churners than churners).  Techniques like SMOTE (Synthetic Minority Oversampling Technique) can help.
        * **Model Interpretability:** Understanding which features are most influential is crucial.

        ### Models
        *   **Logistic Regression:** A simple, interpretable model that provides probability estimates.
        *   **Decision Trees:**  Easy to understand and visualize.
        *   **Random Forest:**  An ensemble method that combines multiple decision trees, often achieving high accuracy.
        *   **Gradient Boosting:**  Another ensemble method that builds trees sequentially, correcting errors from previous trees.
        *   **Support Vector Machines (SVM):**  Effective in high-dimensional spaces.
        *   **Naive Bayes:**  A probabilistic classifier based on Bayes' theorem.

        """)

    st.header("🔄 Interactive Demo")

    # Load and preprocess data
    df = load_data()

    if df is not None:
        # Display data
        st.subheader("Data Preview")
        st.dataframe(df.head())

        # Data Exploration (Basic EDA)
        with st.expander("Exploratory Data Analysis (EDA)"):
            st.subheader("Data Summary")
            st.write(df.describe())

            st.subheader("Churn Distribution")
            churn_counts = df['Churn'].value_counts()
            fig_churn = px.pie(churn_counts, values=churn_counts.values, names=churn_counts.index, title='Churn Distribution')
            st.plotly_chart(fig_churn)

            # Histograms for numerical features
            numerical_features = df.select_dtypes(include=['number']).columns.tolist()
            if 'Churn' in numerical_features:
                numerical_features.remove('Churn')

            if len(numerical_features) >0:
                st.subheader("Histograms of Numerical Features")
                selected_num_feature = st.selectbox("Select a numerical feature:", numerical_features) #selectbox for user input
                fig_hist_num = px.histogram(df, x=selected_num_feature, color="Churn", title=f'Histogram of {selected_num_feature}')
                st.plotly_chart(fig_hist_num)

            # Bar plots for categorical features
            categorical_features = df.select_dtypes(include=['object']).columns.tolist()
            if 'Churn' in categorical_features:
                categorical_features.remove('Churn')
            if len(categorical_features) >0:
                st.subheader("Bar Plots of Categorical Features")
                selected_cat_feature = st.selectbox("Select a categorical feature:", categorical_features) #selectbox
                fig_bar_cat = px.bar(df, x=selected_cat_feature, color="Churn", title=f'Bar Plot of {selected_cat_feature}', barmode='group')
                st.plotly_chart(fig_bar_cat)



        # Data Splitting
        X = df.drop('Churn', axis=1)
        y = df['Churn']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y) #Stratify

        #Preprocessing
        X_train, feature_names, preprocessor = preprocess_data(X_train, fit_preprocessor=True) # FIT preprocessor
        X_test, _, _ = preprocess_data(X_test, preprocessor=preprocessor, fit_preprocessor=False) # Use fitted preprocessor

        # Model Selection and Training
        st.subheader("Model Training and Evaluation")
        available_models = ["Logistic Regression", "Decision Tree", "Random Forest", "Gradient Boosting", "SVM", "Naive Bayes"]
        selected_models = st.multiselect("Select Models:", available_models, default=["Logistic Regression"])
        use_smote = st.checkbox("Use SMOTE for Imbalanced Data (Recommended)", value=True)


        if st.button("Train Models"):
            results = {}
            for model_name in selected_models:
                with st.spinner(f'Training {model_name}...'):
                    model = train_model(X_train, y_train, model_name, smote=use_smote)
                    metrics = evaluate_model(model, X_test, y_test)
                    results[model_name] = {"model": model, "metrics": metrics}

                # Display results for each model
                st.subheader(f"Results for {model_name}")
                st.write("Metrics:")
                for metric_name, metric_value in metrics.items():
                    if metric_name != "Confusion Matrix":
                        st.write(f"{metric_name}: {metric_value:.4f}")
                st.write("Confusion Matrix:")
                st.write(metrics["Confusion Matrix"])
                plot_roc_curve(model, X_test, y_test)

                # Feature Importances (for tree-based models)
                if model_name in ["Decision Tree", "Random Forest", "Gradient Boosting"]:
                    if use_smote: # Handle SMOTE in pipeline
                      importances = model.named_steps['classifier'].feature_importances_
                    else:
                      importances = model.feature_importances_

                    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
                    feature_importance_df = feature_importance_df.sort_values('Importance', ascending=False)

                    fig_importance = px.bar(feature_importance_df, x='Feature', y='Importance', title=f'Feature Importance ({model_name})')
                    st.plotly_chart(fig_importance)

            # Model Comparison (across selected models)
            if len(results) > 1:
              st.subheader("Model Comparison")
              comparison_df = pd.DataFrame({model_name: results[model_name]["metrics"] for model_name in results})
              comparison_df.drop("Confusion Matrix", inplace=True)  # Remove confusion matrix for comparison
              st.dataframe(comparison_df)

              #Bar chart for model performance comparison:
              fig_comparison = px.bar(comparison_df, barmode='group', title='Model Performance Comparison')
              st.plotly_chart(fig_comparison)


    st.header("💪 Practice Exercises")
    st.markdown("""
    1. **Experiment with different models.** Try all available models and compare their performance.
    2. **Tune hyperparameters.** Use the interactive sliders (where available) to adjust model parameters and observe the effects.
    3. **Try different data preprocessing steps.**  Explore different ways of handling missing values or encoding categorical features (if applicable to your dataset).
    4. **Analyze feature importances.** Identify the most important predictors of churn and interpret their impact.
    5. **Use a different dataset.** Apply the same workflow to a different churn prediction dataset and see how the results vary.
    """)

    st.header("🌍 Real-world Applications")
    st.markdown("""
    Churn prediction is vital in many industries:

    *   **Telecommunications:** Identifying customers likely to switch providers.
    *   **Subscription Services:** Predicting cancellations of streaming services, software subscriptions, etc.
    *   **E-commerce:** Identifying customers at risk of not making repeat purchases.
    *   **Banking and Finance:** Predicting loan defaults or account closures.
    *   **SaaS (Software as a Service):** Identifying users likely to stop using a platform.
    """)

    st.header("✅ Knowledge Check")
    quiz_questions = [
        {
            "question": "What is customer churn?",
            "options": ["The number of new customers acquired", "The rate at which customers stop doing business with a company", "The average revenue generated per customer", "The total number of customers"],
            "answer": "The rate at which customers stop doing business with a company",
            "solution": "Churn represents the loss of customers."
        },
        {
            "question": "Which evaluation metric is most appropriate for imbalanced datasets?",
            "options": ["Accuracy", "Precision", "Recall", "F1 Score"],
            "answer": "F1 Score",
            "solution": "The F1 score balances precision and recall, making it suitable for imbalanced data where accuracy can be misleading."
        },
        {
            "question": "What does ROC AUC stand for?",
            "options": ["Receiver Operating Characteristic Area Under Curve", "Regression Output Calculation Area Under Curve", "Receiver Operating Calculation Area Under Curve", "Regression Output Characteristic Area Under Curve"],
            "answer": "Receiver Operating Characteristic Area Under Curve",
            "solution": "ROC AUC is a measure of a model's ability to distinguish between classes."
        },
        {
            "question": "What is the purpose of SMOTE?",
            "options": ["To reduce the number of features", "To handle missing values", "To oversample the minority class in imbalanced datasets", "To undersample the majority class"],
            "answer": "To oversample the minority class in imbalanced datasets",
            "solution": "SMOTE (Synthetic Minority Oversampling Technique) creates synthetic samples of the minority class to balance the dataset."
        },
        {
            "question": "Which of the following models is generally considered the most interpretable?",
            "options": ["Random Forest", "Gradient Boosting", "Logistic Regression", "Support Vector Machine"],
            "answer": "Logistic Regression",
            "solution": "Logistic regression provides coefficients that are relatively easy to interpret in terms of the impact of each feature on the log-odds of the outcome."
        },
        {
            "question": "In a confusion matrix, what does a false positive represent?",
            "options": ["A customer who churned and was predicted to churn",
                        "A customer who did not churn and was predicted not to churn",
                        "A customer who did not churn but was predicted to churn",
                        "A customer who churned but was predicted not to churn"],
            "answer": "A customer who did not churn but was predicted to churn",
            "solution": "A false positive is an incorrect prediction of the positive class (in this case, churn)."
        },
        {
            "question": "What is the main advantage of using ensemble methods like Random Forest and Gradient Boosting?",
            "options": ["They are very easy to interpret",
                        "They are computationally inexpensive",
                        "They often achieve higher accuracy than individual models",
                        "They don't require any data preprocessing"],
            "answer": "They often achieve higher accuracy than individual models",
            "solution": "Ensemble methods combine multiple models to improve prediction accuracy and robustness."
        },
        {
            "question": "What is the purpose of a train-test split?",
            "options": ["To train the model on all available data",
                        "To evaluate the model's performance on unseen data",
                        "To preprocess the data",
                        "To select the best features"],
            "answer": "To evaluate the model's performance on unseen data",
            "solution": "The test set is used to simulate how well the model will generalize to new, unseen data."
        },
         {
            "question": "What does one-hot encoding do?",
            "options": ["Scales numerical features",
                        "Converts categorical features into numerical representations",
                        "Handles missing values",
                        "Reduces the dimensionality of the data"],
            "answer": "Converts categorical features into numerical representations",
            "solution": "One-hot encoding creates binary columns for each category of a categorical feature, allowing machine learning models to use them."
        },
        {
          "question": "Which evaluation metric represents the proportion of *actual* churners who were correctly identified?",
          "options": ["Precision", "Recall", "Accuracy", "F1 Score"],
          "answer": "Recall",
          "solution": "Recall, also known as sensitivity or true positive rate, measures the model's ability to find all the positive cases (churners)."
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

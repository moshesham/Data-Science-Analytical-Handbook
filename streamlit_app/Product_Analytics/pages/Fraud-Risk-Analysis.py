import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest, RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (classification_report, confusion_matrix, average_precision_score,
                             precision_score, recall_score, f1_score)
from sklearn.preprocessing import StandardScaler

# --- Data Generation (Improved) ---
def generate_fraud_data(n_samples=1000, fraud_rate=0.05, random_state=42):
    np.random.seed(random_state)
    n_normal = int(n_samples * (1 - fraud_rate))
    n_fraud = int(n_samples * fraud_rate)

    # --- Features ---
    # Transaction Amount
    normal_amount = np.random.lognormal(mean=np.log(50), sigma=1, size=n_normal)  # Lognormal for realistic skew
    fraud_amount = np.random.lognormal(mean=np.log(500), sigma=1.5, size=n_fraud)  # Higher, more varied

    # Time of Day (0-23 hours) - More fraud at night
    normal_time = np.random.randint(0, 24, n_normal)
    fraud_time = np.random.choice(np.arange(0, 24), size=n_fraud, p=[0.08]*8 + [0.02]*8 + [0.05]*8) # Higher probability at night

    # Merchant Category (simplified)
    normal_category = np.random.choice(['Grocery', 'Retail', 'Online', 'Travel'], n_normal, p=[0.4, 0.3, 0.2, 0.1])
    fraud_category = np.random.choice(['Electronics', 'Online', 'Jewelry', 'Travel'], n_fraud, p=[0.4, 0.3, 0.2, 0.1]) #Higher risk categories

    # Number of Transactions in Last 24 Hours
    normal_freq = np.random.poisson(lam=2, size=n_normal)  # Poisson distribution
    fraud_freq = np.random.poisson(lam=5, size=n_fraud) # Higher frequency

    # Create DataFrames
    df_normal = pd.DataFrame({
        'amount': normal_amount,
        'time_of_day': normal_time,
        'merchant_category': normal_category,
        'transaction_frequency_24h': normal_freq,
        'is_fraud': 0
    })

    df_fraud = pd.DataFrame({
        'amount': fraud_amount,
        'time_of_day': fraud_time,
        'merchant_category': fraud_category,
        'transaction_frequency_24h': fraud_freq,
        'is_fraud': 1
    })

    df = pd.concat([df_normal, df_fraud], ignore_index=True)
    df = df.sample(frac=1, random_state=random_state).reset_index(drop=True) # Shuffle
    return df



# --- Helper Functions ---
def evaluate_model(y_true, y_pred, y_prob=None):
    """Evaluates model performance with various metrics."""
    metrics = {}
    metrics['precision'] = precision_score(y_true, y_pred, zero_division=0)
    metrics['recall'] = recall_score(y_true, y_pred)
    metrics['f1'] = f1_score(y_true, y_pred)
    metrics['confusion_matrix'] = confusion_matrix(y_true, y_pred)
    if y_prob is not None:
        metrics['auprc'] = average_precision_score(y_true, y_prob)
    return metrics


def plot_precision_recall_vs_threshold(y_true, y_prob):
    """Plots precision and recall against different probability thresholds."""
    thresholds = np.linspace(0, 1, 100)
    precisions = []
    recalls = []

    for threshold in thresholds:
        y_pred = (y_prob >= threshold).astype(int)
        precisions.append(precision_score(y_true, y_pred, zero_division=0))
        recalls.append(recall_score(y_true, y_pred))

    fig = px.line(x=thresholds, y=[precisions, recalls],
                  labels={'x': 'Threshold', 'y': 'Score'},
                  title='Precision and Recall vs. Threshold')
    fig.update_traces(name='Precision', selector=dict(name='y0'))
    fig.update_traces(name='Recall', selector=dict(name='y1'))
    st.plotly_chart(fig)

# --- Main App ---
def main():
    st.set_page_config(page_title="Fraud Risk Analysis", page_icon="🕵️‍♀️", layout="wide")

    st.title("Fraud Risk Analysis and Detection")
    st.write("Explore techniques for identifying and mitigating fraudulent activities.")

    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
        Fraud risk analysis is a critical process for identifying, assessing, and mitigating the risk of fraudulent activities.

        ### 1. Types of Fraud (Expanded)

        *   **Financial Statement Fraud:**  Manipulating financial statements (e.g., Enron).
        *   **Asset Misappropriation:**  Employee theft (e.g., skimming cash, inventory theft).
        *   **Corruption:**  Bribery, kickbacks, conflicts of interest.
        *   **Cyber Fraud:**  Phishing, hacking, ransomware.
        *   **Transaction Fraud:**  Unauthorized or fraudulent transactions.
            *   **Credit Card Fraud:**  Using stolen or fake credit cards.
            *   **Account Takeover (ATO):**  Gaining unauthorized access to a user's account.
            *   **New Account Fraud:**  Creating fake accounts to commit fraud.
            *   **Friendly Fraud:**  A legitimate cardholder disputes a valid charge.

        ### 2. Fraud Risk Assessment (Process)

        1.  **Identify Inherent Risks:**  What types of fraud are *possible* in your organization?
        2.  **Assess Likelihood and Impact:**  How likely is each type of fraud, and what would be the damage?
        3.  **Evaluate Existing Controls:**  What controls are already in place to prevent/detect fraud?
        4.  **Identify Control Gaps:**  Where are the weaknesses in your current controls?
        5.  **Develop and Implement Controls:**  Implement new controls or strengthen existing ones.
        6.  **Monitor and Review:**  Continuously monitor the effectiveness of controls and update the risk assessment.

        ### 3. Fraud Detection Techniques (More Detail)

        *   **Rule-Based Systems:**  Essential for catching known fraud patterns.  Examples:
            *   Flag transactions over a certain amount.
            *   Flag transactions from high-risk countries.
            *   Flag multiple transactions from the same IP address in a short time.
        *   **Statistical Analysis:**
            *   **Outlier Detection:**  Identify transactions that deviate significantly from the norm.
            *   **Benford's Law:**  Can detect fabricated numbers in financial data.
        *   **Machine Learning:**
            *   **Supervised Learning:**  Train models on labeled data (fraudulent/non-fraudulent).  Algorithms: Logistic Regression, Random Forest, Gradient Boosting.
            *   **Unsupervised Learning:**  Detect anomalies without labeled data.  Algorithm: Isolation Forest.

        ### 4.  Red Flags (Examples)

        *   **Unusual Transaction Amounts:**  Very large or very small transactions.
        *   **Unusual Transaction Times:**  Transactions occurring outside of normal business hours.
        *   **Unusual Locations:**  Transactions originating from unfamiliar or high-risk locations.
        *   **High-Risk Merchants:**  Transactions with merchants known for fraud.
        *   **Multiple Transactions in Short Time:**  Rapid sequence of transactions.
        *   **Changes to Account Information:**  Frequent changes to address, email, or password.
        *   **Inconsistencies in Data:** Mismatched billing and shipping addresses.

        ### 5. Evaluation Metrics (Beyond Accuracy)

        *   **Precision:** Out of all transactions flagged as fraud, what proportion were *actually* fraudulent?  (Minimizes false positives).
        *   **Recall:** Out of all *actual* fraudulent transactions, what proportion were correctly identified? (Minimizes false negatives).
        *   **F1-Score:**  Harmonic mean of precision and recall.
        *   **AUPRC (Area Under the Precision-Recall Curve):**  A good overall measure for imbalanced datasets.
        * **Cost-Sensitive Evaluation:** Assigning different costs to false positives and false negatives.  A missed fraud (false negative) is usually much more costly than a false alarm (false positive).

        """)

    st.header("🕵️‍♀️ Interactive Fraud Detection Demo")

    # --- Data Source ---
    data_source = st.sidebar.radio("Data Source:", ["Generate Synthetic Data", "Upload CSV"], key='data_source')

    if data_source == "Generate Synthetic Data":
        n_samples = st.sidebar.number_input("Number of Samples:", min_value=100, max_value=10000, value=1000, step=100, key='n_samp')
        fraud_rate = st.sidebar.slider("Fraud Rate (%):", min_value=0.01, max_value=0.2, value=0.05, step=0.01, key='fraud_rate')
        df = generate_fraud_data(n_samples, fraud_rate)
        st.write("Generated Transaction Data:")
        st.dataframe(df)
    else:
        uploaded_file = st.sidebar.file_uploader("Upload CSV File:", type=['csv'], key='upload')
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.write("Uploaded Data:")
                st.dataframe(df)
            except Exception as e:
                st.error(f"Error reading CSV file: {e}")
                df = None
        else:
            df = None

    if df is not None:
        # --- Exploratory Data Analysis (EDA) ---
        with st.expander("Exploratory Data Analysis (EDA) - Fraud vs. Non-Fraud"):
            st.subheader("Data Summary")
            st.write(df.describe())

            st.subheader("Fraud Rate")
            st.write(f"Fraudulent transactions: {df['is_fraud'].sum()} ({df['is_fraud'].mean() * 100:.2f}%)")

            # Visualize distributions *by fraud status*
            for col in df.select_dtypes(include=np.number):
                if col != 'is_fraud':
                  fig = px.histogram(df, x=col, color='is_fraud', marginal='box',
                                      title=f'{col} Distribution by Fraud Status',
                                      barmode='overlay')  # Overlay histograms
                  st.plotly_chart(fig)

            for col in df.select_dtypes(include='object'):
                fig = px.histogram(df, x=col, color='is_fraud', title=f'{col} Distribution by Fraud Status',
                                   barnorm='fraction') # Show proportions within each group.
                st.plotly_chart(fig)


        # --- Rule-Based Detection ---
        with st.expander("Rule-Based Fraud Detection"):
            st.subheader("Define Simple Rules")
            rule_amount = st.number_input("Flag transactions over amount:", value=1000, key='rule_amount')
            rule_time_start = st.number_input("Flag transactions between hours (start):", min_value=0, max_value=23, value=0, key='time_start')
            rule_time_end = st.number_input("Flag transactions between hours (end):", min_value=0, max_value=23, value=6, key='time_end')
            st.write("Number of unique categories")
            st.dataframe(df.select_dtypes(include='object').nunique())
            rule_category = st.multiselect("Flag transactions from categories:", df['merchant_category'].unique(), key='cat_select')

            if st.button('Apply Rules'):
                df['rule_based_flag'] = 0
                df.loc[df['amount'] > rule_amount, 'rule_based_flag'] = 1
                df.loc[(df['time_of_day'] >= rule_time_start) & (df['time_of_day'] <= rule_time_end), 'rule_based_flag'] = 1
                if len(rule_category)>0: #Handle no category selection
                    df.loc[df['merchant_category'].isin(rule_category), 'rule_based_flag'] = 1

                st.subheader("Rule-Based Detection Results")
                st.write(f"Number of transactions flagged: {df['rule_based_flag'].sum()}")
                if 'is_fraud' in df.columns:
                    st.write(classification_report(df['is_fraud'], df['rule_based_flag']))
                    st.write(confusion_matrix(df['is_fraud'], df['rule_based_flag']))

        # --- Preprocessing for Machine Learning ---
        X = df.drop('is_fraud', axis=1, errors='ignore')
        y = df['is_fraud'] if 'is_fraud' in df else None #handle no target

        # One-Hot Encode Categorical Features
        X = pd.get_dummies(X, drop_first=True) # Avoid dummy variable trap

        # Scale Numerical Features
        numerical_cols = X.select_dtypes(include=np.number).columns
        if len(numerical_cols) > 0:
            scaler = StandardScaler()
            X[numerical_cols] = scaler.fit_transform(X[numerical_cols])

        # Split Data (only if we have a target variable)
        if y is not None:
          X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        # --- Anomaly Detection (Isolation Forest) ---
          with st.expander("Anomaly Detection with Isolation Forest"):
              st.subheader("Isolation Forest")
              contamination = st.slider("Contamination (Estimated Fraud Rate):", min_value=0.01, max_value=0.5, value=0.05, step=0.01, key='iso_cont')
              model_iso = IsolationForest(n_estimators=100, contamination=contamination, random_state=42)
              if len(numerical_cols) > 0:
                  model_iso.fit(X_train)
                  df['anomaly_score'] = model_iso.decision_function(X)
                  df['anomaly'] = model_iso.predict(X)
                  df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})  # 0=normal, 1=anomaly

                  st.subheader("Isolation Forest Results")
                  st.write(classification_report(y, df['anomaly'])) # Evaluate on *entire* dataset
                  st.write(confusion_matrix(y, df['anomaly']))


        # --- Supervised Learning ---
          with st.expander("Supervised Learning for Fraud Detection"):
              st.subheader("Supervised Learning Models")
              model_type = st.selectbox("Select Model:", ["Logistic Regression", "Random Forest", "Gradient Boosting"], key='sup_model')

              if st.button("Train and Evaluate", key='train_eval'):
                  if model_type == "Logistic Regression":
                      model = LogisticRegression(random_state=42, solver='liblinear')
                  elif model_type == "Random Forest":
                      model = RandomForestClassifier(random_state=42)
                  elif model_type == "Gradient Boosting":
                      model = GradientBoostingClassifier(random_state=42)

                  model.fit(X_train, y_train)
                  y_pred = model.predict(X_test)
                  y_prob = model.predict_proba(X_test)[:, 1]  # Probabilities for class 1

                  st.subheader(f"{model_type} - Results")
                  metrics = evaluate_model(y_test, y_pred, y_prob)

                  for metric_name, metric_value in metrics.items():
                    if metric_name != "confusion_matrix":
                        st.write(f"{metric_name}: {metric_value:.4f}")

                  st.write("Confusion Matrix:")
                  st.write(metrics['confusion_matrix'])
                  plot_precision_recall_vs_threshold(y_test, y_prob)


        # --- Combined Approach (Example) ---
          with st.expander("Combined Approach (Example)"):
              st.subheader("Combining Rule-Based and Machine Learning")
              st.markdown("""
                A common strategy is to use a combination of techniques:

                1.  **Rule-Based System:**  Flags high-risk transactions based on predefined rules.
                2.  **Machine Learning Model:**  Scores transactions for fraud probability.
                3.  **Thresholding:**  Set thresholds for both rule-based flags and model scores.
                4.  **Investigation:**  Transactions exceeding *either* threshold are flagged for review.
                """)

              if 'rule_based_flag' in df.columns and 'anomaly_score' in df.columns: # Only proceed if we have both
                  combined_threshold_rule = st.number_input("Rule-Based Flag Threshold (0 or 1)", min_value=0, max_value=1, value=1, key='comb_threshold')
                  combined_threshold_ml = st.slider("Anomaly Score Threshold (lower = more likely fraud):", df['anomaly_score'].min(), df['anomaly_score'].max(), value=df['anomaly_score'].quantile(0.1), step=0.01, key='comb_ml_thresh')
                  df['combined_flag'] = 0
                  df.loc[(df['rule_based_flag'] >= combined_threshold_rule) | (df['anomaly_score'] <= combined_threshold_ml), 'combined_flag'] = 1


                  st.subheader("Combined Approach Results")
                  if y is not None:
                      st.write(classification_report(y, df['combined_flag']))
                      st.write(confusion_matrix(y, df['combined_flag']))

    st.header("💪 Practice Exercises")
    st.markdown("""
    1. **Analyze a publicly available fraud dataset.** (e.g., credit card fraud datasets on Kaggle).
    2. **Develop a more comprehensive rule-based system.**  Consider various red flags and combinations of factors.
    3. **Experiment with different machine learning models and hyperparameters.**  Compare their performance using appropriate metrics (precision, recall, AUPRC).
    4. **Research fraud prevention techniques in a specific industry.**  (e.g., e-commerce, banking).
    5. **Design a cost-sensitive evaluation framework.**  Assign different costs to false positives and false negatives based on business context.
    """)

    st.header("🌍 Real-world Applications")
    st.markdown("""
    Fraud risk analysis is crucial in:

    *   **Banking:** Credit card fraud, loan fraud, money laundering.
    *   **Insurance:**  Fraudulent claims.
    *   **E-commerce:**  Payment fraud, account takeover.
    *   **Healthcare:**  Billing fraud, identity theft.
    *   **Government:**  Tax evasion, benefit fraud.
    """)

    st.header("✅ Knowledge Check")
    quiz_questions = [
        {
            "question": "What is the difference between supervised and unsupervised learning in fraud detection?",
            "options": ["Supervised learning requires labeled data, while unsupervised learning does not.",
                        "Unsupervised learning is always more accurate than supervised learning.",
                        "Supervised learning is only used for rule-based systems.",
                        "Unsupervised learning is only used for anomaly detection."],
            "answer": "Supervised learning requires labeled data, while unsupervised learning does not.",
            "solution": "Supervised learning uses examples of known fraud to train a model, while unsupervised learning identifies anomalies without prior knowledge."
        },
        {
            "question": "Why is accuracy a poor metric for evaluating fraud detection models?",
            "options": ["Accuracy is too difficult to calculate.",
                        "Fraud datasets are usually imbalanced (many more non-fraudulent transactions), so accuracy can be misleadingly high.",
                        "Accuracy only considers false positives.",
                        "Accuracy only considers false negatives."],
            "answer": "Fraud datasets are usually imbalanced (many more non-fraudulent transactions), so accuracy can be misleadingly high.",
            "solution": "A model that predicts 'no fraud' for every transaction can have high accuracy but be completely useless."
        },
        {
            "question": "What does 'precision' measure in the context of fraud detection?",
            "options": ["The proportion of actual fraudulent transactions that were correctly identified.",
                        "The proportion of predicted fraudulent transactions that were actually fraudulent.",
                        "The overall accuracy of the model.",
                        "The speed of the model."],
            "answer": "The proportion of predicted fraudulent transactions that were actually fraudulent.",
            "solution": "High precision means fewer false positives."
        },
        {
            "question": "What does 'recall' measure in the context of fraud detection?",
            "options": ["The proportion of actual fraudulent transactions that were correctly identified.",
                        "The proportion of predicted fraudulent transactions that were actually fraudulent.",
                        "The overall accuracy of the model.",
                        "The speed of the model."],
            "answer": "The proportion of actual fraudulent transactions that were correctly identified.",
            "solution": "High recall means fewer false negatives (missed fraud)."
        },
        {
            "question": "What is a 'false positive' in fraud detection?",
            "options": ["A fraudulent transaction that is correctly identified.",
                        "A fraudulent transaction that is missed.",
                        "A legitimate transaction that is incorrectly flagged as fraudulent.",
                        "A legitimate transaction that is correctly identified."],
            "answer": "A legitimate transaction that is incorrectly flagged as fraudulent.",
            "solution": "False positives can lead to unnecessary investigations and customer inconvenience."
        },
        {
            "question": "What is a 'false negative' in fraud detection?",
            "options": ["A fraudulent transaction that is correctly identified.",
                        "A fraudulent transaction that is missed.",
                        "A legitimate transaction that is incorrectly flagged as fraudulent.",
                        "A legitimate transaction that is correctly identified."],
            "answer": "A fraudulent transaction that is missed.",
            "solution": "False negatives represent actual fraud that goes undetected."
        },
        {
            "question": "What is a common advantage of using rule-based systems for fraud detection?",
            "options": ["They can detect complex, unknown patterns.",
                       "They are easy to implement and interpret.",
                       "They don't require any historical data.",
                       "They are always more accurate than machine learning models."],
            "answer": "They are easy to implement and interpret.",
            "solution": "Rule-based systems are good for capturing known fraud scenarios."
        },
         {
            "question": "Which of the following is a good practice for generating synthetic fraud data?",
            "options": ["Make fraudulent transactions identical to normal transactions.",
                        "Create subtle and varied differences between fraudulent and normal transactions.",
                        "Only change one feature to indicate fraud.",
                        "Make the fraud rate extremely high (e.g., 50%)."],
            "answer": "Create subtle and varied differences between fraudulent and normal transactions.",
            "solution": "Realistic synthetic data should reflect the complexities of real-world fraud."
        },
        {
            "question": "What is the purpose of stratifying the data when splitting into training and testing sets?",
            "options": ["To ensure that both sets have a similar distribution of the target variable (fraud/no fraud).",
                        "To make the training set larger than the test set.",
                        "To randomly shuffle the data.",
                        "To remove outliers from the data."],
            "answer": "To ensure that both sets have a similar distribution of the target variable (fraud/no fraud).",
            "solution": "Stratification is especially important for imbalanced datasets."
        },
        {
            "question": "What is a good way to handle categorical features in a machine learning model for fraud detection?",
            "options": ["Ignore them.",
                        "Use one-hot encoding.",
                        "Convert them to sequential integers.",
                        "Use only numerical features."],
            "answer": "Use one-hot encoding.",
            "solution": "One-hot encoding creates binary columns for each category, allowing the model to use the information."
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

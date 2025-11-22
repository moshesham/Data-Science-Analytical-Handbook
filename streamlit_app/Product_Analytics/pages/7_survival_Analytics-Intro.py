import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines import CoxPHFitter
from lifelines.datasets import load_rossi  # Example dataset
from io import StringIO  # For handling CSV input as string
from typing import Optional  # For type hinting

def main():
    st.set_page_config(page_title="Survival Analysis", page_icon="⏳", layout="wide")

    st.title("Survival Analysis: Time-to-Event Modeling")
    st.write("Understand and predict the time until a specific event, like customer churn or equipment failure, using robust statistical methods.") # More concise intro

    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
        Survival analysis is a branch of statistics for analyzing the expected *duration* until one or more events. It's distinct from standard regression because the time-to-event outcome is often *censored*, meaning the event is not observed for all subjects.

        ### Core Concepts:

        1.  **Time-to-Event (T):** The duration until the event.  The *dependent* variable. Examples:
            *   Customer churn (time until unsubscribe).
            *   Machine failure (time until component breaks).
            *   Patient relapse (time until disease recurrence).

        2.  **Censoring:** Incomplete observation of event times. This is the defining characteristic of survival data.
            *   **Right Censoring (Most Common):** We know the subject survived *at least* until a certain time, but the event occurs *after* our observation ends.  Examples:
                *   Customer remains subscribed at study's end.
                *   Patient is alive when data collection stops.
                *   Subject drops out of the study prematurely.
            *   **Left Censoring:** The event occurred *before* a certain time; the exact time is unknown. Example:
                *   Disease present at a check-up, but onset is unknown.
            *   **Interval Censoring:** The event occurs within a known time interval, but the precise time is unknown. Example:
                *   Machine inspected monthly; failure occurred between inspections.

        3.  **Survival Function (S(t)):** Probability that a subject survives *longer than* time *t*.  `S(t) = P(T > t)`, where *T* is the (random) survival time. Properties:
            *   `S(0) = 1` (Everyone's alive at time 0).
            *   `S(t)` is non-increasing (survival probability can't increase).
            *   As `t` → ∞, `S(t)` → 0 (eventually, the event happens).

        4.  **Hazard Function (h(t)):** *Instantaneous* risk of the event at time *t*, *given survival up to t*. This is a *conditional* probability, expressed as a *rate*.  It's *not* `P(T = t)`.  Mathematically:

            `h(t) = lim (Δt -> 0) [ P(t ≤ T < t + Δt | T ≥ t) / Δt ]`

            Higher `h(t)` means higher risk *at that moment*, given the subject has reached that time.

        5.  **Cumulative Hazard Function (H(t)):** Total accumulated risk up to time *t*. The integral of the hazard function.

        ### Key Methods:

        1.  **Kaplan-Meier Estimator (Non-Parametric):**
            *   Estimates `S(t)` directly from data *without* assuming any specific distribution for survival times.
            *   Calculated as a series of step-downs at each observed event time. Step size depends on the number at risk.
                *   Formula (at each event time, t_i): `S(t_i) = S(t_(i-1)) * ( (n_i - d_i) / n_i )`
                    *   `n_i`: Number of individuals at risk at time `t_i` (just before the event).
                    *   `d_i`: Number of events (e.g., deaths, churns) at time `t_i`.

        2.  **Cox Proportional Hazards Model (Semi-Parametric):**
            *   A regression model for the *hazard function*, `h(t)`.
            *   Models the relationship between covariates (predictors) and the hazard.
            *   **Critical Assumption: Proportional Hazards.** The hazard ratio between any two individuals remains *constant* over time, even if the baseline hazard changes.  This is a strong assumption and *must* be checked.
            *   Formula: `h(t|X) = h0(t) * exp(β1X1 + β2X2 + ... + βpXp)`
                *   `h(t|X)`: Hazard for individual with covariates X.
                *   `h0(t)`: Baseline hazard (hazard when all covariates are 0).
                *   `βi`: Coefficients (log hazard ratios).
                *   `Xi`: Covariate values.
            *   **Hazard Ratio (HR):** `exp(βi)`.  The multiplicative effect of a one-unit change in covariate Xi on the hazard.
                *   HR > 1: Increased hazard.
                *   HR < 1: Decreased hazard (protective).
                *   HR = 1: No effect.

        **Further Reading:** (Same excellent links)
            *   [Survival Analysis (Wikipedia)](https://en.wikipedia.org/wiki/Survival_analysis)
            *   [Lifelines Documentation](https://lifelines.readthedocs.io/en/latest/)
        """)

    st.header("🔄 Interactive Demo")

    demo_choice = st.selectbox("Choose a Demo:", ["Kaplan-Meier Estimator", "Cox Proportional Hazards Model"])

    if demo_choice == "Kaplan-Meier Estimator":
        st.subheader("Kaplan-Meier Estimator")
        st.write("Estimate the survival function from time-to-event data.")

        data_source = st.radio("Data Source:", ["Use Example Dataset", "Upload CSV", "Paste CSV Data"])

        if data_source == "Use Example Dataset":
            data = load_rossi()
            time_col = 'week'
            event_col = 'arrest'
            group_col = None

        elif data_source == "Upload CSV":
            uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
            if uploaded_file is not None:
                try:
                    data = pd.read_csv(uploaded_file)
                except Exception as e:
                    st.error(f"Error reading CSV: {e}")
                    data = None
            else:
                data = None

        else:  # data_source == "Paste CSV Data"
            csv_data = st.text_area("Paste your CSV data here:", height=200)
            if csv_data:
                try:
                    data = pd.read_csv(StringIO(csv_data))
                except Exception as e:
                    st.error(f"Error reading CSV data: {e}")
                    data = None
            else:
                data = None

        # 1. **Function for Data Loading and Validation:**  Improves code organization and reusability.
        def load_and_validate_data(data: Optional[pd.DataFrame], data_source: str) -> Optional[pd.DataFrame]:
            if data is None:
                return None

            if data_source != "Use Example Dataset":
                time_col = st.selectbox("Select Time Column:", data.columns)
                event_col = st.selectbox("Select Event Column (1=event, 0=censored):", data.columns)
                group_col = st.selectbox("Select Grouping Column (optional):", ["None"] + list(data.columns), index=0)
                if group_col == "None":
                    group_col = None
            else:
                time_col = 'week'  # For example dataset
                event_col = 'arrest'
                group_col = None

            st.write("Data Preview:")
            st.dataframe(data.head())

             # Data Validation (same as before, but now in the function)
            if data[time_col].isnull().any() or data[event_col].isnull().any():
                st.error(f"Missing values found in Time ({time_col}) or Event ({event_col}) columns.  Please clean your data.")
                return None

            if not all(data[event_col].isin([0, 1])):
                st.error(f"Event column ({event_col}) must contain only 0 (censored) and 1 (event).")
                return None

            if (data[time_col] < 0).any():
                st.error(f"Time column ({time_col}) contains negative values. Time-to-event must be non-negative.")
                return None
            return data, time_col, event_col, group_col # Return all necessary variables.

        data_and_cols = load_and_validate_data(data, data_source)
        if data_and_cols is None: # Check and stop the program.
            st.stop()
        else:
            data, time_col, event_col, group_col = data_and_cols #Unpack values


        kmf = KaplanMeierFitter()

        if group_col:
            fig, ax = plt.subplots()
            for name, grouped_data in data.groupby(group_col):
                kmf.fit(grouped_data[time_col], grouped_data[event_col], label=name)
                kmf.plot_survival_function(ax=ax)
            plt.xlabel("Time")
            plt.ylabel("Survival Probability")
            plt.title("Kaplan-Meier Survival Curves by Group")
            plt.ylim(0, 1)
            plt.legend()
            st.pyplot(fig)

            st.write("Median Survival Times:")
            for name, grouped_data in data.groupby(group_col):
                kmf.fit(grouped_data[time_col], grouped_data[event_col], label=name)
                # 2.  Clearer Median Survival Output:  Use f-strings for better formatting.
                st.write(f"Group: {name}, Median Survival: {kmf.median_survival_time_ if kmf.median_survival_time_ != np.inf else 'Not reached'}")


        else:
            kmf.fit(data[time_col], data[event_col])
            fig, ax = plt.subplots()
            kmf.plot_survival_function(ax=ax)
            plt.xlabel("Time")
            plt.ylabel("Survival Probability")
            plt.title("Kaplan-Meier Survival Curve")
            plt.ylim(0, 1)
            st.pyplot(fig)

            median_survival = kmf.median_survival_time_ if kmf.median_survival_time_ != np.inf else "Not reached"
            st.write(f"Median Survival Time: {median_survival}")

            conf_int = kmf.confidence_interval_survival_function_
            st.write("95% Confidence Interval for Survival Function:")
            st.dataframe(conf_int)



    elif demo_choice == "Cox Proportional Hazards Model":
        st.subheader("Cox Proportional Hazards Model")
        st.write("Analyze the impact of covariates on survival.")

        data_source = st.radio("Data Source:", ["Use Example Dataset", "Upload CSV", "Paste CSV Data"])

        if data_source == "Use Example Dataset":
            data = load_rossi()
            time_col = 'week'
            event_col = 'arrest'
            covariate_cols = ['fin', 'age', 'race', 'wexp', 'mar', 'paro', 'prio']

        elif data_source == "Upload CSV":
             uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
             if uploaded_file is not None:
                try:
                    data = pd.read_csv(uploaded_file)

                except Exception as e:
                    st.error(f"Error: {e}")
                    data = None
             else:
                data = None
        else: # Paste CSV data
            csv_data = st.text_area("Paste your CSV data here:", height = 200)
            if csv_data:
                try:
                    data = pd.read_csv(StringIO(csv_data))
                except Exception as e:
                    st.error(f"Error reading pasted CSV data: {e}")
                    data = None
            else:
                data = None
        #3. Reusing the data loading and validation logic
        def load_and_validate_cox_data(data: Optional[pd.DataFrame], data_source:str) -> Optional[pd.DataFrame]:
            if data is None:
                return None

            if data_source != "Use Example Dataset":
                time_col = st.selectbox("Select Time Column:", data.columns)
                event_col = st.selectbox("Select Event Column (1=event, 0=censored):", data.columns)
                covariate_cols = st.multiselect("Select Covariate Columns:", data.columns)
            else:
                time_col = 'week' # For example dataset
                event_col = 'arrest'
                covariate_cols = ['fin', 'age', 'race', 'wexp', 'mar', 'paro', 'prio']


            st.write("Data Preview:")
            st.dataframe(data.head())

            if data[time_col].isnull().any() or data[event_col].isnull().any() or data[covariate_cols].isnull().any():
                st.error("Missing values found. Please clean your data.")
                return None

            if not all(data[event_col].isin([0, 1])):
                st.error(f"Event column ({event_col}) must contain only 0 and 1.")
                return None

            if (data[time_col] < 0).any():
                st.error(f"Time column ({time_col}) contains negative values.")
                return None

            return data, time_col, event_col, covariate_cols

        cox_data_and_cols = load_and_validate_cox_data(data, data_source)
        if cox_data_and_cols is None:
            st.stop()
        else:
            data, time_col, event_col, covariate_cols = cox_data_and_cols


        cph = CoxPHFitter()
        try:
            cph.fit(data[[time_col, event_col] + covariate_cols], time_col, event_col=event_col)

            with st.expander("Model Summary"):
                st.text(cph.print_summary(model="CoxPH Model", decimals=3)) # 4. Control Decimal Places

            st.subheader("Hazard Ratios")
            st.write("Hazard ratios (exponentiated coefficients) indicate the multiplicative effect on the hazard.")
            st.dataframe(np.exp(cph.summary['coef']).rename(columns={'coef':'Hazard Ratio'}))

            st.subheader("Survival Curves")
            st.write("Plot survival curves for different covariate values (select one covariate to vary).")

            if covariate_cols:
                covariate_to_plot = st.selectbox("Select Covariate to Plot:", covariate_cols)
                if pd.api.types.is_numeric_dtype(data[covariate_to_plot]):
                        values_to_plot = st.slider(f"Select {covariate_to_plot} values:", data[covariate_to_plot].min(), data[covariate_to_plot].max(), (data[covariate_to_plot].quantile(0.25), data[covariate_to_plot].quantile(0.75)))

                else: # Categorical
                    values_to_plot = data[covariate_to_plot].unique().tolist()

                fig, ax = plt.subplots()
                try:
                    cph.plot_partial_effects_on_outcome(covariate_to_plot, values_to_plot, cmap='coolwarm', ax=ax)
                    plt.xlabel("Time")
                    plt.ylabel("Survival Probability")
                    plt.title(f"Survival Curves by {covariate_to_plot}")
                    plt.ylim(0, 1)
                    st.pyplot(fig)
                except Exception as e:
                    st.error(f"Error plotting survival curves: {e}")


        except Exception as e:
            st.error(f"Error fitting Cox model: {e}")

    st.header("💪 Practice Exercises")
    st.markdown("""
    1.  **Interpretation:** In the Kaplan-Meier example, what does a horizontal line at S(t) = 0.8 mean?
    2.  **Censoring:** Give an example of right-censoring in a customer churn context.
    3.  **Hazard Ratio:** If a Cox model shows a hazard ratio of 2 for a feature, what does that imply?
        *   Bonus: What if the hazard ratio is 0.5?
    """)
    if st.button("Show Answers"):
        st.markdown("""
        1.  **Interpretation:**  A horizontal line at S(t) = 0.8 means that the estimated probability of surviving *longer than* that time point is 80%.
        2.  **Censoring:**  A customer is still subscribed at the *end* of the observation period. We know they survived *at least* that long, but not their total subscription time (we don't see them churn).
        3.  **Hazard Ratio:**
            *   Hazard Ratio of 2:  Having that feature *doubles* the hazard (instantaneous risk of the event) compared to *not* having the feature, holding other variables constant.
            *   Bonus: Hazard Ratio of 0.5: Having that feature *halves* the hazard (it's a *protective* factor).
        """)

    st.header("🌍 Real-world Applications")
    st.write("""
    Survival analysis is widely used in:

    *   **Customer Churn:** Predicting when customers will unsubscribe (key for SaaS businesses).
    *   **Predictive Maintenance:** Estimating time until equipment failure (critical for manufacturing).
    *   **Medical Research:** Analyzing patient survival times after treatment (essential for clinical trials).
    *   **Credit Risk:** Modeling time until loan default.
    *   **Marketing:** Analyzing time until customer conversion or response to a campaign.
    *   **Human Resources:** Studying employee retention and time-to-attrition.
    """)

    st.header("✅ Knowledge Check")
    # 9.  Better Quiz Questions: More conceptual, less tied to specific code, and include solutions.
    quiz_questions = [
        {
            "question": "What does *right-censoring* mean in survival analysis?",
            "options": ["The event happened before the study started.",
                        "The event happened during the study, but at an unknown time.",
                        "The event hasn't happened yet by the end of the observation period.",
                        "The event will never happen."],
            "answer": "The event hasn't happened yet by the end of the observation period.",
            "solution": "Right-censoring is the most common type. We only know the subject survived *at least* until the censoring time, but we don't know their full survival time."
        },
        {
            "question": "The survival function, S(t), gives the probability of...",
            "options": ["Experiencing the event *at* time t.",
                        "Surviving *beyond* time t.",
                        "Experiencing the event *before* time t.",
                        "The instantaneous risk of the event at time t."],
            "answer": "Surviving *beyond* time t.",
            "solution": "S(t) = P(T > t), where T is the survival time. It's the probability of *not* having the event before time t."
        },
        {
            "question": "The hazard function, h(t), represents the...",
            "options": ["Probability of surviving beyond time t.",
                        "Probability of the event happening at time t.",
                        "Instantaneous risk of the event at time t, *given survival up to t*.",
                        "Total accumulated risk up to time t."],
            "answer": "Instantaneous risk of the event at time t, *given survival up to t*.",
            "solution": "The hazard function is a *rate*, not a probability.  It's the *conditional* probability of the event happening in the next instant, given the subject has survived up to time t."
        },
        {
            "question": "The Kaplan-Meier estimator is:",
            "options": ["A parametric method.",
                        "A non-parametric method.",
                        "A regression model.",
                        "Used only for small datasets."],
            "answer": "A non-parametric method.",
            "solution": "The Kaplan-Meier estimator makes *no* assumptions about the underlying distribution of survival times. This makes it very flexible."
        },
        {
            "question": "The Cox Proportional Hazards model is:",
            "options": ["A non-parametric method.",
                        "Used only for estimating the survival function.",
                        "A regression model for the hazard function.",
                        "Only applicable when there is no censoring."],
            "answer": "A regression model for the hazard function.",
            "solution": "The Cox model allows us to analyze the impact of covariates (predictor variables) on the *hazard rate*."
        },
        {
            "question": "A hazard ratio of 0.5 for a feature in a Cox model means:",
            "options": ["The feature increases the hazard by 50%.",
                        "The feature decreases the hazard by 50%.",
                        "The feature has no effect on the hazard.",
                        "The feature increases survival time by 50%."],
            "answer": "The feature decreases the hazard by 50%.",
            "solution": "A hazard ratio *less than 1* indicates a *protective* effect (reduced hazard). A hazard ratio of 0.5 means the hazard is halved."
        },
        {
            "question": "What is the main advantage of the Kaplan-Meier estimator?",
            "options": ["It can handle covariates.",
                        "It's very computationally efficient.",
                        "It doesn't assume a specific distribution for survival times.",
                        "It can predict future survival times accurately."],
            "answer": "It doesn't assume a specific distribution for survival times.",
            "solution": "This non-parametric nature makes it very flexible and robust to different data patterns."
        },
        {
            "question": "What is the primary assumption of the Cox Proportional Hazards model?",
            "options": ["Survival times are normally distributed.",
                        "The hazard function is constant over time.",
                        "The hazard ratio between individuals is constant over time.",
                        "There is no censoring."],
            "answer": "The hazard ratio between individuals is constant over time.",
            "solution": "This is the 'proportional hazards' assumption. The *baseline* hazard can change, but the *relative* hazards between individuals with different covariate values remain proportional."
        },
        {
            "question": "In a customer churn context, what does right-censoring typically represent?",
            "options": ["The customer churned at the beginning of the study.",
                        "The customer churned during the study.",
                        "The customer was still subscribed at the end of the study (or observation period).",
                        "The customer churned before the study began."],
            "answer": "The customer was still subscribed at the end of the study (or observation period).",
            "solution": "Right-censoring means we don't observe the churn event (the event of interest) within our study period.  We only know they survived *at least* until the end of observation."
        },
        {
            "question": "What is the median survival time?",
            "options": ["The time at which the hazard function is highest.",
                        "The average survival time.",
                        "The time at which the survival probability is 0.5.",
                        "The time at which all individuals have experienced the event."],
            "answer": "The time at which the survival probability is 0.5.",
            "solution": "The median survival time is the point where S(t) = 0.5.  It's the time by which 50% of subjects have experienced the event."
        },
        {
            "question": "If you increase the sample size, what generally happens to the confidence intervals for the Kaplan-Meier estimate?",
            "options": ["They become wider.",
                       "They become narrower.",
                       "They stay the same.",
                       "It depends on the censoring rate."],
            "answer": "They become narrower.",
            "solution": "Larger sample sizes lead to more precise estimates, and therefore narrower confidence intervals."
        },
        {
          "question": "Which of the following is NOT a typical application of survival analysis?",
          "options":["Predicting customer lifetime value",
                     "Analyzing time until equipment failure.",
                     "Estimating patient survival after surgery.",
                     "Determining optimal pricing for a product."],
          "answer":  "Determining optimal pricing for a product.",
          "solution": "While survival analysis *could* be creatively applied to pricing (e.g., time until a customer accepts a certain price), it's not a standard application. The other options are classic examples."

        }
    ]

    user_answers = []
    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i+1}. {question['question']}**")
        user_answer = st.radio("Select an answer", question["options"], key=f"quiz_question_{i}")
        user_answers.append(user_answer)


    if st.button("Submit Quiz"):
        num_correct = 0
        for user_answer, question in zip(user_answers, quiz_questions):
            if user_answer == question["answer"]:
                num_correct += 1

        # 10.  Clear and Concise Feedback:  Directly state the score.
        st.write(f"You scored {num_correct} / {len(quiz_questions)}")

        with st.expander("Show Detailed Solutions"):
            for i, question in enumerate(quiz_questions):
                st.markdown(f"**Question {i+1}:** {question['question']}")
                st.markdown(f"**Your Answer:** {user_answers[i]}")
                st.markdown(f"**Correct Answer:** {question['answer']}")
                st.markdown(f"**Solution:** {question['solution']}")
                if user_answers[i] == question['answer']:
                    st.success("Correct!")  # Immediate feedback
                else:
                    st.error("Incorrect.")

if __name__ == "__main__":
    main()




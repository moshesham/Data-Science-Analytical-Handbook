from io import StringIO  # For handling CSV input as string

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from lifelines import CoxPHFitter, KaplanMeierFitter
from lifelines.datasets import load_rossi  # Example dataset


def show_theoretical_concepts():
    with st.expander("📖 Theoretical Concepts"):
        st.markdown(
            """
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
        """
        )


def show_interactive_demo():
    demo_choice = st.selectbox(
        "Choose a Demo:",
        ["Kaplan-Meier Estimator", "Cox Proportional Hazards Model", "Quiz"],
    )

    if demo_choice == "Kaplan-Meier Estimator":
        show_kaplan_meier_demo()
    elif demo_choice == "Cox Proportional Hazards Model":
        show_cox_model_demo()
    elif demo_choice == "Quiz":
        show_quiz()


def show_kaplan_meier_demo():
    st.subheader("Kaplan-Meier Estimator")
    st.write("Estimate the survival function from time-to-event data.")

    data, time_col, event_col, group_col = load_kaplan_meier_data()
    if data is None:
        st.stop()

    plot_kaplan_meier_results(data, time_col, event_col, group_col)


def load_kaplan_meier_data():
    data_source = st.radio(
        "Data Source:", ["Use Example Dataset", "Upload CSV", "Paste CSV Data"]
    )

    data = load_data_by_source(data_source)
    return validate_kaplan_meier_data(data, data_source)


def load_data_by_source(data_source):
    if data_source == "Use Example Dataset":
        return load_rossi()
    elif data_source == "Upload CSV":
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
        if uploaded_file is not None:
            try:
                return pd.read_csv(uploaded_file)
            except Exception as e:
                st.error(f"Error reading CSV: {e}")
        return None
    else:  # data_source == "Paste CSV Data"
        csv_data = st.text_area("Paste your CSV data here:", height=200)
        if csv_data:
            try:
                return pd.read_csv(StringIO(csv_data))
            except Exception as e:
                st.error(f"Error reading CSV data: {e}")
        return None


def validate_kaplan_meier_data(data, data_source):
    if data is None:
        return None, None, None, None

    if data_source != "Use Example Dataset":
        time_col = st.selectbox("Select Time Column:", data.columns)
        event_col = st.selectbox(
            "Select Event Column (1=event, 0=censored):", data.columns
        )
        group_col = st.selectbox(
            "Select Grouping Column (optional):",
            ["None"] + list(data.columns),
            index=0,
        )
        if group_col == "None":
            group_col = None
    else:
        time_col = "week"  # For example dataset
        event_col = "arrest"
        group_col = None

    st.write("Data Preview:")
    st.dataframe(data.head())

    # Data Validation
    if data[time_col].isnull().any() or data[event_col].isnull().any():
        st.error(
            f"Missing values found in Time ({time_col}) or Event ({event_col}) columns.  Please clean your data."
        )
        return None, None, None, None

    if not all(data[event_col].isin([0, 1])):
        st.error(
            f"Event column ({event_col}) must contain only 0 (censored) and 1 (event)."
        )
        return None, None, None, None

    if (data[time_col] < 0).any():
        st.error(
            f"Time column ({time_col}) contains negative values. Time-to-event must be non-negative."
        )
        return None, None, None, None

    return data, time_col, event_col, group_col


def plot_kaplan_meier_results(data, time_col, event_col, group_col):
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
            st.write(
                f"Group: {name}, Median Survival: {kmf.median_survival_time_ if kmf.median_survival_time_ != np.inf else 'Not reached'}"
            )

    else:
        kmf.fit(data[time_col], data[event_col])
        fig, ax = plt.subplots()
        kmf.plot_survival_function(ax=ax)
        plt.xlabel("Time")
        plt.ylabel("Survival Probability")
        plt.title("Kaplan-Meier Survival Curve")
        plt.ylim(0, 1)
        st.pyplot(fig)

        median_survival = (
            kmf.median_survival_time_
            if kmf.median_survival_time_ != np.inf
            else "Not reached"
        )
        st.write(f"Median Survival Time: {median_survival}")

        conf_int = kmf.confidence_interval_survival_function_
        st.write("95% Confidence Interval for Survival Function:")
        st.dataframe(conf_int)


def show_cox_model_demo():
    st.subheader("Cox Proportional Hazards Model")
    st.write("Analyze the impact of covariates on survival.")

    data, time_col, event_col, covariate_cols = load_cox_model_data()
    if data is None:
        st.stop()

    plot_cox_model_results(data, time_col, event_col, covariate_cols)


def load_cox_model_data():
    data_source = st.radio(
        "Data Source:", ["Use Example Dataset", "Upload CSV", "Paste CSV Data"]
    )

    data = load_data_by_source(data_source)
    return validate_cox_model_data(data, data_source)


def validate_cox_model_data(data, data_source):
    if data is None:
        return None, None, None, None

    if data_source != "Use Example Dataset":
        time_col = st.selectbox("Select Time Column:", data.columns)
        event_col = st.selectbox(
            "Select Event Column (1=event, 0=censored):", data.columns
        )
        covariate_cols = st.multiselect(
            "Select Covariate Columns:",
            [col for col in data.columns if col not in [time_col, event_col]],
        )
    else:
        time_col = "week"
        event_col = "arrest"
        covariate_cols = ["fin", "age", "race", "wexp", "mar", "paro", "prio"]

    st.write("Data Preview:")
    st.dataframe(data.head())

    # Data validation
    if data[time_col].isnull().any() or data[event_col].isnull().any():
        st.error(f"Missing values in Time ({time_col}) or Event ({event_col}) columns.")
        return None, None, None, None

    if not all(data[event_col].isin([0, 1])):
        st.error(f"Event column ({event_col}) must be 0/1.")
        return None, None, None, None

    if (data[time_col] < 0).any():
        st.error("Time values must be non-negative.")
        return None, None, None, None

    if not covariate_cols:
        st.error("Select at least one covariate.")
        return None, None, None, None

    return data, time_col, event_col, covariate_cols


def plot_cox_model_results(data, time_col, event_col, covariate_cols):
    # Fit Cox model
    cph = CoxPHFitter()
    cph.fit(
        data[[time_col, event_col] + covariate_cols],
        duration_col=time_col,
        event_col=event_col,
    )

    # Display results
    st.write("Model Summary:")
    st.dataframe(cph.summary)

    # Plot hazard ratios
    fig, ax = plt.subplots()
    cph.plot(ax=ax)
    plt.title("Hazard Ratios (log scale)")
    st.pyplot(fig)

    # Check proportional hazards assumption
    if st.button("Check Proportional Hazards Assumption"):
        try:
            cph.check_assumptions(
                data[[time_col, event_col] + covariate_cols], p_value_threshold=0.05
            )
            st.success("Proportional hazards assumption appears to hold.")
        except Exception as e:
            st.error(f"Proportional hazards assumption may be violated: {e}")


def show_quiz():
    st.subheader("Survival Analysis Quiz")
    st.write("Test your understanding of survival analysis concepts!")

    quiz_questions = [
        {
            "question": "What is the primary difference between survival analysis and standard regression?",
            "options": [
                "Survival analysis uses different statistical tests.",
                "Survival analysis deals with censored data.",
                "Survival analysis requires larger sample sizes.",
                "Survival analysis only works with time data.",
            ],
            "answer": "Survival analysis deals with censored data.",
            "solution": "Survival analysis is specifically designed to handle censored observations, where the event of interest is not observed for all subjects within the study period.",
        },
        {
            "question": "What does right-censoring mean?",
            "options": [
                "The event occurred before the study began.",
                "The event occurred after the study ended.",
                "The subject was removed from the study.",
                "The data was recorded incorrectly.",
            ],
            "answer": "The event occurred after the study ended.",
            "solution": "Right-censoring occurs when we know a subject survived at least until a certain time, but the event happens after our observation period ends.",
        },
        {
            "question": "What does the survival function S(t) represent?",
            "options": [
                "The probability of experiencing the event at time t.",
                "The probability of surviving longer than time t.",
                "The rate of events at time t.",
                "The total number of events by time t.",
            ],
            "answer": "The probability of surviving longer than time t.",
            "solution": "S(t) = P(T > t), where T is the survival time. It represents the probability that a subject survives beyond time t.",
        },
        {
            "question": "What is the hazard function h(t)?",
            "options": [
                "The probability of the event at time t.",
                "The instantaneous risk of the event at time t, given survival to t.",
                "The cumulative risk up to time t.",
                "The expected survival time.",
            ],
            "answer": "The instantaneous risk of the event at time t, given survival to t.",
            "solution": "The hazard function represents the instantaneous risk rate at time t for subjects who have survived up to that time.",
        },
        {
            "question": "What does a hazard ratio of 2.0 mean?",
            "options": [
                "The event is twice as likely to occur.",
                "The survival time is doubled.",
                "The risk is doubled compared to the baseline.",
                "The study lasted twice as long.",
            ],
            "answer": "The risk is doubled compared to the baseline.",
            "solution": "A hazard ratio of 2.0 means the hazard (risk) is twice as high for that group compared to the reference group.",
        },
        {
            "question": "What is the Kaplan-Meier estimator used for?",
            "options": [
                "Estimating hazard ratios.",
                "Estimating the survival function from data.",
                "Testing proportional hazards.",
                "Fitting parametric survival models.",
            ],
            "answer": "Estimating the survival function from data.",
            "solution": "The Kaplan-Meier estimator is a non-parametric method to estimate the survival function directly from observed data.",
        },
        {
            "question": "What is a key assumption of the Cox proportional hazards model?",
            "options": [
                "Survival times follow an exponential distribution.",
                "The hazard ratio between groups remains constant over time.",
                "All covariates are normally distributed.",
                "The censoring rate is less than 50%.",
            ],
            "answer": "The hazard ratio between groups remains constant over time.",
            "solution": "The proportional hazards assumption means that the relative risk between any two individuals remains constant over time.",
        },
        {
            "question": "What does it mean if the median survival time is 'not reached'?",
            "options": [
                "The data was censored.",
                "More than 50% of subjects experienced the event.",
                "The study ended before 50% experienced the event.",
                "The calculation was incorrect.",
            ],
            "answer": "The study ended before 50% experienced the event.",
            "solution": "When median survival time is 'not reached', it means that less than 50% of subjects experienced the event during the study period.",
        },
        {
            "question": "In survival analysis, what does 'at risk' mean?",
            "options": [
                "Subjects who have already experienced the event.",
                "Subjects who are still being observed and haven't experienced the event yet.",
                "Subjects who were censored.",
                "Subjects with complete follow-up.",
            ],
            "answer": "Subjects who are still being observed and haven't experienced the event yet.",
            "solution": "'At risk' refers to subjects who are still under observation and have not yet experienced the event of interest.",
        },
        {
            "question": "What is the customer was still subscribed at the end of the study (or observation period).",
            "options": [
                "Left censoring",
                "Right censoring",
                "Interval censoring",
                "No censoring",
            ],
            "answer": "Right censoring",
            "solution": "Right-censoring means we don't observe the churn event (the event of interest) within our study period.  We only know they survived *at least* until the end of observation.",
        },
        {
            "question": "What is the median survival time?",
            "options": [
                "The time at which the hazard function is highest.",
                "The average survival time.",
                "The time at which the survival probability is 0.5.",
                "The time at which all individuals have experienced the event.",
            ],
            "answer": "The time at which the survival probability is 0.5.",
            "solution": "The median survival time is the point where S(t) = 0.5.  It's the time by which 50% of subjects have experienced the event.",
        },
        {
            "question": "If you increase the sample size, what generally happens to the confidence intervals for the Kaplan-Meier estimate?",
            "options": [
                "They become wider.",
                "They become narrower.",
                "They stay the same.",
                "It depends on the censoring rate.",
            ],
            "answer": "They become narrower.",
            "solution": "Larger sample sizes lead to more precise estimates, and therefore narrower confidence intervals.",
        },
        {
            "question": "Which of the following is NOT a typical application of survival analysis?",
            "options": [
                "Predicting customer lifetime value",
                "Analyzing time until equipment failure.",
                "Estimating patient survival after surgery.",
                "Determining optimal pricing for a product.",
            ],
            "answer": "Determining optimal pricing for a product.",
            "solution": "While survival analysis *could* be creatively applied to pricing (e.g., time until a customer accepts a certain price), it's not a standard application. The other options are classic examples.",
        },
    ]

    user_answers = []
    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i+1}. {question['question']}**")
        user_answer = st.radio(
            "Select an answer", question["options"], key=f"quiz_question_{i}"
        )
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
                if user_answers[i] == question["answer"]:
                    st.success("Correct!")  # Immediate feedback
                else:
                    st.error("Incorrect.")


def main():
    st.set_page_config(page_title="Survival Analysis", page_icon="⏳", layout="wide")

    st.title("Survival Analysis: Time-to-Event Modeling")
    st.write(
        "Understand and predict the time until a specific event, like customer churn or equipment failure, using robust statistical methods."
    )  # More concise intro

    show_theoretical_concepts()

    show_interactive_demo()


if __name__ == "__main__":
    main()

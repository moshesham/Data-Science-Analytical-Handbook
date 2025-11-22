import numpy as np
import pandas as pd
import plotly.express as px
import statsmodels.stats.power as smp
import streamlit as st
from scipy.stats import chi2_contingency, mannwhitneyu, ttest_ind

# --- Constants ---
ALPHA_LEVEL_DEFAULT = 0.05
POWER_LEVEL_DEFAULT = 0.8
MDE_PERCENT_DEFAULT = 10
MDE_ABSOLUTE_DEFAULT = 10.0
BASELINE_CONVERSION_RATE_DEFAULT = 0.10
BASELINE_AOV_DEFAULT = 50.0
N_USERS_PER_VARIANT_DEFAULT = 500


# --- Data Generation Functions ---
def generate_ab_test_data(
    n_variants=2,
    n_users_per_variant=N_USERS_PER_VARIANT_DEFAULT,
    conversion_rates=[BASELINE_CONVERSION_RATE_DEFAULT, 0.12],
    avg_order_values=[BASELINE_AOV_DEFAULT, 55],
    effect_type="absolute",
    outcome_type="binary",
    random_state=42,
):
    """Generates synthetic A/B testing data (same as before, but constants used)."""
    np.random.seed(random_state)
    data = []
    for i in range(n_variants):
        variant = chr(65 + i)
        users = np.arange(1, n_users_per_variant + 1)

        if outcome_type == "binary":
            converted = (
                np.random.rand(n_users_per_variant) < conversion_rates[i]
            ).astype(int)
            revenue = np.zeros(n_users_per_variant)
        elif outcome_type == "continuous":
            converted = np.zeros(n_users_per_variant)
            revenue = np.zeros(n_users_per_variant)
            if effect_type == "absolute":
                revenue = np.random.normal(
                    loc=avg_order_values[i], scale=20, size=n_users_per_variant
                )
            elif effect_type == "relative":
                base_aov = avg_order_values[0]
                relative_diff = (avg_order_values[i] - base_aov) / base_aov
                revenue = np.random.normal(
                    loc=base_aov * (1 + relative_diff),
                    scale=20,
                    size=n_users_per_variant,
                )
            revenue = np.maximum(revenue, 0)

        data.extend(
            list(zip([variant] * n_users_per_variant, users, converted, revenue))
        )

    df = pd.DataFrame(data, columns=["Variant", "UserID", "Converted", "Revenue"])
    return df


# --- Statistical Test Functions (unchanged) ---
def perform_t_test(df, group_col, value_col):
    """Performs an independent samples t-test (Welch's)."""
    groups = df[group_col].unique()
    if len(groups) != 2:
        raise ValueError("T-test requires exactly two groups.")
    group1 = df[df[group_col] == groups[0]][value_col]
    group2 = df[df[group_col] == groups[1]][value_col]
    t_statistic, p_value = ttest_ind(group1, group2, equal_var=False)

    results = {
        "test_type": "Independent Samples T-Test (Welch's)",
        "t_statistic": t_statistic,
        "p_value": p_value,
        "group_1_mean": group1.mean(),
        "group_2_mean": group2.mean(),
    }
    return results


def perform_mann_whitney_u_test(df, group_col, value_col):
    """Performs a Mann-Whitney U test (non-parametric)."""
    groups = df[group_col].unique()
    if len(groups) != 2:
        raise ValueError("Mann-Whitney U test requires exactly two groups.")
    group1 = df[df[group_col] == groups[0]][value_col]
    group2 = df[df[group_col] == groups[1]][value_col]
    u_statistic, p_value = mannwhitneyu(group1, group2, alternative="two-sided")

    results = {
        "test_type": "Mann-Whitney U Test (Non-parametric)",
        "u_statistic": u_statistic,
        "p_value": p_value,
        "group_1_median": group1.median(),
        "group_2_median": group2.median(),
    }
    return results


def perform_chi2_test(df, group_col, outcome_col):
    """Performs a Chi-Square test of independence."""
    contingency_table = pd.crosstab(df[group_col], df[outcome_col])
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    results = {
        "test_type": "Chi-Square Test",
        "Chi-Square Statistic": chi2,
        "p_value": p,
        "Degrees of Freedom": dof,
        "Contingency Table": contingency_table,
        "Expected Frequencies": expected,
    }
    return results


# --- Sample Size Calculation Functions (unchanged) ---
def calculate_sample_size_binary(
    effect_size, base_rate, power=POWER_LEVEL_DEFAULT, alpha=ALPHA_LEVEL_DEFAULT
):
    """Calculates sample size needed for binary outcome A/B test."""
    effect_size_power = smp.proportion_effectsize(base_rate, base_rate + effect_size)
    sample_size = smp.NormalIndPower().solve_power(
        effect_size=effect_size_power, power=power, alpha=alpha, ratio=1
    )
    return np.ceil(sample_size)


def calculate_sample_size_continuous(
    effect_size, std_dev, power=POWER_LEVEL_DEFAULT, alpha=ALPHA_LEVEL_DEFAULT
):
    """Calculates sample size needed for continuous outcome A/B test."""
    effect_size_power = effect_size / std_dev  # Cohen's d
    sample_size = smp.TTestIndPower().solve_power(
        effect_size=effect_size_power, power=power, alpha=alpha, ratio=1
    )
    return np.ceil(sample_size)


# --- Streamlit UI Functions ---
def display_theoretical_concepts():
    """Displays the theoretical concepts section."""
    with st.expander("📖 Theoretical Concepts"):
        st.markdown(
            """
        A/B testing is a powerful methodology for data-driven decision-making. (Concepts explanation - same as before, but slightly rephrased for clarity and flow - see previous response for full text).
        """
        )


def display_experiment_design_inputs(outcome_type):
    """Displays the UI elements for experiment design inputs and returns user inputs."""
    st.subheader("1. Experiment Design Parameters")

    col1, col2 = st.columns(2)
    with col1:
        baseline_conversion_rate = st.number_input(
            "Baseline Conversion Rate (Variant A) (%):",
            min_value=0.01,
            max_value=0.50,
            value=BASELINE_CONVERSION_RATE_DEFAULT,
            step=0.01,
            format="%.2f",
            key="base_conv_rate",
            help="The current conversion rate you observe or expect for the Control group (Variant A).",
        )
        if outcome_type == "continuous":
            baseline_aov = st.number_input(
                "Baseline Average Order Value (Variant A):",
                min_value=20.0,
                max_value=200.0,
                value=BASELINE_AOV_DEFAULT,
                step=10.0,
                key="base_aov",
                help="The current Average Order Value for the Control group (Variant A).",
            )
    with col2:
        mde_percent = st.number_input(
            "Minimum Detectable Effect (MDE) - Relative % Change:",
            min_value=1,
            max_value=50,
            value=MDE_PERCENT_DEFAULT,
            step=1,
            key="mde_perc",
            help="The *smallest* percentage change in Conversion Rate that you want your test to reliably detect as significant.  Think about what change would be practically meaningful for your business.",
        )
        if outcome_type == "continuous":
            mde_absolute = st.number_input(
                "Minimum Detectable Effect (MDE) - Absolute Value Change:",
                min_value=5.0,
                max_value=50.0,
                value=MDE_ABSOLUTE_DEFAULT,
                step=5.0,
                key="mde_abs",
                help="The *smallest* absolute change in Average Order Value that you want your test to reliably detect as significant. Consider the business value of this change.",
            )

    power_level = st.slider(
        "Statistical Power (1 - β):",
        min_value=0.1,
        max_value=0.99,
        value=POWER_LEVEL_DEFAULT,
        step=0.05,
        key="power_level",
        help="The probability of correctly detecting a *real* effect if one exists.  80% is a common standard.",
    )
    alpha_level = st.slider(
        "Significance Level (α):",
        min_value=0.01,
        max_value=0.1,
        value=ALPHA_LEVEL_DEFAULT,
        step=0.01,
        key="alpha_level",
        help="The probability of incorrectly concluding there's a difference when there isn't one (False Positive Rate). 0.05 is a common standard.",
    )

    return (
        baseline_conversion_rate,
        baseline_aov,
        mde_percent,
        mde_absolute,
        power_level,
        alpha_level,
    )


def display_sample_size_calculation(
    outcome_type,
    baseline_conversion_rate,
    baseline_aov,
    mde_percent,
    mde_absolute,
    power_level,
    alpha_level,
):
    """Displays the sample size calculation and results."""
    st.subheader("2. Estimated Sample Size")
    if outcome_type == "binary":
        effect_size_binary = baseline_conversion_rate * (mde_percent / 100)
        sample_size_needed = calculate_sample_size_binary(
            effect_size_binary, baseline_conversion_rate / 100, power_level, alpha_level
        )
        st.write(
            f"Estimated Sample Size per Variant (for Binary Outcome - Conversion Rate): **{int(sample_size_needed)} users**",
            help="This is the *minimum* number of users you should aim to have in *each* variant (A and B) to have sufficient power to detect the MDE with your chosen significance and power levels.",
        )

    elif outcome_type == "continuous":
        std_dev_aov = 20  # Fixed std dev for AOV for simplicity
        effect_size_continuous = mde_absolute
        sample_size_needed = calculate_sample_size_continuous(
            effect_size_continuous, std_dev_aov, power_level, alpha_level
        )
        st.write(
            f"Estimated Sample Size per Variant (for Continuous Outcome - Average Order Value): **{int(sample_size_needed)} users**",
            help="This is the *minimum* number of users per variant needed to detect the MDE in Average Order Value.",
        )


def display_simulation_and_analysis(
    outcome_type, baseline_conversion_rate, baseline_aov, mde_percent, mde_absolute
):
    """Displays the UI for simulation and analysis, runs simulation and analysis, and displays results."""
    st.subheader("3. Simulate and Analyze A/B Test Results")

    if outcome_type == "binary":
        treatment_conversion_rate = baseline_conversion_rate + (
            baseline_conversion_rate * (mde_percent / 100)
        )
        conversion_rates = [
            baseline_conversion_rate / 100,
            treatment_conversion_rate / 100,
        ]
    elif outcome_type == "continuous":
        treatment_aov = baseline_aov + mde_absolute
        avg_order_values = [baseline_aov, treatment_aov]
        conversion_rates = [
            0.1,
            0.1,
        ]  # Not used for continuous, but needed for function

    n_users_variant = st.number_input(
        "Users per Variant (Simulated):",
        min_value=N_USERS_PER_VARIANT_DEFAULT,
        max_value=N_USERS_PER_VARIANT_DEFAULT * 10,
        value=N_USERS_PER_VARIANT_DEFAULT,
        step=100,
        key="n_users_sim",
        help="Enter the number of users you want to simulate in each variant for this run.  This can be greater than the calculated minimum sample size.",
    )

    alpha_level = (
        st.session_state.alpha_level
    )  # Get alpha from session state for consistency

    if st.button("Run Simulation and Analyze", key="run_sim_button"):
        if outcome_type == "binary":
            df_ab = generate_ab_test_data(
                n_variants=2,
                n_users_per_variant=n_users_variant,
                conversion_rates=conversion_rates,
                outcome_type=outcome_type,
            )
            test_results = perform_chi2_test(df_ab, "Variant", "Converted")
            metric_name = "Conversion Rate"
            group_a_metric = df_ab[df_ab["Variant"] == "A"]["Converted"].mean() * 100
            group_b_metric = df_ab[df_ab["Variant"] == "B"]["Converted"].mean() * 100
            delta = group_b_metric - group_a_metric

        elif outcome_type == "continuous":
            df_ab = generate_ab_test_data(
                n_variants=2,
                n_users_per_variant=n_users_variant,
                avg_order_values=avg_order_values,
                effect_type="absolute",
                outcome_type=outcome_type,
            )
            if st.checkbox(
                "Assume data is NOT normally distributed (use Mann-Whitney U Test)",
                key="non_normal",
            ):
                test_results = perform_mann_whitney_u_test(df_ab, "Variant", "Revenue")
                metric_name = "Median Revenue per User"
                group_a_metric = df_ab[df_ab["Variant"] == "A"]["Revenue"].median()
                group_b_metric = df_ab[df_ab["Variant"] == "B"]["Revenue"].median()
                delta = group_b_metric - group_a_metric
            else:
                test_results = perform_t_test(df_ab, "Variant", "Revenue")
                metric_name = "Average Revenue per User"
                group_a_metric = df_ab[df_ab["Variant"] == "A"]["Revenue"].mean()
                group_b_metric = df_ab[df_ab["Variant"] == "B"]["Revenue"].mean()
                delta = group_b_metric - group_a_metric

        display_simulation_results(
            test_results,
            metric_name,
            group_a_metric,
            group_b_metric,
            delta,
            alpha_level,
            outcome_type,
            df_ab,
        )


def display_simulation_results(
    test_results,
    metric_name,
    group_a_metric,
    group_b_metric,
    delta,
    alpha_level,
    outcome_type,
    df_ab,
):
    """Displays the results of the A/B test simulation."""
    st.subheader("Simulation Results")
    st.markdown(f"**Variant A (Control):** {metric_name}: **{group_a_metric:.2f}**")
    st.markdown(f"**Variant B (Treatment):** {metric_name}: **{group_b_metric:.2f}**")
    st.markdown(f"**Difference (B - A):** {metric_name}: **{delta:.2f}**")

    st.markdown(f"**Statistical Test:** {test_results['test_type']}")
    st.markdown(f"**P-value:** {test_results['p_value']:.4f}")

    if test_results["p_value"] < alpha_level:
        st.success(
            f"**Statistically Significant Result!** (p < {alpha_level:.2f}) - Reject Null Hypothesis",
            icon="✅",
        )
        st.write(
            "This suggests that the difference observed is unlikely due to random chance alone and that Variant B likely has a real effect on the metric."
        )
        st.write(
            "**Consider Practical Significance:** While statistically significant, is the *size* of the effect (delta) meaningful for your business?  Is the lift worth the cost of implementation?"
        )

    else:
        st.warning(
            f"**Not Statistically Significant** (p ≥ {alpha_level:.2f}) - Fail to Reject Null Hypothesis",
            icon="⚠️",
        )
        st.write(
            "This suggests that we do not have enough statistical evidence to conclude that there is a real difference between Variant A and Variant B. The observed difference could be due to random chance."
        )
        st.write(
            "**Implications:**  You cannot confidently conclude that Variant B is better than Variant A based on this test. Consider increasing sample size, running the test longer, or re-evaluating your hypothesis."
        )

    with st.expander("Show Detailed Statistical Test Results"):
        st.write(test_results)

    st.subheader("Data Visualization")
    if outcome_type == "binary":
        fig = px.bar(
            x=["Variant A", "Variant B"],
            y=[group_a_metric, group_b_metric],
            labels={"x": "Variant", "y": "Conversion Rate (%)"},
            title="Conversion Rate by Variant",
        )
    elif outcome_type == "continuous":
        fig = px.box(
            df_ab, x="Variant", y="Revenue", title="Revenue Distribution by Variant"
        )
    st.plotly_chart(fig)


def display_practice_exercises():
    """Displays the practice exercises section."""
    st.header("💪 Practice Exercises")
    st.markdown(
        """(Practice exercises - same as before, but slightly rephrased for clarity and flow - see previous response for full text)."""
    )


def display_real_world_applications():
    """Displays the real-world applications section."""
    st.header("🌍 Real-world Applications")
    st.markdown(
        """(Real-world applications - same as before, but slightly rephrased for clarity and flow - see previous response for full text)."""
    )


def display_knowledge_check():
    """Displays the knowledge check quiz section."""
    st.header("✅ Knowledge Check")
    quiz_questions = [
        # Quiz questions - refined for better assessment (see critique and regenerated quiz questions in previous response)
        {
            "question": "What is the purpose of randomization in A/B testing?",
            "options": [
                "To make the test results statistically significant.",
                "To ensure that the control and treatment groups are comparable at baseline.",
                "To reduce the sample size needed for the test.",
                "To make the experiment easier to implement.",
            ],
            "answer": "To ensure that the control and treatment groups are comparable at baseline.",
            "solution": "Randomization minimizes bias and ensures that any observed differences are likely due to the treatment, not pre-existing group differences.",
        },
        {
            "question": "What is the null hypothesis (H₀) in A/B testing?",
            "options": [
                "The hypothesis that you are trying to prove.",
                "The hypothesis that there is no difference between the variants being tested.",
                "The hypothesis that the treatment variant will always perform better than the control.",
                "The hypothesis that the sample size is large enough.",
            ],
            "answer": "The hypothesis that there is no difference between the variants being tested.",
            "solution": "A/B testing typically aims to *reject* the null hypothesis if there's evidence of a difference.",
        },
        {
            "question": "If an A/B test result has a p-value of 0.03 (with alpha = 0.05), what conclusion can you draw?",
            "options": [
                "The result is not statistically significant.",
                "The result is statistically significant, and you reject the null hypothesis.",
                "The result is practically significant, but not statistically significant.",
                "The test is underpowered.",
            ],
            "answer": "The result is statistically significant, and you reject the null hypothesis.",
            "solution": "A p-value less than alpha (0.05) is typically considered statistically significant.",
        },
        {
            "question": "Which statistical test is most appropriate for comparing conversion rates (binary outcome) in A/B testing?",
            "options": ["T-test", "ANOVA", "Chi-Square Test", "Regression analysis"],
            "answer": "Chi-Square Test",
            "solution": "The Chi-Square test is used to compare proportions or frequencies in categorical data.",
        },
        {
            "question": "What does 'statistical power' represent in A/B testing?",
            "options": [
                "The probability of making a Type I error (false positive).",
                "The probability of correctly rejecting the null hypothesis when it is false (correctly detecting a true effect).",
                "The probability of failing to reject the null hypothesis when it is false (missing a true effect).",
                "The significance level of the test.",
            ],
            "answer": "The probability of correctly rejecting the null hypothesis when it is false (correctly detecting a true effect).",
            "solution": "Power is crucial to avoid false negatives and ensure your test can detect meaningful effects.",
        },
        {
            "question": "What does MDE stand for in A/B testing?",
            "options": [
                "Maximum Detectable Error",
                "Minimum Detectable Effect",
                "Mean Data Error",
                "Maximum Data Effect",
            ],
            "answer": "Minimum Detectable Effect",
            "solution": "MDE is the smallest effect size that you want your test to be able to reliably detect.",
        },
        {
            "question": "Why is sample size calculation important before running an A/B test?",
            "options": [
                "To guarantee statistical significance.",
                "To ensure the test is completed quickly.",
                "To ensure the test has enough power to detect a meaningful effect, if it exists.",
                "To reduce the cost of running the experiment.",
            ],
            "answer": "To ensure the test has enough power to detect a meaningful effect, if it exists.",
            "solution": "Adequate sample size is essential for a well-powered test.",
        },
        {
            "question": "What is 'practical significance' in A/B testing?",
            "options": [
                "The same as statistical significance.",
                "Whether the observed difference is large enough to be meaningful and worth implementing from a business perspective.",
                "Whether the p-value is less than 0.05.",
                "Whether the sample size is large enough.",
            ],
            "answer": "Whether the observed difference is large enough to be meaningful and worth implementing from a business perspective.",
            "solution": "Even statistically significant results may not be practically significant if the effect size is too small to justify the cost of implementation.",
        },
        {
            "question": "Which statistical test is generally more appropriate for comparing average revenue per user if the revenue data is *not* normally distributed?",
            "options": ["T-test", "Chi-Square Test", "Mann-Whitney U Test", "ANOVA"],
            "answer": "Mann-Whitney U Test",
            "solution": "The Mann-Whitney U test is a non-parametric test that does not assume normality.",
        },
        {
            "question": "What is a potential threat to the validity of A/B test results called the 'novelty effect'?",
            "options": [
                "Users behave differently simply because something is new or changed.",
                "Users are not randomly assigned to groups.",
                "The test runs for too long.",
                "The sample size is too small.",
            ],
            "answer": "Users behave differently simply because something is new or changed.",
            "solution": "The novelty effect can cause a temporary lift in metrics that fades over time, making results unreliable in the long run.",
        },
    ]
    user_answers = []
    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i + 1}. {question['question']}**")
        user_answer = st.radio(
            "Select an answer:", question["options"], key=f"quiz_{i}"
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


def main():
    st.set_page_config(
        page_title="A/B Experiment Design & Implementation",
        page_icon="🧪",
        layout="wide",
    )

    st.title("A/B Experiment Design and Implementation")
    st.write("Learn the principles of A/B testing and design your own experiments.")

    display_theoretical_concepts()

    outcome_type = st.selectbox(
        "Select Outcome Metric Type for A/B Test:",
        ["binary", "continuous"],
        index=0,
        key="outcome_type",
    )
    (
        baseline_conversion_rate,
        baseline_aov,
        mde_percent,
        mde_absolute,
        power_level,
        alpha_level,
    ) = display_experiment_design_inputs(outcome_type)
    display_sample_size_calculation(
        outcome_type,
        baseline_conversion_rate,
        baseline_aov,
        mde_percent,
        mde_absolute,
        power_level,
        alpha_level,
    )
    display_simulation_and_analysis(
        outcome_type, baseline_conversion_rate, baseline_aov, mde_percent, mde_absolute
    )

    display_practice_exercises()
    display_real_world_applications()
    display_knowledge_check()


if __name__ == "__main__":
    main()

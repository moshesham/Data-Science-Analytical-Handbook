import streamlit as st


def main():
    st.set_page_config(
        page_title="Creating Effective KRIs and KPIs", page_icon="🎯", layout="wide"
    )

    st.title("Creating Informative KRIs and KPIs")
    st.write(
        "Learn how to define, design, and implement effective Key Risk Indicators (KRIs) and Key Performance Indicators (KPIs)."
    )

    with st.expander("📖 Theoretical Concepts"):
        st.markdown(
            """
        KRIs and KPIs are essential tools for monitoring and managing risk and performance.  However, poorly designed indicators can be misleading or ineffective.

        ### 1. Key Differences

        *   **KPI (Key Performance Indicator):** Measures *performance* against strategic objectives.  Focuses on *achieving goals*.  Often forward-looking.
        *   **KRI (Key Risk Indicator):** Measures *risk exposure* and the likelihood of adverse events. Focuses on *preventing problems*. Often leading indicators of potential issues.

        ### 2. Characteristics of Effective Indicators

        *   **SMART:**
            *   **Specific:**  Clearly defined and unambiguous.
            *   **Measurable:**  Quantifiable using reliable data.
            *   **Achievable/Attributable:**  Can be influenced by actions (for KPIs) or linked to specific risks (for KRIs).
            *   **Relevant:**  Aligned with strategic objectives (KPIs) or key risks (KRIs).
            *   **Time-bound:**  Measured and reported at appropriate intervals.
        *   **Actionable:**  Provides insights that can lead to specific actions or decisions.
        *   **Understandable:**  Easily interpreted by stakeholders.
        *   **Balanced:**  Covers a range of perspectives (e.g., financial, customer, operational).
        * **Leading vs Lagging**: KPIs are often lagging indicators of past performance. KRIs should ideally be *leading* indicators, providing early warning of potential problems.

        ### 3. Defining KRIs and KPIs: A Step-by-Step Approach

        1.  **Identify Objectives/Risks:**  Start with strategic objectives (for KPIs) or key risks (for KRIs).
        2.  **Define Indicators:**  For each objective/risk, define specific, measurable indicators.
        3.  **Establish Targets/Thresholds:**  Set targets (KPIs) or thresholds (KRIs) that define acceptable levels of performance or risk.
        4.  **Data Sources and Collection:**  Identify the data sources and establish processes for collecting the data.
        5.  **Reporting and Monitoring:**  Determine the frequency and format for reporting and monitoring the indicators.
        6.  **Review and Refine:**  Regularly review and refine the indicators to ensure they remain relevant and effective.

        ### 4. Common Mistakes to Avoid

        *   **Too Many Indicators:**  Focus on a small number of *key* indicators.
        *   **Vague Indicators:**  Use clear, specific definitions.
        *   **Lack of Targets/Thresholds:**  Without targets/thresholds, it's difficult to assess performance or risk.
        *   **Poor Data Quality:**  Ensure the data used to calculate the indicators is accurate and reliable.
        *   **Ignoring Context:**  Consider the broader context when interpreting indicators.
        * **No Ownership:** Indicators should have clear owners responsible for monitoring and reporting.

        **Further Reading:**
            *   [KPIs vs. KRIs (ClearRisk)](https://www.clearrisk.com/risk-management-blog/kpis-vs-kris)
            *   [Key Performance Indicators (KPIs) (Investopedia)](https://www.investopedia.com/terms/k/kpi.asp)
            * [Key Risk Indicators (KRIs) (Corporate Finance Institute)](https://corporatefinanceinstitute.com/resources/management/key-risk-indicators-kris/)
        """
        )

    st.header("📝 Interactive Design Tool")

    indicator_type = st.selectbox("Select Indicator Type:", ["KPI", "KRI"])

    if indicator_type == "KPI":
        st.subheader("Defining a Key Performance Indicator (KPI)")

        # Step 1: Objective
        objective = st.text_input(
            "1. Strategic Objective:", "Increase customer satisfaction"
        )

        # Step 2: KPI Definition
        kpi_name = st.text_input("2. KPI Name:", "Customer Satisfaction Score")
        kpi_definition = st.text_area(
            "3. KPI Definition:",
            "The average customer satisfaction rating based on a survey (1-5 scale).",
        )
        kpi_formula = st.text_input(
            "4. KPI Formula:", "Total Satisfaction Ratings / Number of Respondents"
        )

        # Step 3: Target
        target_type = st.selectbox(
            "Target Type:", ["Specific Value", "Range", "Improvement over Baseline"]
        )
        if target_type == "Specific Value":
            target_value = st.number_input("Target Value:", min_value=0.0, value=4.5)
        elif target_type == "Range":
            lower_bound = st.number_input("Lower Bound:", min_value=0.0, value=4.0)
            upper_bound = st.number_input(
                "Upper Bound:", min_value=lower_bound, value=4.8
            )  # Ensure upper>lower
        elif target_type == "Improvement over Baseline":
            baseline_value = st.number_input(
                "Baseline Value:", min_value=0.0, value=3.8
            )
            improvement_percentage = st.number_input(
                "Improvement Percentage:", min_value=0.0, value=10.0
            )
            target_value = baseline_value * (1 + (improvement_percentage / 100))
            st.write(f"Target: {target_value:.2f}")  # display calculated target

        # Step 4: Data Source and Collection
        data_source = st.text_input(
            "5. Data Source:", "Customer satisfaction survey responses"
        )
        collection_frequency = st.selectbox(
            "6. Collection Frequency:",
            ["Daily", "Weekly", "Monthly", "Quarterly", "Annually"],
        )
        data_owner = st.text_input("7. Data Owner:", "Customer Service Department")

        # Step 5: Reporting and Monitoring
        reporting_frequency = st.selectbox(
            "8. Reporting Frequency:",
            ["Daily", "Weekly", "Monthly", "Quarterly", "Annually"],
        )
        reporting_format = st.text_input(
            "9. Reporting Format:", "Dashboard, email report"
        )
        review_frequency = st.selectbox(
            "10. Review Frequency:", ["Monthly", "Quarterly", "Annually"]
        )

        if st.button("Generate KPI Summary"):
            st.subheader("KPI Summary:")
            st.markdown(f"**Objective:** {objective}")
            st.markdown(f"**KPI Name:** {kpi_name}")
            st.markdown(f"**Definition:** {kpi_definition}")
            st.markdown(f"**Formula:** {kpi_formula}")
            if target_type == "Specific Value":
                st.markdown(f"**Target:** {target_value}")
            elif target_type == "Range":
                st.markdown(f"**Target Range:** {lower_bound} - {upper_bound}")
            elif target_type == "Improvement over Baseline":
                st.markdown(
                    f"**Target:** {target_value:.2f}"
                )  # display calculated target

            st.markdown(f"**Data Source:** {data_source}")
            st.markdown(f"**Collection Frequency:** {collection_frequency}")
            st.markdown(f"**Data Owner:** {data_owner}")
            st.markdown(f"**Reporting Frequency:** {reporting_frequency}")
            st.markdown(f"**Reporting Format:** {reporting_format}")
            st.markdown(f"**Review Frequency:** {review_frequency}")

            # SMART Assessment
            st.subheader("SMART Assessment")
            smart_assessment = {
                "Specific": "✅" if kpi_definition else "❌",
                "Measurable": "✅" if kpi_formula else "❌",
                "Achievable/Attributable": "❓ (Needs further analysis)",  # Placeholder, needs more context.
                "Relevant": "✅" if objective else "❌",  # Basic check, needs context.
                "Time-bound": "✅"
                if collection_frequency and reporting_frequency
                else "❌",
            }

            for key, value in smart_assessment.items():
                st.write(f"{key}: {value}")

    elif indicator_type == "KRI":
        st.subheader("Defining a Key Risk Indicator (KRI)")

        # Step 1: Risk
        risk = st.text_input("1. Key Risk:", "Data breach due to unauthorized access")

        # Step 2: KRI Definition
        kri_name = st.text_input("2. KRI Name:", "Number of Failed Login Attempts")
        kri_definition = st.text_area(
            "3. KRI Definition:",
            "The number of failed login attempts per user per day.",
        )
        kri_formula = st.text_input(
            "4. KRI Formula:", "Total Failed Login Attempts / Number of Users"
        )

        # Step 3: Thresholds
        threshold_type = st.selectbox(
            "Threshold Type", ["Upper Limit", "Lower Limit", "Range"]
        )

        if threshold_type == "Upper Limit":
            upper_threshold = st.number_input("Upper Threshold:", min_value=0, value=5)

        elif threshold_type == "Lower Limit":
            lower_threshold = st.number_input("Lower Threshold:", min_value=0, value=0)

        elif threshold_type == "Range":
            lower_threshold = st.number_input("Lower Threshold:", min_value=0, value=1)
            upper_threshold = st.number_input(
                "Upper Threshold:", min_value=lower_threshold, value=5
            )  # ensure upper > lower

        # Step 4: Data Source and Collection
        data_source = st.text_input("5. Data Source:", "System login logs")
        collection_frequency = st.selectbox(
            "6. Collection Frequency:", ["Real-time", "Hourly", "Daily", "Weekly"]
        )
        data_owner = st.text_input("7. Data Owner:", "IT Security Department")

        # Step 5: Reporting and Monitoring
        reporting_frequency = st.selectbox(
            "8. Reporting Frequency:", ["Real-time", "Hourly", "Daily", "Weekly"]
        )
        reporting_format = st.text_input(
            "9. Reporting Format:", "Dashboard, alert notification"
        )
        review_frequency = st.selectbox(
            "10. Review Frequency:", ["Monthly", "Quarterly", "Annually"]
        )

        if st.button("Generate KRI Summary"):
            st.subheader("KRI Summary:")
            st.markdown(f"**Risk:** {risk}")
            st.markdown(f"**KRI Name:** {kri_name}")
            st.markdown(f"**Definition:** {kri_definition}")
            st.markdown(f"**Formula:** {kri_formula}")
            if threshold_type == "Upper Limit":
                st.markdown(f"**Threshold:**  ≤ {upper_threshold}")
            elif threshold_type == "Lower Limit":
                st.markdown(f"**Threshold:** ≥ {lower_threshold}")
            elif threshold_type == "Range":
                st.markdown(
                    f"**Threshold Range:** {lower_threshold} - {upper_threshold}"
                )

            st.markdown(f"**Data Source:** {data_source}")
            st.markdown(f"**Collection Frequency:** {collection_frequency}")
            st.markdown(f"**Data Owner:** {data_owner}")
            st.markdown(f"**Reporting Frequency:** {reporting_frequency}")
            st.markdown(f"**Reporting Format:** {reporting_format}")
            st.markdown(f"**Review Frequency:** {review_frequency}")

            # SMART Assessment
            st.subheader("SMART Assessment")
            smart_assessment = {
                "Specific": "✅" if kri_definition else "❌",
                "Measurable": "✅" if kri_formula else "❌",
                "Achievable/Attributable": "❓ (Needs further analysis)",  # Placeholder.
                "Relevant": "✅" if risk else "❌",  # Basic check, needs more context
                "Time-bound": "✅"
                if collection_frequency and reporting_frequency
                else "❌",
            }

            for key, value in smart_assessment.items():
                st.write(f"{key}: {value}")

    st.header("💪 Practice Exercises")
    st.markdown(
        """
    1. **Identify 3-5 KPIs for a specific business or department (e.g., sales, marketing, customer service).**  Use the SMART criteria to define each KPI.
    2. **Identify 3-5 KRIs for a specific organization or industry (e.g., healthcare, finance, manufacturing).**  Use the SMART criteria to define each KRI.
    3. **Develop a reporting template for a KPI or KRI.**  Include the indicator name, definition, formula, target/threshold, current value, trend, and any relevant comments.
    4. **Analyze a set of existing KPIs or KRIs.**  Assess whether they meet the SMART criteria and identify any areas for improvement.
    5.  **Consider a scenario where a KPI target is consistently missed or a KRI threshold is frequently breached.**  What actions might be taken?
    """
    )

    st.header("🌍 Real-world Applications")
    st.markdown(
        """
    KRIs and KPIs are used in virtually all industries and functions:

    *   **Finance:**  Return on equity (KPI), credit risk exposure (KRI).
    *   **Sales:**  Sales growth (KPI), number of lost deals (KRI).
    *   **Marketing:**  Conversion rate (KPI), customer acquisition cost (KPI), brand sentiment (KRI).
    *   **Operations:**  Production efficiency (KPI), number of defects (KRI).
    *   **IT:**  System uptime (KPI), number of security incidents (KRI).
    *   **Human Resources:**  Employee satisfaction (KPI), employee turnover rate (KPI), number of safety incidents (KRI).
    * **Healthcare:** Patient Wait Times (KPI), Hospital-Acquired Infection Rate (KRI)
    """
    )

    st.header("✅ Knowledge Check")
    quiz_questions = [
        {
            "question": "What is the main difference between a KPI and a KRI?",
            "options": [
                "KPIs measure performance, while KRIs measure risk.",
                "KPIs are leading indicators, while KRIs are lagging indicators.",
                "KPIs are used for external reporting, while KRIs are used for internal monitoring.",
                "KPIs are quantitative, while KRIs are qualitative.",
            ],
            "answer": "KPIs measure performance, while KRIs measure risk.",
            "solution": "KPIs focus on achieving strategic objectives, while KRIs focus on preventing adverse events.",
        },
        {
            "question": "What does the acronym SMART stand for in the context of KPIs and KRIs?",
            "options": [
                "Specific, Measurable, Achievable, Relevant, Time-bound",
                "Strategic, Measurable, Actionable, Realistic, Timely",
                "Simple, Measurable, Achievable, Relevant, Time-bound",
                "Specific, Measurable, Actionable, Realistic, Time-bound",
            ],
            "answer": "Specific, Measurable, Achievable, Relevant, Time-bound",
            "solution": "The SMART framework helps to ensure that indicators are well-defined and effective.",
        },
        {
            "question": "Which of the following is an example of a good KPI for a customer service department?",
            "options": [
                "Number of phone calls answered",
                "Average call handling time",
                "Customer satisfaction score",
                "Number of customer complaints",
            ],
            "answer": "Customer satisfaction score",
            "solution": "While the other options are operational metrics, customer satisfaction score is a *key* performance indicator directly related to a strategic objective.",
        },
        {
            "question": "Which of the following is an example of a good KRI for cybersecurity?",
            "options": [
                "Number of employees trained on security awareness",
                "Number of successful phishing attacks",
                "IT budget spent on security",
                "Number of security policies in place",
            ],
            "answer": "Number of successful phishing attacks",
            "solution": "This is a leading indicator of potential security breaches. The other options are related to security *efforts*, but not necessarily *risk exposure*.",
        },
        {
            "question": "What is a common mistake when defining KPIs and KRIs?",
            "options": [
                "Setting targets that are too easy to achieve",
                "Using too many indicators",
                "Focusing only on financial metrics",
                "All of the above",
            ],
            "answer": "All of the above",
            "solution": "These are all common pitfalls that can reduce the effectiveness of KPIs and KRIs.",
        },
        {
            "question": "Which is a better practice?",
            "options": [
                "Having 100's of KPIs and KRIs so everything is monitored",
                "Having a small number of key indicators",
            ],
            "answer": "Having a small number of key indicators",
            "solution": "It is much better to have few well defined indicators.",
        },
        {
            "question": "What is a 'leading indicator'?",
            "options": [
                "An indicator that measures past performance",
                "An indicator that predicts future performance or risk",
            ],
            "answer": "An indicator that predicts future performance or risk",
            "solution": "Leading indicators are better for proactive management",
        },
        {
            "question": "What is a 'lagging indicator'?",
            "options": [
                "An indicator that measures past performance",
                "An indicator that predicts future performance or risk",
            ],
            "answer": "An indicator that measures past performance",
            "solution": "Lagging indicators are helpful for measuring overall progress.",
        },
        {
            "question": "What is a KPI threshold?",
            "options": [
                "A value that when crossed signals a significant risk",
                "A target or acceptable range for a KPI",
            ],
            "answer": "A target or acceptable range for a KPI",
            "solution": "KPI thresholds define acceptable levels of performance.",
        },
        {
            "question": "What is a KRI threshold?",
            "options": [
                "A value that when crossed signals a significant risk",
                "A target or acceptable range for a KRI",
            ],
            "answer": "A value that when crossed signals a significant risk",
            "solution": "KRI thresholds define unacceptable levels of risk.",
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

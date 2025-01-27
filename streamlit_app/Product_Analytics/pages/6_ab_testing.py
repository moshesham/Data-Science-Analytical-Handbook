# pages/6_ab_testing.py
import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
from utils import data_utils, stats_utils, viz_utils, style_utils  # Import utility functions
from statsmodels.stats.power import TTestIndPower
import math

def main():
    # Page Configuration
    st.set_page_config(
        page_title="A/B Testing",
        page_icon="🧮",
        layout="wide"
    )

    # Header Section
    st.title("A/B Testing")
    st.write("Learn about A/B testing, a core technique for product development.")

    # Theory Section
    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
            A/B testing is a controlled experiment to compare two versions of a single variable. It's a fundamental method for making data-driven decisions in product development.

            ### Key Concepts

            - **Control Group:** The group that does not receive the treatment or intervention being tested.
            - **Treatment Group:** The group that receives the treatment or intervention.
            - **Randomization:** Users are randomly assigned to control and treatment groups to ensure comparability.
            - **Statistical Significance:** The likelihood that the observed differences are not due to random chance.
            -   **Metrics:** The quantitative values that measure the user behaviour.
            - **Sample Size:** The number of users in the experiment, the larger the better the statistical power and reliability.
            - **Effect Size:** The true difference between the treatment and control groups (which A/B testing is designed to test).
             - **Statistical Power:** The probability of correctly detecting a statistically significant difference when one exists.

            **Further Reading:**
            - [A/B Testing (Wikipedia)](https://en.wikipedia.org/wiki/A/B_testing)
            - [A/B Testing Guide](https://www.optimizely.com/optimization-glossary/ab-testing/)
            - [A/B Testing Calculator](https://www.optimizely.com/sample-size-calculator/)
        """)

    # Interactive Demo Section
    st.header("🔄 Interactive Demo")
    st.write("Simulate an A/B test to understand the effect of an intervention. Adjust the parameters below to see how different factors impact the result of the test.")

    # A/B Test Parameters
    st.subheader("A/B Test Parameters")
    control_size = st.slider("Control Group Size", min_value=50, max_value=1000, value=200, step=50, help="The sample size for the control group.")
    treatment_size = st.slider("Treatment Group Size", min_value=50, max_value=1000, value=200, step=50, help = "The sample size for the treatment group.")
    base_conversion_rate = st.slider("Base Conversion Rate (Control Group)", min_value=0.01, max_value=0.5, value=0.10, step=0.01, help="The baseline conversion rate for the control group.")
    treatment_effect = st.slider("Treatment Effect (Relative Change)", min_value=-0.2, max_value=0.2, value=0.05, step=0.01, help="The change in the conversion rate for the treatment group (relative to the base rate).")
    alpha = st.slider("Significance Level (alpha)", min_value=0.01, max_value=0.1, value=0.05, step=0.01, help="The significance level used for the hypothesis test.")
    power = st.slider("Desired Statistical Power (1-Type 2 Error)", min_value = 0.5, max_value=0.99, value = 0.8, step = 0.01, help = "Probability of rejecting the null hypothesis when it is false.")


    if st.button("Run A/B Test Simulation", help="Run the A/B test simulation with the specified parameters."):
        with st.spinner("Running A/B test simulation..."):
            # Data Generation
            control_group = np.random.binomial(1, base_conversion_rate, control_size)
            treatment_conversion_rate = base_conversion_rate + treatment_effect
            treatment_conversion_rate = np.clip(treatment_conversion_rate, 0, 1) #make sure within [0,1]
            treatment_group = np.random.binomial(1, treatment_conversion_rate, treatment_size)

            # Calculate Conversion Rates
            control_conversion_rate = np.mean(control_group)
            treatment_conversion_rate = np.mean(treatment_group)

            # Perform independent samples t-test
            t_stat, p_value = stats.ttest_ind(control_group, treatment_group)
            st.write(f"**T Statistic:** {t_stat:.3f}")
            st.write(f"**P Value:** {p_value:.3f}")

           # Sample Size Calculation for specified power:
            effect_size = stats_utils.calculate_sample_size_power(effect_size=treatment_effect, power=power, alpha=alpha)
            st.write(f"**Sample Size Needed (for each group for given power):** {effect_size:.2f}")


            # Decision
            if p_value < alpha:
                st.success("Reject the null hypothesis. There is a statistically significant difference between the control and treatment groups.")
            else:
                st.error("Fail to reject the null hypothesis. There is not a statistically significant difference between the control and treatment groups.")
                if treatment_conversion_rate > control_conversion_rate:
                  st.write("Note that although not statistically significant, the treatment group has a slightly higher conversion rate.")


           # Visualization
            data_sets = {
                    "Control Group": control_group,
                    "Treatment Group": treatment_group
                }
            fig = viz_utils.plot_multiple_histograms(data_sets, title="Control vs Treatment Distribution", xlabel = "Conversion (0/1)", ylabel = "Frequency")
            st.pyplot(fig)
            st.write("The histograms show the distribution of users in the control and treatment group that converted or did not convert. The mean of these histogram corresponds to the conversion rate.")
            st.write(f"The conversion rate for the control group is: {control_conversion_rate:.2f}")
            st.write(f"The conversion rate for the treatment group is: {treatment_conversion_rate:.2f}")


    # Real-world Application
    st.header("🌍 Real-world Application")
    st.write("A/B testing allows product teams to measure the effectiveness of product changes, such as a new feature, an updated user interface, or a different algorithm. These tests are important part of making data-driven decisions in product development.")

    st.subheader("Example Scenario")
    st.write("Imagine you want to test a new checkout button on a website. You can use A/B testing to compare the performance of the new button against the old one by dividing users randomly into two groups. The control group would see the old button, and the treatment group would see the new button. Then you would measure their conversion rate, and use hypothesis testing to see if the results are statistically significant.")
    st.write("By following this process, you can measure product changes, and make sure that new changes actually have a positive impact.")

if __name__ == "__main__":
    main()
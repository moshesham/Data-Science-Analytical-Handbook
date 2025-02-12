# pages/5_hypothesis_testing.py
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
        page_title="Hypothesis Testing",
        page_icon="🧪",
        layout="wide"
    )

    # Header Section
    st.title("Hypothesis Testing")
    st.write("Learn the fundamentals of hypothesis testing, including null and alternative hypotheses, p-values, and statistical significance.")

    # Theory Section
    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
            Hypothesis testing is a statistical method used to determine whether there is enough evidence to reject a null hypothesis.

            ### Key Concepts

            - **Null Hypothesis (H0):** The default assumption or statement of no effect or no difference.
            - **Alternative Hypothesis (H1 or Ha):** The statement we are trying to find evidence for.
            - **p-value:** The probability of observing the data (or more extreme data) if the null hypothesis is true.
            - **Significance Level (alpha):** A predetermined threshold (typically 0.05) used to decide whether to reject the null hypothesis.
            - **Type I Error (False Positive):** Rejecting the null hypothesis when it is actually true.
            - **Type II Error (False Negative):** Failing to reject the null hypothesis when it is actually false.
            - **Statistical Power:** The probability of correctly rejecting the null hypothesis when it is false.
           **Further Reading:**
            - [Hypothesis Testing (Wikipedia)](https://en.wikipedia.org/wiki/Hypothesis_testing)
            - [P-value (Wikipedia)](https://en.wikipedia.org/wiki/P-value)
             - [Type I and Type II Errors (Wikipedia)](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors)
             - [Statistical Power (Wikipedia)](https://en.wikipedia.org/wiki/Statistical_power)

        """)

    # Interactive Demo Section
    st.header("🔄 Interactive Demo")
    st.write("Explore hypothesis testing with an interactive simulation. Experiment with the different parameters to see how they affect the outcome of each test.")
    test_type = st.selectbox("Select Hypothesis Test", ["One Sample T-test", "Two Sample T-test", "Chi-square Test"], index=0,
                            help="Select the type of hypothesis test to simulate.")

    if test_type == "One Sample T-test":
         st.subheader("One Sample T-test Simulation")
         pop_mean = st.number_input("Population Mean", value=10.0, help="The known population mean.")
         sample_size = st.slider("Sample Size", min_value=30, max_value=500, value=100, step = 10, help="The sample size to generate.")
         effect_size = st.slider("Effect Size (difference from population mean)", min_value = -2.0, max_value = 2.0, value = 0.5, step = 0.1, help = "The true difference from the population mean.")
         alpha = st.slider("Significance Level (alpha)", min_value = 0.01, max_value = 0.1, value = 0.05, step = 0.01, help="The significance level used for hypothesis testing.")
         power = st.slider("Desired Statistical Power (1-Type 2 Error)", min_value = 0.5, max_value=0.99, value = 0.8, step = 0.01, help = "Probability of rejecting the null hypothesis when it is false.")

         if st.button("Run One-Sample T-test Simulation", help = "Simulate a T-test with provided inputs"):
             with st.spinner("Running the simulation..."):
                # Generate sample with an effect, to show an example where we reject the null hypothesis
                sample_mean_true = pop_mean + effect_size
                sample = np.random.normal(loc = sample_mean_true, scale = 2, size = sample_size)

                #Perform one-sample t-test
                t_stat, p_value = stats.ttest_1samp(sample, pop_mean)
                st.write(f"**T Statistic:** {t_stat:.3f}")
                st.write(f"**P Value:** {p_value:.3f}")

                # Make a decision based on p-value
                if p_value < alpha:
                    st.success("Reject null hypothesis. The sample mean is significantly different from the population mean.")
                else:
                    st.error("Fail to reject null hypothesis. There is not a significant difference.")
                sample_size_power = stats_utils.calculate_sample_size_power(effect_size=effect_size, power=power, alpha = alpha)
                st.write(f"**Sample Size Needed (for given power):** {sample_size_power}")

                # Example histogram to visualize
                fig = viz_utils.plot_histogram(sample, title="Sample Data", xlabel="Values", ylabel="Frequency")
                plt.axvline(pop_mean, color='r', linestyle='dashed', label="Pop. mean")
                plt.axvline(np.mean(sample), color='g', linestyle="dashed", label="Sample mean")
                plt.legend()

                st.pyplot(fig)
                st.write("The histogram above shows the simulated data and the population mean as a dashed line.")
    elif test_type == "Two Sample T-test":
         st.subheader("Two Sample T-test Simulation")
         group_a_size = st.slider("Sample Size Group A", min_value=30, max_value=500, value=100, step = 10, help="The sample size for group A.")
         group_b_size = st.slider("Sample Size Group B", min_value=30, max_value=500, value=100, step = 10, help="The sample size for group B.")
         mean_diff = st.slider("Mean Difference Between Groups", min_value = -2.0, max_value = 2.0, value = 0.5, step = 0.1, help = "The true difference in mean between group A and B.")
         alpha = st.slider("Significance Level (alpha)", min_value = 0.01, max_value = 0.1, value = 0.05, step = 0.01, help="The significance level used for hypothesis testing.")
         power = st.slider("Desired Statistical Power (1-Type 2 Error)", min_value = 0.5, max_value=0.99, value = 0.8, step = 0.01, help = "Probability of rejecting the null hypothesis when it is false.")


         if st.button("Run Two Sample T-test Simulation", help="Simulate a two sample t-test with provided values."):
            with st.spinner("Running the simulation..."):
                group_a = np.random.normal(loc=10, scale=2, size=group_a_size)
                group_b = np.random.normal(loc=10 + mean_diff, scale=2, size=group_b_size)

                #Perform independent samples t-test
                t_stat, p_value = stats.ttest_ind(group_a, group_b)
                st.write(f"**T Statistic:** {t_stat:.3f}")
                st.write(f"**P Value:** {p_value:.3f}")


                if p_value < alpha:
                    st.success("Reject the null hypothesis. There is a statistically significant difference between group A and group B.")
                else:
                    st.error("Fail to reject the null hypothesis. There is not a statistically significant difference between group A and group B.")

                sample_size_power = stats_utils.calculate_sample_size_power(effect_size=mean_diff, power=power, alpha = alpha)
                st.write(f"**Sample Size Needed (for given power, for each group):** {sample_size_power:.2f}")

                # Visualize
                data_sets = {
                         "Group A": group_a,
                         "Group B": group_b
                    }
                fig = viz_utils.plot_multiple_histograms(data_sets, title="Group A vs B Histogram")
                st.pyplot(fig)
                st.write("The histograms above show the distribution of the two simulated groups.")


    elif test_type == "Chi-square Test":
        st.subheader("Chi-Square Test Simulation")
        st.write("Enter a table of observed counts below.")
        observed_counts_str = st.text_area("Observed Counts (Comma-separated rows, rows separated by new lines)", value="30,70\n40,60", help="Enter a table of observed counts.")
        alpha = st.slider("Significance Level (alpha)", min_value = 0.01, max_value = 0.1, value = 0.05, step = 0.01, help="The significance level used for hypothesis testing.")

        if st.button("Run Chi-Square Test", help="Perform the chi-square test with the observed counts provided."):
           try:
              observed_counts = np.array([[int(x.strip()) for x in row.split(',')] for row in observed_counts_str.splitlines()])
              #Perform the test
              chi2_stat, p_value_chi, _, _ = stats.chi2_contingency(observed_counts)
              st.write(f"**Chi2 statistic:** {chi2_stat:.3f}")
              st.write(f"**P value:** {p_value_chi:.3f}")

              if p_value_chi < alpha:
                st.success("Reject the null. There is an association between the groups and the event.")
              else:
                   st.error("Fail to reject. There isn't an association between the groups and the event.")

           except Exception as e:
               st.error(f"Error processing inputs: {e}")

    # Practice Section
    st.header("💪 Practice Exercise")
    st.write("Test your understanding of hypothesis testing with the following exercises.")

    st.subheader("Exercise 1: One Sample T-Test")
    st.write("A company claims their product has a mean rating of 4.5. You collect data from 100 users and find a sample mean of 4.3 with a standard deviation of 0.8. Perform a one sample t-test to see if this claim is true. (Assume a significance level of 0.05).")
    if st.button("Check Solution for Exercise 1"):
        # Data from exercise
        sample_mean = 4.3
        pop_mean_exercise = 4.5
        sample_std_dev = 0.8
        sample_size_exercise = 100
        alpha_exercise = 0.05

        #Perform one-sample t-test manually
        t_stat_exercise = (sample_mean - pop_mean_exercise)/(sample_std_dev/np.sqrt(sample_size_exercise))
        p_value_exercise = 2 * (1 - stats.t.cdf(np.abs(t_stat_exercise), df = sample_size_exercise-1))

        st.write(f"**T Statistic:** {t_stat_exercise:.3f}")
        st.write(f"**P Value:** {p_value_exercise:.3f}")
        if p_value_exercise < alpha_exercise:
                st.success("Reject null hypothesis. The sample mean is significantly different from the population mean.")
        else:
                st.error("Fail to reject null hypothesis. There is not a significant difference.")
    st.subheader("Exercise 2: Two Sample T-Test")
    st.write("You're comparing the average session duration for two different app layouts, A and B. 2 groups of 100 users each were tested. Group A showed a mean session of 12 minutes with a standard deviation of 3, Group B showed a mean session of 13.5 minutes with a standard deviation of 2.5. Is there a statistically significant difference between the two app layouts? (Assume a significance level of 0.05)")
    if st.button("Check Solution for Exercise 2"):
        mean_a = 12
        std_a = 3
        sample_size_a = 100
        mean_b = 13.5
        std_b = 2.5
        sample_size_b = 100
        alpha_exercise = 0.05

        #Perform t-test manually
        t_stat_exercise, p_value_exercise = stats.ttest_ind(np.random.normal(mean_a, std_a, sample_size_a), np.random.normal(mean_b, std_b, sample_size_b))
        st.write(f"**T Statistic:** {t_stat_exercise:.3f}")
        st.write(f"**P Value:** {p_value_exercise:.3f}")
        if p_value_exercise < alpha_exercise:
              st.success("Reject the null hypothesis. There is a statistically significant difference between group A and group B.")
        else:
            st.error("Fail to reject the null hypothesis. There is not a statistically significant difference between group A and group B.")


    # Real-world Application
    st.header("🌍 Real-world Application")
    st.write("Hypothesis testing is the cornerstone of A/B testing and other statistical analyses in product development. By understanding these concepts, we are able to quantify our findings and know if our data is statistically significant, or if it's just random noise.")


if __name__ == "__main__":
    main()
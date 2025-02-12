import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli, binom, norm  # Import norm for continuous example
from math import comb

def main():

    # Page Configuration (Mimicking descriptive_statistics.py)
    st.set_page_config(
        page_title="Probability Fundamentals",
        page_icon="🎲",  # Using a dice icon
        layout="wide"
    )

    # Header Section
    st.title("Probability Fundamentals")
    st.write("Explore essential probability concepts used in data analytics, including basic probability, conditional probability, Bayes' Theorem, and random variables.")

    # Theory Section
    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
        Probability forms the foundation for understanding uncertainty in data analysis. Key concepts include:

        ### Basic Probability
        -   **Experiment:** A process with an uncertain outcome.
        -   **Outcome:** A possible result of an experiment.
        -   **Sample Space (Ω):** The set of all possible outcomes.
        -   **Event (E):** A subset of the sample space.
        -   **Probability (P(E)):**  A number between 0 and 1 (inclusive) representing the likelihood of event E.
        -   **Formula (Equally Likely Outcomes):** P(E) = (Number of outcomes in E) / (Total number of outcomes in Ω)

        ### Conditional Probability
        -   **P(A|B):** The probability of event A *given that* event B has occurred.
        -   **Formula:** P(A|B) = P(A and B) / P(B)  (where P(B) > 0)
        -   **Independence:** Events A and B are independent if P(A|B) = P(A) and P(B|A) = P(B).  Also, P(A and B) = P(A) * P(B).

        ### Bayes' Theorem
        -   A way to update probabilities based on new evidence.
        -   **Formula:** P(A|B) = [P(B|A) * P(A)] / P(B)
        -   **Components:**
            -   P(A|B): Posterior probability
            -   P(B|A): Likelihood
            -   P(A): Prior probability
            -   P(B): Evidence

        ### Random Variables
        -   A variable whose value is a numerical outcome of a random phenomenon.
        -   **Discrete Random Variable:** Takes on countable values.
        -   **Continuous Random Variable:** Can take on any value within a range.
        -   **Probability Distributions:** Describe how probabilities are distributed.
            -   **PMF (Probability Mass Function):** For discrete variables.
            -   **PDF (Probability Density Function):** For continuous variables.
        -   **Expected Value (E[X]):** The "average" value of a random variable.  For discrete: E[X] = Σ [x * P(X=x)]

        **Further Reading:**
        - [Probability (Wikipedia)](https://en.wikipedia.org/wiki/Probability)
        - [Conditional Probability (Khan Academy)](https://www.khanacademy.org/math/statistics-probability/counting-permutations-and-combinations/conditional-probability-independence/v/introduction-to-conditional-probability)
        - [Bayes' Theorem (Khan Academy)](https://www.khanacademy.org/math/statistics-probability/counting-permutations-and-combinations/bayes-theorem/v/bayes-theorem)
        - [Random Variables (Khan Academy)](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library)
        """)

    # Interactive Demo Section
    st.header("🔄 Interactive Demo")
    st.write("Use the controls below to simulate probability concepts and visualize their distributions. Experiment with different parameters to see how they affect the outcomes.")

    # Choose a concept to demonstrate
    demo_concept = st.selectbox("Choose a Concept:", ["Bernoulli Trial", "Binomial Distribution", "Conditional Probability (Coin Flip)", "Normal Distribution (Continuous)"], index=0)

    if demo_concept == "Bernoulli Trial":
        p_success = st.slider("Probability of Success (p):", 0.0, 1.0, 0.5, 0.01, help="Probability between 0 and 1")
        if st.button("Simulate Bernoulli Trial"):
            outcome = bernoulli.rvs(p_success)
            st.write(f"Outcome: {'Success' if outcome == 1 else 'Failure'}")
            fig, ax = plt.subplots()
            ax.bar(["Success", "Failure"], [p_success, 1 - p_success])
            ax.set_ylim([0, 1])
            ax.set_ylabel("Probability")
            ax.set_title("Bernoulli Trial Probabilities")
            st.pyplot(fig)

    elif demo_concept == "Binomial Distribution":
        n_trials = st.number_input("Number of Trials (n):", min_value=1, max_value=100, value=10, step=1, help = "Number of trials, max value is 100")
        p_success = st.slider("Probability of Success (p):", 0.0, 1.0, 0.5, 0.01, key="binom_p", help="Probability between 0 and 1")
        if st.button("Plot Binomial Distribution"):
            k_values = np.arange(0, n_trials + 1)
            probabilities = binom.pmf(k_values, n_trials, p_success)
            fig, ax = plt.subplots()
            ax.bar(k_values, probabilities)
            ax.set_xlabel("Number of Successes (k)")
            ax.set_ylabel("Probability P(X=k)")
            ax.set_title(f"Binomial Distribution (n={n_trials}, p={p_success:.2f})")
            st.pyplot(fig)

    elif demo_concept == "Conditional Probability (Coin Flip)":
        # Simulate a biased coin and conditional probability
        p_heads = st.slider("Probability of Heads (P(H)):", 0.0, 1.0, 0.6, 0.01, help="Probability between 0 and 1") # Biased coin
        p_tails = 1 - p_heads

        st.write("Assume we know the first flip is Heads. What's the probability of the *second* flip being Heads?")
        if st.button("Simulate Two Coin Flips"):
            first_flip = "Heads" if bernoulli.rvs(p_heads) == 1 else "Tails"
            second_flip = "Heads" if bernoulli.rvs(p_heads) == 1 else "Tails"
            st.write(f"First Flip: {first_flip}, Second Flip: {second_flip}")

            # Since coin flips are independent, P(Second Heads | First Heads) = P(Second Heads)
            st.write(f"P(Second Heads | First Heads) = P(Second Heads) = {p_heads:.2f}")

            fig, ax = plt.subplots()
            ax.bar(["Heads", "Tails"], [p_heads, p_tails])
            ax.set_ylim([0, 1])
            ax.set_ylabel("Probability")
            ax.set_title("Probability of Second Flip (Given First Flip is Heads)")
            st.pyplot(fig)
    elif demo_concept == "Normal Distribution (Continuous)":
        mean = st.slider("Mean (μ):", -5.0, 5.0, 0.0, 0.1, help="Mean Value")
        std_dev = st.slider("Standard Deviation (σ):", 0.1, 5.0, 1.0, 0.1, help = "Standard Deviation")
        if st.button("Plot Normal Distribution"):
            x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
            y = norm.pdf(x, mean, std_dev)
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.set_xlabel("x")
            ax.set_ylabel("Probability Density")
            ax.set_title(f"Normal Distribution (μ={mean:.2f}, σ={std_dev:.2f})")
            st.pyplot(fig)

    # Practice Section (Simple - could be expanded)
    st.header("💪 Practice Exercise")
    st.write("Calculate probabilities for the given scenarios.  You can use the interactive demos above to help visualize.")
    st.write("- What's the probability of rolling a 4 on a six-sided die?")
    st.write("- If you flip a coin twice, what's the probability of getting two heads?")

    if st.button("Show Answers"):
        st.write("Probability of rolling a 4: 1/6")
        st.write("Probability of two heads: 1/4")

    # Real-world Application
    st.header("🌍 Real-world Application")
    st.write("""
    Probability is fundamental to data analysis and is used extensively in:

    *   **A/B Testing:** Assessing the statistical significance of differences between groups.
    *   **Click-Through Rate Prediction:** Modeling the probability of user clicks.
    *   **Churn Prediction:** Estimating customer churn probability.
    *   **Customer Lifetime Value Modeling:** Predicting future customer value.
    *   **Fraud Detection:** Identifying unusual patterns using probability.
    *   **Recommendation Systems:** Suggesting items based on probabilities.
    *   **Spam Filtering:** Classifying emails using Bayes' Theorem.
    """)

    # Knowledge Check
    st.header("✅ Knowledge Check")
    quiz_questions = [
        {
            "question": "Which of the following best describes the sample space?",
            "options": ["Favorable outcomes", "All possible outcomes", "Single outcome probability", "Non-mutually exclusive events"],
            "answer": "All possible outcomes"
        },
        {
            "question": "If A and B are mutually exclusive, what is P(A and B)?",
            "options": ["P(A) * P(B)", "P(A) + P(B)", "0", "1"],
            "answer": "0"
        },
        {
            "question": "If P(A|B) = 0.4 and P(B) = 0.5, what is P(A and B) *if A and B are independent*?",
            "options": ["0.2", "0.9", "0.1", "Cannot be determined"],
            "answer": "Cannot be determined"
        },
        {
            "question": "Which part of Bayes' Theorem is the prior probability?",
            "options": ["P(A|B)", "P(B|A)", "P(A)", "P(B)"],
            "answer": "P(A)"
        },
        {
            "question": "A random variable taking any value within a range is:",
            "options": ["Discrete", "Continuous", "Bernoulli", "Binomial"],
            "answer": "Continuous"
        },
        {
           "question": "What is the expected value of a fair six-sided die roll?",
            "options": ["3", "3.5", "4", "Depends on rolls"],
            "answer": "3.5"
        },
        {
            "question": "In A/B testing, what does 'statistically significant' mean?",
            "options": ["Large difference", "Likely due to change, not chance", "Guaranteed improvement", "Perfect test design"],
            "answer": "Likely due to change, not chance"
        },
        {
            "question": "Which distribution models successes in fixed independent trials with the same probability?",
            "options": ["Normal", "Exponential", "Binomial", "Poisson"],
            "answer": "Binomial"
        },
        {
            "question": "Probability of at least one head in three coin flips?",
            "options": ["1/8", "3/8", "7/8", "1/2"],
            "answer": "7/8"
        },
        {
            "question": "If P(A) = 0.6, P(B) = 0.4, and P(A and B) = 0.24, are A and B independent?",
            "options": ["Yes", "No", "Cannot be determined", "Only if P(A|B) = P(B|A)"],
            "answer": "Yes"
        },
        {
            "question": "What does P(B|A) represent in Bayes' Theorem?",
            "options": ["Probability of A given B", "Probability of B given A", "Prior probability of A", "Prior probability of B"],
            "answer": "Probability of B given A"
        },
        {
            "question": "Two dice are rolled. What's the probability the sum is 7?",
            "options": ["1/6", "1/12", "1/36", "7/36"],
            "answer": "1/6"
        },
        {
            "question": "A company has a 5% churn rate.  Which distribution models churn out of 100 customers?",
            "options": ["Normal", "Exponential", "Binomial", "Poisson"],
            "answer": "Binomial"
        },
        {
            "question": "Which is NOT a typical application of Bayes' Theorem?",
            "options": ["Spam filtering", "Medical diagnosis", "Area of a circle", "Updating beliefs"],
            "answer": "Area of a circle"
        },
        {
            "question": "Two cards drawn *without* replacement. Probability both are hearts?",
            "options": ["1/16", "13/52 * 12/51", "1/4", "13/52 * 13/52"],
            "answer": "13/52 * 12/51"
        }
    ]

    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i + 1}. {question['question']}**")
        user_answer = st.radio(f"Options for question {i+1}", options=question["options"], key=f"radio_{i}")

        if st.button(f"Check answer for {i+1}", key=f"check_button_{i}"):
            if user_answer == question["answer"]:
                st.success("Correct!")
            else:
                st.error(f"Incorrect. The correct answer is: {question['answer']}")       
if __name__ == "__main__":
    main()
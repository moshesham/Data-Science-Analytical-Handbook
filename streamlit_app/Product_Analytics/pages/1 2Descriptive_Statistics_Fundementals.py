from itertools import product

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from numpy import random
from scipy.stats import (
    bernoulli,
    binom,
    chi2,
    expon,
    geom,
    norm,
    poisson,
    randint,
    t,
    uniform,
)


def generate_bernoulli_samples(p, size):
    """Generates Bernoulli samples."""
    return bernoulli.rvs(p, size=size)


def generate_binomial_samples(n, p, size):
    """Generates Binomial samples."""
    return binom.rvs(n, p, size=size)


def generate_poisson_samples(mu, size):
    """Generates Poisson samples."""
    return poisson.rvs(mu=mu, size=size)


def generate_geometric_samples(p, size):
    """Generates Geometric samples."""
    return geom.rvs(p=p, size=size)


def generate_discrete_uniform_samples(low, high, size):
    """Generates Discrete Uniform samples."""
    return randint.rvs(low=low, high=high, size=size)


def generate_continuous_uniform_samples(low, high, size):
    """Generates Continuous Uniform samples."""
    return uniform.rvs(loc=low, scale=high - low, size=size)


def generate_exponential_samples(scale, size):
    """Generates Exponential samples."""
    return expon.rvs(scale=scale, size=size)


def generate_normal_samples(mu, sigma, size):
    """Generates Normal samples."""
    return norm.rvs(loc=mu, scale=sigma, size=size)


def generate_chisquare_samples(df, size):
    """Generates Chi-Squared samples."""
    return chi2.rvs(df=df, size=size)


def generate_t_samples(df, size):
    """Generates t-distribution samples."""
    return t.rvs(df=df, size=size)


def generate_dice_roll(num_rolls=1):
    """Simulates dice rolls."""
    return [random.randint(1, 6) for _ in range(num_rolls)]


def calculate_empirical_probability(outcomes, event):
    """Calculates empirical probability."""
    favorable_outcomes = sum(1 for outcome in outcomes if event(outcome))
    total_outcomes = len(outcomes)
    return favorable_outcomes / total_outcomes if total_outcomes > 0 else 0


def plot_discrete_distribution(distribution_type, params, num_points=15):
    """Plots PMF and CDF for discrete distributions."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    x_vals = np.arange(0, num_points)
    probs = []
    cdf_vals = []

    if distribution_type == "Bernoulli":
        p = params.get("p", 0.5)
        probs = binom.pmf(x_vals, 1, p)  # Bernoulli is Binomial(n=1)
        cdf_vals = binom.cdf(x_vals, 1, p)
    elif distribution_type == "Binomial":
        n = params.get("n", 10)
        p = params.get("p", 0.5)
        probs = binom.pmf(x_vals, n, p)
        cdf_vals = binom.cdf(x_vals, n, p)
    elif distribution_type == "Poisson":
        mu = params.get("mu", 5)
        probs = poisson.pmf(x_vals, mu)
        cdf_vals = poisson.cdf(x_vals, mu)
    elif distribution_type == "Geometric":
        p = params.get("p", 0.3)
        probs = geom.pmf(x_vals + 1, p)  # Geometric starts at 1 in scipy.stats
        cdf_vals = geom.cdf(x_vals + 1, p)
    elif distribution_type == "Discrete Uniform":
        low = params.get("low", 1)
        high = params.get("high", 6)
        x_vals = np.arange(low, high + 1)  # Adjust x_vals for uniform range
        probs = [1 / (high - low + 1)] * len(x_vals)
        cdf_vals = np.cumsum(probs)

    axes[0].bar(x_vals, probs, color="skyblue")
    axes[0].set_title(f"{distribution_type} PMF")
    axes[0].set_xlabel("Value (x)")
    axes[0].set_ylabel("P(X=x)")

    axes[1].step(x_vals, cdf_vals, where="post", color="coral")
    axes[1].set_title(f"{distribution_type} CDF")
    axes[1].set_xlabel("Value (x)")
    axes[1].set_ylabel("P(X≤x)")
    axes[1].set_ylim([0, 1.1])

    plt.tight_layout()
    return fig


def plot_continuous_distribution(distribution_type, params):
    """Plots PDF and CDF for continuous distributions."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    x_vals = np.linspace(
        params.get("x_min", -5), params.get("x_max", 5), 500
    )  # Default x range

    pdf_vals = []
    cdf_vals = []

    if distribution_type == "Uniform (Continuous)":
        a = params.get("a", 0)
        b = params.get("b", 1)
        pdf_vals = uniform.pdf(x_vals, loc=a, scale=b - a)
        cdf_vals = uniform.cdf(x_vals, loc=a, scale=b - a)
    elif distribution_type == "Exponential":
        lam = params.get("lambda", 1)
        pdf_vals = expon.pdf(x_vals, scale=1 / lam)  # Scale is 1/lambda in scipy
        cdf_vals = expon.cdf(x_vals, scale=1 / lam)
    elif distribution_type == "Normal (Gaussian)":
        mu = params.get("mu", 0)
        sigma = params.get("sigma", 1)
        pdf_vals = norm.pdf(x_vals, loc=mu, scale=sigma)
        cdf_vals = norm.cdf(x_vals, loc=mu, scale=sigma)
    elif (
        distribution_type == "Standard Normal"
    ):  # No params needed - fixed mean=0, std=1
        pdf_vals = norm.pdf(x_vals, loc=0, scale=1)
        cdf_vals = norm.cdf(x_vals, loc=0, scale=1)
    elif distribution_type == "Chi-Squared":
        df = params.get("df", 5)
        pdf_vals = chi2.pdf(x_vals, df)
        cdf_vals = chi2.cdf(x_vals, df)
        x_vals = x_vals[
            x_vals >= 0
        ]  # Chi-Squared is for non-negative values, adjust x_vals to avoid errors in plotting for negative range.
        pdf_vals = pdf_vals[x_vals >= 0]
        cdf_vals = cdf_vals[x_vals >= 0]

    elif distribution_type == "t-Distribution":
        df = params.get("df", 5)
        pdf_vals = t.pdf(x_vals, df)
        cdf_vals = t.cdf(x_vals, df)

    axes[0].plot(x_vals, pdf_vals, color="skyblue")
    axes[0].fill_between(x_vals, pdf_vals, color="skyblue", alpha=0.4)
    axes[0].set_title(f"{distribution_type} PDF")
    axes[0].set_xlabel("Value (x)")
    axes[0].set_ylabel("f(x)")  # PDF is density, not probability directly

    axes[1].plot(x_vals, cdf_vals, color="coral")
    axes[1].fill_between(x_vals, cdf_vals, color="coral", alpha=0.4)
    axes[1].set_title(f"{distribution_type} CDF")
    axes[1].set_xlabel("Value (x)")
    axes[1].set_ylabel("P(X≤x)")
    axes[1].set_ylim([0, 1.1])

    plt.tight_layout()
    return fig


def main():
    st.set_page_config(page_title="Probability Theory", page_icon="🎲", layout="wide")

    st.title("Probability Distributions: A Comprehensive Guide")
    st.write(
        "Explore random variables, discrete and continuous probability distributions, joint distributions, expectation, variance, and limit theorems."
    )

    with st.expander("📚 Random Variables"):
        st.markdown(
            """
        ### 5. Random Variables
        #### Definition of a Random Variable
        A **random variable (RV)** is a variable whose value is a numerical outcome of a random phenomenon or experiment. Formally, it is a function that maps outcomes from the sample space to the real numbers.

        *   **Purpose:** Random variables provide a way to quantify and analyze random phenomena mathematically. They allow us to work with probabilities and statistical measures.

        #### 5.2 Types of Random Variables: Discrete and Continuous
        Random variables are broadly categorized into two types based on the nature of their possible values:

        *   **Discrete Random Variable:** A random variable whose possible values are countable and typically finite, or countably infinite. These values are usually distinct and separate, often integers.
            *   **Characteristics:**
                *   Values are countable and distinct.
                *   Can be integers, whole numbers, or categories that can be numerically coded.
                *   Gaps exist between possible values.
            *   *Examples:*
                *   The **number of heads** observed when flipping a coin a fixed number of times (e.g., 0, 1, 2, 3 heads).
                *   The **number of defective items** in a batch of manufactured goods.
                *   The **number of customers** arriving at a store in an hour.
                *   The **outcome of rolling a die** (1, 2, 3, 4, 5, or 6).

        *   **Continuous Random Variable:** A random variable whose possible values can take on any value within a given range or interval. The possible values are uncountable and form a continuum.
            *   **Characteristics:**
                *   Values can be any number within a range.
                *   Infinitely many possible values between any two given values.
                *   Associated with measurements rather than counts.
            *   *Examples:*
                *   The **height of a person** (can be any value within a range, e.g., 1.5 meters, 1.75 meters, 1.8234 meters...).
                *   The **temperature of a room**.
                *   The **time until a light bulb burns out**.
                *   The **weight of a product**.
                *   **Stock prices** (over short time scales, can be modeled as continuous).

        The distinction between discrete and continuous random variables is crucial as it dictates the type of probability distribution and mathematical tools used for their analysis. Discrete variables are associated with probability mass functions (PMFs) and summations, while continuous variables are associated with probability density functions (PDFs) and integrals.
        """
        )

    with st.expander("📊Discrete Probability Distributions"):
        st.markdown(
            """
        ### Discrete Probability Distributions
        #### Probability Mass Function (PMF)
        For a discrete random variable, the **Probability Mass Function (PMF)**, denoted as P(X=x) or f(x), gives the probability that the random variable X takes on a specific value x. It is the discrete counterpart to the Probability Density Function (PDF) for continuous variables.

        *   **Formal Definition:** For a discrete random variable X, the PMF is a function f(x) that satisfies:
            *   f(x) = P(X = x)
            *   f(x) ≥ 0 for all x (Probabilities are non-negative)
            *   Σ f(x) = 1, where the sum is over all possible values of X (Total probability sums to 1)

        *   **Interpretation:** The PMF directly gives the probability of each possible outcome for a discrete random variable.
            For example, if X is the outcome of a die roll, the PMF tells you P(X=1), P(X=2), P(X=3), ..., P(X=6).

        #### 6.2 Cumulative Distribution Function (CDF) for Discrete Variables
        The **Cumulative Distribution Function (CDF)**, denoted as F(x) or P(X ≤ x), for a discrete random variable X gives the probability that X takes a value less than or equal to x.  It provides the cumulative probability up to a certain point.

        *   **Formal Definition:** For a discrete random variable X, the CDF is a function F(x) defined as:
            *   F(x) = P(X ≤ x) = Σ P(X=i)  where the sum is over all possible values i of X such that i ≤ x.

        *   **Properties of CDF:**
            *   0 ≤ F(x) ≤ 1 for all x (CDF values are probabilities).
            *   F(x) is non-decreasing (as x increases, the cumulative probability cannot decrease).
            *   lim (x→-∞) F(x) = 0  (As x approaches negative infinity, the CDF approaches 0).
            *   lim (x→+∞) F(x) = 1  (As x approaches positive infinity, the CDF approaches 1).
            *   F(x) is right-continuous (limit from the right equals the function value).

        *   **Interpretation:** The CDF provides the probability of being *at or below* a certain value.  It's useful for finding probabilities like P(X < 3), P(X ≤ 5), or P(2 < X ≤ 7).

    ####  Common Discrete Distributions:
    Let's explore some of the most frequently encountered discrete probability distributions:
    """
        )

    with st.expander("Bernoulli Distribution"):
        st.markdown(
            """
        ##### Bernoulli Distribution
        *   **Description:** The simplest discrete distribution, the Bernoulli distribution models a single binary trial or experiment that can have only two possible outcomes: "success" or "failure".  It's like a single flip of a potentially biased coin.
        *   **Examples:**
            *   A single coin flip (Heads or Tails).
            *   Whether a customer clicks on an ad (Click or No Click).
            *   Whether a product is defective or not defective.
            *   Whether a basketball shot is made or missed.
        *   **Parameters:**
            *   *p* (Probability of success): The only parameter is the probability of getting a "success" outcome. This value must be between 0 and 1 (inclusive).
        *   **Support:** The random variable X can take only two values: {0, 1}
            *   X = 1 represents "success"
            *   X = 0 represents "failure"
        *   **Probability Mass Function (PMF):**
            *   P(X=1) = *p*   (probability of success)
            *   P(X=0) = 1 - *p* (probability of failure)
        *   **Cumulative Distribution Function (CDF):**
            *   F(x) = 0 for x < 0
            *   F(x) = 1 - *p* for 0 ≤ x < 1
            *   F(x) = 1 for x ≥ 1
        *   **Mean (Expected Value):** E[X] = *p*
            *   On average, in the long run, the proportion of "successes" will be *p*.
        *   **Variance:** Var(X) = *p*(1 - *p*)
            *   The variance is maximized when p=0.5 (equal probability of success and failure) and minimized when p is close to 0 or 1.

        """
        )
        p_bernoulli = st.slider(
            "Bernoulli p (Probability of Success):",
            min_value=0.01,
            max_value=1.0,
            value=0.3,
            step=0.01,
            format="%.2f",
            key="bernoulli_p_slider",
        )
        num_samples_bernoulli = st.slider(
            "Number of Samples (Bernoulli):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="bernoulli_sample_slider",
        )
        if st.button("Generate Bernoulli Samples", key="bernoulli_button"):
            samples_bernoulli = generate_bernoulli_samples(
                p_bernoulli, num_samples_bernoulli
            )
            fig_bernoulli = px.histogram(
                x=samples_bernoulli,
                title="Bernoulli Distribution Samples",
                labels={"x": "Outcome (0 or 1)"},
            )
            st.plotly_chart(fig_bernoulli)

    with st.expander("Binomial Distribution"):
        st.markdown(
            """
        ##### Binomial Distribution
        *   **Description:** The Binomial distribution is one of the most fundamental discrete distributions. It models the **number of successes** in a fixed number (*n*) of independent and identical Bernoulli trials.  Imagine repeating a Bernoulli experiment (like a coin flip) *n* times and counting how many times you get "success".

        *   **Examples:**
            *   The **number of heads** in *n* coin flips.
            *   The **number of customers** who click on an ad out of *n* people who see it.
            *   The **number of defective items** in a random sample of *n* items from a production line.
            *   The **number of students** who pass an exam in a class of *n* students.

        *   **Parameters:**
            *   *n* (Number of trials): A positive integer representing the fixed number of Bernoulli trials performed.
            *   *p* (Probability of success): The probability of success on each *individual* trial. This is the same for all trials and is between 0 and 1.

        *   **Support:** The random variable X (number of successes) can take integer values from 0 to *n*:  {0, 1, 2, ..., *n*}.

        *   **Probability Mass Function (PMF):**
            *   P(X=k) = (n choose k) * p^k * (1-*p*)^(*n*-k)  for k = 0, 1, 2, ..., *n*
                *   Where (n choose k) = n! / (k! * (n-k)!) is the binomial coefficient, representing the number of ways to choose *k* successes out of *n* trials.

        *   **Cumulative Distribution Function (CDF):**
            *   F(x) = P(X ≤ x) =  Σ  [(n choose k) * p^k * (1-*p*)^(*n*-k)]  summed from k=0 to floor(x)

        *   **Mean (Expected Value):** E[X] = *n* * *p*
            *   The average number of successes you expect in *n* trials is simply *n* times the probability of success on a single trial.

        *   **Variance:** Var(X) = *n* * *p* * (1 - *p*)
            *   The variance increases with both *n* and *p*, being maximized when p=0.5.

        """
        )
        n_binomial = st.slider(
            "Binomial n (Number of Trials):",
            min_value=1,
            max_value=100,
            value=10,
            step=1,
            key="binomial_n_slider",
        )
        p_binomial = st.slider(
            "Binomial p (Probability of Success):",
            min_value=0.01,
            max_value=1.0,
            value=0.3,
            step=0.01,
            format="%.2f",
            key="binomial_p_slider",
        )
        num_samples_binomial = st.slider(
            "Number of Samples (Binomial):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="binomial_sample_slider",
        )

        if st.button("Generate Binomial Samples", key="binomial_button"):
            samples_binomial = generate_binomial_samples(
                n_binomial, p_binomial, num_samples_binomial
            )
            fig_binomial = px.histogram(
                x=samples_binomial,
                nbins=n_binomial + 1,
                title="Binomial Distribution Samples",
                labels={"x": "Number of Successes"},
            )
            st.plotly_chart(fig_binomial)

    with st.expander("Poisson Distribution"):
        st.markdown(
            """
        ##### Poisson Distribution
        *   **Description:** The Poisson distribution is crucial for modeling the **number of rare events** that occur in a fixed interval of time or space.  It's applicable when events happen randomly and independently at a constant average rate. Think of things that happen infrequently but you are counting how many occur within a given window.

        *   **Examples:**
            *   The **number of customers arriving at a store** during a specific hour.
            *   The **number of phone calls received by a call center** per minute.
            *   The **number of emails arriving in your inbox** per hour.
            *   The **number of accidents** at a particular intersection per week.
            *   The **number of radioactive decays** per second.
            *   The **number of defects** in a manufactured product per unit area.

        *   **Parameters:**
            *   μ (mu or lambda):  The average rate of events. This is the *expected* number of events in the specified interval.  Mu must be greater than 0.

        *   **Support:** The random variable X (number of events) can take any non-negative integer value: {0, 1, 2, 3, ...} (countably infinite).

        *   **Probability Mass Function (PMF):**
            *   P(X=k) = (e^(-μ) * μ^k) / k!  for k = 0, 1, 2, 3, ...
                *   Where 'e' is Euler's number (approximately 2.71828), and k! is the factorial of k.

        *   **Cumulative Distribution Function (CDF):**
            *   F(x) = P(X ≤ x) = Σ [(e^(-μ) * μ^k) / k!]  summed from k=0 to floor(x)

        *   **Mean (Expected Value):** E[X] = μ
            *   The average number of events is equal to the rate parameter μ.

        *   **Variance:** Var(X) = μ
            *   A key property of the Poisson distribution is that its variance is equal to its mean.

        """
        )
        mu_poisson = st.slider(
            "Poisson μ (Average Rate):",
            min_value=0.1,
            max_value=20.0,
            value=3.0,
            step=0.1,
            format="%.1f",
            key="poisson_mu_slider",
        )
        num_samples_poisson = st.slider(
            "Number of Samples (Poisson):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="poisson_sample_slider",
        )
        if st.button("Generate Poisson Samples", key="poisson_button"):
            samples_poisson = generate_poisson_samples(mu_poisson, num_samples_poisson)
            fig_poisson = px.histogram(
                x=samples_poisson,
                nbins=15,
                title="Poisson Distribution Samples",
                labels={"x": "Number of Events"},
            )
            st.plotly_chart(fig_poisson)

    with st.expander("Geometric Distribution"):
        st.markdown(
            """
        ##### Geometric Distribution
        *   **Description:** The Geometric distribution models the **number of trials needed until the *first* success** occurs in a sequence of independent Bernoulli trials. Think of it as asking "How many times do I have to try until I finally succeed?".

        *   **Examples:**
            *   The **number of coin flips** required to get the first head.
            *   The **number of sales calls** a salesperson needs to make to get their first sale.
            *   The **number of job applications** someone submits until they receive their first job offer.
            *   The **number of attempts** to start a car before it finally starts.

        *   **Parameters:**
            *   *p* (Probability of success):  The probability of success on each individual Bernoulli trial. It must be between 0 and 1 (exclusive of 0, inclusive of 1).

        *   **Support:** The random variable X (trials until first success) can take integer values starting from 1 and going to infinity: {1, 2, 3, ...} (countably infinite, because theoretically you might never succeed, though it becomes increasingly unlikely).

        *   **Probability Mass Function (PMF):**
            *   P(X=k) = (1-*p*)^(*k*-1) * *p*  for k = 1, 2, 3, ...
                *   This formula shows that the probability decreases geometrically as *k* increases (hence the name).  It's most likely to succeed on the first trial (k=1), less likely on the second (k=2), and so on.

        *   **Cumulative Distribution Function (CDF):**
            *   F(x) = P(X ≤ x) = 1 - (1-*p*)^floor(x)   for x ≥ 1
            *   F(x) = 0 for x < 1

        *   **Mean (Expected Value):** E[X] = 1/*p*
            *   The expected number of trials until the first success is inversely related to the probability of success. If success is very likely (p is high), you expect to succeed quickly (E[X] is low). If success is rare (p is low), you expect to try many times (E[X] is high).

        *   **Variance:** Var(X) = (1 - *p*) / *p*^2
            *   The variance is higher when *p* is small (success is rare), indicating more variability in the number of trials needed.

        """
        )
        p_geometric = st.slider(
            "Geometric p (Probability of Success):",
            min_value=0.01,
            max_value=1.0,
            value=0.5,
            step=0.01,
            format="%.2f",
            key="geometric_p_slider",
        )
        num_samples_geometric = st.slider(
            "Number of Samples (Geometric):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="geometric_sample_slider",
        )
        if st.button("Generate Geometric Samples", key="geometric_button"):
            samples_geometric = generate_geometric_samples(
                p_geometric, num_samples_geometric
            )
            fig_geometric = px.histogram(
                x=samples_geometric,
                nbins=20,
                title="Geometric Distribution Samples",
                labels={"x": "Trials until First Success"},
            )
            st.plotly_chart(fig_geometric)

    with st.expander("Discrete Uniform Distribution"):
        st.markdown(
            """
        ##### Discrete Uniform Distribution
        *   **Description:** The Discrete Uniform distribution is used when all possible outcomes in a *finite* set are **equally likely**.  It's the discrete version of "perfect fairness" – every value has the same chance of occurring.

        *   **Examples:**
            *   **Rolling a fair die:** Each face (1, 2, 3, 4, 5, 6) has an equal probability of 1/6.
            *   **Drawing a card at random** from a deck *after* shuffling (if considering just the rank, e.g., Ace, 2, 3,...King, but not suits).
            *   **Randomly selecting a month of the year** (each month has probability 1/12).
            *   **Picking a random integer** from a given range (e.g., integers from 1 to 10, if each has probability 1/10).

        *   **Parameters:**
            *   *a* (low): The minimum value in the set of possible outcomes (integer).
            *   *b* (high): The maximum value in the set of possible outcomes **plus one** (integer, *exclusive* upper bound).  The actual range of values is from *a* to *b*-1 (inclusive).

        *   **Support:** The random variable X can take integer values from *a* up to *b*-1: {*a*, *a*+1, ..., *b*-1} (finite and equally spaced).

        *   **Probability Mass Function (PMF):**
            *   P(X=k) = 1 / (*b* - *a*)  for k = *a*, *a*+1, ..., *b*-1
                *   The probability is constant for all values within the range, and zero outside the range. The value 1/(*b* - *a*) is just whatever is needed to make the probabilities sum to 1.

        *   **Cumulative Distribution Function (CDF):**
            *   F(x) = 0 for x < *a*
            *   F(x) = (floor(x) - *a* + 1) / (*b* - *a*)  for *a* ≤ x < *b*
            *   F(x) = 1 for x ≥ *b*

        *   **Mean (Expected Value):** E[X] = (*a* + *b* - 1) / 2
            *   The mean is simply the midpoint of the range of values.

        *   **Variance:** Var(X) = ((*b* - *a*)^2 - 1) / 12
            *   The variance depends on the spread of the range (*b* - *a*). A wider range leads to higher variance.

        """
        )
        low_uniform_discrete = st.slider(
            "Discrete Uniform Low (a):",
            min_value=1,
            max_value=5,
            value=1,
            step=1,
            key="uniform_discrete_low_slider",
        )
        high_uniform_discrete = st.slider(
            "Discrete Uniform High (b):",
            min_value=6,
            max_value=10,
            value=7,
            step=1,
            key="uniform_discrete_high_slider",
        )
        num_samples_uniform_discrete = st.slider(
            "Number of Samples (Discrete Uniform):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="uniform_discrete_sample_slider",
        )

        if st.button(
            "Generate Discrete Uniform Samples", key="uniform_discrete_button"
        ):
            samples_uniform_discrete = generate_discrete_uniform_samples(
                low_uniform_discrete,
                high_uniform_discrete,
                num_samples_uniform_discrete,
            )
            fig_uniform_discrete = px.histogram(
                x=samples_uniform_discrete,
                title="Discrete Uniform Distribution Samples",
                labels={"x": "Outcome Value"},
            )
            st.plotly_chart(fig_uniform_discrete)

    with st.expander("📈 Continuous Probability Distributions"):
        st.markdown(
            """
        ### 7. Continuous Probability Distributions
        #### 7.1 Probability Density Function (PDF)
        For continuous random variables, probability is described using the **Probability Density Function (PDF)**, denoted as f(x).  Unlike PMFs, the PDF itself does *not* give the probability of X taking on a specific value. Instead, the **probability of X falling within a range [a, b]** is given by the **area under the PDF curve between a and b**.

        *   **Formal Definition:** For a continuous random variable X, the PDF is a function f(x) that satisfies:
            *   f(x) ≥ 0 for all x (The PDF is always non-negative)
            *   The total area under the PDF curve over its entire support is equal to 1:  ∫ from -∞ to +∞ f(x) dx = 1

        *   **Important Note:**  For a continuous random variable, the probability of X being *exactly equal* to a specific value is always zero: P(X = c) = 0.  Probabilities are only defined for *intervals*.

        #### 7.2 Cumulative Distribution Function (CDF) for Continuous Variables
        The **Cumulative Distribution Function (CDF)** for a continuous random variable X is defined analogously to the discrete case, giving the probability that X takes a value less than or equal to x: F(x) = P(X ≤ x).  For a continuous variable, this is calculated by integrating the PDF from negative infinity up to x.

        *   **Formula:** F(x) = P(X ≤ x) = ∫ from -∞ to x f(t) dt

        *   **Relationship between PDF and CDF:**
            *   The CDF is the integral of the PDF.
            *   Conversely, the PDF is the derivative of the CDF: f(x) = dF(x)/dx

        *   **Properties of CDF (same as discrete CDF):**
            *   0 ≤ F(x) ≤ 1 for all x
            *   F(x) is non-decreasing
            *   lim (x→-∞) F(x) = 0
            *   lim (x→+∞) F(x) = 1
            *   F(x) is continuous (for continuous random variables)

        #### 7.3 Common Continuous Distributions:
        Let's explore some essential continuous probability distributions:
        """
        )

    with st.expander("Continuous Uniform Distribution"):
        st.markdown(
            """
        ##### Continuous Uniform Distribution
        *   **Description:** The Continuous Uniform distribution (also just called Uniform distribution when the context is clear) models situations where a random variable is **equally likely to take any value within a specified continuous interval**.  It's the continuous counterpart to the Discrete Uniform distribution and represents "perfect randomness" over a continuous range.

        *   **Examples:**
            *   **Random number generation:**  Idealized random number generators in computers aim to produce numbers uniformly distributed between 0 and 1 (or some other range).
            *   **Waiting time for a bus** if buses arrive exactly every 30 minutes, and you arrive at the bus stop at a completely random time.  Your waiting time will be uniformly distributed between 0 and 30 minutes.
            *   **Measurement errors** in some situations can be approximated as uniformly distributed within a small range.

        *   **Parameters:**
            *   *a* (low or loc): The minimum value of the interval (lower bound).
            *   *b* (high): The maximum value of the interval (upper bound).

        *   **Support:** The random variable X can take any real value within the interval [*a*, *b*]:  *a* ≤ X ≤ *b*.

        *   **Probability Density Function (PDF):**
            *   f(x) = 1 / (*b* - *a*)   for *a* ≤ x ≤ *b*
            *   f(x) = 0                  otherwise
                *   The PDF is constant within the interval [*a*, *b*], making the probability density uniform across the range.  The height 1/(*b* - *a*) is chosen so that the total area under the PDF is 1.

        *   **Cumulative Distribution Function (CDF):**
            *   F(x) = 0                      for x < *a*
            *   F(x) = (x - *a*) / (*b* - *a*)  for *a* ≤ x ≤ *b*
            *   F(x) = 1                      for x > *b*
                *   The CDF increases linearly from 0 to 1 over the interval [*a*, *b*].

        *   **Mean (Expected Value):** E[X] = (*a* + *b*) / 2
            *   The mean is the midpoint of the interval, as expected for a uniform distribution.

        *   **Variance:** Var(X) = (*b* - *a*)^2 / 12
            *   The variance depends on the square of the interval width (*b* - *a*)^2. A wider interval leads to a larger variance, reflecting greater spread.

        """
        )
        low_uniform_continuous = st.slider(
            "Continuous Uniform Low (a):",
            min_value=-5.0,
            max_value=0.0,
            value=0.0,
            step=0.1,
            format="%.1f",
            key="uniform_continuous_low_slider",
        )
        high_uniform_continuous = st.slider(
            "Continuous Uniform High (b):",
            min_value=5.0,
            max_value=10.0,
            value=5.0,
            step=0.1,
            format="%.1f",
            key="uniform_continuous_high_slider",
        )
        num_samples_uniform_continuous = st.slider(
            "Number of Samples (Continuous Uniform):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="uniform_continuous_sample_slider",
        )

        if st.button(
            "Generate Continuous Uniform Samples", key="uniform_continuous_button"
        ):
            samples_uniform_continuous = generate_continuous_uniform_samples(
                low_uniform_continuous,
                high_uniform_continuous,
                num_samples_uniform_continuous,
            )
            fig_uniform_continuous = px.histogram(
                x=samples_uniform_continuous,
                nbins=20,
                title="Continuous Uniform Distribution Samples",
                labels={"x": "Outcome Value"},
            )
            st.plotly_chart(fig_uniform_continuous)

    with st.expander("Exponential Distribution"):
        st.markdown(
            """
        ##### 7.3.2 Exponential Distribution
        *   **Description:** The Exponential distribution models the **time until an event occurs** in a Poisson process, where events happen continuously and independently at a constant average rate.  It is often used for modeling waiting times, survival times, or the duration of events.  A key characteristic is its "memoryless" property: the probability of an event occurring in the *next* time interval is independent of how much time has *already passed* without an event.

        *   **Examples:**
            *   The **time until a light bulb burns out**.
            *   The **time between customer arrivals** at a fast-food restaurant (if arrivals follow a Poisson process).
            *   The **duration of a phone call**.
            *   The **lifetime of an electronic component**.
            *   The **time until a radioactive atom decays**.

        *   **Parameters:**
            *   λ (lambda) or scale (often used in scipy): The rate parameter (λ > 0) represents the average number of events per unit of time.  Often, the `scale` parameter (which is 1/λ) is used instead, representing the average *time between events*.  In `scipy.stats.expon`, the `scale` parameter is used. We will use `scale`.

        *   **Support:** The random variable X (time until event) can take any non-negative real value: X ≥ 0 (continuous and starting from zero).

        *   **Probability Density Function (PDF):**
            *   f(x) = (1/scale) * e^(-x/scale)  for x ≥ 0
            *   f(x) = 0                        for x < 0
                *   The PDF is highest at x=0 and decays exponentially as x increases.  This reflects that shorter waiting times are more probable.

        *   **Cumulative Distribution Function (CDF):**
            *   F(x) = 1 - e^(-x/scale)   for x ≥ 0
            *   F(x) = 0                  for x < 0
                *   The CDF increases from 0 to 1 as x increases, showing the cumulative probability of the event happening within time *x*.

        *   **Mean (Expected Value):** E[X] = scale
            *   The expected time until the event is equal to the scale parameter (which is the inverse of the rate).

        *   **Variance:** Var(X) = scale^2
            *   The variance is the square of the scale parameter.  Higher scale (longer average time) also implies higher variance.

        *   **Memoryless Property:**  P(X > s + t | X > s) = P(X > t) for any s, t ≥ 0.
            *   This means that if an event has not occurred up to time *s*, the probability of it occurring after an *additional* time *t* is the same as the probability of it occurring after time *t* from the beginning.  The past has no bearing on future probabilities.

        """
        )
        scale_exponential = st.slider(
            "Exponential Scale (Average Time):",
            min_value=0.1,
            max_value=10.0,
            value=1.0,
            step=0.1,
            format="%.1f",
            key="exponential_scale_slider",
        )
        num_samples_exponential = st.slider(
            "Number of Samples (Exponential):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="exponential_sample_slider",
        )

        if st.button("Generate Exponential Samples", key="exponential_button"):
            samples_exponential = generate_exponential_samples(
                scale_exponential, num_samples_exponential
            )
            fig_exponential = px.histogram(
                x=samples_exponential,
                nbins=20,
                title="Exponential Distribution Samples",
                labels={"x": "Time until Event"},
            )
            st.plotly_chart(fig_exponential)

    with st.expander("Normal Distribution (Gaussian Distribution)"):
        st.markdown(
            """
        ##### Normal Distribution (Gaussian Distribution)
        *   **Description:** The Normal distribution, also known as the Gaussian distribution or "bell curve", is arguably the **most important and widely used continuous distribution in statistics and probability**.  It models a vast array of natural phenomena where values tend to cluster around a mean, with symmetrical spread.  It's central to the Central Limit Theorem, making it fundamental to statistical inference.

        *   **Examples:**
            *   **Heights and weights of people** in a population (approximately normal).
            *   **IQ scores**.
            *   **Measurement errors** in scientific experiments.
            *   **Financial asset returns** (often modeled as approximately normal, though with limitations).
            *   **Many biological traits**.
            *   **Phenomena that are the sum of many independent random factors** tend to be normally distributed (this is the essence of the Central Limit Theorem).

        *   **Parameters:**
            *   μ (mu): The mean (or location parameter).  It determines the center of the distribution (peak of the bell curve).
            *   σ (sigma): The standard deviation (or scale parameter).  It controls the spread or width of the distribution.  A larger sigma means a wider, flatter curve; a smaller sigma means a narrower, taller curve. Sigma must be greater than 0.

        *   **Support:** The random variable X can take any real value: -∞ < X < +∞ (unbounded support).

        *   **Probability Density Function (PDF):**
            *   f(x) = (1 / (σ * sqrt(2π))) * e^(-((x - μ)^2 / (2σ^2)))
                *   This is the famous "bell curve" formula.  It's symmetrical around the mean μ, and its shape is determined by the standard deviation σ.

        *   **Cumulative Distribution Function (CDF):**
            *   F(x) = P(X ≤ x) =  (1/2) * [1 + erf((x - μ) / (σ * sqrt(2)))]
                *   Where 'erf' is the error function, a special function related to the normal distribution.  The CDF has an S-shape, increasing from 0 to 1 as x goes from -∞ to +∞.

        *   **Mean (Expected Value):** E[X] = μ
            *   The mean is directly given by the parameter μ.

        *   **Variance:** Var(X) = σ^2
            *   The variance is the square of the standard deviation σ.  Standard deviation σ itself is often used to describe the spread, as it's in the original units of X.

        """
        )
        mu_normal = st.slider(
            "Normal μ (Mean):",
            min_value=-5.0,
            max_value=5.0,
            value=0.0,
            step=0.1,
            format="%.1f",
            key="normal_mu_slider",
        )
        sigma_normal = st.slider(
            "Normal σ (Standard Deviation):",
            min_value=0.1,
            max_value=5.0,
            value=1.0,
            step=0.1,
            format="%.1f",
            key="normal_sigma_slider",
        )
        num_samples_normal = st.slider(
            "Number of Samples (Normal):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="normal_sample_slider",
        )

        if st.button("Generate Normal Samples", key="normal_button"):
            samples_normal = generate_normal_samples(
                mu_normal, sigma_normal, num_samples_normal
            )
            fig_normal = px.histogram(
                x=samples_normal,
                nbins=20,
                title="Normal Distribution Samples",
                labels={"x": "Outcome Value"},
            )
            st.plotly_chart(fig_normal)

    with st.expander("Standard Normal Distribution"):
        st.markdown(
            """
        ##### Standard Normal Distribution
        *   **Description:** The Standard Normal distribution is a **special case of the Normal distribution** where the mean (μ) is 0 and the standard deviation (σ) is 1. It is denoted as Z ~ N(0, 1).  It serves as a fundamental reference distribution in statistics.  Any normal distribution can be standardized (transformed into a standard normal distribution) by subtracting the mean and dividing by the standard deviation.

        *   **Parameters:**  None. It's fixed with μ=0 and σ=1.

        *   **Support:**  Same as the general Normal distribution: -∞ < Z < +∞.

        *   **Probability Density Function (PDF):**
            *   φ(z) = (1 / sqrt(2π)) * e^(-z^2 / 2)
                *   This is simplified form of the Normal PDF with μ=0 and σ=1, often denoted by φ (phi).

        *   **Cumulative Distribution Function (CDF):**
            *   Φ(z) = P(Z ≤ z) = (1/2) * [1 + erf(z / sqrt(2))]
                *   This is the CDF of the Standard Normal distribution, often denoted by Φ (Phi).  Values of Φ(z) are widely tabulated (Z-tables) and computationally available.

        *   **Mean (Expected Value):** E[Z] = 0

        *   **Variance:** Var(Z) = 1

        """
        )
        num_samples_standard_normal = st.slider(
            "Number of Samples (Standard Normal):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="standard_normal_sample_slider",
        )

        if st.button("Generate Standard Normal Samples", key="standard_normal_button"):
            samples_standard_normal = generate_normal_samples(
                0, 1, num_samples_standard_normal
            )  # mu=0, sigma=1
            fig_standard_normal = px.histogram(
                x=samples_standard_normal,
                nbins=20,
                title="Standard Normal Distribution Samples",
                labels={"x": "Outcome Value (Z)"},
            )
            st.plotly_chart(fig_standard_normal)

    with st.expander("Chi-Squared Distribution"):
        st.markdown(
            """
        ##### Chi-Squared Distribution (χ²)
        *   **Description:** The Chi-Squared distribution (χ²) arises frequently in statistics, particularly in hypothesis testing and constructing confidence intervals for variances.  It is fundamentally related to the Normal distribution: if you square a standard normal random variable (Z ~ N(0, 1)), you get a Chi-Squared distribution with 1 degree of freedom.  More generally, if you sum the squares of *df* independent standard normal random variables, you get a Chi-Squared distribution with *df* degrees of freedom.

        *   **Examples:**
            *   **Sample variance:**  The sample variance of data drawn from a normal distribution, when properly scaled, follows a Chi-Squared distribution. This is used in confidence intervals for variance.
            *   **Goodness-of-fit tests:**  Chi-Squared tests are used to assess how well observed categorical data matches expected frequencies (e.g., in contingency tables, tests of independence).
            *   **Variance ratio tests:**  Used to compare variances of two populations.

        *   **Parameters:**
            *   *df* (Degrees of freedom):  A positive integer.  It determines the shape of the Chi-Squared distribution.  Degrees of freedom are related to the sample size and the number of constraints in statistical applications.

        *   **Support:** The random variable X (Chi-Squared value) takes non-negative real values: X ≥ 0.

        *   **Probability Density Function (PDF):**
            *   f(x; df) = [1 / (2^(df/2) * Γ(df/2))] * x^((df/2)-1) * e^(-x/2)   for x ≥ 0
                *   Where Γ is the Gamma function, a generalization of the factorial function.  The formula is somewhat complex but results in a distribution skewed to the right, with the skewness decreasing as degrees of freedom (*df*) increase.

        *   **Cumulative Distribution Function (CDF):**
            *   F(x; df) = P(X ≤ x) =  Regularized lower incomplete gamma function (complex formula, usually computed numerically)

        *   **Mean (Expected Value):** E[X] = *df*
            *   The mean of a Chi-Squared distribution is equal to its degrees of freedom.

        *   **Variance:** Var(X) = 2 * *df*
            *   The variance is twice the degrees of freedom.

        """
        )
        df_chisquare = st.slider(
            "Chi-Squared Degrees of Freedom (df):",
            min_value=1,
            max_value=20,
            value=3,
            step=1,
            key="chisquare_df_slider",
        )
        num_samples_chisquare = st.slider(
            "Number of Samples (Chi-Squared):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="chisquare_sample_slider",
        )

        if st.button("Generate Chi-Squared Samples", key="chisquare_button"):
            samples_chisquare = generate_chisquare_samples(
                df_chisquare, num_samples_chisquare
            )
            fig_chisquare = px.histogram(
                x=samples_chisquare,
                nbins=20,
                title="Chi-Squared Distribution Samples",
                labels={"x": "Outcome Value"},
            )
            st.plotly_chart(fig_chisquare)

    with st.expander("t-Distribution (Student's t-distribution)"):
        st.markdown(
            """
        ##### t-Distribution (Student's t-distribution)
        *   **Description:** The t-Distribution, also known as Student's t-distribution, is another crucial distribution in statistics, especially when dealing with **small sample sizes** and **unknown population standard deviation** when making inferences about population means. It is similar in shape to the Normal distribution – bell-shaped and symmetric – but has **heavier tails**. This means it has more probability in the tails (far from the mean) and less in the center compared to a Normal distribution, especially for low degrees of freedom.  As the degrees of freedom increase, the t-distribution approaches the Standard Normal distribution.

        *   **Examples:**
            *   **Hypothesis testing for means with small samples:**  When you want to test hypotheses about a population mean using a small sample (e.g., less than 30) and you don't know the population standard deviation, you use t-tests, which rely on the t-distribution.
            *   **Confidence intervals for means with small samples** under the same conditions.
            *   **Regression analysis:** The t-distribution is used in hypothesis testing and confidence intervals for regression coefficients.

        *   **Parameters:**
            *   *df* (Degrees of freedom): A positive integer.  It controls the tail heaviness and shape of the t-distribution.  Lower *df* means heavier tails (more spread out, more non-normality); higher *df* makes it closer to a Normal distribution.

        *   **Support:** The random variable X (t-statistic) can take any real value: -∞ < X < +∞.

        *   **Probability Density Function (PDF):**
            *   f(x; df) = [Γ((df+1)/2) / (sqrt(df*π) * Γ(df/2))] * (1 + (x^2)/df)^(-(df+1)/2)
                *   Where Γ is the Gamma function.  The formula is complex but results in a bell-shaped, symmetric distribution with tails heavier than normal, especially for small *df*.

        *   **Cumulative Distribution Function (CDF):**
            *   F(x; df) =  Computed numerically (no simple closed-form formula).

        *   **Mean (Expected Value):** E[X] = 0  (for df > 1)
            *   The t-distribution is centered at zero, just like the Standard Normal distribution.

        *   **Variance:** Var(X) = df / (df - 2)   (for df > 2)
            *   The variance is always greater than 1 (variance of Standard Normal), reflecting the heavier tails. As *df* increases, the variance approaches 1, and the t-distribution approaches the Standard Normal. For df ≤ 2, the variance is technically infinite (or undefined).

        """
        )
        df_t = st.slider(
            "t-Distribution Degrees of Freedom (df):",
            min_value=1,
            max_value=30,
            value=5,
            step=1,
            key="t_df_slider",
        )
        num_samples_t = st.slider(
            "Number of Samples (t-Distribution):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="t_sample_slider",
        )

        if st.button("Generate t-Distribution Samples", key="t_button"):
            samples_t = generate_t_samples(df_t, num_samples_t)
            fig_t = px.histogram(
                x=samples_t,
                nbins=20,
                title="t-Distribution Samples",
                labels={"x": "Outcome Value (t-statistic)"},
            )
            st.plotly_chart(fig_t)

    with st.expander("🤝 Joint Probability Distributions"):
        st.markdown(
            """
        ### 8. Joint Probability Distributions
        #### 8.1 Bivariate and Multivariate Distributions
        *   **Bivariate Distribution:**  Describes the probability distribution of **two random variables** considered together (e.g., height and weight of individuals). It tells you how these two variables vary jointly and any relationships between them.
        *   **Multivariate Distribution:**  Extends this to describe the probability distribution of **more than two random variables** simultaneously (e.g., temperature, humidity, and pressure at a location).  It captures the joint behavior and dependencies among multiple variables.
        *   **Joint PMF/PDF:**  For discrete variables, we have a Joint Probability Mass Function, P(X=x, Y=y). For continuous variables, we have a Joint Probability Density Function, f(x, y). These functions give the probability of specific combinations of values (discrete) or probability density over regions in the variable space (continuous).

        #### 8.2 Marginal and Conditional Distributions
        *   **Marginal Distribution:** The probability distribution of just **one** of the variables from a joint distribution, disregarding the other variables. It's like looking at the distribution of height *regardless* of weight.
            *   **Calculation:**
                *   Discrete: Sum the Joint PMF over all values of the other variable(s).
                *   Continuous: Integrate the Joint PDF over all values of the other variable(s).
        *   **Conditional Distribution:** The probability distribution of one variable **given a specific value of another variable** in the joint distribution.  It describes how one variable behaves *when we know* the value of the other.  For example, the distribution of weight *given* that a person is 1.8 meters tall.
            *   **Calculation:**
                *   Conditional PMF: P(X=x | Y=y) = P(X=x, Y=y) / P(Y=y)
                *   Conditional PDF: f(x | y) = f(x, y) / f_Y(y)  (where f_Y(y) is the marginal PDF of Y)

        #### 8.3 Independence of Random Variables
        Two random variables X and Y are **independent** if knowing the value of one variable provides no information about the probability distribution of the other.  Their joint distribution factorizes into the product of their marginal distributions.

        *   **Condition for Independence:**
            *   For all values of x and y:
                *   P(X=x, Y=y) = P(X=x) * P(Y=y)  (for discrete variables)
                *   f(x, y) = f_X(x) * f_Y(y)      (for continuous variables)

        #### 8.4 Covariance and Correlation
        **Covariance and Correlation** measure the **linear relationship** between two random variables. They indicate how much two variables change together.

        *   **Covariance (Cov(X, Y) or σ_XY):** Measures the direction and strength of the linear relationship.
            *   Positive covariance: X and Y tend to increase or decrease together.
            *   Negative covariance: As X increases, Y tends to decrease (or vice versa).
            *   Covariance of zero: No linear relationship (but doesn't rule out non-linear relationships).
            *   Formula: Cov(X, Y) = E[(X - E[X]) * (Y - E[Y])] = E[X*Y] - E[X]*E[Y]
            *   **Units:** Units of Cov(X, Y) are (units of X) * (units of Y), making it hard to compare across different pairs of variables.

        *   **Correlation (Corr(X, Y) or ρ_XY or r):**  A standardized measure of linear relationship, ranging from -1 to +1. Solves the unit problem of covariance.
            *   Correlation of +1: Perfect positive linear relationship.
            *   Correlation of -1: Perfect negative linear relationship.
            *   Correlation of 0: No linear relationship.
            *   Correlation near 0: Weak linear relationship.
            *   Formula: Corr(X, Y) = Cov(X, Y) / (SD(X) * SD(Y))  =  Covariance divided by the product of standard deviations.
            *   **Unitless:** Correlation is a pure number between -1 and +1, allowing for comparison across different variable pairs.

        **Important Note:** Correlation and covariance only measure *linear* relationships. Two variables can be highly dependent but have zero correlation if their relationship is non-linear (e.g., quadratic, cyclical). Also, correlation does not imply causation!
        """
        )

    with st.expander("🧮 9. Expectation and Variance"):
        st.markdown(
            """
        ### 9. Expectation and Variance
        #### 9.1 Expected Value (Mean) of a Random Variable (E[X] or μ)
        The **Expected Value** (or Mean) of a random variable X, denoted as E[X] or μ, represents the **average value** we expect X to take in the long run, over many repetitions of the random experiment. It's a measure of the "center" of the distribution.

        *   **Formulas:**
            *   Discrete RV: E[X] = Σ [x * P(X=x)]  (sum over all possible values x)
            *   Continuous RV: E[X] = ∫ x * f(x) dx  (integral over all possible values x)

        *   **Interpretation:**  If you were to repeat the random experiment many, many times and average the outcomes, this average would approach the expected value E[X]. It's a weighted average of all possible values, weighted by their probabilities (or probability densities).

        #### 9.2 Variance and Standard Deviation (Var(X) or σ², SD(X) or σ)
        **Variance and Standard Deviation** measure the **spread or dispersion** of a random variable's distribution around its mean. They quantify how much the values of X typically deviate from the expected value E[X].

        *   **Variance (Var(X) or σ²):** The average of the squared differences from the Mean.
            *   Formula: Var(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2
            *   Units: Units of Var(X) are (units of X)^2.

        *   **Standard Deviation (SD(X) or σ):** The square root of the variance.
            *   Formula: SD(X) = sqrt(Var(X))
            *   Units: SD(X) has the same units as X, making it often easier to interpret than variance.

        *   **Interpretation:**
            *   Higher variance/standard deviation means the values of X are more spread out around the mean - greater variability or volatility.
            *   Lower variance/standard deviation means the values of X are clustered more tightly around the mean - less variability, more concentrated distribution.
            *   Standard deviation, especially, is often used to describe the typical or "average" deviation from the mean. For example, in a normal distribution, about 68% of the values fall within one standard deviation of the mean.

        #### 9.3 Properties of Expectation and Variance
        Expectation and Variance have several useful properties that simplify calculations and analysis:

        *   **Properties of Expectation (Linearity of Expectation):**
            *   E[c] = c (Expected value of a constant is the constant itself)
            *   E[c*X] = c*E[X] (Constant factor can be pulled out)
            *   E[X + c] = E[X] + c (Adding a constant shifts the expectation by the constant)
            *   E[X + Y] = E[X] + E[Y] (Expectation of a sum is the sum of expectations - holds even if X and Y are dependent)
            *   E[aX + bY] = aE[X] + bE[Y]  (General linearity property)

        *   **Properties of Variance:**
            *   Var(c) = 0 (Variance of a constant is zero)
            *   Var(c*X) = c^2 * Var(X) (Constant factor squared when pulled out)
            *   Var(X + c) = Var(X) (Adding a constant doesn't change the variance - just shifts the distribution)
            *   If X and Y are *independent*: Var(X + Y) = Var(X) + Var(Y) (Variance of sum of independent RVs is sum of variances)
            *   **Important:** Var(X + Y) ≠ Var(X) + Var(Y) if X and Y are *dependent*. In general: Var(X + Y) = Var(X) + Var(Y) + 2*Cov(X, Y)

        These properties are fundamental for simplifying calculations involving expected values and variances of linear combinations of random variables.
        """
        )

    with st.expander("📜 10. Limit Theorems"):
        st.markdown(
            """
        ### 10. Limit Theorems: Cornerstones of Statistical Inference
        Limit theorems are fundamental results in probability theory that describe the **behavior of sequences of random variables as the number of variables grows infinitely large**. They are absolutely crucial for statistical inference because they provide the theoretical foundation for using sample statistics to make inferences about population parameters, especially when sample sizes are large.

        #### 10.1 Law of Large Numbers (LLN)
        The **Law of Large Numbers (LLN)**, in its simplest form (Weak Law of Large Numbers), states that the **sample average** of a sequence of independent and identically distributed (i.i.d.) random variables **converges in probability to the true population mean (expected value)** as the sample size increases.

        *   **Informal Statement:**  "As you take more and more samples from a population, the sample mean gets closer and closer to the population mean."

        *   **Formal Statement (Weak Law):** Let X₁, X₂, X₃, ... be a sequence of i.i.d. random variables with mean μ = E[Xᵢ]. Let  X̄_n = (1/n) * Σ from i=1 to n Xᵢ  be the sample mean of the first *n* variables. Then for any ε > 0:
            *   lim (n→∞) P(|X̄_n - μ| > ε) = 0

        *   **Interpretation:** This means that for any small margin of error ε, the probability that the sample mean X̄_n differs from the true mean μ by more than ε approaches zero as *n* goes to infinity. In other words, the sample mean becomes a reliable estimator of the population mean with sufficiently large sample sizes.

        *   **Importance:**
            *   **Foundation of Empirical Estimation:** The LLN justifies using sample means to estimate population means.  It tells us that if we collect enough data, our sample average will likely be close to the true average.
            *   **Basis for Simulation and Monte Carlo Methods:** LLN underpins Monte Carlo simulations.  By simulating a random process many times and averaging the results, we can approximate the true expected value of the process.
            *   **Understanding Long-Run Averages:** It explains why long-run averages in games of chance, experiments, or real-world phenomena tend to stabilize around a predictable value (the expected value).

        #### 10.2 Central Limit Theorem (CLT)
        The **Central Limit Theorem (CLT)** is arguably the most important theorem in statistics. It states that the **sample mean** of a sufficiently large number of i.i.d. random variables, **regardless of the shape of the original population distribution**, will be **approximately normally distributed**.  Furthermore, the distribution of this sample mean will be centered at the population mean (μ) and its standard deviation (standard error of the mean) will be σ/sqrt(n), where σ is the population standard deviation and n is the sample size.

        *   **Informal Statement:** "The distribution of sample means is approximately normal, no matter what the original population looks like (as long as you have a large enough sample size)."

        *   **Formal Statement:** Let X₁, X₂, X₃, ... be a sequence of i.i.d. random variables with mean μ = E[Xᵢ] and standard deviation σ = SD(Xᵢ). Let  X̄_n = (1/n) * Σ from i=1 to n Xᵢ  be the sample mean of the first *n* variables.  Then, as n approaches infinity, the distribution of the **standardized sample mean**:

            *   Z_n = (X̄_n - μ) / (σ/sqrt(n))

            **approaches the Standard Normal Distribution N(0, 1).**

        *   **Interpretation:**
            *   **Shape:**  The distribution of sample means becomes approximately normal, regardless of whether the original population is normal, uniform, exponential, or any other shape.  The bell curve emerges!
            *   **Center:** The distribution of sample means is centered at the population mean μ.  Sample means are unbiased estimators of the population mean.
            *   **Spread:** The standard deviation of the sample mean (standard error) is σ/sqrt(n).  This means the spread of sample means *decreases* as the sample size *n* increases, and it decreases proportionally to the square root of n. Larger samples lead to more precise estimates of the population mean (sample means cluster more tightly around μ).

        *   **Importance:**
            *   **Foundation of Statistical Inference:**  CLT is the cornerstone of many statistical procedures, including hypothesis testing, confidence intervals, and regression analysis. It allows us to use normal distribution theory even when dealing with non-normal populations, as long as we are working with sample means and have reasonably large samples.
            *   **Simplifies Complex Problems:**  Even when dealing with complex or unknown population distributions, CLT allows us to approximate the distribution of sample means with the well-understood normal distribution, making statistical analysis tractable.
            *   **Explains Ubiquity of Normal Distribution:**  The CLT explains why the normal distribution appears so often in nature and various fields. Many observed phenomena are effectively sums or averages of many underlying random factors, and thus tend to be normally distributed due to the CLT.

        **Key Takeaway on Limit Theorems:** The Law of Large Numbers and the Central Limit Theorem are not just abstract mathematical results; they are the workhorses of statistical inference. They bridge the gap between sample data and population characteristics, allowing us to make valid and powerful statistical conclusions and predictions from limited data, which is essential in virtually all data-driven fields.
        """
        )

    with st.expander("📚 Resources for Further Learning"):
        st.markdown(
            """
        To deepen your understanding of probability distributions and related concepts, consider these resources:

        *   **Textbooks:**
            *   **"Introduction to Probability Models" by Sheldon Ross:**  A classic, comprehensive textbook covering probability theory, stochastic processes, and statistical inference.  Excellent for undergraduate and graduate level study.
            *   **"Probability and Statistics for Engineering and the Sciences" by Jay L. Devore:**  A widely used textbook focused on applications in engineering and science. Strong on both probability foundations and statistical methods.
            *   **"Mathematical Statistics with Applications" by Dennis Wackerly, William Mendenhall III, and Richard L. Scheaffer:** A more mathematically rigorous text, suitable for a deeper dive into statistical theory.

        *   **Online Courses:**
            *   **Khan Academy Probability and Statistics:**  Excellent free resource for learning probability and statistics from basic to advanced levels.  Includes video lessons, practice exercises, and personalized learning paths. [https://www.khanacademy.org/math/statistics-probability](https://www.khanacademy.org/math/statistics-probability)
            *   **Coursera and edX Platforms:** Search for courses like "Probability and Statistics," "Statistical Inference," "Probability Theory," "Mathematical Statistics" offered by top universities. Many courses are available for audit (free) or with certificates for a fee. Platforms like Coursera ([https://www.coursera.org/](https://www.coursera.org/)) and edX ([https://www.edx.org/](https://www.edx.org/)).
            *   **MIT OpenCourseware (18.650 Statistics for Applications):**  MIT's undergraduate probability and statistics course materials available freely online.  More mathematically advanced but very comprehensive. [https://ocw.mit.edu/courses/mathematics/18-650-statistics-for-applications-fall-2016/](https://ocw.mit.edu/courses/mathematics/18-650-statistics-for-applications-fall-2016/)

        *   **Websites and Articles:**
            *   **Wolfram MathWorld - Probability and Statistics:** A comprehensive online resource for mathematical definitions, formulas, and explanations related to probability and statistics. [https://mathworld.wolfram.com/ProbabilityandStatistics.html](https://mathworld.wolfram.com/ProbabilityandStatistics.html)
            *   **Seeing Theory: A Visual Introduction to Probability and Statistics:**  Excellent website with interactive visualizations to build intuition for probability and statistics concepts. [https://seeingtheory.brown.edu/](https://seeingtheory.brown.edu/)
            *   **Wikipedia - Probability Distribution:**  A good starting point for overviews and quick definitions of various probability distributions. [https://en.wikipedia.org/wiki/Probability_distribution](https://en.wikipedia.org/wiki/Probability_distribution)
        """
        )

    st.header("🕹️ Interactive Probability Explorations")

    with st.expander("🔢 Random Variables: Discrete vs. Continuous"):
        st.subheader("Identify Random Variable Types")
        rv_examples = [
            "Number of heads in 5 coin flips",
            "Height of a randomly selected person",
            "Number of cars passing a point on a highway per hour",
            "Temperature of a room",
            "Time it takes for a light bulb to burn out",
            "Shoe size of a randomly selected adult",
            "Weight of a bag of apples",
            "Number of emails received per day",
            "Daily rainfall in millimeters",
            "Exam score (percentage)",
        ]
        selected_rv_example = st.selectbox(
            "Select a Random Variable Example:", rv_examples
        )
        variable_type = "Unknown"

        if selected_rv_example in [
            "Number of heads in 5 coin flips",
            "Number of cars passing a point on a highway per hour",
            "Shoe size of a randomly selected adult",
            "Number of emails received per day",
            "Exam score (percentage)",
        ]:  # Exam score can be discrete if only integer percentages are allowed.
            variable_type = "Discrete"
        elif selected_rv_example in [
            "Height of a randomly selected person",
            "Temperature of a room",
            "Time it takes for a light bulb to burn out",
            "Weight of a bag of apples",
            "Daily rainfall in millimeters",
        ]:
            variable_type = "Continuous"

        st.write(f"You selected: **{selected_rv_example}**")
        st.write(f"This Random Variable is likely **{variable_type}**.")
        if variable_type == "Discrete":
            st.success(
                "Correct! Discrete random variables take countable values, often integers (counts)."
            )
        elif variable_type == "Continuous":
            st.success(
                "Correct! Continuous random variables can take any value within a range (measurements)."
            )
        else:
            st.warning("Try selecting an example to see its classification.")

    with st.expander("🎲 Discrete Probability Distributions"):
        st.subheader("Explore Discrete Distributions")
        dist_options_discrete = [
            "Bernoulli",
            "Binomial",
            "Poisson",
            "Geometric",
            "Discrete Uniform",
        ]
        selected_discrete_dist = st.selectbox(
            "Choose a Discrete Distribution:", dist_options_discrete
        )

        st.write(f"### {selected_discrete_dist} Distribution")

        dist_params_discrete = {}  # Dictionary to hold parameters
        if selected_discrete_dist == "Bernoulli":
            dist_params_discrete["p"] = st.slider(
                "Probability of success (p):", 0.01, 1.0, 0.5, step=0.05
            )
            st.write(
                "*(Represents the probability of success in a single trial, like a single coin flip)*"
            )
        elif selected_discrete_dist == "Binomial":
            dist_params_discrete["n"] = st.slider(
                "Number of trials (n):", min_value=1, max_value=50, value=10, step=1
            )
            dist_params_discrete["p"] = st.slider(
                "Probability of success (p):", 0.01, 1.0, 0.5, step=0.05
            )
            st.write(
                "*(Models the number of successes in a fixed number of independent trials)*"
            )
        elif selected_discrete_dist == "Poisson":
            dist_params_discrete["mu"] = st.slider(
                "Average rate of events (λ):",
                min_value=0.1,
                max_value=20.0,
                value=5.0,
                step=0.5,
            )
            st.write(
                "*(Describes the number of events occurring in a fixed interval of time or space)*"
            )
        elif selected_discrete_dist == "Geometric":
            dist_params_discrete["p"] = st.slider(
                "Probability of success (p):", 0.01, 1.0, 0.3, step=0.05
            )
            st.write("*(Models the number of trials needed until the first success)*")
        elif selected_discrete_dist == "Discrete Uniform":
            dist_params_discrete["low"] = st.slider(
                "Lower bound:", min_value=1, max_value=10, value=1, step=1
            )
            dist_params_discrete["high"] = st.slider(
                "Upper bound:",
                min_value=dist_params_discrete["low"],
                max_value=20,
                value=6,
                step=1,
            )
            st.write("*(All outcomes within a range are equally likely)*")

        if selected_discrete_dist != "Discrete Uniform":
            st.pyplot(
                plot_discrete_distribution(selected_discrete_dist, dist_params_discrete)
            )
        else:
            st.pyplot(
                plot_discrete_distribution(
                    selected_discrete_dist,
                    dist_params_discrete,
                    num_points=dist_params_discrete["high"] + 5,
                )
            )  # Adjust num_points for uniform range

        st.markdown(
            """
        **Key Concepts:**
        *   **Probability Mass Function (PMF):**  Gives the probability that a discrete random variable is exactly equal to a certain value.
        *   **Cumulative Distribution Function (CDF):** Gives the probability that a discrete random variable is less than or equal to a certain value.
        """
        )

    with st.expander("📈 Continuous Probability Distributions"):
        st.subheader("Explore Continuous Distributions")
        dist_options_continuous = [
            "Uniform (Continuous)",
            "Exponential",
            "Normal (Gaussian)",
            "Standard Normal",
            "Chi-Squared",
            "t-Distribution",
        ]
        selected_continuous_dist = st.selectbox(
            "Choose a Continuous Distribution:", dist_options_continuous
        )

        st.write(f"### {selected_continuous_dist} Distribution")

        dist_params_continuous = {
            "x_min": -10,
            "x_max": 10,
        }  # Default x range, adjustable
        if selected_continuous_dist == "Uniform (Continuous)":
            dist_params_continuous["a"] = st.slider(
                "Lower bound (a):", -10.0, 10.0, 0.0, step=1.0
            )
            dist_params_continuous["b"] = st.slider(
                "Upper bound (b):", dist_params_continuous["a"], 20.0, 5.0, step=1.0
            )
            st.write("*(Every value within the range [a, b] is equally likely)*")
            dist_params_continuous["x_min"] = dist_params_continuous["a"] - 2
            dist_params_continuous["x_max"] = (
                dist_params_continuous["b"] + 2
            )  # Adjust x range for uniform plot
        elif selected_continuous_dist == "Exponential":
            dist_params_continuous["lambda"] = st.slider(
                "Rate parameter (λ):", 0.1, 5.0, 1.0, step=0.1
            )
            st.write(
                "*(Models the time until an event occurs, often used for waiting times)*"
            )
            dist_params_continuous["x_min"] = 0  # Exponential is for positive values
            dist_params_continuous["x_max"] = 10
        elif selected_continuous_dist == "Normal (Gaussian)":
            dist_params_continuous["mu"] = st.slider(
                "Mean (μ):", -5.0, 5.0, 0.0, step=0.5
            )
            dist_params_continuous["sigma"] = st.slider(
                "Standard deviation (σ):", 0.1, 3.0, 1.0, step=0.1
            )
            st.write(
                "*(The most famous distribution, bell-shaped, describes many natural phenomena)*"
            )
        elif selected_continuous_dist == "Standard Normal":
            st.write("*(Normal distribution with mean=0 and standard deviation=1)*")
            st.write("**Parameters are fixed: μ=0, σ=1**")
        elif selected_continuous_dist == "Chi-Squared":
            dist_params_continuous["df"] = st.slider(
                "Degrees of freedom (df):", min_value=1, max_value=20, value=5, step=1
            )
            st.write(
                "*(Arises in statistics, related to sums of squared standard normal variables)*"
            )
            dist_params_continuous["x_min"] = 0  # Chi-Squared is for positive values
            dist_params_continuous["x_max"] = 20
        elif selected_continuous_dist == "t-Distribution":
            dist_params_continuous["df"] = st.slider(
                "Degrees of freedom (df):", min_value=1, max_value=30, value=5, step=1
            )
            st.write(
                "*(Similar to Normal but with heavier tails, used when population standard deviation is unknown)*"
            )

        st.pyplot(
            plot_continuous_distribution(
                selected_continuous_dist, dist_params_continuous
            )
        )

        st.markdown(
            """
        **Key Concepts:**
        *   **Probability Density Function (PDF):**  Describes the relative likelihood for a continuous random variable to take on a given value. The area under the PDF curve over an interval gives the probability.
        *   **Cumulative Distribution Function (CDF):** Gives the probability that a continuous random variable is less than or equal to a certain value.
        """
        )

    with st.expander("🤝 Joint Probability Distributions (Simplified Example)"):
        st.subheader("Bivariate Distribution: Sum of Two Dice Revisited")
        st.write(
            "Let's visualize the joint distribution of the outcomes when rolling two dice, focusing on their sum."
        )

        if st.button("Show Joint Distribution of Two Dice Sums"):
            sample_space_two_dice = list(product(range(1, 7), range(1, 7)))
            dice_sums = [sum(outcome) for outcome in sample_space_two_dice]
            sum_counts = pd.Series(dice_sums).value_counts().sort_index()
            sum_probs = sum_counts / len(
                sample_space_two_dice
            )  # Probability of each sum

            joint_dist_df = pd.DataFrame(
                {"Sum": sum_probs.index, "Probability": sum_probs.values}
            )

            fig_joint_dice = px.bar(
                joint_dist_df,
                x="Sum",
                y="Probability",
                title="Probability Distribution of Sum of Two Dice (Bivariate)",
                labels={"Sum": "Sum of Dice", "Probability": "P(Sum)"},
            )
            st.plotly_chart(fig_joint_dice)

            st.markdown(
                """
            *   This bar chart represents a **marginal distribution** – specifically, the marginal distribution of the *sum* of the two dice. We've effectively 'marginalized' over the individual die outcomes to focus on the sum.
            *   In a true **joint distribution**, we'd consider the probability of each *pair* of outcomes (e.g., P(Die1=1, Die2=1), P(Die1=1, Die2=2), etc.). Visualizing this directly is a 2D or 3D table or heatmap. This example simplifies to show the distribution of the sum, a derived variable.
            """
            )
            st.info(
                "For truly joint distributions of two or more variables, we analyze the probabilities of combinations of their values. This example simplifies to the sum as a derived variable."
            )

    with st.expander("📊 Expectation and Variance"):
        st.subheader("Calculate Expectation and Variance Interactively")
        st.write(
            "Define a simple discrete random variable and see how expectation and variance change."
        )

        num_outcomes_exp_var = st.number_input(
            "Number of Possible Outcomes:", min_value=2, max_value=6, value=3, step=1
        )
        outcomes_exp_var = []
        probabilities_exp_var = []

        st.write("Define Outcomes and Probabilities:")
        for i in range(num_outcomes_exp_var):
            col1, col2 = st.columns(2)
            with col1:
                outcome = st.number_input(
                    f"Outcome {i+1}:", value=i + 1, key=f"outcome_{i}"
                )
                outcomes_exp_var.append(outcome)
            with col2:
                probability = st.number_input(
                    f"Probability {i+1}:",
                    min_value=0.0,
                    max_value=1.0,
                    value=1.0 / num_outcomes_exp_var,
                    step=0.05,
                    format="%.2f",
                    key=f"prob_{i}",
                )
                probabilities_exp_var.append(probability)

        if (
            len(probabilities_exp_var) == num_outcomes_exp_var
        ):  # Ensure probabilities are entered
            if (
                abs(sum(probabilities_exp_var) - 1.0) > 1e-6
            ):  # Check if probabilities sum to approximately 1
                st.error("Probabilities must sum to 1. Please adjust.")
            else:
                expected_value = sum(
                    [
                        outcomes_exp_var[i] * probabilities_exp_var[i]
                        for i in range(num_outcomes_exp_var)
                    ]
                )
                variance = sum(
                    [
                        (outcomes_exp_var[i] - expected_value) ** 2
                        * probabilities_exp_var[i]
                        for i in range(num_outcomes_exp_var)
                    ]
                )
                std_deviation = variance**0.5

                st.write(f"**Expected Value (Mean):** {expected_value:.3f}")
                st.write(f"**Variance:** {variance:.3f}")
                st.write(f"**Standard Deviation:** {std_deviation:.3f}")

                st.markdown(
                    """
                **Key Concepts:**
                *   **Expected Value (Mean):** The average value you would expect to get if you repeated the experiment many times. It's a measure of central tendency.
                *   **Variance:**  Measures the spread or dispersion of the random variable around its mean.
                *   **Standard Deviation:** The square root of the variance, also measures spread but in the original units of the random variable.
                """
                )

    with st.expander(
        "📈 Limit Theorems: Law of Large Numbers & Central Limit Theorem (Visual Demos)"
    ):
        st.subheader("Visualizing Limit Theorems")

        st.subheader("Law of Large Numbers (LLN)")
        st.write(
            "See how the sample mean approaches the true mean as sample size increases."
        )
        num_trials_lln = st.slider(
            "Number of Trials (LLN Demo):",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            key="lln_slider",
        )

        if st.button("Run LLN Demo (Dice Rolls)"):
            cumulative_means = []
            dice_rolls_lln = generate_dice_roll(num_trials_lln)

            for i in range(1, num_trials_lln + 1):
                sample = dice_rolls_lln[:i]
                sample_mean = np.mean(sample)
                cumulative_means.append(sample_mean)

            fig_lln, ax_lln = plt.subplots()
            ax_lln.plot(
                range(1, num_trials_lln + 1),
                cumulative_means,
                label="Cumulative Sample Mean",
            )
            ax_lln.axhline(y=3.5, color="r", linestyle="--", label="True Mean (3.5)")
            ax_lln.set_xlabel("Number of Rolls")
            ax_lln.set_ylabel("Cumulative Sample Mean")
            ax_lln.set_title("Law of Large Numbers Demo")
            ax_lln.legend()
            st.pyplot(fig_lln)
            st.info(
                "Observe how the cumulative sample mean converges towards the true mean (3.5) of a fair die as the number of rolls increases."
            )

        st.subheader("Central Limit Theorem (CLT)")
        st.write(
            "See how the distribution of sample means approaches a Normal distribution, regardless of the original population distribution."
        )
        sample_size_clt = st.slider(
            "Sample Size (for CLT, n):",
            min_value=2,
            max_value=50,
            value=10,
            step=1,
            key="clt_sample_size",
        )
        num_samples_clt = st.slider(
            "Number of Samples (CLT Demo):",
            min_value=100,
            max_value=5000,
            value=1000,
            step=100,
            key="clt_num_samples",
        )
        population_dist_clt = st.selectbox(
            "Choose Population Distribution:",
            ["Uniform (Discrete)", "Exponential"],
            index=0,
            key="clt_dist_select",
        )

        if st.button("Run CLT Demo"):
            sample_means_clt = []
            with st.spinner("Simulating Central Limit Theorem..."):
                for _ in range(num_samples_clt):
                    if population_dist_clt == "Uniform (Discrete)":
                        population_samples = [
                            random.randint(1, 6) for _ in range(sample_size_clt)
                        ]  # Discrete Uniform (Dice)
                    elif population_dist_clt == "Exponential":
                        population_samples = np.random.exponential(
                            scale=1, size=sample_size_clt
                        )  # Exponential (mean=1)
                    sample_mean_clt = np.mean(population_samples)
                    sample_means_clt.append(sample_mean_clt)

                fig_clt = px.histogram(
                    sample_means_clt,
                    nbins=30,
                    title=f"Central Limit Theorem Demo (Population: {population_dist_clt}, Sample Size n={sample_size_clt})",
                    labels={"value": "Sample Mean", "count": "Frequency"},
                )
                st.plotly_chart(fig_clt)
                st.info(
                    "Notice how the distribution of sample means becomes approximately Normal (bell-shaped) as the number of samples increases, even if the original population distribution is not Normal (like Uniform or Exponential)."
                )

        st.markdown(
            """
        **Key Concepts:**
        *   **Law of Large Numbers (LLN):**  The average of the results obtained from a large number of trials should be close to the expected value, and will tend to become closer as more trials are performed.
        *   **Central Limit Theorem (CLT):**  The distribution of the *sum* (or average) of a large number of independent, identically-distributed random variables, regardless of the original distribution's form, will be approximately a normal distribution. This is incredibly powerful in statistics!
        """
        )

    st.header("💪 Practice Exercises")
    st.markdown(
        """
    1.  **Bernoulli Distribution:**
        *   Consider a biased coin with probability of heads p=0.6. What is the probability of getting tails in a single flip? Calculate the mean and variance of this Bernoulli distribution.
        *   Simulate 1000 flips of this biased coin and calculate the empirical probability of heads. How close is it to the theoretical probability?

    2.  **Binomial Distribution:**
        *   Suppose you roll a fair six-sided die 5 times. What is the probability of getting exactly two sixes? What is the expected number of sixes?
        *   Generate 10,000 samples from a Binomial distribution with n=5 and p=1/6. Plot a histogram of the samples and compare the empirical distribution to the theoretical PMF.

    3.  **Poisson Distribution:**
        *   Customers arrive at a store at an average rate of 5 per hour. What is the probability that exactly 3 customers will arrive in a given hour? What is the probability that more than 5 customers will arrive?
        *   Simulate customer arrivals for 1000 hours using a Poisson distribution with μ=5. Calculate the empirical mean and variance of customer arrivals per hour.

    4.  **Geometric Distribution:**
        *   You are trying to sell a product door-to-door. Suppose the probability of making a sale at any given house is 0.1. What is the probability that you will make your first sale on your 3rd attempt? What is the expected number of houses you need to visit until your first sale?
        *   Simulate this sales process 10,000 times and visualize the distribution of the number of attempts needed for the first sale.

    5.  **Normal Distribution:**
        *   Assume human heights are normally distributed with a mean of 170 cm and a standard deviation of 10 cm. What is the probability that a randomly selected person is taller than 190 cm? What is the probability they are between 160 cm and 180 cm tall?
        *   Generate 10,000 samples from this normal distribution. Plot a histogram and overlay the theoretical PDF to visualize the fit.

    6.  **Central Limit Theorem (CLT):**
        *   Consider a Uniform distribution between 0 and 1. It is definitely not normal. Generate 1000 samples of size n=2, n=10, and n=30. For each sample size, calculate the sample mean. Plot histograms of these sample means for each sample size. Observe how the distribution of sample means changes as n increases and approaches a normal distribution, even though the original distribution is uniform.

    7. **Covariance and Correlation:**
        *   Consider two random variables, X = height and Y = weight of individuals.  Explain whether you would expect a positive, negative, or zero covariance/correlation between them. Why?
        *   Think of two variables that you would expect to have a negative correlation. Provide a real-world example.
    """
    )

    st.header("✅ Knowledge Check: Test Your Understanding")

    quiz_questions = [  # Quiz questions - same as before for now
        {
            "question": "Which of the following is NOT a fundamental axiom of probability?",
            "options": [
                "Non-negativity: P(E) ≥ 0",
                "Probability of Sample Space: P(S) = 1",
                "Additivity for Mutually Exclusive Events",
                "Multiplicativity for Independent Events",
            ],
            "answer": "Multiplicativity for Independent Events",
            "solution": "Multiplicativity for independent events is a consequence of the axioms, not an axiom itself. The three axioms are Non-negativity, Probability of Sample Space, and Additivity for Mutually Exclusive Events.",
        },
        {
            "question": "What is the formula for calculating classical probability?",
            "options": [
                "P(Event) = (Number of favorable outcomes) / (Total number of possible outcomes)",
                "P(Event) ≈ (Number of times event occurred) / (Total trials)",
                "P(A|B) = P(A ∩ B) / P(B)",
                "P(A|B) = [P(B|A) * P(A)] / P(B)",
            ],
            "answer": "P(Event) = (Number of favorable outcomes) / (Total number of possible outcomes)",
            "solution": "Classical probability applies when all outcomes are equally likely.",
        },
        {
            "question": "If events A and B are mutually exclusive, what is P(A ∩ B)?",
            "options": ["P(A) + P(B)", "P(A) * P(B)", "0", "1"],
            "answer": "0",
            "solution": "Mutually exclusive events cannot occur together, so their intersection is empty, and its probability is 0.",
        },
        {
            "question": "Bayes' Theorem is used to:",
            "options": [
                "Calculate empirical probability",
                "Reverse conditional probability",
                "Determine if events are independent",
                "Calculate classical probability",
            ],
            "answer": "Reverse conditional probability",
            "solution": "Bayes' Theorem allows us to find P(A|B) if we know P(B|A), P(A), and P(B).",
        },
        {
            "question": "Which type of random variable can take on any value within a given range?",
            "options": [
                "Discrete Random Variable",
                "Continuous Random Variable",
                "Categorical Random Variable",
                "Binary Random Variable",
            ],
            "answer": "Continuous Random Variable",
            "solution": "Continuous random variables have uncountable possible values within a range.",
        },
        {
            "question": "What is 'Empirical Probability' based on?",
            "options": [
                "Theoretical calculations",
                "Personal beliefs",
                "Observed data from experiments",
                "Mathematical axioms",
            ],
            "answer": "Observed data from experiments",
            "solution": "Empirical probability is derived from actual experiments or observations.",
        },
        {
            "question": "If events A and B are independent, then P(A ∩ B) = ?",
            "options": ["P(A) + P(B)", "P(A) * P(B)", "0", "1"],
            "answer": "P(A) * P(B)",
            "solution": "This is the condition for independence of events.",
        },
        {
            "question": "In Bayes' Theorem, P(A) represents the:",
            "options": [
                "Posterior probability",
                "Likelihood",
                "Prior probability",
                "Evidence",
            ],
            "answer": "Prior probability",
            "solution": "P(A) is the prior probability of event A, before considering event B.",
        },
        {
            "question": "Which field does NOT heavily rely on probability theory?",
            "options": ["Finance", "Physics", "Literature", "Machine Learning"],
            "answer": "Literature",
            "solution": "While probability might indirectly influence narrative structure in literature, it is not a *foundational* tool in the same way as in the other fields.",
        },
        {
            "question": "What is a 'sample space'?",
            "options": [
                "A subset of possible outcomes",
                "The set of all possible outcomes of an experiment",
                "A visual representation of probabilities",
                "A measure of risk",
            ],
            "answer": "The set of all possible outcomes of an experiment",
            "solution": "The sample space is the foundation for defining events and probabilities.",
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
                st.success(f"Question {i+1}: Correct! 🎉")  # More engaging feedback
            else:
                st.error(
                    f"Question {i+1}: Incorrect. Let's review the solution below. 🧐"
                )  # More encouraging tone

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

    st.header("🌐 Real-World Applications of Probability")
    st.markdown(
        """
    Probability theory is not just abstract math—it's a fundamental tool that shapes our understanding and interacts with the world around us. Here are just a few examples:

    *   **Finance:**  From pricing options and managing risk in investment portfolios to developing algorithmic trading strategies, probability and statistics are at the heart of modern finance. Models like Geometric Brownian Motion (a stochastic process) are used to describe stock price movements, though more sophisticated models are constantly being developed.
    *   **Insurance:** Actuarial science relies heavily on probability to calculate premiums and assess risk. Insurance companies use probability distributions to model the likelihood of events like accidents, natural disasters, or mortality, ensuring they can cover potential payouts.
    *   **Medicine and Public Health:**  Clinical trials, epidemiology, and drug development all use probability and statistics.  Understanding the probability of treatment success, disease spread, or side effects is crucial for medical decision-making and public health policy.  Bayesian methods are increasingly used in medical diagnostics and personalized medicine.
    *   **Weather Forecasting:**  Modern weather forecasting is probabilistic. Instead of saying "it will rain tomorrow," forecasts often give a probability of rain (e.g., "70% chance of rain"). These probabilities are derived from complex models that incorporate vast amounts of atmospheric data and use probability to quantify uncertainty.
    *   **Genetics and Biology:**  Probability is used to understand genetic inheritance, model population dynamics, and analyze biological data.  Markov Chains are applied to DNA sequencing analysis, and stochastic processes are used to model the random behavior of molecules in cells.
    *   **Telecommunications and Networking:**  Designing efficient and reliable communication networks relies on probability. Queuing theory (based on stochastic processes) helps optimize network traffic flow, and probability is used to model signal noise and error rates in data transmission.
    *   **Machine Learning and Artificial Intelligence:**  Probability is absolutely foundational to machine learning. Many ML algorithms are probabilistic at their core, from Bayesian networks to neural networks (which are trained using probabilistic methods like gradient descent). Probability is essential for handling uncertainty, making predictions, and assessing the confidence of AI systems.
    *   **Quality Control and Manufacturing:**  Probability and statistics are used to monitor manufacturing processes, detect defects, and ensure product quality. Statistical process control (SPC) uses control charts and probability to identify when a process is going out of control.
    *   **Gaming and Entertainment:**  From designing fair casino games to creating realistic simulations and AI opponents in video games, probability is obviously essential. Random number generators (RNGs) are a core component of many entertainment systems.
    *   **Scientific Research (across disciplines):**  Probability and statistics are the bedrock of empirical research in nearly every scientific field. From designing experiments and collecting data to analyzing results and drawing conclusions, probability provides the tools to handle uncertainty and make inferences from data.

    These examples barely scratch the surface. Probability is a universal language for dealing with uncertainty, and its applications are constantly expanding as our ability to collect and analyze data grows.
    """
    )


if __name__ == "__main__":
    main()

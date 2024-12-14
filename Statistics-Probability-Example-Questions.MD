# Statistics & Probability for Meta Data Science Interviews

This page provides a detailed review of statistics and probability concepts relevant to Meta Data Science (Analytical) interviews. 
It is intended as a supplement to the main Meta Data Science Interview Preparation Handbook.

---

## Detailed Concepts and Practice Questions

### Probability and Combinations

**Question 1: On Instagram, the probability of a user watching a story to completion is 0.8. If a user posts a sequence of 4 stories, what is the probability that a viewer will watch all 4 stories? What about at least 2 stories?**

**Key Concept(s):** Independent Events, Binomial Probability

**Explanation:** This question tests understanding of independent events and binomial probability (for the "at least 2" part).

*   **Watching all 4:** Since each story view is independent, we multiply the probabilities: 0.8 * 0.8 * 0.8 * 0.8 = 0.8<sup>4</sup> = 0.4096 or 40.96%
*   **Watching at least 2:** This means watching 2, 3, or 4 stories. It's easier to calculate the complement (0 or 1 story) and subtract from 1.

    *   0 stories: 0.2<sup>4</sup> = 0.0016
    *   1 story: (4 choose 1) * 0.8 * 0.2<sup>3</sup> = 4 * 0.8 * 0.008 = 0.0256
    *   P(at least 2) = 1 - (0.0016 + 0.0256) = 1 - 0.0272 = 0.9728 or 97.28%

**Answer:** The probability of watching all 4 stories is 40.96%. The probability of watching at least 2 is 97.28%.

### Hypothesis Testing

**Question 2: What is the difference between Type I and Type II errors in hypothesis testing?**

**Key Concept(s):** Type I Error, Type II Error, Null Hypothesis, Alternative Hypothesis

**Explanation:** This is a fundamental concept in hypothesis testing.

*   **Type I Error (False Positive):** Rejecting the null hypothesis when it is actually true. This is often represented by α (alpha), the significance level. Example: Concluding that a new feature improves conversion rates when it actually has no effect.
*   **Type II Error (False Negative):** Failing to reject the null hypothesis when it is actually false. This is often represented by β (beta). Example: Concluding that a new feature has no effect on conversion rates when it actually does improve them.

**Answer:** A Type I error is a false positive (incorrectly rejecting a true null hypothesis), while a Type II error is a false negative (incorrectly failing to reject a false null hypothesis).

### Probability

**Question 3: Say you roll a die three times. What is the probability of getting two sixes in a row?**

**Key Concept(s):** Independent Events, Probability

**Explanation:** This involves calculating probabilities of sequential events.

There are 6<sup>3</sup> = 216 possible outcomes when rolling a die three times. The sequences with two sixes in a row are:

*   6, 6, 1
*   6, 6, 2
*   6, 6, 3
*   6, 6, 4
*   6, 6, 5
*   6, 6, 6
*   1, 6, 6
*   2, 6, 6
*   3, 6, 6
*   4, 6, 6
*   5, 6, 6

There are 11 such outcomes.

**Answer:** The probability is 11/216, or approximately 5.09%.

### Statistical Inference

**Question 4: Can you explain what a p-value and confidence interval are, but in layman's terms?**

**Key Concept(s):** p-value, Confidence Interval, Statistical Significance

**Explanation:** These are key concepts for interpreting statistical results.

*   **p-value:** The probability of observing the results (or more extreme results) of your experiment if there were actually no real effect (if the null hypothesis were true). A small p-value (typically below 0.05) suggests strong evidence against the null hypothesis. Imagine you're testing a new drug. If the p-value is 0.03, it means there's only a 3% chance you'd see the observed improvement in patients if the drug was actually useless.
*   **Confidence Interval:** A range of values that is likely to contain the true population parameter (like the average user session time or conversion rate). A 95% confidence interval means that if you were to repeat the experiment many times, 95% of the calculated intervals would contain the true population value. For example, a 95% confidence interval for average session time of (10-12 seconds) means that we are 95% sure that the true average session time lies between 10 and 12 seconds.

**Answer:** A p-value tells you how surprising your results are if there's no real effect. A confidence interval gives you a plausible range for the true value you're trying to estimate.

### Statistical Relationships

**Question 5: Explain the concept of covariance and correlation. How are they different, and what do they measure?**

**Key Concept(s):** Covariance, Correlation

**Explanation:** These measures describe the relationship between two variables.

*   **Covariance:** Measures how two variables change together. A positive covariance means they tend to increase or decrease together, while a negative covariance means they tend to move in opposite directions. However, the magnitude of covariance is difficult to interpret because it's dependent on the scales of the variables.
*   **Correlation:** A standardized measure of the linear relationship between two variables. It ranges from -1 to +1. -1 indicates a perfect negative correlation, +1 indicates a perfect positive correlation, and 0 indicates no linear correlation. Correlation is easier to interpret than covariance because it's on a fixed scale.

**Answer:** Covariance measures the direction of a linear relationship, while correlation measures both the direction and strength of the linear relationship, making it easier to compare relationships between different pairs of variables.

### Bayes' Theorem (Applied)

**Question 6: A Facebook Ads analyst is investigating the effectiveness of a new ad targeting algorithm. As a general baseline, they know that 1% of all users who see an ad convert (make a purchase). The new algorithm correctly identifies 80% of users who will convert for an ad. The algorithm also incorrectly flags 10% of non-converting users as likely to convert. Given that the algorithm has flagged a user as likely to convert, what is the probability that this user will actually convert?**

**Key Concept(s):** Bayes' Theorem, Conditional Probability

**Explanation:** This is a classic application of Bayes' Theorem.

*   P(Convert) = 0.01 (Prior probability of conversion)
*   P(Not Convert) = 0.99
*   P(Flagged | Convert) = 0.80 (True Positive Rate)
*   P(Flagged | Not Convert) = 0.10 (False Positive Rate)

We want to find P(Convert | Flagged). Using Bayes' Theorem:

P(Convert | Flagged) = \[P(Flagged | Convert) \* P(Convert)] / P(Flagged)

First, we need to calculate P(Flagged):

P(Flagged) = P(Flagged | Convert) \* P(Convert) + P(Flagged | Not Convert) \* P(Not Convert)
P(Flagged) = (0.80 \* 0.01) + (0.10 \* 0.99) = 0.008 + 0.099 = 0.107

Now we can calculate P(Convert | Flagged):

P(Convert | Flagged) = (0.80 \* 0.01) / 0.107 = 0.008 / 0.107 ≈ 0.0748 or 7.48%

**Answer:** Given that the algorithm has flagged a user as likely to convert, there is approximately a 7.48% chance that the user will actually convert. This highlights that even with a good algorithm, if the base conversion rate is very low, the positive predictions will still have a relatively high false positive rate.

### Hypothesis Testing (A/B Testing)

**Question 7: You're analyzing user engagement with a new feature. You observe that users who interact with the feature spend significantly more time on the platform. How would you determine if this increase in time spent is statistically significant?**

**Key Concept(s):** Hypothesis Testing, A/B Testing, Statistical Significance, t-test, Mann-Whitney U test

**Explanation:** This tests understanding of hypothesis testing and A/B testing.

**Answer:** You would conduct an A/B test.

1.  **Define Hypotheses:**

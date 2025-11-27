# Statistics & Probability for Meta Data Science Interviews

This page provides a detailed review of statistics and probability concepts relevant to Meta Data Science (Analytical) interviews. It is intended as a supplement to the main Meta Data Science Interview Preparation Handbook.

---

<div style="page-break-after: always;"></div>

## Detailed Concepts and Practice Questions

### Probability and Combinations

**Question 1: On Instagram, the probability of a user watching a story to completion is 0.8. If a user posts a sequence of 4 stories, what is the probability that a viewer will watch all 4 stories? What about at least 2 stories?**

**Key Concept(s):** Independent Events, Binomial Probability

**Explanation:** This question tests understanding of independent events and binomial probability (for the "at least 2" part).

*   **Watching all 4:** Since each story view is independent, we multiply the probabilities: \(0.8 * 0.8 * 0.8 * 0.8 = 0.8^4 = 0.4096\) or 40.96%
*   **Watching at least 2:** This means watching 2, 3, or 4 stories. It's easier to calculate the complement (0 or 1 story) and subtract from 1.
    *   0 stories: \(0.2^4 = 0.0016\)
    *   1 story: \(\binom{4}{1} * 0.8 * 0.2^3 = 4 * 0.8 * 0.008 = 0.0256\)
    *   P(at least 2) = \(1 - (0.0016 + 0.0256) = 1 - 0.0272 = 0.9728\) or 97.28%

**Answer:** The probability of watching all 4 stories is 40.96%. The probability of watching at least 2 is 97.28%.

<div style="page-break-after: always;"></div>

### Hypothesis Testing

**Question 2: What is the difference between Type I and Type II errors in hypothesis testing?**

**Key Concept(s):** Type I Error, Type II Error, Null Hypothesis, Alternative Hypothesis

**Explanation:** This is a fundamental concept in hypothesis testing.

*   **Type I Error (False Positive):** Rejecting the null hypothesis when it is actually true. This is often represented by \(\alpha\) (alpha), the significance level. Example: Concluding that a new feature improves conversion rates when it actually has no effect.
*   **Type II Error (False Negative):** Failing to reject the null hypothesis when it is actually false. This is often represented by \(\beta\) (beta). Example: Concluding that a new feature has no effect on conversion rates when it actually does improve them.

**Answer:** A Type I error is a false positive (incorrectly rejecting a true null hypothesis), while a Type II error is a false negative (incorrectly failing to reject a false null hypothesis).

<div style="page-break-after: always;"></div>

### Probability

**Question 3: Say you roll a die three times. What is the probability of getting two sixes in a row?**

**Key Concept(s):** Independent Events, Probability

**Explanation:** This involves calculating probabilities of sequential events.

There are \(6^3 = 216\) possible outcomes when rolling a die three times. The sequences with two sixes in a row are:

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

<div style="page-break-after: always;"></div>

### Statistical Inference
**Question 4: Can you explain what a p-value and confidence interval are, but in layman's terms?**

**Key Concept(s):** p-value, Confidence Interval, Statistical Significance

**Explanation:** These are key concepts for interpreting statistical results.

*   **p-value:** The probability of observing the results (or more extreme results) of your experiment if there were actually no real effect (if the null hypothesis were true). A small p-value (typically below 0.05) suggests strong evidence against the null hypothesis. Imagine you're testing a new drug. If the p-value is 0.03, it means there's only a 3% chance you'd see the observed improvement in patients if the drug was actually useless.
*   **Confidence Interval:** A range of values that is likely to contain the true population parameter (like the average user session time or conversion rate). A 95% confidence interval means that if you were to repeat the experiment many times, 95% of the calculated intervals would contain the true population value. For example, a 95% confidence interval for average session time of (10-12 seconds) means that we are 95% sure that the true average session time lies between 10 and 12 seconds.

**Answer:** A p-value tells you how surprising your results are if there's no real effect. A confidence interval gives you a plausible range for the true value you're trying to estimate.

<div style="page-break-after: always;"></div>

### Statistical Relationships

**Question 5: Explain the concept of covariance and correlation. How are they different, and what do they measure?**

**Key Concept(s):** Covariance, Correlation

**Explanation:** These measures describe the relationship between two variables.

*   **Covariance:** Measures how two variables change together. A positive covariance means they tend to increase or decrease together, while a negative covariance means they tend to move in opposite directions. However, the magnitude of covariance is difficult to interpret because it's dependent on the scales of the variables.
*   **Correlation:** A standardized measure of the linear relationship between two variables. It ranges from -1 to +1. -1 indicates a perfect negative correlation, +1 indicates a perfect positive correlation, and 0 indicates no linear correlation. Correlation is easier to interpret than covariance because it's on a fixed scale.

**Answer:** Covariance measures the direction of a linear relationship, while correlation measures both the direction and strength of the linear relationship, making it easier to compare relationships between different pairs of variables.

<div style="page-break-after: always;"></div>

### Bayes' Theorem (Applied)

**Question 6: A Facebook Ads analyst is investigating the effectiveness of a new ad targeting algorithm. As a general baseline, they know that 1% of all users who see an ad convert (make a purchase). The new algorithm correctly identifies 80% of users who will convert for an ad. The algorithm also incorrectly flags 10% of non-converting users as likely to convert. Given that the algorithm has flagged a user as likely to convert, what is the probability that this user will actually convert?**

**Key Concept(s):** Bayes' Theorem, Conditional Probability

**Explanation:** This is a classic application of Bayes' Theorem.

*   \(P(\text{Convert}) = 0.01\) (Prior probability of conversion)
*  \( P(\text{Not Convert}) = 0.99 \)
*   \(P(\text{Flagged} | \text{Convert}) = 0.80\) (True Positive Rate)
*   \(P(\text{Flagged} | \text{Not Convert}) = 0.10\) (False Positive Rate)

We want to find \(P(\text{Convert} | \text{Flagged})\). Using Bayes' Theorem:

\(P(\text{Convert} | \text{Flagged}) = \frac{P(\text{Flagged} | \text{Convert}) * P(\text{Convert})}{P(\text{Flagged})}\)

First, we need to calculate \(P(\text{Flagged})\):

\(P(\text{Flagged}) = P(\text{Flagged} | \text{Convert}) * P(\text{Convert}) + P(\text{Flagged} | \text{Not Convert}) * P(\text{Not Convert})\)
\(P(\text{Flagged}) = (0.80 * 0.01) + (0.10 * 0.99) = 0.008 + 0.099 = 0.107\)

Now we can calculate \(P(\text{Convert} | \text{Flagged})\):

\(P(\text{Convert} | \text{Flagged}) = (0.80 * 0.01) / 0.107 = 0.008 / 0.107 \approx 0.0748\) or 7.48%

**Answer:** Given that the algorithm has flagged a user as likely to convert, there is approximately a 7.48% chance that the user will actually convert. This highlights that even with a good algorithm, if the base conversion rate is very low, the positive predictions will still have a relatively high false positive rate.

<div style="page-break-after: always;"></div>

### Hypothesis Testing (A/B Testing)

**Question 7: You're analyzing user engagement with a new feature. You observe that users who interact with the feature spend significantly more time on the platform. How would you determine if this increase in time spent is statistically significant?**

**Key Concept(s):** Hypothesis Testing, A/B Testing, Statistical Significance, Z-test, Mann-Whitney U test

**Answer:**

1.  **Define Hypotheses:**

    *   Null Hypothesis (H0): There is no significant difference in the proportion (e.g., CTR) between the control group (A) and the treatment group (B). Mathematically:
    
         \( p_A = p_B \)  or equivalently \( p_A - p_B = 0 \)

        Where:

        *   \( p_A \) is the proportion (e.g., CTR) of the control group.
        *   \( p_B \) is the proportion of the treatment group.

    *   Alternative Hypothesis (H1): There is a significant difference in the proportion between the two groups. This is a two-tailed test (we're not specifying the direction). Mathematically:

        \( p_A \ne p_B \) or equivalently \( p_A - p_B \ne 0 \)

2.  **Choose a Test:** A two-sample Z-test for proportions is appropriate when we are dealing with proportions (like click-through rates, conversion rates) and the sample sizes are large enough to invoke the Central Limit Theorem.

3.  **Calculate the Test Statistic (Z-score) and p-value:**

    To calculate the Z-score and p-value, we follow these steps:

    *   **Collect Data:** Let:
        *   \( x_A \) = Number of successes (e.g., clicks) in group A
        *   \( n_A \) = Total number of trials (e.g., impressions) in group A
        *   \( x_B \) = Number of successes in group B
        *   \( n_B \) = Total number of trials in group B

    *   **Calculate Observed Proportions:**
        *   \(\hat{p}_A = \frac{x_A}{n_A}\)
        *  \(\hat{p}_B = \frac{x_B}{n_B}\)

    *   **Calculate the Pooled Proportion (\(\hat{p}\)):**
        *  \(\hat{p} = \frac{x_A + x_B}{n_A + n_B}\)

    *   **Calculate the Standard Error of the Difference (SE):**
        *  \(SE = \sqrt{\hat{p}(1 - \hat{p}) \left(\frac{1}{n_A} + \frac{1}{n_B}\right)}\)

    *   **Calculate the Z-score:**
        *   \(Z = \frac{\hat{p}_B - \hat{p}_A}{SE}\)

    *   **Calculate the p-value:** For a two-tailed test:
        *   \(p\text{-value} = 2 \times P(Z > |Z|)\)

        Where \(P(Z > |Z|)\) is found using a Z-table or statistical software.

4.  **Interpret the Results:**

    *   Compare the p-value to the chosen significance level (\(\alpha\)), typically 0.05.
    *   **If \(p\text{-value} \le \alpha\):** Reject the null hypothesis (H0). This indicates that there is statistically significant evidence of a difference in proportions between the two groups.
    *   **If \(p\text{-value} > \alpha\):** Fail to reject the null hypothesis (H0). This means there is not enough evidence to conclude a statistically significant difference.

    In addition to statistical significance (determined by the p-value), it's crucial to consider the *effect size*. The effect size quantifies the magnitude of the observed difference. Even if a difference is statistically significant, it might be too small to be practically meaningful. For proportions, common effect size measures include the absolute difference (\(\hat{p}_B - \hat{p}_A\)) or relative change.


<div style="page-break-after: always;"></div>

**Question 8: Explain the difference between a one-tailed and a two-tailed hypothesis test. When would you use each?**

**Key Concept(s):** One-tailed Test, Two-tailed Test, Hypothesis Testing

**Explanation:** This is about the directionality of the hypothesis.

*   **One-tailed Test:** Tests for a difference in *one* direction. For example, testing if a new feature *increases* conversion rates. The alternative hypothesis specifies a direction (e.g.,  \(\mu > \mu_0\) or \(\mu < \mu_0\)).
*   **Two-tailed Test:** Tests for a difference in *either* direction. For example, testing if a new feature has *any* effect (positive or negative) on conversion rates. The alternative hypothesis simply states that there is a difference (e.g., \(\mu \ne \mu_0\)).

**Answer:** Use a one-tailed test when you have a specific directional hypothesis (you only care about an increase or a decrease). Use a two-tailed test when you're interested in any difference, regardless of direction.

<div style="page-break-after: always;"></div>

**Question 9: You have data on user sign-ups for your platform. You notice a large spike in sign-ups during a particular week. How would you investigate the cause of this spike?**

**Key Concept(s):** Data Analysis, Segmentation, Time Series Analysis, Correlation Analysis

**Explanation:** This tests analytical thinking and applying statistical concepts to a real-world problem.

**Answer:**

1.  **Data Validation:** Ensure the data is accurate and not due to a tracking error.
2.  **External Factors:** Check for any external events that might have driven the spike (e.g., marketing campaigns, media coverage, competitor issues, holidays, viral trends).
3.  **Segmentation:** Analyze sign-ups by different user segments (e.g., demographics, acquisition channel, device type, location) to see if the spike is concentrated in any particular group.
4.  **A/B Testing (if applicable):** If any changes were made to the sign-up process during that week (e.g., new landing page, simplified form), analyze the A/B test results to see if they contributed to the spike.
5.  **Time Series Analysis:** Look for patterns in sign-up data over time (e.g., seasonality, weekly trends) to see if the spike is unusual or part of a recurring trend.
6.  **Correlation Analysis:** Examine correlations between sign-ups and other metrics (e.g., website traffic, social media mentions, search volume, app store rankings) to identify potential contributing factors.

<div style="page-break-after: always;"></div>

**Question 10: What are some methods for dealing with imbalanced datasets, and why are they important?**

**Key Concept(s):** Imbalanced Datasets, Oversampling, Undersampling, SMOTE, Cost-Sensitive Learning

**Explanation:** This is important in machine learning and data analysis when one class is significantly more prevalent than another.

**Answer:** Imbalanced datasets can bias models towards the majority class. Methods to address this include:

*   **Oversampling:** Duplicating instances from the minority class.
*   **Undersampling:** Removing instances from the majority class.
*   **SMOTE (Synthetic Minority Over-sampling Technique):** Creating synthetic instances of the minority class by interpolating between existing minority class instances.
*   **Cost-sensitive learning:** Assigning higher misclassification costs to the minority class during model training.
*   **Collecting more data:** If possible, collecting more data for the minority class can help balance the dataset.

These methods are important because they help models learn to accurately predict the minority class, which is often the class of interest (e.g., fraud detection, churn prediction).

<div style="page-break-after: always;"></div>

**Question 11: Explain the concept of statistical power and its importance in experiment design.**

**Key Concept(s):** Statistical Power, Type II Error, Sample Size, Effect Size, Significance Level

**Explanation:** Relates to the ability of a test to find an effect if one exists.

**Answer:** Statistical power is the probability of correctly rejecting the null hypothesis when it is false (i.e., finding a real effect). It's typically set at 80% (0.8). Low power means the experiment has a low chance of detecting a true effect, leading to potential Type II errors (false negatives). Factors affecting power include:

*   **Sample Size:** Larger sample sizes increase power.
*  **Effect Size:** Larger effects are easier to detect (higher power).
*  **Significance Level (alpha):** Lower alpha (e.g., 0.01 instead of 0.05) decreases power.
*  **Variability (Standard Deviation):** Lower variability in the data increases power.

Power analysis is crucial in experiment design to determine the appropriate sample size needed to achieve the desired power. It helps avoid underpowered studies that may fail to detect real effects, wasting resources and time.

<div style="page-break-after: always;"></div>

### Harder Practice Questions (Social Network Focus)

**Question 18: Confidence Intervals - Click-Through Rates:** You're analyzing the click-through rate (CTR) of a new ad campaign. You observe a CTR of 2% from a sample of 10,000 impressions. Calculate a 95% confidence interval for the true CTR. How would a larger sample size (e.g. 100,000 impressions) impact the width of the confidence interval?**

**Key Concept(s):** Confidence Intervals, Proportions, Sample Size

**Explanation:** This tests the application and interpretation of confidence intervals.

**Answer:**

1.  **Calculate the Standard Error (n=10,000):** \(SE = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{(0.02 * 0.98)}{10000}} \approx 0.0014\)
2.  **Find the Z-score:** For a 95% confidence interval, the z-score is approximately 1.96.
3.  **Calculate the Confidence Interval (n=10,000):** \(CI = p \pm z * SE = 0.02 \pm 1.96 * 0.0014 \approx (0.0173, 0.0227)\) or (1.73%, 2.27%)

With a larger sample size (100,000 impressions):

1.  **Calculate the Standard Error (n=100,000):** \(SE = \sqrt{\frac{(0.02 * 0.98)}{100000}} \approx 0.00044\)
2.  **Calculate the Confidence Interval (n=100,000):** \(CI = 0.02 \pm 1.96 * 0.00044 \approx (0.0191, 0.0209)\) or (1.91%, 2.09%)

**Impact of Sample Size:** As you can see, the confidence interval is much narrower with the larger sample size. This is because the standard error decreases as the sample size increases, leading to a more precise estimate of the true CTR.

<div style="page-break-after: always;"></div>

**Question 19: Combining Concepts - Outliers, Central Limit Theorem, and A/B Testing:** You are A/B testing a new algorithm for ranking posts in a user's feed. You are measuring the average time spent per session. You notice some users have extremely long session durations (potential outliers).

1.  How would you handle these outliers before conducting your statistical test?
2.  How does the Central Limit Theorem help you in this scenario, given that session durations are likely right-skewed?
3.  What statistical test would you use to compare the average time spent between the control and treatment groups?

**Key Concept(s):** Outliers, Central Limit Theorem, A/B Testing, t-test, Mann-Whitney U test

**Explanation:** This question combines several important concepts.

**Answer:**

1.  **Handling Outliers:**
    *   **Investigate:** Determine if the long session durations are due to errors (e.g., app crashes, background activity) or genuine user behavior (e.g., users leaving the app open).
    *   **Transformation:** Consider a log transformation of the session duration data to reduce the influence of outliers and potentially normalize the distribution. This is often a good approach for right-skewed data like session durations.
    *   **Winsorizing/Trimming:** Replace extreme values with less extreme values (Winsorizing) or remove them entirely (Trimming). This should be done cautiously and with a clear justification.
2.  **Central Limit Theorem:** The Central Limit Theorem states that the distribution of the *sample means* of session duration will be approximately normal, even if individual session durations are right-skewed, *provided the sample size is large enough*. This is crucial because it allows you to use statistical tests that assume normality (like t-tests or z-tests) to make inferences about the *population mean* session duration, even though the original data is not normally distributed.
3.  **Statistical Test:**
    *   If the data is approximately normally distributed *after handling outliers/transformations* and the sample sizes are reasonably large, a two-sample t-test is appropriate.
    *   If the data remains skewed even after transformation or if the sample size is small, the Mann-Whitney U test (a non-parametric test) is a better choice as it does not assume normality.

<div style="page-break-after: always;"></div>

**Question 20: Joint Probability and Conditional Probability - User Demographics and Feature Usage:** You have the following data about user demographics and usage of a new feature:

| Demographic | Used Feature | Did Not Use Feature | Total |
|---|---|---|---|
| Age 18-24 | 300 | 200 | 500 |
| Age 25-34 | 400 | 100 | 500 |
| Total | 700 | 300 | 1000 |

1.  What is the probability that a randomly selected user is aged 18-24 *and* used the feature?
2.  What is the probability that a user used the feature *given* they are aged 25-34?
3. Are age demographic and feature usage independent events?

**Key Concept(s):** Joint Probability, Conditional Probability, Independence

**Explanation:** This tests understanding of joint and conditional probabilities and how to assess independence.

**Answer:**

1.  **P(Age 18-24 and Used Feature):** 300/1000 = 0.3
2.  **P(Used Feature | Age 25-34):** 400/500 = 0.8
3.  **Independence:**
    *   P(Age 18-24) = 500/1000 = 0.5
    *   P(Used Feature) = 700/1000 = 0.7
    *   If independent, P(Age 18-24 and Used Feature) should equal P(Age 18-24) \* P(Used Feature) = 0.5 * 0.7 = 0.35
    *   Since 0.3 ≠ 0.35, the events are *not* independent.

<div style="page-break-after: always;"></div>

**Question 21: Confidence Intervals and A/B Testing for Engagement:** You run an A/B test on a new notification system designed to increase user engagement. You measure the average number of sessions per week. The control group (A) has a mean of 5.2 sessions with a standard deviation of 1.5, and the treatment group (B) has a mean of 5.5 sessions with a standard deviation of 1.6. Both groups have a sample size of 5000 users.

1.  Calculate a 95% confidence interval for the difference in means between the two groups.
2.  Based on the confidence interval, can you conclude that the new notification system significantly increased user engagement?

**Key Concept(s):** Confidence Intervals, A/B Testing, Difference of Means, Standard Error

**Explanation:** This tests understanding of confidence intervals in the context of A/B testing.

**Answer:**

1.  **Calculate the Standard Error of the Difference (SE):**

    The standard error of the difference between two means is calculated as:

    $SE = \sqrt{\frac{SD_A^2}{n_A} + \frac{SD_B^2}{n_B}}$

    Where:

    *   $SD_A$ is the standard deviation of group A.
    *   $SD_B$ is the standard deviation of group B.
    *   $n_A$ is the sample size of group A.
    *   $n_B$ is the sample size of group B.

    Plugging in the given values:

    $SE = \sqrt{\frac{1.5^2}{5000} + \frac{1.6^2}{5000}} = \sqrt{\frac{2.25}{5000} + \frac{2.56}{5000}} = \sqrt{0.00045 + 0.000512} = \sqrt{0.000962} \approx 0.031$

2.  **Find the Z-score:**

    For a 95% confidence interval, the Z-score is approximately 1.96. This value corresponds to the point on the standard normal distribution where 95% of the data falls within $\pm$ 1.96 standard deviations of the mean.

3.  **Calculate the Confidence Interval for the Difference in Means:**

    The confidence interval for the difference in means is calculated as:

    $CI = (\bar{x}_B - \bar{x}_A) \pm z \times SE$

    Where:

    *   $\bar{x}_A$ is the mean of group A.
    *   $\bar{x}_B$ is the mean of group B.
    *   $z$ is the Z-score corresponding to the desired confidence level.

    Plugging in the values:

    $CI = (5.5 - 5.2) \pm 1.96 \times 0.031 = 0.3 \pm 0.061 \approx (0.239, 0.361)$

4.  **Conclusion:**

    Since the 95% confidence interval (0.239, 0.361) does *not* contain zero, we can conclude with 95% confidence that there is a statistically significant difference in the average number of sessions per week between the two groups. Because the entire interval is positive, we can confidently state that the new notification system *significantly increased* user engagement, as measured by sessions per week. The average number of sessions per week in group B is likely to be between 0.239 and 0.361 sessions greater than in group A.

<div style="page-break-after: always;"></div>

# Additional Statistics & Probability Practice Questions for Meta Data Science Interviews

These questions build upon the previous set, offering more practice and deeper insights into the required concepts for a Meta Data Science (Analytical) interview.

---
<div style="page-break-after: always;"></div>

### Probability and Combinations

**Question 1: A social media platform notices that 70% of users like at least one post per day. If you randomly select 5 users, what is the probability that exactly 3 of them like at least one post daily?**

**Key Concept(s):** Binomial Probability

**Explanation:** This question tests understanding of the binomial probability distribution.

*   **Setup**: \(n=5\), \(p=0.7\), and we want the probability of exactly 3 successes (\(k=3\)). We will need to use the formula
    \(P(X=k) = \binom{n}{k} * p^k * (1-p)^{n-k}\)
    \(P(X=3) = \binom{5}{3} * 0.7^3 * (1-0.7)^{5-3} =  \frac{5!}{3!2!} * 0.7^3 * 0.3^2 = 10* 0.343 * 0.09= 0.3087 \)

**Answer:** The probability that exactly 3 out of 5 users like at least one post per day is approximately 0.3087 or 30.87%.

<div style="page-break-after: always;"></div>

**Question 2: You have a bag containing 8 red balls and 4 blue balls. If you draw two balls without replacement, what is the probability that both balls are red?**

**Key Concept(s):** Conditional Probability, Dependent Events

**Explanation:** This problem tests understanding of probability without replacement.

*   **1st ball is red**: There are 12 total balls so probability is \(\frac{8}{12}\)
*   **2nd ball is red**: Given the first ball is red, then there are 7 red balls and 11 balls total left so probability is \(\frac{7}{11}\)
*    The probabilty of the two independent steps is \(\frac{8}{12} * \frac{7}{11} = \frac{56}{132} = 0.424\).

**Answer:** The probability that both balls drawn are red is approximately \(\frac{56}{132} \) which equals approximately 0.424.

<div style="page-break-after: always;"></div>

### Hypothesis Testing

**Question 3: Define what a Null Hypothesis is and explain in the context of a A/B test example.**

**Key Concept(s):** Null Hypothesis, A/B Testing

**Explanation:** Tests understanding of the fundamental concept of the Null Hypothesis

*   The null hypothesis in statistical testing, such as during A/B testing, is the statement that there is no significant difference or effect between different scenarios, variables, or groups that are being studied. It essentially asserts that any changes observed in our testing or observation are not because of any real phenomena being studied but are due to random chance. An A/B testing context is if we want to understand the effectiveness of a redesign to the UI interface and so an appropriate Null hypothesis is “There is no statistically significant change between interface A and Interface B when looking at conversion rates".

**Answer:** The Null Hypothesis states there is no effect and it is what you set out to disprove.

<div style="page-break-after: always;"></div>

**Question 4: In hypothesis testing, what is the relationship between the p-value and the significance level? Explain with example scenarios when you would chose to use differing levels of signifcance.**

**Key Concept(s):** p-value, Significance Level

**Explanation:** Tests knowledge of statistical concepts and implications

*   The p-value is compared against the chosen significance level \(\alpha\) (alpha) to determine if the results are statistically significant and if the null hypothesis is to be rejected.
*  The significance level (\(\alpha\)), is typically set at a chosen threshold (often at 0.05), to establish how rare your observation of differences under a Null hypothesis scenario has to be in order to deem our findings statistically signficant.
 * A p-value smaller than  \(\alpha\) results in rejecting the Null Hypothesis. If the \(p>\alpha\), then fail to reject.
* The threshold that is chosen, will relate to your real world needs and so \(\alpha=0.05\)  is not always the right approach. If you were working on high-risk scenarios (e.g., drug trials), a lower \(\alpha\) (such as \(\alpha\)= 0.01 or 0.001) is required. When the risk of falsely concluding that a change makes no impact ( when it in fact might exist) has a higher cost, then you would increase \(\alpha\) above \(0.05\), like 0.10 for less crucial experiments

**Answer:**  The p-value is directly compared with the pre-selected  significance level (\(\alpha\)) to see if findings are statistically significant to reject the null hypothesis, the choice of \(\alpha\) needs to reflect the cost of Type 1 errors for a given research context

<div style="page-break-after: always;"></div>

### Statistical Inference

**Question 5: Describe what a histogram visually represents and discuss how it is different from a box plot, in practical terms.**

**Key Concept(s):** Data Visualization, Histogram, Box Plot

**Explanation:** Tests understanding of common methods to present data.

*   **Histogram:** A histogram displays the distribution of numerical data, grouping it into bins, which the counts then become represented by vertical bars. They highlight how frequent numerical data values or a specified bin occur in the dataset. Histograms show the shape of the distribution, such as being normal or skewed.

*   **Box Plot**:  Box plots, use median and quartiles to demonstrate key percentiles. Box Plots are ideal for understanding measures like inter quartile range and outlier values of your numerical data. They display data by dividing the data into quarters and so less insightful to understand distributional patterns. They show general distribution spread, whereas histograms can visually represent a higher resolution into those distributions and how their underlying nature. Box plots can quickly compare different group of data on key metrics like median and percentiles, histograms generally only display one series of data at one time.

**Answer:** Histograms represent the distribution via frequencies for values of your data, whilst boxplots present key statistical points that show distribution of your dataset and outlier metrics. The use depends on the task at hand and how you wish to represent the core information of a dataset..

<div style="page-break-after: always;"></div>

**Question 6:  You want to know the average daily time a user spends on your application. Explain when you would use the sample mean vs when to use the median.**

**Key Concept(s):** Measures of Central Tendency, Sample Mean, Median

**Explanation:** Tests awareness of when it is more apprpriate to use sample mean or median.

*   The **sample mean**, or average,  is appropriate when the data are reasonably symmetrical or roughly normal and there is little to no outlier data. This can also work if large enough sample is observed to make any distortions small enough due to outlier issues.
*   The **median** on the other hand is more appropriate if your data shows skewed distributions, due to outliers as they wont influence this measure so readily, and often results in better reflection of central tendency in many use case contexts.
* The **Median** could be very insightful, if you wanted to measure something where you felt most common users don’t exhibit an effect of your population parameter (time in application), with outlier values being an unwanted distortion for such analysis. For example If a small subsegment uses the platform for a vast length of time vs everyone else.
* Often use mean as one method to check if the distribution has outlier behaviour where the median would likely also be evaluated if means appears far away, when that can indicate skew that might influence average calculations for certain measures.
 **Answer:** Sample means are appropriate for relatively normal distributions, but you need to observe distribution and make decisions accordingly, but be cautious of potential distortions. In practice mean and median together should also be viewed to highlight these insights with a measure such as median also being evaluated for skew where applicable in such circumstances..


# Statistics & Probability for Meta Data Science Interviews

This page provides a detailed review of statistics and probability concepts relevant to Meta Data Science (Analytical) interviews. It is intended as a supplement to the main Meta Data Science Interview Preparation Handbook.

---

## Probability and Combinations

### Basic Probability

**Question 1: (Easy) On Instagram, the probability of a user watching a story to completion is 0.8. If a user posts a sequence of 4 stories, what is the probability that a viewer will watch all 4 stories?**

**Key Concept(s):** Independent Events

**Explanation:** This question tests understanding of independent events.

*   Since each story view is independent, we multiply the probabilities: \(0.8 * 0.8 * 0.8 * 0.8 = 0.8^4 = 0.4096\)

**Answer:** The probability of watching all 4 stories is 40.96%.

**Question 2: (Easy)  You have a bag containing 8 red balls and 4 blue balls. If you draw two balls without replacement, what is the probability that both balls are red?**

**Key Concept(s):** Conditional Probability, Dependent Events

**Explanation:** This problem tests understanding of probability without replacement.

*   **1st ball is red**: There are 12 total balls so probability is \(\frac{8}{12}\)
*   **2nd ball is red**: Given the first ball is red, then there are 7 red balls and 11 balls total left so probability is \(\frac{7}{11}\)
*    The probability of the two independent steps is \(\frac{8}{12} * \frac{7}{11} = \frac{56}{132} = 0.424\).

**Answer:** The probability that both balls drawn are red is approximately \(\frac{56}{132} \) which equals approximately 0.424.

**Question 3: (Easy) A coin is flipped three times. What is the probability of getting exactly two heads?**

**Key Concept(s):** Binomial Probability

**Explanation:** There are 2^3 = 8 possible outcomes. The combinations with two heads are: HHT, HTH, THH. So 3/8. You can also use the binomial formula
\(P(X=2) = \binom{3}{2} * 0.5^2 * 0.5^1= \frac{3!}{2!1!} * 0.25 * 0.5 = 3*0.125 = 0.375 \)

**Answer:** The probability of getting exactly two heads is 3/8 or 0.375.

**Question 4: (Easy) A six-sided die is rolled once. What is the probability of rolling a number greater than 4?**

**Key Concept(s):** Basic Probability

**Explanation:** There are six possible outcomes, and two are greater than 4 (5 and 6).

**Answer:** The probability is 2/6 or 1/3.

**Question 5: (Easy)  A deck of cards has 52 cards. What is the probability of drawing a King?**

**Key Concept(s):** Basic Probability

**Explanation:** There are 4 Kings in a standard deck of 52 cards.

**Answer:** The probability is 4/52 or 1/13.

**Question 6: (Easy) If you have two independent events, A and B, with \(P(A) = 0.4\) and \(P(B) = 0.6\), what is \(P(A \cap B)\)?**

**Key Concept(s):** Independent Events

**Explanation:** For independent events, \(P(A \cap B) = P(A) * P(B)\).

**Answer:**  \(P(A \cap B) = 0.4 * 0.6 = 0.24\)

**Question 7: (Easy) A lottery has 100 tickets. You buy 5. What's the probability you hold the winning ticket?**

**Key Concept(s):** Basic Probability

**Explanation:**  There are 5 winning tickets out of 100

**Answer:** 5/100 or 1/20.

**Question 8: (Easy) In a group of 10 people, 3 are left-handed. If you randomly select one person, what is the probability they are right-handed?**

**Key Concept(s):** Basic Probability, Complementary Probability

**Explanation:**  If 3 are left-handed, then 7 are right-handed.

**Answer:** 7/10 or 0.7

**Question 9: (Medium) A social media platform notices that 70% of users like at least one post per day. If you randomly select 5 users, what is the probability that exactly 3 of them like at least one post daily?**

**Key Concept(s):** Binomial Probability

**Explanation:** This question tests understanding of the binomial probability distribution.

*   **Setup**: \(n=5\), \(p=0.7\), and we want the probability of exactly 3 successes (\(k=3\)). We will need to use the formula
    \(P(X=k) = \binom{n}{k} * p^k * (1-p)^{n-k}\)
    \(P(X=3) = \binom{5}{3} * 0.7^3 * (1-0.7)^{5-3} =  \frac{5!}{3!2!} * 0.7^3 * 0.3^2 = 10* 0.343 * 0.09= 0.3087 \)

**Answer:** The probability that exactly 3 out of 5 users like at least one post per day is approximately 0.3087 or 30.87%.

**Question 10: (Medium) On a video-sharing platform, 60% of users watch a video at least 5 minutes long. If 6 users are randomly selected, what is the probability that exactly 4 of them watch a video for at least 5 minutes?**

**Key Concept(s):** Binomial Probability

**Explanation:**  Use the binomial probability formula. \(n=6\), \(p=0.6\), \(k=4\).
\(P(X=4) = \binom{6}{4} * 0.6^4 * (1-0.6)^{6-4}\)
\(P(X=4) = 15 * 0.1296 * 0.16 = 0.31104\)

**Answer:** The probability is approximately 0.311, or 31.1%

**Question 11: (Medium) A music streaming service offers a 'daily mix' playlist. If 30% of users listen to the entire mix, and you pick 4 users randomly, what is the probability that at least 1 of them will listen to the full mix?**

**Key Concept(s):** Complement Probability, Binomial Probability

**Explanation:** Calculate the complement (none listen to full mix) and subtract from 1.
Probability of not listening: \(1-0.3 = 0.7\).
Probability of none listening: \(0.7^4 = 0.2401\)
Probability of at least one: \(1 - 0.2401 = 0.7599\)

**Answer:** The probability is approximately 0.76, or 76%.

**Question 12: (Medium) Say you roll a die three times. What is the probability of getting two sixes in a row?**

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

### Conditional Probability and Bayes' Theorem

**Question 13: (Medium) A Facebook Ads analyst is investigating the effectiveness of a new ad targeting algorithm. As a general baseline, they know that 1% of all users who see an ad convert (make a purchase). The new algorithm correctly identifies 80% of users who will convert for an ad. The algorithm also incorrectly flags 10% of non-converting users as likely to convert. Given that the algorithm has flagged a user as likely to convert, what is the probability that this user will actually convert?**

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

**Question 14: (Medium) An email provider uses a spam filter. The filter correctly identifies 95% of spam emails, and incorrectly flags 1% of non-spam emails as spam. If 40% of all incoming emails are actually spam, what is the probability that an email flagged as spam is actually spam?**

**Key Concept(s):** Bayes' Theorem, Conditional Probability

**Explanation:** Applying Bayes' Theorem with correct probabilities.

*   \(P(Spam) = 0.40\)
*   \(P(Not Spam) = 0.60\)
*   \(P(Flagged | Spam) = 0.95\)
*   \(P(Flagged | Not Spam) = 0.01\)
*   \(P(Spam|Flagged) = \frac{P(Flagged|Spam) * P(Spam)}{P(Flagged)}\)
*   \(P(Flagged) = P(Flagged|Spam)*P(Spam)+P(Flagged|NotSpam)*P(NotSpam) = (0.95*0.40)+(0.01*0.60)=0.38+0.006 = 0.386\)
*   \(P(Spam | Flagged) = \frac{0.95 * 0.40}{0.386} = \frac{0.38}{0.386} = 0.984\)

**Answer:** The probability that an email flagged as spam is actually spam is approximately 0.984, or 98.4%.

**Question 15: (Medium) A mobile gaming app uses a push notification system, where 70% of users have enabled push notifications.  The notification system correctly alerts 80% of players who have a new level available and 10% of players who do not have a level available are incorrectly alerted. If you receive a push notification, what is the probability that you actually have a new level available?**

**Key Concept(s):** Bayes' Theorem, Conditional Probability

**Explanation:** Bayes' Theorem problem with push notifications.

*  \(P(\text{Level}) = 0.70\)
*   \(P(\text{No Level}) = 0.30\)
*   \(P(\text{Notified} | \text{Level}) = 0.80\)
*  \(P(\text{Notified} | \text{No Level}) = 0.10\)
*   \(P(\text{Level} | \text{Notified}) = \frac{P(\text{Notified} | \text{Level}) * P(\text{Level})}{P(\text{Notified})}\)
*  \(P(\text{Notified}) = P(\text{Notified} | \text{Level})*P(\text{Level}) + P(\text{Notified} | \text{No Level})*P(\text{No Level}) = (0.80*0.70) + (0.10*0.30) = 0.56+0.03 = 0.59\)
*   \(P(\text{Level} | \text{Notified}) = \frac{0.80*0.70}{0.59} =  0.56/0.59 = 0.949\)

**Answer:**  The probability that a user has a new level available given they received a push notification is approximately 0.949, or 94.9%.

**Question 16: (Medium) You have the following data about user demographics and usage of a new feature:

| Demographic | Used Feature | Did Not Use Feature | Total |
|---|---|---|---|
| Age 18-24 | 300 | 200 | 500 |
| Age 25-34 | 400 | 100 | 500 |
| Total | 700 | 300 | 1000 |

1.  What is the probability that a randomly selected user is aged 18-24 *and* used the feature?
2.  What is the probability that a user used the feature *given* they are aged 25-34?
3. Are age demographic and feature usage independent events?**

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

## Hypothesis Testing

### Fundamentals of Hypothesis Testing

**Question 17: (Easy) What is the difference between Type I and Type II errors in hypothesis testing?**

**Key Concept(s):** Type I Error, Type II Error, Null Hypothesis, Alternative Hypothesis

**Explanation:** This is a fundamental concept in hypothesis testing.

*   **Type I Error (False Positive):** Rejecting the null hypothesis when it is actually true. This is often represented by \(\alpha\) (alpha), the significance level. Example: Concluding that a new feature improves conversion rates when it actually has no effect.
*   **Type II Error (False Negative):** Failing to reject the null hypothesis when it is actually false. This is often represented by \(\beta\) (beta). Example: Concluding that a new feature has no effect on conversion rates when it actually does improve them.

**Answer:** A Type I error is a false positive (incorrectly rejecting a true null hypothesis), while a Type II error is a false negative (incorrectly failing to reject a false null hypothesis).

**Question 18: (Easy) Define what a Null Hypothesis is and explain in the context of a A/B test example.**

**Key Concept(s):** Null Hypothesis, A/B Testing

**Explanation:** Tests understanding of the fundamental concept of the Null Hypothesis

*   The null hypothesis in statistical testing, such as during A/B testing, is the statement that there is no significant difference or effect between different scenarios, variables, or groups that are being studied. It essentially asserts that any changes observed in our testing or observation are not because of any real phenomena being studied but are due to random chance. An A/B testing context is if we want to understand the effectiveness of a redesign to the UI interface and so an appropriate Null hypothesis is “There is no statistically significant change between interface A and Interface B when looking at conversion rates".

**Answer:** The Null Hypothesis states there is no effect and it is what you set out to disprove.

**Question 19: (Easy) Explain the difference between a one-tailed and a two-tailed hypothesis test. When would you use each?**

**Key Concept(s):** One-tailed Test, Two-tailed Test, Hypothesis Testing

**Explanation:** This is about the directionality of the hypothesis.

*   **One-tailed Test:** Tests for a difference in *one* direction. For example, testing if a new feature *increases* conversion rates. The alternative hypothesis specifies a direction (e.g.,  \(\mu > \mu_0\) or \(\mu < \mu_0\)).
*   **Two-tailed Test:** Tests for a difference in *either* direction. For example, testing if a new feature has *any* effect (positive or negative) on conversion rates. The alternative hypothesis simply states that there is a difference (e.g., \(\mu \ne \mu_0\)).

**Answer:** Use a one-tailed test when you have a specific directional hypothesis (you only care about an increase or a decrease). Use a two-tailed test when you're interested in any difference, regardless of direction.

**Question 20: (Easy)  A company is testing a new website design. The null hypothesis is that the new design does not change the average time users spend on the website.  What does a Type I error mean in this context?**

**Key Concept(s):** Type I Error, Null Hypothesis

**Explanation:** Relating Type 1 error to a real world scenario.

*   Type 1 error is rejecting the Null hypothesis when it is true.
*   In this case it would mean concluding that the new design changed the average time, when it did not.

**Answer:**  A Type I error would be concluding that the new design changed user engagement time when, in reality, it has no impact.

**Question 21: (Easy)  A study is done on whether a new app feature increases engagement. If a type 2 error occurs, what does this mean?**

**Key Concept(s):** Type II Error

**Explanation:** Testing understanding of a type 2 error in a test context.

* A type 2 error is to not reject the Null hypothesis when it is false.
*  In this context it means concluding there was no increase in engagement when there in fact was.

**Answer:** A type 2 error in this case means that concluding there was no increase in user engagement with the new feature, when there actually was an increase in user engagement that went undetected.

**Question 22: (Easy) If a p-value is 0.01, and significance level \(\alpha\) is 0.05, would you reject the null hypothesis, and what is the reason?**

**Key Concept(s):** p-value, Significance Level

**Explanation:** Tests knowledge of statistical concepts and implications

*   The p-value is compared to \(\alpha\).
*  A p-value below \(\alpha\) results in rejection.

**Answer:** Yes, you would reject the null hypothesis because the p-value (0.01) is less than the significance level (0.05).

**Question 23: (Easy) In hypothesis testing, what is the relationship between the p-value and the significance level? Explain with example scenarios when you would chose to use differing levels of significance.**

**Key Concept(s):** p-value, Significance Level

**Explanation:** Tests knowledge of statistical concepts and implications

*   The p-value is compared against the chosen significance level \(\alpha\) (alpha) to determine if the results are statistically significant and if the null hypothesis is to be rejected.
*  The significance level (\(\alpha\)), is typically set at a chosen threshold (often at 0.05), to establish how rare your observation of differences under a Null hypothesis scenario has to be in order to deem our findings statistically significant.
 * A p-value smaller than  \(\alpha\) results in rejecting the Null Hypothesis. If the \(p>\alpha\), then fail to reject.
* The threshold that is chosen, will relate to your real world needs and so \(\alpha=0.05\)  is not always the right approach. If you were working on high-risk scenarios (e.g., drug trials), a lower \(\alpha\) (such as \(\alpha\)= 0.01 or 0.001) is required. When the risk of falsely concluding that a change makes no impact ( when it in fact might exist) has a higher cost, then you would increase \(\alpha\) above \(0.05\), like 0.10 for less crucial experiments

**Answer:**  The p-value is directly compared with the pre-selected  significance level (\(\alpha\)) to see if findings are statistically significant to reject the null hypothesis, the choice of \(\alpha\) needs to reflect the cost of Type 1 errors for a given research context

**Question 24: (Medium) In the context of A/B testing, if your p-value is 0.10 and the alpha level is 0.05, what conclusion would you draw about your null hypothesis?**

**Key Concept(s):** p-value, Significance Level, Hypothesis Testing

**Explanation:** Tests p-value interpretation.

*   The p-value is greater than the alpha level.
*   Therefore, the null hypothesis (that there is no significant difference between the groups) is not rejected.

**Answer:** We would fail to reject the null hypothesis, meaning there is not enough evidence to conclude there is a statistically significant difference between the two groups being tested.

**Question 25: (Medium)  What is the relationship between sample size and the power of a test? Explain how these relate to Type II error?**

**Key Concept(s):** Statistical Power, Type II Error, Sample Size

**Explanation:** Relate sample size and power and error.

*   A larger sample size increases the statistical power of a test and thus the ability to detect a real effect if it exists.
*  Statistical power is inversely related to a Type II error (False Negative).
*  A bigger sample size will mean you will be more likely to find an effect (more power) and it also means you are less likely to commit a type 2 error.

**Answer:** Increasing the sample size improves the power of the test, reducing the risk of a Type II error (failing to reject a false null hypothesis).

### A/B Testing

**Question 26: (Medium) You're analyzing user engagement with a new feature. You observe that users who interact with the feature spend significantly more time on the platform. How would you determine if this increase in time spent is statistically significant?**

**Key Concept(s):** Hypothesis Testing, A/B Testing, Statistical Significance, Z-test, Mann-Whitney U test

**Answer:**

1.  **Define Hypotheses:**

    *   Null Hypothesis (H0): There is no significant difference in the average time spent on the platform between users who interact with the feature and those who don't.
    *   Alternative Hypothesis (H1): There is a significant difference in the average time spent between the two groups.

2.  **Choose a Test:**

     * If the data is approximately normally distributed, a two-sample t-test is appropriate.
     * If the data is skewed, the Mann-Whitney U test (a non-parametric test) is a better choice.

3. **Collect Data:**
   * Record the time spent on the platform for both users who interacted and users who didn’t with the new feature. Ensure you have an equal and sufficient number of users for each group, to determine if you can reasonably use a t-test.

4. **Calculate the Test Statistic:**
   * **For the t-test:** Calculate the sample means, sample variances, and standard error, then compute the t-statistic.
   * **For the Mann-Whitney U test:** rank the data of both groups together, and calculate the U statistic.

5. **Calculate the p-value:**
   * Calculate the p-value based on the t-statistic or U statistic.

6.  **Interpret the Results:**

    *   Compare the p-value to the chosen significance level (\(\alpha\)), typically 0.05.
    *   **If \(p\text{-value} \le \alpha\):** Reject the null hypothesis (H0). This indicates that there is statistically significant evidence of a difference in time spent between the two groups.
    *   **If \(p\text{-value} > \alpha\):** Fail to reject the null hypothesis (H0). This means there is not enough evidence to conclude a statistically significant difference.
    * Consider Effect Size to determine practical significance of a statistically significant result.

**Question 27: (Medium) You're testing a new search algorithm on an e-commerce platform. How would you set up your A/B test to determine if it increases the click-through rate of search results?**

**Key Concept(s):** A/B Testing, Control Group, Treatment Group, Randomization

**Explanation:** Design of a good A/B test.

*   Randomly assign users into a control group (old algorithm) and a treatment group (new algorithm).
*   Ensure the randomization process is robust, and users are evenly distributed to avoid confounding results.
*   Measure the click-through rate (CTR) in each group.
*   Choose an appropriate statistical test (e.g. z-test for proportions) to compare the means of each group.
*   Decide on a significance level \(\alpha\) to assess the outcome.

**Answer:** Randomly assign users to control and treatment groups, measure the CTR, and use a hypothesis test to determine statistical significance.

**Question 28: (Medium) You run an A/B test on a new notification system designed to increase user engagement. You measure the average number of sessions per week. The control group (A) has a mean of 5.2 sessions with a standard deviation of 1.5, and the treatment group (B) has a mean of 5.5 sessions with a standard deviation of 1.6. Both groups have a sample size of 5000 users.

1.  Calculate a 95% confidence interval for the difference in means between the two groups.
2.  Based on the confidence interval, can you conclude that the new notification system significantly increased user engagement?**

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

**Question 29: (Medium)  What are some common threats to the validity of A/B tests, and how can these threats be mitigated?**

**Key Concept(s):** A/B Testing, Confounding Variables, Validity

**Explanation:** A/B testing pitfalls.

*   **Novelty Effects**: New features may initially cause user behaviour changes but will fade over time. Solution: Run tests long enough to see stable behaviours.
*  **Sample Bias**: If users are not evenly distributed, or self select then the sample can be biased and not representative of the population. Solution: Use randomisation and if not feasible, account for source of bias.
*   **Confounding Variables**: External factors, like marketing pushes, can influence the test outcome. Solution: Reduce impact of external factor or account for influence in analysis.
* **Data Quality Issues**: Incorrect tracking or data collection errors can invalidate results. Solution: Ensure solid data capture mechanisms are in place.
* **Multiple Testing**:  If you are running multiple tests on the same data, then you increase the chance of type 1 error. Solution: Use a correction method for multiple testing such as Bonferroni correction

**Answer:** Common threats include novelty effects, sample bias, confounding variables, data issues and multiple testing. They are usually mitigated by using random assignment, ensuring data accuracy, accounting for external effects and using correction methods where necessary.

**Question 30: (Medium) Explain in simple terms what is the concept of effect size in the context of an A/B test and why is it important?**

**Key Concept(s):** Effect Size, A/B testing

**Explanation:** Testing awareness of Effect Size.

*  Effect Size measures the magnitude of the difference or impact of an intervention in your A/B test in a meaningful, unitful way.
*  Effect Size gives you a good sense of the practical importance of the finding beyond just looking at statistical significance from the p-value.
*   A small effect size, even with significant p value could mean the practical gain from a change is not worth the time and resource.
*  Effect Size is more insightful than just p-values as p values are impacted by sample size and therefore can be misleading without further context

**Answer:** Effect size measures the real-world magnitude of the difference between groups, highlighting practical significance beyond statistical significance.

## Statistical Inference and Data Analysis

### Descriptive Statistics and Distributions

**Question 31: (Easy) Can you explain what a p-value and confidence interval are, but in layman's terms?**

**Key Concept(s):** p-value, Confidence Interval, Statistical Significance

**Explanation:** These are key concepts for interpreting statistical results.

*   **p-value:** The probability of observing the results (or more extreme results) of your experiment if there were actually no real effect (if the null hypothesis were true). A small p-value (typically below 0.05) suggests strong evidence against the null hypothesis. Imagine you're testing a new drug. If the p-value is 0.03, it means there's only a 3% chance you'd see the observed improvement in patients if the drug was actually useless.
*   **Confidence Interval:** A range of values that is likely to contain the true population parameter (like the average user session time or conversion rate). A 95% confidence interval means that if you were to repeat the experiment many times, 95% of the calculated intervals would contain the true population value. For example, a 95% confidence interval for average session time of (10-12 seconds) means that we are 95% sure that the true average session time lies between 10 and 12 seconds.

**Answer:** A p-value tells you how surprising your results are if there's no real effect. A confidence interval gives you a plausible range for the true value you're trying to estimate.

**Question 32: (Easy) You are given two datasets. One contains the average time users spend on your mobile app per session, and the other shows the number of clicks users make per session.  Which type of chart would be best to compare the distributions of these two variables side-by-side, and why?**

**Key Concept(s):** Data Visualization, Box Plot, Distribution Comparison

**Explanation:** Tests understanding of how to compare distributions.

*   While histograms can show distributions, comparing multiple histograms side by side can become difficult.
* Box plots are ideal to compare distributions of different datasets, visually demonstrating medians, quartiles, and outlier values for different datasets and how they differ.

**Answer:** A box plot is ideal to visually compare the distributions of the two datasets side-by-side, highlighting their central tendencies and spread.

**Question 33: (Easy)  You want to know the average daily time a user spends on your application. Explain when you would use the sample mean vs when to use the median.**

**Key Concept(s):** Measures of Central Tendency, Sample Mean, Median

**Explanation:** Tests awareness of when it is more appropriate to use sample mean or median.

*   The **sample mean**, or average,  is appropriate when the data are reasonably symmetrical or roughly normal and there is little to no outlier data. This can also work if large enough sample is observed to make any distortions small enough due to outlier issues.
*   The **median** on the other hand is more appropriate if your data shows skewed distributions, due to outliers as they wont influence this measure so readily, and often results in better reflection of central tendency in many use case contexts.
* The **Median** could be very insightful, if you wanted to measure something where you felt most common users don’t exhibit an effect of your population parameter (time in application), with outlier values being an unwanted distortion for such analysis. For example If a small subsegment uses the platform for a vast length of time vs everyone else.
* Often use mean as one method to check if the distribution has outlier behaviour where the median would likely also be evaluated if means appears far away, when that can indicate skew that might influence average calculations for certain measures.
 **Answer:** Sample means are appropriate for relatively normal distributions, but you need to observe distribution and make decisions accordingly, but be cautious of potential distortions. In practice mean and median together should also be viewed to highlight these insights with a measure such as median also being evaluated for skew where applicable in such circumstances..

**Question 34: (Easy)  What does a standard deviation represent in a dataset?**

**Key Concept(s):** Standard Deviation, Data Dispersion

**Explanation:** Tests understanding of standard deviation.

*   Standard deviation measures the dispersion or spread of data points around the mean of the dataset.
*   A higher standard deviation means the data is more spread out.
*   A lower standard deviation means the data is more concentrated around the mean.

**Answer:** Standard deviation quantifies how much the data points in a set deviate from the mean.

**Question 35: (Easy) You are given a dataset showing the number of daily active users (DAU) for a mobile app. How would you visually represent this data to identify trends and patterns over time?**

**Key Concept(s):** Data Visualization, Time Series Analysis, Line Chart

**Explanation:** This assesses understanding of time-series visualization.

* A line chart is the best method to visualize this data as it shows change over time and therefore can highlight trends, seasonality, and changes in activity over the given timeline.

**Answer:**  Use a line chart to visualize the daily active users over time.

**Question 36: (Medium) You have a dataset of user ages that is right-skewed. How would you calculate a measure of central tendency that is robust to outliers?**

**Key Concept(s):** Measures of Central Tendency, Skewed Data, Median

**Explanation:** Testing awareness of median as a robust measure.

* The mean is highly sensitive to outliers in a skewed distribution.
* The median is robust to outliers and can be ideal to describe the central value for skewed distributions.

**Answer:** Calculate the median as it is less sensitive to outliers than the mean for skewed data.

**Question 37: (Medium) A social media platform is analyzing the distribution of likes per post. They notice the data is highly right-skewed. What does this imply about the distribution, and which summary statistics should they use to describe the center and spread of the data?**

**Key Concept(s):** Skewed Data, Measures of Central Tendency, Median, IQR

**Explanation:** Tests understanding of skewed distributions and appropriate stats.

*   Right-skewed data has a long tail on the right side, meaning a few posts have a large number of likes while most have few.
*   For the center of the data, the median is a more robust measure than the mean, as it is not influenced by outliers.
*   For the spread of the data, the interquartile range (IQR) is more robust than the standard deviation.

**Answer:** The data has a long tail, use the median for the center, and IQR for the spread.

**Question 38: (Medium) You're analyzing the distribution of session lengths on your website. You notice that it's bimodal. What could this indicate and what would you need to investigate further?**

**Key Concept(s):** Bimodal Distribution, Data Segmentation

**Explanation:** Testing interpretation of bimodal data.

* A bimodal distribution indicates there may be two distinct groups within the population.
* It would be important to investigate the user behaviour to identify if there are any two types of user groups with very different engagement behaviours.

**Answer:** A bimodal distribution suggests the presence of distinct user groups; investigate segments and perform separate analyses of each group.

### Statistical Relationships

**Question 39: (Easy) Explain the concept of covariance and correlation. How are they different, and what do they measure?**

**Key Concept(s):** Covariance, Correlation

**Explanation:** These measures describe the relationship between two variables.

*   **Covariance:** Measures how two variables change together. A positive covariance means they tend to increase or decrease together, while a negative covariance means they tend to move in opposite directions. However, the magnitude of covariance is difficult to interpret because it's dependent on the scales of the variables.
*   **Correlation:** A standardized measure of the linear relationship between two variables. It ranges from -1 to +1. -1 indicates a perfect negative correlation, +1 indicates a perfect positive correlation, and 0 indicates no linear correlation. Correlation is easier to interpret than covariance because it's on a fixed scale.

**Answer:** Covariance measures the direction of a linear relationship, while correlation measures both the direction and strength of the linear relationship, making it easier to compare relationships between different pairs of variables.

**Question 40: (Easy) If the covariance between two variables is zero, what can you conclude about their relationship?**

**Key Concept(s):** Covariance, Linear Relationship

**Explanation:** Understanding zero covariance.

* Zero covariance implies that two variables have no *linear* relationship.
* It doesn't mean that they have absolutely no relationship, as it could be non-linear.

**Answer:** A zero covariance indicates no linear relationship between the variables.

**Question 41: (Easy) What does a correlation coefficient of -1 indicate?**

**Key Concept(s):** Correlation, Linear Relationship

**Explanation:** Interpreting correlation coefficients.

* A correlation of -1 implies a perfect negative linear relationship.
* As one value increases the other will decrease at same rate.

**Answer:** A correlation of -1 means a perfect negative linear relationship.

**Question 42: (Medium) If the covariance between two variables is positive, what does that indicate about the relationship between the variables? Is there any drawback to just using covariance?**

**Key Concept(s):** Covariance

**Explanation:** Tests for correlation knowledge.

*   A positive covariance indicates that two variables tend to increase or decrease together.
*   Covariance is difficult to interpret since it is not standardized so the magnitude is difficult to interpret in an absolute sense.

**Answer:**  A positive covariance means the variables tend to move in the same direction. The lack of standardization however makes it difficult to compare across datasets.

**Question 43: (Medium) Explain what correlation does well and its practical limitations in measuring relationship between variables.**

**Key Concept(s):** Correlation, Linearity

**Explanation:** Understanding use and limits of correlation.

*   Correlation measures the strength and direction of a *linear* relationship between two variables. It will vary between -1 and 1.
*   A correlation of 0 indicates no *linear* relationship.
*   Correlation doesn't capture non-linear relationships between variables (like quadratic). This is a crucial and practical limitation of its usage.
*   Correlation does not imply causation, only an association between two variables.
*   Outliers may also skew correlation results so its important to investigate such instances before drawing conclusions based on correlative insight

**Answer:** Correlation captures linear relationships well but can miss non-linear dependencies, should be interpreted with outliers accounted for, and it cannot imply causation.

**Question 44: (Medium) You observe a strong positive correlation between the number of ads a user sees and the number of purchases they make. What are some possible explanations, and how would you investigate if the ads are causing the purchases?**

**Key Concept(s):** Correlation vs Causation, Confounding Variables

**Explanation:** Testing understanding that correlation isn't causation

* Correlation does not imply causation. There are a few possibilities such as users that purchase more may also be more active and see more ads. Or that an external factor influences both.
* Investigating causality would need A/B testing where you randomise users and expose a subset to a variable like ads, to understand direct causal effects

**Answer:** A positive correlation doesn't imply ads cause purchases. Investigate with A/B testing, controlling for confounders.

### Time Series Analysis

**Question 45: (Medium) You have collected the daily active users (DAU) for your platform for the past year. You are asked to estimate DAU for next month, what methods would be appropriate for forecasting this time series data?**

**Key Concept(s):** Time Series Analysis, Forecasting, ARIMA, Exponential Smoothing

**Explanation:** Tests awareness of time series methods

*   Time series analysis techniques are required for time based data.
*   Suitable methods could include: ARIMA models (Autoregressive Integrated Moving Average) which are suited to find patterns in time series data.
*   Exponential Smoothing methods also work which uses weighted averages of the previous data points.
* The choice of method would need to account for trend, seasonality and auto correlation in historical data.

**Answer:** Employ time series analysis techniques like ARIMA or exponential smoothing, taking into account patterns in historical data such as trend and seasonality.

**Question 46: (Medium) You're analyzing website traffic data and notice a recurring pattern of higher traffic on weekends. Which time series analysis concept does this demonstrate?**

**Key Concept(s):** Time Series Analysis, Seasonality

**Explanation:** Identifying seasonality.

*  A recurring pattern at regular intervals in a time series, such as higher website traffic on weekends, indicates the presence of seasonality

**Answer:** This demonstrates seasonality in the time series data.

**Question 47: (Medium) What is the difference between trend and seasonality in a time series? Give an example of each in the context of e-commerce sales.**

**Key Concept(s):** Time Series Analysis, Trend, Seasonality

**Explanation:** Defining trend and seasonality in time series data.

* **Trend** - is a long term upward or downward pattern in data over time, such as sales going up due to adoption.
* **Seasonality** - patterns that repeat over fixed periods, such as higher sales around holidays.

**Answer:** Trend is long-term direction, seasonality is patterns that repeat at fixed intervals. Example: Overall e-commerce growth = trend. Increased sales around Black Friday = seasonality.

### Handling Outliers and Imbalanced Data

**Question 48: (Medium) You have data on the number of comments a post receives on a social network, and you notice the data is heavily right-skewed. Explain what method you would use for a confidence interval calculation and why?**

**Key Concept(s):** Confidence Intervals, Skewed Data, Bootstrapping

**Explanation:** Addressing confidence intervals with non-normal data.

*   Standard methods for confidence intervals (such as using the t distribution) assume approximately normal distributions.
*   When data is heavily skewed, the assumption of normality is not met.
*  Bootstrapping (resampling) methods are a robust approach to construct confidence intervals without the normality assumption.

**Answer:** Use a bootstrapping method for confidence interval calculation when dealing with heavily skewed data like comment counts, as it doesn't rely on a normality assumption.

**Question 49: (Medium) In a social network, you're analyzing the number of friend requests sent by users. You observe that a few users have sent an extremely high number of requests.  How would you address these outliers before calculating summary statistics like the mean and standard deviation?**

**Key Concept(s):** Outliers, Data Cleaning, Robust Statistics

**Explanation:** Outlier impact and mitigation.

*   Outliers can significantly skew the mean and standard deviation, which are not robust to extreme values.
*   Options include: Winsorizing (capping the extreme values to a percentile range), transformation (log or square root), or removing the outlier values. However it may also be useful to evaluate the origin of outliers as they may provide unique insights into the population parameter.
*   Robust statistics, such as the median and interquartile range, which are less sensitive to outliers are also useful to use.

**Answer:** Address outliers through winsorizing, transforming data or removing, while also investigating outliers. Robust statistics like the median and IQR are preferred for summarizing such datasets.

**Question 50: (Medium) Explain in practical terms why a log transformation might be useful when dealing with user engagement metrics that may be right-skewed?**

**Key Concept(s):** Log Transformation, Skewed Data

**Explanation:** Log transformation for skewed data.

*   Log transformations compress higher values, and stretch lower values which reduces the impact of outliers on summary statistics.
*   This can make the data more normally distributed, which helps for statistical methods that assume such distributions like t-tests.

**Answer:** Log transformations compress the scale of high values and expand the scale of low values, which can help make heavily skewed, long-tailed data more suitable for statistical analysis by reducing the influence of outliers and approaching a normal distribution.

**Question 51: (Medium) What are some methods for dealing with imbalanced datasets, and why are they important?**

**Key Concept(s):** Imbalanced Datasets, Oversampling, Undersampling, SMOTE, Cost-Sensitive Learning

**Explanation:** This is important in machine learning and data analysis when one class is significantly more prevalent than another.

**Answer:** Imbalanced datasets can bias models towards the majority class. Methods to address this include:

*   **Oversampling:** Duplicating instances from the minority class.
*   **Undersampling:** Removing instances from the majority class.
*   **SMOTE (Synthetic Minority Over-sampling Technique):** Creating synthetic instances of the minority class by interpolating between existing minority class instances.
*   **Cost-sensitive learning:** Assigning higher misclassification costs to the minority class during model training.
*   **Collecting more data:** If possible, collecting more data for the minority class can help balance the dataset.

These methods are important because they help models learn to accurately predict the minority class, which is often the class of interest (e.g., fraud detection, churn prediction).

### Harder Practice Questions (Social Network Focus)

**Question 52: (Hard) You are A/B testing a new algorithm for ranking posts in a user's feed. You are measuring the average time spent per session. You notice some users have extremely long session durations (potential outliers).

1.  How would you handle these outliers before conducting your statistical test?
2.  How does the Central Limit Theorem help you in this scenario, given that session durations are likely right-skewed?
3.  What statistical test would you use to compare the average time spent between the control and treatment groups?**

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

**Question 53: (Hard) You are analyzing user engagement with a new feature. You are measuring engagement by the number of clicks per user per day, and you find that the data follows a power-law distribution. How should you analyze and interpret such data?**

**Key Concept(s):** Power-Law Distribution, Heavy-Tailed Distributions, Log Transformation, Robust Statistics

**Explanation:** Addressing power law distributions

*  Power laws are common in user engagement metrics. The data will be highly skewed, with a few users having a large number of clicks and the majority having very few.
*  Traditional statistical methods assuming normality (like the mean and standard deviation) are not suitable.
* You should employ metrics like the median and interquartile range (IQR).
* Transforming the data via logs and further analysis can also be useful to see distribution insights.
* Consider also modelling via non parametric tests.

**Answer:** Due to skew, use robust statistics (median, IQR), consider transformations, and model via non parametric tests.

**Question 54: (Hard) You are tasked with evaluating a new ranking algorithm for a social media feed. You want to assess how diverse the content is that users are seeing. How would you define and quantify content diversity? Provide examples of metrics you might calculate.**

**Key Concept(s):** Diversity Metric, Information Retrieval, Entropy, Pairwise dissimilarity.

**Explanation:** Measuring diversity in recommendations.

*   Quantifying diversity is not straight forward and depends on definition of diversity.
*   One approach is to calculate the entropy of categories for the recommended items. A high entropy indicates a more diverse set of recommendations as items are not from the same categories. Calculate entropy over different categories.
*   Another method is to measure the pairwise dissimilarity between items, where more diverse recommendations will have a higher dissimilarity score. Use measures of distance (like Euclidean) to calculate dissimilarity.
*   A simpler way is to measure the number of unique categories of items across a recommendation list.

**Answer:** Diversity can be quantified using metrics such as entropy of item categories, pairwise dissimilarity between items, or by the number of unique categories, adapting to the specific context.
For example:

*   **Category Entropy:**  Calculate the probability of each category appearing in the recommendations. Then calculate the entropy: \( -\sum_{i=1}^{n} p_i * log(p_i)\) where  pᵢ is the probability of the i-th category.
*   **Pairwise Dissimilarity**: calculate a dissimilarity score (e.g using euclidean disstance) between each item in recommendation, and average.
*   **Unique Categories:** Simply count the number of unique categories in the recommendations.

**Question 55: (Hard) You are analyzing a dataset containing user activity on a social platform, including the number of posts, likes, and comments each user makes. You are asked to understand the relationship between these different engagement metrics, but are unsure of whether you should be using correlation, or covariance. Provide your thoughts on which metric and explain why.**

**Key Concept(s):** Correlation vs Covariance, Feature Relationship

**Explanation:** Testing understanding between covariance and correlation, feature relationship

* Covariance will show direction, but the unstandardised metrics make absolute comparison and interpretation difficult
* Correlation, on the other hand standardises, but is only useful if looking for linear relationships.
* Therefore If interested in only direction use covariance, if you are looking for linear relationships and strength you will have to use correlation.

**Answer:**  If interested in the direction of relationship only, use covariance, if strength and direction are important, use correlation. If non linear relationships, then neither covariance nor correlation will work, and would need other forms of techniques.

**Question 56: (Hard) You are analyzing the click-through rate (CTR) of a new ad campaign. You observe a CTR of 2% from a sample of 10,000 impressions. Calculate a 95% confidence interval for the true CTR. How would a larger sample size (e.g. 100,000 impressions) impact the width of the confidence interval?**

**Key Concept(s):** Confidence Intervals, Proportions, Sample Size, Standard Error

**Explanation:** This tests the application and interpretation of confidence intervals.

**Answer:**

1.  **Calculate the Standard Error (n=10,000):** \(SE = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{(0.02 * 0.98)}{10000}} \approx 0.0014\)
2.  **Find the Z-score:** For a 95% confidence interval, the z-score is approximately 1.96.
3.  **Calculate the Confidence Interval (n=10,000):** \(CI = p \pm z * SE = 0.02 \pm 1.96 * 0.0014 \approx (0.0173, 0.0227)\) or (1.73%, 2.27%)

With a larger sample size (100,000 impressions):

1.  **Calculate the Standard Error (n=100,000):** \(SE = \sqrt{\frac{(0.02 * 0.98)}{100000}} \approx 0.00044\)
2.  **Calculate the Confidence Interval (n=100,000):** \(CI = 0.02 \pm 1.96 * 0.00044 \approx (0.0191, 0.0209)\) or (1.91%, 2.09%)

**Impact of Sample Size:** As you can see, the confidence interval is much narrower with the larger sample size. This is because the standard error decreases as the sample size increases, leading to a more precise estimate of the true CTR.

**Question 57: (Hard) You're running an A/B test to evaluate a new recommendation system. The primary metric is the average time users spend on the platform per session. However, you notice a significant number of users who have extremely short sessions (less than 10 seconds). How would you analyze this data, accounting for these short sessions?**

**Key Concept(s):** Outliers, Data Transformation, Trimming, Winsorizing, Segmentation, A/B Testing

**Explanation:** Addressing outlier data

*   Very short session lengths are likely to be due to accidental opens or technical issues, and are not indicative of genuine user behaviour, so could distort your results by skewing means.
*   Consider investigating and removing the very short sessions (trimming) or capping them to a threshold (Winsorizing).
*   Consider if the session data is better represented via a non parametric test if transforming the data to be gaussian proves difficult.
*  Segment data to understand different patterns, like very active vs less active users.
* Run robust statistical tests that don't assume normal data.

**Answer:** Trim/winsorize short sessions. Segment users, non parametric tests, check distribution.

**Question 58: (Hard) You have a dataset showing the number of items purchased per user on an e-commerce platform. You notice that the data is heavily skewed to the right. What approach would you take to calculate a 95% confidence interval for the median number of items purchased per user?**

**Key Concept(s):** Confidence Intervals, Skewed Data, Bootstrapping, Median

**Explanation:** This tests knowledge of confidence intervals for non-normal data, and median

*   Standard confidence interval formulas assume a normal distribution, which is not suitable for highly skewed data.
* Bootstrapping allows us to resample the data and generate many values for the median and get its sampling distribution which can be used to create the confidence intervals.
* You would resample from original data many times and calculate a new median every time and then use the distribution to calculate confidence interval.

**Answer:** Since the data is skewed use the bootstrapping method to get confidence intervals of the median.

**Question 59: (Hard) You're analyzing the effectiveness of a new personalized recommendation algorithm on a music streaming platform. You are measuring the average number of songs listened to per session. You notice that user behavior is highly variable, with some users listening to hundreds of songs per session, while others listen to only a few. You want to assess if the new algorithm is improving the average number of songs listened to. How would you conduct the statistical analysis? Which test would be more appropriate and why?**

**Key Concept(s):** Skewed Data, Non-Parametric Tests, Mann-Whitney U test, A/B testing

**Explanation:** Testing awareness of non parametric tests when assumptions of normality are broken.

*   The data is highly variable with potentially skew distribution so a t-test (which assumes normality) is likely not the best choice for this data.
*   A non-parametric test such as the Mann-Whitney U test is preferred as it doesn't assume normal data.
* Apply robust tests such as this one and compare mean / median. Evaluate effect size of changes, not just statistical significance.

**Answer:** Use Mann-Whitney U test for analysis of the skewed distribution data, and not t-test. Further, evaluate effect size not just statistical significance.

**Question 60: (Hard) You're investigating a drop in user sign-ups on your social media platform. You suspect that the drop may be related to a change in the signup flow that was deployed a few weeks ago. How would you approach this problem systematically, including appropriate statistical analysis?**

**Key Concept(s):** Data Analysis, Time Series Analysis, A/B Testing, Hypothesis Testing, Segmentation

**Explanation:** This tests analytical thinking and applying statistical concepts to a real-world problem.

**Answer:**

1.  **Data Validation:** Start by validating the data for accuracy, ensure there are no tracking issues or data collection errors.
2.  **Time Series Analysis:** Check sign-up trends before the change was implemented and after the deployment to identify the extent of drop, and to see whether this is part of larger seasonal or temporal change.
3.  **Segmentation Analysis:** Check sign-ups across different user segments (geo, demographic, channel). If one group shows much larger drop, investigate that sub segment more deeply.
4.  **A/B Testing Analysis:** Analyze data collected from A/B test during that week to see if the new changes resulted in significantly different sign-ups. Consider any statistical test to determine the extent of impact (using mean / proportion and their respective tests as applicable to your particular business context).
5.  **Correlation Analysis:** Check correlation between sign-up rate with other metrics to investigate other potentially causative factors for the drop.
6. **External Factors:** Investigate external factors like competitor activity, marketing, or trends that may influence sign-ups.

This approach provides a systematic way to validate data, identify the extent of the drop, investigate potential reasons using segmentation, and see if the change itself is the primary driver of the dip.
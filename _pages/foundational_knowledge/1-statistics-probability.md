---
layout: default
title: "Statistics & Probability"
permalink: /foundational_knowledge/1/
difficulty: "Beginner"
estimated_time: "45 mins"
tags: [Statistics, Probability, Hypothesis Testing]
track: "Foundational Knowledge"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Foundational Knowledge & Skills</a> <span>&gt;</span>
  <span>Statistics & Probability</span>
</div>

<div class="header">
  <h1>Statistics & Probability</h1>
  <p>Your Guide To Statistical Mastery for Data Science</p>
</div>

<div class="section" id="statistics-probability">
  
  <div class="card">
    <h3>Overview</h3>
    <p>This section covers the fundamental concepts and skills required for a Data Science (Analytical) role at Meta. At Meta, Data Scientists play a crucial role in driving product development and business strategy through rigorous data analysis and statistical reasoning. This role is heavily focused on using statistical methods to understand user behavior, measure the impact of product changes, and inform data-driven decisions across Meta's vast ecosystem of products (Facebook, Instagram, WhatsApp, etc.).</p>
    
    <p>Working at this scale, dealing with billions of users and petabytes of data, statistical rigor is paramount. Data Scientists at Meta are expected to design and analyze A/B tests to evaluate the impact of product changes, develop metrics and KPIs to track product performance and user engagement, build statistical models to predict user behavior and identify opportunities for improvement, and effectively communicate complex statistical findings to both technical and non-technical audiences. Therefore, a strong foundation in statistics and probability is absolutely essential.</p>
  </div>

  <div class="card">
    <h3>What Can You Expect?</h3>
    <p>You can expect questions that not only test your knowledge of statistical concepts but also your ability to apply them to real-world product scenarios. Interviewers will be looking for your understanding of how to use data to answer business questions and drive product improvements. Expect questions on:</p>
    <ul>
      <li><strong>Descriptive statistics</strong> (mean, median, mode, variance, standard deviation): These form the basis for understanding data distributions and identifying key trends. Be prepared to calculate these metrics and explain their significance in a business context.</li>
      <li><strong>Probability distributions</strong> (normal, binomial, Poisson, exponential): Understanding these distributions is crucial for modeling various phenomena, such as user activity, event occurrences, and time-to-event analyses.</li>
      <li><strong>Hypothesis testing</strong> (A/B testing, t-tests, p-values, confidence intervals, statistical power): A/B testing is a cornerstone of product development at Meta. Be prepared to design A/B tests, calculate sample sizes, interpret p-values and confidence intervals, and understand the concept of statistical power.</li>
      <li><strong>Regression analysis</strong> (linear, logistic): Regression models are used to understand relationships between variables and predict outcomes. You should be comfortable with both linear and logistic regression and be able to interpret model coefficients and evaluate model performance.</li>
      <li><strong>Experimental design</strong>: Designing sound experiments is crucial for drawing valid conclusions from data. You should understand the principles of randomization, control groups, and how to minimize bias.</li>
      <li><strong>Bayes' theorem</strong>: Bayes' theorem is used to update probabilities based on new evidence. It's particularly relevant for problems involving classification, filtering, and prediction.</li>
    </ul>
  </div>

  <div class="card">
    <h3>How to Prep</h3>
    <ul>
      <li>Review fundamental statistical concepts and practice applying them to product scenarios.</li>
      <li>Focus on understanding p-values, confidence intervals, and how to design and interpret A/B tests.</li>
      <li><strong>Resources:</strong>
        <ul>
          <li><a href="https://www.openintro.org/book/os/" target="_blank">OpenIntro Statistics</a></li>
          <li><a href="https://www.khanacademy.org/math/statistics-probability" target="_blank">Khan Academy Statistics</a></li>
          <li><a href="https://www.youtube.com/@statquest" target="_blank">StatQuest YouTube channel</a></li>
          <li><a href="https://www.optimizely.com/sample-size-calculator/" target="_blank">Optimizely's sample size calculator</a></li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="card" id="descriptive-statistics">
    <h3>1. Descriptive Statistics</h3>
    <p><strong>Explanation:</strong> Descriptive statistics summarize and describe the main features of a dataset. They provide a snapshot of the data's central tendency (where the data is centered) and dispersion (how spread out the data is). Key measures include:</p>
    <ul>
      <li><strong>Mean:</strong> The average value (sum of all values divided by the number of values). Formula: μ = Σx / n</li>
      <li><strong>Median:</strong> The middle value when the data is ordered. If there's an even number of values, the median is the average of the two middle values.</li>
      <li><strong>Mode:</strong> The most frequent value. A dataset can have multiple modes or no mode at all.</li>
      <li><strong>Variance:</strong> The average of the squared differences from the mean. Formula: σ² = Σ(x - μ)² / n</li>
      <li><strong>Standard Deviation:</strong> The square root of the variance, representing the typical deviation from the mean. Formula: σ = √σ²</li>
    </ul>
    <p>These measures are crucial for understanding data distributions and identifying patterns or anomalies. For instance, comparing the mean and median can reveal skewness in the data. Standard deviation helps quantify the data's volatility or spread.</p>
    <p><strong>Wikipedia:</strong> <a href="https://en.wikipedia.org/wiki/Descriptive_statistics" target="_blank">Descriptive statistics</a></p>
    
    <h4>Practice Questions:</h4>
    <ol>
      <li>You have website session durations (in seconds): 10, 15, 20, 20, 25, 30, 60. Calculate the mean, median, mode, variance, and standard deviation.
        <ul>
          <li>Mean: (10+15+20+20+25+30+60)/7 = 25.71</li>
          <li>Median: 20</li>
          <li>Mode: 20</li>
          <li>Variance: Calculate the squared differences from the mean, sum them, and divide by 7. Result ~228.57</li>
          <li>Standard Deviation: √228.57 ~ 15.12</li>
        </ul>
      </li>
      <li>A product has daily active users (DAU) for a week: 1000, 1200, 1100, 1300, 1050, 950, 1150. Calculate the average DAU and the standard deviation. What does the standard deviation tell you about the DAU?
        <ul>
          <li>Average DAU: 1107.14</li>
          <li>Standard Deviation: ~127.6</li>
          <li>The standard deviation tells us about the variability or spread of the DAU around the average. A higher standard deviation indicates more fluctuation in DAU.</li>
        </ul>
      </li>
      <li>Explain how outliers can affect the mean and median. Provide an example.
        <ul>
          <li>Outliers significantly affect the mean because the mean takes into account all values. However, the median is less sensitive to outliers as it only considers the middle value(s).</li>
          <li>Example: Consider the dataset: 1, 2, 3, 4, 100. The mean is 22, while the median is 3. The outlier (100) drastically pulls the mean upwards but has no effect on the median.</li>
        </ul>
      </li>
    </ol>
  </div>

  <div class="card" id="probability-distributions">
    <h3>2. Probability Distributions</h3>
    <p><strong>Explanation:</strong> Probability distributions describe how values are distributed across a range. Understanding these distributions helps you model real-world phenomena and choose appropriate statistical tests.</p>
    
    <h4>Common Distributions:</h4>
    <ul>
      <li><strong>Normal Distribution:</strong> Bell-shaped, symmetric. Many natural phenomena follow this distribution.</li>
      <li><strong>Binomial Distribution:</strong> Number of successes in n independent trials with probability p.</li>
      <li><strong>Poisson Distribution:</strong> Number of events occurring in a fixed interval of time/space.</li>
      <li><strong>Exponential Distribution:</strong> Time between events in a Poisson process.</li>
    </ul>
    
    <h4>Worked Examples:</h4>
    <ol>
      <li><strong>Normal Distribution:</strong> User session times on a website are normally distributed with mean μ = 5 minutes and standard deviation σ = 1.5 minutes. What's the probability a user spends more than 7 minutes?
        <ul>
          <li>Z-score = (7 - 5) / 1.5 = 1.33</li>
          <li>P(Z > 1.33) = 1 - P(Z < 1.33) = 1 - 0.9082 = 0.0918 or 9.18%</li>
        </ul>
      </li>
      <li><strong>Binomial Distribution:</strong> In an A/B test, 40% of users in the control group convert. If you have 100 users, what's the probability exactly 35 convert?
        <ul>
          <li>P(X = 35) = C(100,35) × (0.4)^35 × (0.6)^65</li>
          <li>This is approximately 0.028 or 2.8%</li>
        </ul>
      </li>
      <li><strong>Poisson Distribution:</strong> Customers arrive at a store at an average rate of 3 per hour. What's the probability exactly 5 arrive in the next hour?
        <ul>
          <li>P(X = 5) = e^(-3) × 3^5 / 5! = 0.0498 or 4.98%</li>
        </ul>
      </li>
    </ol>
  </div>

  <div class="card" id="hypothesis-testing">
    <h3>3. Hypothesis Testing</h3>
    <p><strong>Explanation:</strong> Hypothesis testing helps determine whether observed differences are statistically significant or due to chance. The process involves stating null and alternative hypotheses, choosing a significance level, calculating a test statistic, and making a decision.</p>
    
    <h4>Key Concepts:</h4>
    <ul>
      <li><strong>Null Hypothesis (H₀):</strong> No difference exists</li>
      <li><strong>Alternative Hypothesis (H₁):</strong> A difference exists</li>
      <li><strong>p-value:</strong> Probability of observing the data (or more extreme) assuming H₀ is true</li>
      <li><strong>Significance Level (α):</strong> Threshold for rejecting H₀ (commonly 0.05)</li>
      <li><strong>Type I Error:</strong> Rejecting H₀ when it's true (false positive)</li>
      <li><strong>Type II Error:</strong> Failing to reject H₀ when it's false (false negative)</li>
    </ul>
    
    <h4>Worked Examples:</h4>
    <ol>
      <li><strong>A/B Test Analysis:</strong> You run an A/B test with 10,000 users per variant. Control converts at 4.2%, treatment at 4.8%. The p-value is 0.03. What do you conclude at α = 0.05?
        <ul>
          <li>Since p-value (0.03) < α (0.05), reject H₀</li>
          <li>Conclusion: Treatment significantly outperforms control</li>
          <li>Lift = (4.8% - 4.2%) / 4.2% = 14.3%</li>
        </ul>
      </li>
      <li><strong>Sample Size Calculation:</strong> You want to detect a 5% relative lift (from 10% to 10.5% conversion). What's the required sample size per variant for 80% power and α = 0.05?
        <ul>
          <li>Baseline conversion p₁ = 0.10</li>
          <li>Expected conversion p₂ = 0.105</li>
          <li>Use sample size formula: n = (Z_α/2 + Z_β)² × (p₁(1-p₁) + p₂(1-p₂)) / (p₂ - p₁)²</li>
          <li>Approximately 15,000 users per variant</li>
        </ul>
      </li>
      <li><strong>Confidence Intervals:</strong> Your A/B test shows a 2% absolute lift with 95% CI of [1.2%, 2.8%]. How do you interpret this?
        <ul>
          <li>The true lift is likely between 1.2% and 2.8%</li>
          <li>Since the CI doesn't include 0, the result is statistically significant</li>
          <li>You can be 95% confident the true lift is at least 1.2%</li>
        </ul>
      </li>
    </ol>
  </div>

  <div class="card" id="regression-analysis">
    <h3>4. Regression Analysis</h3>
    <p><strong>Explanation:</strong> Regression analysis models relationships between variables. Linear regression assumes a linear relationship, while logistic regression is used for binary outcomes.</p>
    
    <h4>Linear Regression:</h4>
    <ul>
      <li><strong>Equation:</strong> Y = β₀ + β₁X₁ + β₂X₂ + ... + ε</li>
      <li><strong>Coefficient Interpretation:</strong> β₁ represents the change in Y for a 1-unit increase in X₁</li>
      <li><strong>R-squared:</strong> Proportion of variance in Y explained by the model</li>
    </ul>
    
    <h4>Worked Examples:</h4>
    <ol>
      <li><strong>Simple Linear Regression:</strong> You model user engagement (Y) as a function of time spent on app (X). The equation is Y = 10 + 2X. Interpret the coefficients.
        <ul>
          <li>β₀ = 10: Expected engagement when time spent = 0</li>
          <li>β₁ = 2: Each additional minute increases engagement by 2 units</li>
        </ul>
      </li>
      <li><strong>Multiple Regression:</strong> Predicting revenue with price and marketing spend. Revenue = 1000 + 50×Price - 2×Spend. R² = 0.75.
        <ul>
          <li>$50 increase in price → $50,000 more revenue</li>
          <li>$1,000 more marketing spend → $2,000 less revenue</li>
          <li>Model explains 75% of revenue variance</li>
        </ul>
      </li>
    </ol>
  </div>

  <div class="card" id="experimental-design">
    <h3>5. Experimental Design</h3>
    <p><strong>Explanation:</strong> Good experimental design ensures valid conclusions. Key principles include randomization, control groups, and adequate sample sizes.</p>
    
    <h4>Key Principles:</h4>
    <ul>
      <li><strong>Randomization:</strong> Randomly assign users to treatment/control to eliminate bias</li>
      <li><strong>Control Group:</strong> Baseline for comparison</li>
      <li><strong>Blinding:</strong> Participants don't know their group assignment</li>
      <li><strong>Sample Size:</strong> Large enough to detect meaningful effects</li>
    </ul>
    
    <h4>Worked Examples:</h4>
    <ol>
      <li><strong>A/B Test Design:</strong> Testing a new checkout flow. How would you design this experiment?
        <ul>
          <li><strong>Metric:</strong> Conversion rate (primary), revenue per user (secondary)</li>
          <li><strong>Randomization:</strong> Randomly assign users at page load</li>
          <li><strong>Sample Size:</strong> Calculate based on expected effect size</li>
          <li><strong>Duration:</strong> 1-2 weeks to capture weekly patterns</li>
          <li><strong>Analysis:</strong> Compare means, check for significance and practical importance</li>
        </ul>
      </li>
      <li><strong>Common Pitfalls:</strong> What could go wrong with this experiment?
        <ul>
          <li><strong>Novelty Effect:</strong> Users react differently to new features initially</li>
          <li><strong>Seasonal Effects:</strong> Holiday traffic patterns affect results</li>
          <li><strong>Multiple Testing:</strong> Running many tests increases false positive risk</li>
          <li><strong>Sample Ratio Mismatch:</strong> Unequal group sizes reduce statistical power</li>
        </ul>
      </li>
    </ol>
  </div>

  <div class="card" id="bayes-theorem">
    <h3>6. Bayes' Theorem</h3>
    <p><strong>Explanation:</strong> Bayes' theorem updates probabilities based on new evidence. It's fundamental for understanding conditional probability and is used in spam filtering, medical testing, and A/B test analysis.</p>
    
    <h4>Formula:</h4>
    <p>P(A|B) = [P(B|A) × P(A)] / P(B)</p>
    
    <h4>Worked Examples:</h4>
    <ol>
      <li><strong>Medical Testing:</strong> A disease affects 1% of the population. Test is 99% accurate. If you test positive, what's the probability you have the disease?
        <ul>
          <li>P(Disease) = 0.01, P(Positive|Disease) = 0.99, P(Positive|No Disease) = 0.01</li>
          <li>P(Disease|Positive) = (0.99 × 0.01) / [(0.99 × 0.01) + (0.01 × 0.99)] = 0.5 or 50%</li>
          <li>Even with a positive test, only 50% chance of having the disease!</li>
        </ul>
      </li>
      <li><strong>A/B Test with Prior Knowledge:</strong> You have historical data showing 10% of feature changes are successful. Your current test shows p = 0.04. How does this update your belief?
        <ul>
          <li>Prior P(Success) = 0.10</li>
          <li>Likelihood P(p=0.04|Success) based on historical distribution</li>
          <li>Posterior probability combines prior belief with new evidence</li>
        </ul>
      </li>
    </ol>
  </div>

  <div class="navigation-buttons">
    <a href="{{ '/introduction/' | relative_url }}">Previous: Introduction</a>
    <a href="{{ '/foundational_knowledge/2-SQL/' | relative_url }}">Next: SQL & Data Manipulation</a>
  </div>

</div>

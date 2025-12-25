---
layout: default
title: "Appendix"
permalink: /appendix/
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <span>Appendix</span>
</div>

<div class="header">
  <h1>Appendix</h1>
  <p>Glossary, cheatsheets, and quick reference materials for data science interviews.</p>
</div>

<div class="section">

  <div class="card">
    <h2>📖 Glossary of Terms</h2>
    <p>Quick reference definitions for key concepts used throughout the handbook.</p>
  </div>

  <div class="card">
    <h3>A</h3>
    <dl>
      <dt><strong>A/B Testing</strong></dt>
      <dd>A randomized controlled experiment comparing two versions (A and B) to determine which performs better on a defined metric. Also called split testing.</dd>
      
      <dt><strong>Accuracy</strong></dt>
      <dd>The proportion of correct predictions (true positives + true negatives) among the total number of cases examined. Formula: (TP + TN) / (TP + TN + FP + FN)</dd>
      
      <dt><strong>Alpha (α)</strong></dt>
      <dd>The significance level in hypothesis testing; the probability of rejecting the null hypothesis when it's actually true (Type I error rate). Commonly set at 0.05.</dd>
      
      <dt><strong>ANOVA (Analysis of Variance)</strong></dt>
      <dd>A statistical method for comparing means of three or more groups to determine if at least one group mean differs significantly from others.</dd>
      
      <dt><strong>ARPU (Average Revenue Per User)</strong></dt>
      <dd>A metric measuring the average revenue generated per user, commonly used in subscription and freemium business models.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>B</h3>
    <dl>
      <dt><strong>Bayes' Theorem</strong></dt>
      <dd>A formula for calculating conditional probabilities: P(A|B) = P(B|A) × P(A) / P(B). Used for updating beliefs based on new evidence.</dd>
      
      <dt><strong>Beta (β)</strong></dt>
      <dd>In hypothesis testing, the probability of failing to reject the null hypothesis when it's actually false (Type II error rate). Statistical power = 1 - β.</dd>
      
      <dt><strong>Binomial Distribution</strong></dt>
      <dd>A probability distribution for the number of successes in n independent trials, each with probability p of success.</dd>
      
      <dt><strong>Bias</strong></dt>
      <dd>Systematic error that causes results to deviate from the true value in a consistent direction. In ML, it refers to underfitting due to oversimplified models.</dd>
      
      <dt><strong>Bonferroni Correction</strong></dt>
      <dd>A method to adjust significance levels when performing multiple comparisons, dividing α by the number of tests to control family-wise error rate.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>C</h3>
    <dl>
      <dt><strong>Central Limit Theorem (CLT)</strong></dt>
      <dd>States that the sampling distribution of the sample mean approaches a normal distribution as sample size increases, regardless of the population's distribution.</dd>
      
      <dt><strong>Chi-Square Test</strong></dt>
      <dd>A statistical test for categorical data to assess whether observed frequencies differ from expected frequencies.</dd>
      
      <dt><strong>Cohort Analysis</strong></dt>
      <dd>A type of analysis that groups users by shared characteristics (often acquisition date) to track behavior over time.</dd>
      
      <dt><strong>Confidence Interval</strong></dt>
      <dd>A range of values that likely contains the true population parameter with a specified probability (e.g., 95% CI).</dd>
      
      <dt><strong>Confounding Variable</strong></dt>
      <dd>A variable that influences both the dependent and independent variables, potentially creating a spurious association.</dd>
      
      <dt><strong>Conversion Rate</strong></dt>
      <dd>The percentage of users who complete a desired action (e.g., sign up, purchase) out of total users exposed.</dd>
      
      <dt><strong>Correlation</strong></dt>
      <dd>A statistical measure of the linear relationship between two variables, ranging from -1 to +1.</dd>
      
      <dt><strong>CTE (Common Table Expression)</strong></dt>
      <dd>A temporary named result set in SQL that can be referenced within a SELECT, INSERT, UPDATE, or DELETE statement.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>D</h3>
    <dl>
      <dt><strong>DAU/MAU (Daily/Monthly Active Users)</strong></dt>
      <dd>Metrics measuring the number of unique users who engage with a product within a day or month. DAU/MAU ratio indicates stickiness.</dd>
      
      <dt><strong>Degrees of Freedom</strong></dt>
      <dd>The number of independent values that can vary in a statistical calculation. Often n-1 for sample variance.</dd>
      
      <dt><strong>Distribution</strong></dt>
      <dd>A function showing all possible values of a variable and their frequencies or probabilities.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>E</h3>
    <dl>
      <dt><strong>Effect Size</strong></dt>
      <dd>A quantitative measure of the magnitude of a phenomenon. Common measures include Cohen's d and odds ratio.</dd>
      
      <dt><strong>Expected Value</strong></dt>
      <dd>The long-run average value of a random variable over many repeated experiments. E(X) = Σ(x × P(x)).</dd>
      
      <dt><strong>Exponential Distribution</strong></dt>
      <dd>A probability distribution describing time between events in a Poisson process. Characterized by constant hazard rate.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>F</h3>
    <dl>
      <dt><strong>F-statistic</strong></dt>
      <dd>A ratio of two variances used in ANOVA and regression to test if group means or model parameters differ significantly.</dd>
      
      <dt><strong>False Positive (Type I Error)</strong></dt>
      <dd>Incorrectly rejecting the null hypothesis when it's actually true. Controlled by significance level α.</dd>
      
      <dt><strong>False Negative (Type II Error)</strong></dt>
      <dd>Failing to reject the null hypothesis when it's actually false. Related to statistical power.</dd>
      
      <dt><strong>Feature Engineering</strong></dt>
      <dd>The process of creating new features from raw data to improve model performance.</dd>
      
      <dt><strong>Funnel Analysis</strong></dt>
      <dd>A method of analyzing the user journey through sequential steps, measuring conversion rates at each stage.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>G</h3>
    <dl>
      <dt><strong>Gaussian Distribution</strong></dt>
      <dd>Another name for normal distribution. Characterized by mean (μ) and standard deviation (σ).</dd>
      
      <dt><strong>Guardrail Metrics</strong></dt>
      <dd>Metrics monitored during experiments to ensure changes don't negatively impact critical aspects of the product.</dd>
      
      <dt><strong>GROUP BY</strong></dt>
      <dd>SQL clause that groups rows with the same values in specified columns, often used with aggregate functions.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>H</h3>
    <dl>
      <dt><strong>Hypothesis Testing</strong></dt>
      <dd>A statistical method for making decisions about population parameters based on sample data, comparing null and alternative hypotheses.</dd>
      
      <dt><strong>Heteroscedasticity</strong></dt>
      <dd>When the variance of residuals is not constant across all levels of independent variables in regression.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>I-J</h3>
    <dl>
      <dt><strong>IQR (Interquartile Range)</strong></dt>
      <dd>The range between the 25th and 75th percentiles. Used to identify outliers (values beyond 1.5×IQR from quartiles).</dd>
      
      <dt><strong>Imputation</strong></dt>
      <dd>The process of replacing missing data with substituted values using various strategies (mean, median, mode, or predictive methods).</dd>
      
      <dt><strong>JOIN</strong></dt>
      <dd>SQL operation combining rows from two or more tables based on a related column. Types: INNER, LEFT, RIGHT, FULL, CROSS.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>K</h3>
    <dl>
      <dt><strong>K-fold Cross Validation</strong></dt>
      <dd>A model validation technique that divides data into k subsets, training on k-1 folds and testing on the remaining fold, rotating k times.</dd>
      
      <dt><strong>KPI (Key Performance Indicator)</strong></dt>
      <dd>A measurable value demonstrating how effectively a company is achieving key business objectives.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>L</h3>
    <dl>
      <dt><strong>Linear Regression</strong></dt>
      <dd>A statistical method modeling the relationship between a dependent variable and one or more independent variables using a linear equation.</dd>
      
      <dt><strong>Logistic Regression</strong></dt>
      <dd>A classification algorithm that models the probability of a binary outcome using the logistic function.</dd>
      
      <dt><strong>Log-Normal Distribution</strong></dt>
      <dd>A distribution of a variable whose logarithm follows a normal distribution. Common in revenue and engagement metrics.</dd>
      
      <dt><strong>LTV (Lifetime Value)</strong></dt>
      <dd>The predicted total revenue a customer will generate throughout their relationship with a business.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>M</h3>
    <dl>
      <dt><strong>Mean</strong></dt>
      <dd>The arithmetic average of a set of values. Sum of all values divided by the count. Sensitive to outliers.</dd>
      
      <dt><strong>Median</strong></dt>
      <dd>The middle value in a sorted dataset. More robust to outliers than mean.</dd>
      
      <dt><strong>Mode</strong></dt>
      <dd>The most frequently occurring value in a dataset. A distribution can have multiple modes.</dd>
      
      <dt><strong>Multicollinearity</strong></dt>
      <dd>When two or more independent variables in a regression model are highly correlated, making it difficult to isolate individual effects.</dd>
      
      <dt><strong>MLE (Maximum Likelihood Estimation)</strong></dt>
      <dd>A method for estimating parameters by finding values that maximize the likelihood of observing the data.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>N</h3>
    <dl>
      <dt><strong>Normal Distribution</strong></dt>
      <dd>A symmetric, bell-shaped probability distribution characterized by mean and standard deviation. 68-95-99.7 rule applies.</dd>
      
      <dt><strong>Null Hypothesis (H₀)</strong></dt>
      <dd>The default assumption in hypothesis testing that there is no effect or difference. What we try to reject.</dd>
      
      <dt><strong>NPS (Net Promoter Score)</strong></dt>
      <dd>A customer loyalty metric calculated from survey responses asking likelihood to recommend (0-10), ranging from -100 to +100.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>O-P</h3>
    <dl>
      <dt><strong>Outlier</strong></dt>
      <dd>A data point that differs significantly from other observations. May indicate measurement error or genuinely unusual cases.</dd>
      
      <dt><strong>Overfitting</strong></dt>
      <dd>When a model learns noise in training data, performing well on training data but poorly on new data.</dd>
      
      <dt><strong>P-value</strong></dt>
      <dd>The probability of observing results at least as extreme as the actual results, assuming the null hypothesis is true.</dd>
      
      <dt><strong>Poisson Distribution</strong></dt>
      <dd>A distribution describing the probability of a given number of events occurring in a fixed interval when events occur at a constant rate.</dd>
      
      <dt><strong>Power (Statistical)</strong></dt>
      <dd>The probability of correctly rejecting the null hypothesis when it's false (1 - β). Typically aim for 80%.</dd>
      
      <dt><strong>Precision</strong></dt>
      <dd>The proportion of positive predictions that are actually correct: TP / (TP + FP). Minimizes false positives.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>Q-R</h3>
    <dl>
      <dt><strong>Quartile</strong></dt>
      <dd>Values that divide a dataset into four equal parts: Q1 (25th percentile), Q2 (median), Q3 (75th percentile).</dd>
      
      <dt><strong>R-squared (R²)</strong></dt>
      <dd>The proportion of variance in the dependent variable explained by the independent variables. Ranges from 0 to 1.</dd>
      
      <dt><strong>Recall (Sensitivity)</strong></dt>
      <dd>The proportion of actual positives correctly identified: TP / (TP + FN). Minimizes false negatives.</dd>
      
      <dt><strong>Regression</strong></dt>
      <dd>Statistical methods for modeling relationships between variables to make predictions or understand associations.</dd>
      
      <dt><strong>Retention Rate</strong></dt>
      <dd>The percentage of customers who continue using a product over a specific time period.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>S</h3>
    <dl>
      <dt><strong>Sample Size</strong></dt>
      <dd>The number of observations in a sample. Larger samples provide more precise estimates and greater statistical power.</dd>
      
      <dt><strong>Standard Deviation (σ)</strong></dt>
      <dd>A measure of the amount of variation in a dataset. The square root of variance.</dd>
      
      <dt><strong>Standard Error</strong></dt>
      <dd>The standard deviation of a sampling distribution. For means: SE = σ/√n.</dd>
      
      <dt><strong>Statistical Significance</strong></dt>
      <dd>When the p-value is less than the chosen significance level (α), indicating the result is unlikely due to chance alone.</dd>
      
      <dt><strong>Subquery</strong></dt>
      <dd>A query nested inside another SQL query. Can be used in SELECT, FROM, WHERE, or HAVING clauses.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>T</h3>
    <dl>
      <dt><strong>T-test</strong></dt>
      <dd>A statistical test comparing means. Types include one-sample, independent two-sample, and paired t-tests.</dd>
      
      <dt><strong>Type I Error</strong></dt>
      <dd>Rejecting the null hypothesis when it's true (false positive). Probability equals α.</dd>
      
      <dt><strong>Type II Error</strong></dt>
      <dd>Failing to reject the null hypothesis when it's false (false negative). Probability equals β.</dd>
      
      <dt><strong>Time Series</strong></dt>
      <dd>A sequence of data points indexed in time order, often analyzed for trends, seasonality, and patterns.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>U-V</h3>
    <dl>
      <dt><strong>Underfitting</strong></dt>
      <dd>When a model is too simple to capture underlying patterns, performing poorly on both training and test data.</dd>
      
      <dt><strong>Variance</strong></dt>
      <dd>A measure of how spread out data points are from the mean. The average of squared deviations from the mean.</dd>
      
      <dt><strong>VIF (Variance Inflation Factor)</strong></dt>
      <dd>A measure of multicollinearity in regression. VIF > 10 typically indicates problematic multicollinearity.</dd>
    </dl>
  </div>

  <div class="card">
    <h3>W-Z</h3>
    <dl>
      <dt><strong>Welch's t-test</strong></dt>
      <dd>A variation of the t-test that doesn't assume equal variances between groups. More robust than Student's t-test.</dd>
      
      <dt><strong>Window Function</strong></dt>
      <dd>SQL functions that perform calculations across a set of rows related to the current row (e.g., ROW_NUMBER, RANK, LAG, LEAD).</dd>
      
      <dt><strong>Z-score</strong></dt>
      <dd>The number of standard deviations a data point is from the mean. Formula: z = (x - μ) / σ.</dd>
      
      <dt><strong>Z-test</strong></dt>
      <dd>A statistical test for comparing sample and population means when the population variance is known or sample size is large.</dd>
    </dl>
  </div>

  <div class="card">
    <h2>🔢 Quick Formulas Reference</h2>
    
    <h4>Descriptive Statistics</h4>
    <ul>
      <li><strong>Mean:</strong> μ = Σx / n</li>
      <li><strong>Variance:</strong> σ² = Σ(x - μ)² / n</li>
      <li><strong>Standard Deviation:</strong> σ = √(σ²)</li>
      <li><strong>Standard Error:</strong> SE = σ / √n</li>
      <li><strong>Coefficient of Variation:</strong> CV = (σ / μ) * 100%</li>
    </ul>
    
    <h4>Probability</h4>
    <ul>
      <li><strong>Bayes' Theorem:</strong> P(A|B) = P(B|A) * P(A) / P(B)</li>
      <li><strong>Addition Rule:</strong> P(A ∪ B) = P(A) + P(B) - P(A ∩ B)</li>
      <li><strong>Multiplication Rule:</strong> P(A ∩ B) = P(A) * P(B|A)</li>
    </ul>
    
    <h4>Hypothesis Testing</h4>
    <ul>
      <li><strong>Z-statistic:</strong> z = (x̄ - μ) / (σ / √n)</li>
      <li><strong>T-statistic:</strong> t = (x̄ - μ) / (s / √n)</li>
      <li><strong>Confidence Interval:</strong> x̄ ± z* × (σ / √n)</li>
    </ul>
    
    <h4>Sample Size (for proportions)</h4>
    <ul>
      <li><strong>Formula:</strong> n = (z² × p × (1-p)) / E²</li>
      <li>Where E is the margin of error</li>
    </ul>
  </div>

  <div class="navigation-buttons">
    <a href="{{ '/conclusion/' | relative_url }}">Previous: Conclusion</a>
    <a href="{{ '/' | relative_url }}">Back to Home</a>
  </div>
</div>

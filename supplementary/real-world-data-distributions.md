# Real-World Data Distributions in Product Analytics

Understanding data distributions is crucial for choosing the right statistical tests, designing experiments, and interpreting results correctly. This guide covers common distributions you'll encounter in product analytics and data science interviews.

## Why Distributions Matter

- **Statistical Tests**: Many tests assume normality; knowing your distribution helps select appropriate methods
- **A/B Testing**: Sample size calculations and result interpretation depend on data distribution
- **Outlier Detection**: What's an outlier depends on the expected distribution
- **Metric Design**: Choosing mean vs. median depends on distribution shape

---

## Common Distributions in Product Data

### 1. Normal (Gaussian) Distribution

**Where You'll See It:**
- Aggregated metrics over large samples (Central Limit Theorem)
- Measurement errors
- User session durations (after log transformation)
- Physical measurements (height, weight)

**Key Properties:**
- Symmetric, bell-shaped
- Mean = Median = Mode
- 68-95-99.7 rule: 68% within ±1σ, 95% within ±2σ, 99.7% within ±3σ

**When to Assume Normality:**
- Large sample sizes (n > 30) for sample means
- After log transformation of right-skewed data
- Residuals in regression analysis

```python
import numpy as np
from scipy import stats

# Generate normal data
data = np.random.normal(loc=100, scale=15, size=1000)

# Check for normality
statistic, p_value = stats.shapiro(data)
print(f"Shapiro-Wilk test p-value: {p_value:.4f}")
```

---

### 2. Log-Normal Distribution

**Where You'll See It:**
- **Revenue per user** (many small, few large transactions)
- Time between purchases
- User engagement scores
- Session duration
- File sizes

**Why It Matters:**
Many "long-tail" metrics in product analytics are log-normal. Taking the log makes them normal, enabling standard statistical tests.

**Key Properties:**
- Right-skewed (long tail on the right)
- Always positive values
- Multiplicative processes (compounding effects)

**Practical Tip:**
```python
import numpy as np

# Transform log-normal to normal
revenue = [10, 15, 20, 25, 100, 500, 1000]  # Skewed
log_revenue = np.log(revenue)  # Now approximately normal

# Use geometric mean instead of arithmetic mean
geometric_mean = np.exp(np.mean(log_revenue))
```

---

### 3. Poisson Distribution

**Where You'll See It:**
- Number of app opens per day per user
- Customer support tickets per hour
- Clicks on a page
- Events in a time window
- Number of errors per session

**Key Properties:**
- Discrete counts (0, 1, 2, 3, ...)
- Mean = Variance (λ)
- Useful for rare events

**Interview Application:**
When asked about modeling counts or rates, consider Poisson. Check if mean ≈ variance to validate.

```python
from scipy import stats

# Model daily app opens
lambda_param = 3  # Average opens per day
poisson = stats.poisson(lambda_param)

# Probability of exactly 5 opens
prob_5 = poisson.pmf(5)
print(f"P(X=5): {prob_5:.4f}")
```

---

### 4. Exponential Distribution

**Where You'll See It:**
- Time between user actions
- Session inter-arrival times
- Time to first conversion
- Wait time until next event

**Key Properties:**
- Continuous, always positive
- Memoryless property (waiting doesn't change future probability)
- Often paired with Poisson (time between Poisson events)

**Practical Use:**
Modeling time-to-event metrics like time to churn or time to first purchase.

---

### 5. Power Law (Pareto/Zipf) Distribution

**Where You'll See It:**
- User engagement (few users generate most content)
- Revenue concentration (few customers drive most revenue)
- Social connections (few users have most followers)
- Product popularity (few products get most sales)
- Word frequencies in text

**Key Properties:**
- 80/20 rule (Pareto principle)
- No meaningful average (can be infinite)
- Log-log plot appears linear

**Why This Matters for Interviews:**
Understanding power laws helps explain:
- Why averages can be misleading for engagement metrics
- Why personalization focuses on "whale" users
- Why A/B tests on engagement can be tricky

---

### 6. Binomial Distribution

**Where You'll See It:**
- Conversion rates (success/failure outcomes)
- Click-through rates
- A/B test success counts
- Any yes/no outcome across n trials

**Key Properties:**
- n independent trials, each with probability p of success
- Mean = np, Variance = np(1-p)
- Approximates normal for large n

**A/B Testing Application:**
```python
from scipy import stats

# Conversion test: 1000 users, 5% conversion
n, p = 1000, 0.05
binom = stats.binom(n, p)

# 95% confidence interval for conversions
lower, upper = binom.ppf(0.025), binom.ppf(0.975)
print(f"95% CI: [{lower}, {upper}] conversions")
```

---

## Practical Implications for A/B Testing

### Non-Normal Data Handling

| Data Type | Common Distribution | Recommended Approach |
|-----------|---------------------|---------------------|
| Revenue | Log-normal | Log-transform, then t-test |
| Counts | Poisson | Poisson regression or bootstrap |
| Proportions | Binomial | Chi-squared or Z-test for proportions |
| Time-to-event | Exponential/Weibull | Survival analysis |
| Heavy-tailed | Power law | Bootstrap, use medians |

### When to Transform Data

1. **Log Transform**: Right-skewed data (revenue, time metrics)
2. **Square Root**: Count data with Poisson-like properties
3. **Box-Cox**: General normalizing transformation

### Bootstrap for Complex Metrics

When distribution is unclear or complex, use bootstrapping:

```python
import numpy as np

def bootstrap_mean_ci(data, n_bootstrap=10000, ci=0.95):
    """Calculate bootstrap confidence interval for mean."""
    bootstrap_mean_samples = [np.mean(np.random.choice(data, len(data), replace=True)) 
                              for _ in range(n_bootstrap)]
    lower = np.percentile(bootstrap_mean_samples, (1-ci)/2 * 100)
    upper = np.percentile(bootstrap_mean_samples, (1+ci)/2 * 100)
    return lower, upper
```

---

## Distribution Selection Decision Tree

> **Note:** This is a simplified decision tree for initial guidance. Always complement these rules with domain knowledge, visual inspection of your data (histograms, Q-Q plots), and formal statistical tests for distribution fitting (e.g., Shapiro–Wilk test for normality, Kolmogorov–Smirnov test, Anderson–Darling test).

```
Is your data continuous?
├── YES: Is it always positive?
│   ├── YES: Is it right-skewed?
│   │   ├── YES → Consider Log-Normal or Exponential
│   │   └── NO → Consider Normal
│   └── NO: Can it be negative?
│       └── YES → Consider Normal
└── NO (Discrete): Is it a count?
    ├── YES: Is mean ≈ variance?
    │   ├── YES → Consider Poisson
    │   └── NO → Consider Negative Binomial
    └── NO: Is it binary (yes/no)?
        └── YES → Consider Binomial/Bernoulli
```

---

## Summary Table: Distributions by Domain

| Domain | Metric Example | Likely Distribution | Key Consideration |
|--------|---------------|--------------------|--------------------|
| E-commerce | Revenue per user | Log-normal | Use geometric mean |
| Social Media | Followers count | Power law | Median more meaningful |
| SaaS | Daily active usage | Poisson | Check mean=variance |
| Fintech | Transaction amount | Log-normal | Heavy tail risk |
| Gaming | Session duration | Log-normal | Consider censoring |
| Healthcare | Test results | Normal (often) | Validate assumptions |

---

## Interview Tips

1. **Always ask about the distribution** before recommending a statistical test
2. **Know when mean is misleading** (power law, heavily skewed data)
3. **Understand CLT** - sample means become normal even if population isn't
4. **Be ready to suggest transformations** for non-normal data
5. **Bootstrapping is your friend** when unsure about distribution

---

## Additional Resources

- [StatQuest: Probability Distributions](https://www.youtube.com/c/joshstarmer)
- [Khan Academy: Random Variables and Probability Distributions](https://www.khanacademy.org/math/statistics-probability)
- [Seeing Theory: Probability Distributions Visualized](https://seeing-theory.brown.edu/)

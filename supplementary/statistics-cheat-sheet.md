---
layout: page
title: "Statistics Cheat Sheet"
permalink: /supplementary/statistics-cheat-sheet/
nav_order: 11
parent: "Supplementary Materials"
difficulty: "Beginner"
estimated_time: "25 mins"
tags: [Statistics, Probability, Reference, Cheat Sheet]
track: "Reference"
---

# Statistics Cheat Sheet

## Descriptive Statistics Formulas

### Measures of Central Tendency

**Mean (Arithmetic Mean):**
$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

**Median:**
- For odd n: Middle value when sorted
- For even n: Average of two middle values

**Mode:** Most frequently occurring value

### Measures of Variability

**Variance:**
$$\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n} \quad (\text{population})$$
$$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1} \quad (\text{sample})$$

**Standard Deviation:**
$$\sigma = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}} \quad (\text{population})$$
$$s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}} \quad (\text{sample})$$

**Range:** Maximum - Minimum

**Interquartile Range (IQR):** Q3 - Q1

## Probability Rules

### Basic Rules
- **Addition Rule:** P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- **Multiplication Rule:** P(A ∩ B) = P(A) × P(B|A)
- **Conditional Probability:** P(A|B) = P(A ∩ B) / P(B)
- **Bayes' Theorem:** P(A|B) = [P(B|A) × P(A)] / P(B)

### Independence
Events A and B are independent if: P(A ∩ B) = P(A) × P(B)

## Common Probability Distributions

### Normal Distribution
**PDF:** $$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$$

**Standard Normal:** Z = (X - μ) / σ

**68-95-99.7 Rule:**
- 68% within 1σ
- 95% within 2σ
- 99.7% within 3σ

### Binomial Distribution
**PMF:** $$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

**Mean:** μ = np
**Variance:** σ² = np(1-p)

### Poisson Distribution
**PMF:** $$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}$$

**Mean = Variance = λ**

### Exponential Distribution
**PDF:** $$f(x) = \lambda e^{-\lambda x} \quad (x \geq 0)$$

**Mean:** 1/λ
**Variance:** 1/λ²

## Hypothesis Testing Framework

### Steps:
1. State null (H₀) and alternative (H₁) hypotheses
2. Choose significance level (α)
3. Calculate test statistic
4. Find p-value or critical value
5. Make decision: Reject H₀ if p-value < α

### Common Test Statistics

**Z-test:** $$z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}$$

**T-test:** $$t = \frac{\bar{x} - \mu}{s/\sqrt{n}}$$

**Chi-Square test:** $$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

## Confidence Intervals

### For Mean (σ known):
$$\bar{x} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

### For Mean (σ unknown):
$$\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$$

### For Proportion:
$$\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

## Sample Size Calculations

### For Mean:
$$n = \left( \frac{z_{\alpha/2} \sigma}{E} \right)^2$$

Where E is the margin of error.

### For Proportion:
$$n = \frac{z_{\alpha/2}^2 p(1-p)}{E^2}$$

### For A/B Testing (Two proportions):
$$n = \frac{(z_{\alpha/2} + z_\beta)^2 (p_1(1-p_1) + p_2(1-p_2))}{(p_1 - p_2)^2}$$

## Effect Size Calculations

### Cohen's d (for means):
$$d = \frac{\bar{x}_1 - \bar{x}_2}{s}$$

**Interpretation:**
- Small: 0.2
- Medium: 0.5
- Large: 0.8

### Odds Ratio:
$$OR = \frac{p_1/(1-p_1)}{p_2/(1-p_2)}$$

## Regression Formulas

### Simple Linear Regression
**Slope:** $$b_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$$

**Intercept:** $$b_0 = \bar{y} - b_1\bar{x}$$

**Prediction:** $$\hat{y} = b_0 + b_1x$$

### R-squared
$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = \frac{SS_{reg}}{SS_{tot}}$$

### Correlation Coefficient
$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

## Common Statistical Tests Decision Tree

```
Is the data normally distributed?
├── Yes
│   ├── One sample?
│   │   ├── Mean known? → Z-test
│   │   └── Mean unknown? → T-test
│   ├── Two samples?
│   │   ├── Paired? → Paired T-test
│   │   └── Independent? → Two-sample T-test
│   └── Multiple groups? → ANOVA
└── No
    ├── Categorical data? → Chi-square test
    ├── Ordinal data? → Mann-Whitney U or Kruskal-Wallis
    └── Non-parametric alternatives
```

## P-value Interpretation Guide

| p-value | Evidence against H₀ |
|---------|---------------------|
| p > 0.10 | No evidence |
| 0.05 < p ≤ 0.10 | Weak evidence |
| 0.01 < p ≤ 0.05 | Moderate evidence |
| 0.001 < p ≤ 0.01 | Strong evidence |
| p ≤ 0.001 | Very strong evidence |

## Power Analysis

**Power = 1 - β**

**Factors affecting power:**
- Sample size (n ↑ → power ↑)
- Effect size (δ ↑ → power ↑)
- Significance level (α ↑ → power ↑)
- Variability (σ ↓ → power ↑)

**Power formula (for two-sample t-test):**
$$1 - \beta = \Phi\left( \frac{|\mu_1 - \mu_2|}{\sigma/\sqrt{n}} - z_{1-\alpha/2} \right)$$

## Common Mistakes to Avoid

1. **Confusing correlation with causation**
2. **Multiple testing problem** (use Bonferroni correction)
3. **p-hacking** (fishing for significant results)
4. **Ignoring effect size** (focus only on p-values)
5. **Assuming normality** without checking
6. **Using parametric tests** on non-normal data
7. **Small sample sizes** leading to unreliable results
8. **Not checking assumptions** of statistical tests
---
layout: default
title: "A/B Testing & Experimentation"
permalink: /foundational_knowledge/4-ab-testing/
difficulty: "Intermediate"
estimated_time: "60 mins"
tags: [A/B Testing, Experimentation, Statistics, Hypothesis Testing]
track: "Foundational Knowledge"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Foundational Knowledge & Skills</a> <span>&gt;</span>
  <span>A/B Testing & Experimentation</span>
</div>

<div class="header">
  <h1>A/B Testing & Experimentation</h1>
  <p>Design, analyze, and interpret experiments like a senior data scientist.</p>
</div>

<div class="section">
  
  <div class="card">
    <h3>Why This Matters</h3>
    <p>A/B testing is the backbone of data-driven product development. At companies like Meta, Google, Netflix, and Amazon, <strong>every major product change goes through experimentation</strong>. Expect 30%+ of your DS interview to focus on experiment design, analysis, and interpretation.</p>
    
    <p><strong>What interviewers are looking for:</strong></p>
    <ul>
      <li>Can you design a valid experiment from scratch?</li>
      <li>Do you understand when experiments can go wrong?</li>
      <li>Can you interpret results correctly, including edge cases?</li>
      <li>Do you know when NOT to run an A/B test?</li>
    </ul>
  </div>

  <div class="card">
    <h3>The A/B Testing Mental Model</h3>
    <pre>
┌─────────────────────────────────────────────────────────────────┐
│  1. DEFINE THE QUESTION                                         │
│     → What are we trying to learn?                              │
│     → What decision will we make based on results?              │
├─────────────────────────────────────────────────────────────────┤
│  2. DESIGN THE EXPERIMENT                                       │
│     → Hypothesis (H₀ and H₁)                                    │
│     → Metrics (primary, secondary, guardrail)                   │
│     → Sample size & duration                                    │
│     → Randomization unit                                        │
├─────────────────────────────────────────────────────────────────┤
│  3. RUN THE EXPERIMENT                                          │
│     → Validate randomization (A/A check)                        │
│     → Monitor for bugs & anomalies                              │
│     → DON'T peek and make decisions early!                      │
├─────────────────────────────────────────────────────────────────┤
│  4. ANALYZE RESULTS                                             │
│     → Statistical significance                                  │
│     → Practical significance (effect size)                      │
│     → Segment analysis (but beware multiple testing)            │
├─────────────────────────────────────────────────────────────────┤
│  5. MAKE A DECISION                                             │
│     → Ship, iterate, or kill                                    │
│     → Document learnings                                        │
└─────────────────────────────────────────────────────────────────┘
    </pre>
  </div>

  <div class="card">
    <h3>Key Concepts You Must Know</h3>
    
    <h4>1. Hypothesis Testing Fundamentals</h4>
    <ul>
      <li><strong>Null Hypothesis (H₀):</strong> There is no difference between control and treatment</li>
      <li><strong>Alternative Hypothesis (H₁):</strong> There is a difference</li>
      <li><strong>p-value:</strong> Probability of seeing data this extreme IF H₀ is true</li>
      <li><strong>Significance level (α):</strong> Threshold for rejecting H₀ (typically 0.05)</li>
      <li><strong>Power (1-β):</strong> Probability of detecting a real effect (typically 0.80)</li>
    </ul>
    
    <h4>2. Error Types</h4>
    <table>
      <tr>
        <th></th>
        <th>H₀ True (No Effect)</th>
        <th>H₀ False (Real Effect)</th>
      </tr>
      <tr>
        <td><strong>Reject H₀</strong></td>
        <td>Type I Error (α) – False Positive</td>
        <td>✅ Correct – True Positive</td>
      </tr>
      <tr>
        <td><strong>Fail to Reject H₀</strong></td>
        <td>✅ Correct – True Negative</td>
        <td>Type II Error (β) – False Negative</td>
      </tr>
    </table>
    
    <h4>3. Sample Size Formula (Proportions)</h4>
    <p>For a two-proportion z-test with equal group sizes:</p>
    <pre><code>n = 2 × [(Z_α/2 + Z_β)² × p̄(1-p̄)] / (p₁ - p₂)²

where:
  p̄ = (p₁ + p₂) / 2  (pooled proportion)
  p₁ = baseline conversion rate
  p₂ = expected treatment conversion rate
  Z_α/2 = 1.96 for α=0.05 (two-tailed)
  Z_β = 0.84 for power=0.80</code></pre>
    
    <p><strong>Quick Python implementation:</strong></p>
    <pre><code>from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Example: baseline 5%, want to detect 5.5% (10% relative lift)
effect_size = proportion_effectsize(0.05, 0.055)
analysis = NormalIndPower()
n = analysis.solve_power(effect_size=effect_size, alpha=0.05, power=0.8, alternative='two-sided')
print(f"Sample size per group: {n:.0f}")  # ~31,000</code></pre>
  </div>

  <div class="card">
    <h3>Metrics Framework</h3>
    <p>Every experiment needs three types of metrics:</p>
    
    <table>
      <tr>
        <th>Metric Type</th>
        <th>Purpose</th>
        <th>Example</th>
      </tr>
      <tr>
        <td><strong>Primary (North Star)</strong></td>
        <td>The ONE metric that determines success</td>
        <td>Conversion rate, DAU, Revenue/user</td>
      </tr>
      <tr>
        <td><strong>Secondary</strong></td>
        <td>Additional insights, explain mechanisms</td>
        <td>Click-through rate, time on page</td>
      </tr>
      <tr>
        <td><strong>Guardrail</strong></td>
        <td>Ensure we don't break something important</td>
        <td>Page load time, error rate, unsubscribes</td>
      </tr>
    </table>
    
    <p><strong>Example:</strong> Testing a new checkout flow</p>
    <ul>
      <li><strong>Primary:</strong> Purchase completion rate</li>
      <li><strong>Secondary:</strong> Average order value, cart abandonment rate</li>
      <li><strong>Guardrail:</strong> Page load time, support tickets, refund rate</li>
    </ul>
  </div>

  <div class="card">
    <h3>Common Pitfalls & How to Avoid Them</h3>
    
    <h4>1. Peeking Problem</h4>
    <p><strong>What:</strong> Checking results multiple times and stopping when significant.</p>
    <p><strong>Why it's bad:</strong> Inflates false positive rate. With daily peeking for 20 days at α=0.05, your actual false positive rate can exceed 25%!</p>
    <p><strong>Fix:</strong> Pre-commit to a sample size and analysis date. If you must peek, use sequential testing (e.g., alpha spending functions).</p>
    
    <h4>2. Multiple Testing Problem</h4>
    <p><strong>What:</strong> Testing 20 metrics and declaring victory on the one that's significant.</p>
    <p><strong>Why it's bad:</strong> At α=0.05, testing 20 metrics gives ~64% chance of at least one false positive.</p>
    <p><strong>Fix:</strong> Pre-specify ONE primary metric. Apply Bonferroni (α/n) or Benjamini-Hochberg (FDR) corrections for secondaries.</p>
    
    <h4>3. Network Effects / Spillover</h4>
    <p><strong>What:</strong> Treatment users affect control users through social connections.</p>
    <p><strong>Why it's bad:</strong> Dilutes treatment effect; biases toward null.</p>
    <p><strong>Fix:</strong> Cluster randomization (randomize by geography, community, or time).</p>
    
    <h4>4. Novelty / Primacy Effects</h4>
    <p><strong>What:</strong> New features show temporary lift from curiosity, or underperform while users adapt.</p>
    <p><strong>Fix:</strong> Run experiments for 2+ weeks; segment by new vs returning users; look at effect over time.</p>
    
    <h4>5. Simpson's Paradox</h4>
    <p><strong>What:</strong> Treatment wins overall but loses in every segment (or vice versa).</p>
    <p><strong>Why it happens:</strong> Unequal segment sizes between variants.</p>
    <p><strong>Fix:</strong> Always check segment-level results; investigate sample ratio mismatch (SRM).</p>
  </div>

  <div class="card">
    <h3>🧠 Challenge Questions with Solutions</h3>
    
    <details>
    <summary><strong>Challenge 1: Design an A/B Test</strong></summary>
    <p><strong>Scenario:</strong> Instagram is considering changing the "Like" button from a heart to a thumbs-up. Design the experiment.</p>
    
    <h4>Solution Framework:</h4>
    <ol>
      <li><strong>Hypothesis:</strong>
        <ul>
          <li>H₀: Thumbs-up will not change like rate</li>
          <li>H₁: Thumbs-up will change like rate (two-tailed since we're unsure of direction)</li>
        </ul>
      </li>
      <li><strong>Metrics:</strong>
        <ul>
          <li>Primary: Like rate (likes / impressions)</li>
          <li>Secondary: Engagement rate, time spent, content creation rate</li>
          <li>Guardrail: DAU, session duration, negative feedback rate</li>
        </ul>
      </li>
      <li><strong>Sample Size:</strong>
        <ul>
          <li>Assume baseline like rate = 5%</li>
          <li>MDE = 2% relative (detect 5% → 5.1%)</li>
          <li>α = 0.05, power = 0.80</li>
          <li>Result: ~1.5M users per variant (use calculator)</li>
        </ul>
      </li>
      <li><strong>Randomization:</strong>
        <ul>
          <li>Unit: User ID (not session, not device)</li>
          <li>Consider cluster randomization by region if network effects expected</li>
        </ul>
      </li>
      <li><strong>Duration:</strong>
        <ul>
          <li>Minimum 2 weeks to capture weekly cycles</li>
          <li>Consider novelty effects—new icon might get more clicks initially</li>
        </ul>
      </li>
      <li><strong>Risks:</strong>
        <ul>
          <li>Strong brand association with heart—user backlash</li>
          <li>Novelty effect—temporary lift from curiosity</li>
          <li>Should run sentiment analysis alongside quantitative metrics</li>
        </ul>
      </li>
    </ol>
    </details>
    
    <details>
    <summary><strong>Challenge 2: Interpret Conflicting Results</strong></summary>
    <p><strong>Scenario:</strong> Your A/B test shows:</p>
    <ul>
      <li>Primary metric (conversion): +3% (p=0.03) ✅</li>
      <li>Guardrail metric (page load time): +200ms (p=0.001) ❌</li>
    </ul>
    <p>What do you recommend?</p>
    
    <h4>Solution:</h4>
    <ol>
      <li><strong>Acknowledge the trade-off:</strong> We have a conversion win but a performance regression.</li>
      <li><strong>Quantify the trade-off:</strong>
        <ul>
          <li>What's the revenue impact of +3% conversion?</li>
          <li>What's the long-term cost of +200ms load time? (Research shows ~1% bounce per 100ms)</li>
        </ul>
      </li>
      <li><strong>Investigate root cause:</strong>
        <ul>
          <li>Is the load time increase inherent to the feature, or a fixable implementation issue?</li>
          <li>Segment by device/connection—is it only affecting slow connections?</li>
        </ul>
      </li>
      <li><strong>Recommendation:</strong>
        <ul>
          <li>If load time is fixable: Hold launch, fix performance, re-test</li>
          <li>If inherent trade-off: Model long-term impact; usually don't ship perf regressions</li>
        </ul>
      </li>
    </ol>
    <p><strong>Key insight:</strong> Never ignore guardrail metrics. Short-term wins often become long-term losses.</p>
    </details>
    
    <details>
    <summary><strong>Challenge 3: Low Power, What Now?</strong></summary>
    <p><strong>Scenario:</strong> Your sample size calculation shows you need 2M users per variant, but you only get 500K users/week. The experiment would take 2 months. What are your options?</p>
    
    <h4>Solution Options:</h4>
    <table>
      <tr>
        <th>Option</th>
        <th>Trade-off</th>
        <th>When to Use</th>
      </tr>
      <tr>
        <td>Increase MDE</td>
        <td>Can only detect larger effects</td>
        <td>If smaller effects aren't worth shipping anyway</td>
      </tr>
      <tr>
        <td>Reduce power to 0.70</td>
        <td>30% chance of missing real effect</td>
        <td>Low-stakes decisions</td>
      </tr>
      <tr>
        <td>Use one-tailed test</td>
        <td>Can't detect negative effects</td>
        <td>Only if you'd never ship a negative result</td>
      </tr>
      <tr>
        <td>Variance reduction (CUPED)</td>
        <td>Requires pre-experiment data</td>
        <td>Best option if feasible</td>
      </tr>
      <tr>
        <td>Target high-impact segment</td>
        <td>Results may not generalize</td>
        <td>Power users, specific geo</td>
      </tr>
      <tr>
        <td>Just wait (run longer)</td>
        <td>Delays product roadmap</td>
        <td>High-stakes decisions</td>
      </tr>
    </table>
    
    <p><strong>CUPED (Controlled-experiment Using Pre-Experiment Data):</strong></p>
    <pre><code># CUPED reduces variance by controlling for pre-experiment behavior
# Adjusted metric: Y_adj = Y - θ × (X - X̄)
# where X = pre-experiment value of the metric
# θ = Cov(Y, X) / Var(X)

# Can reduce required sample size by 50%+ in some cases</code></pre>
    </details>
    
    <details>
    <summary><strong>Challenge 4: Sample Ratio Mismatch (SRM)</strong></summary>
    <p><strong>Scenario:</strong> Your 50/50 experiment shows 1,020,000 users in control and 980,000 in treatment. Is this a problem?</p>
    
    <h4>Solution:</h4>
    <pre><code>from scipy.stats import chi2_contingency

observed = [1020000, 980000]
expected = [1000000, 1000000]

# Chi-squared test for SRM
chi2 = sum((o - e)**2 / e for o, e in zip(observed, expected))
# chi2 = 800

# For df=1, chi2 > 3.84 is significant at α=0.05
# This is HIGHLY significant - something is wrong!</code></pre>
    
    <p><strong>Common causes of SRM:</strong></p>
    <ul>
      <li>Bot filtering applied differently</li>
      <li>Redirect/loading issues in one variant</li>
      <li>Bucketing bug in the experiment system</li>
      <li>Treatment causing more users to log out (lose tracking)</li>
    </ul>
    
    <p><strong>Action:</strong> DO NOT interpret results until SRM is resolved. Investigate root cause first.</p>
    </details>
    
    <details>
    <summary><strong>Challenge 5: When NOT to A/B Test</strong></summary>
    <p><strong>Question:</strong> Give 5 scenarios where A/B testing is NOT appropriate.</p>
    
    <h4>Solution:</h4>
    <ol>
      <li><strong>Obvious improvements:</strong> Fixing a bug, improving load time. Just ship it.</li>
      <li><strong>Legal/compliance changes:</strong> GDPR requirements. No choice but to comply.</li>
      <li><strong>Low traffic:</strong> Would take years to reach significance. Use qualitative research.</li>
      <li><strong>Network effects dominate:</strong> Marketplace features where treatment affects control through shared inventory.</li>
      <li><strong>Long-term effects matter most:</strong> Education/habit-forming features. Effect emerges over months, not weeks.</li>
      <li><strong>Ethical concerns:</strong> Testing features that could harm users (e.g., addiction-promoting).</li>
      <li><strong>Launch-and-iterate is cheaper:</strong> Low-risk UI changes with easy rollback.</li>
    </ol>
    
    <p><strong>Alternative methods:</strong></p>
    <ul>
      <li>User research & qualitative testing</li>
      <li>Quasi-experimental designs (diff-in-diff, regression discontinuity)</li>
      <li>Holdout/long-term experiments</li>
      <li>Synthetic control methods</li>
    </ul>
    </details>
  </div>

  <div class="card">
    <h3>Interview Cheat Sheet</h3>
    <table>
      <tr>
        <th>Question Type</th>
        <th>What They're Testing</th>
        <th>Key Points to Hit</th>
      </tr>
      <tr>
        <td>"Design an A/B test for..."</td>
        <td>Structured thinking</td>
        <td>Hypothesis → Metrics → Sample size → Randomization → Duration → Risks</td>
      </tr>
      <tr>
        <td>"Results are significant but..."</td>
        <td>Critical thinking</td>
        <td>Statistical vs practical significance, trade-offs, segment analysis</td>
      </tr>
      <tr>
        <td>"What could go wrong?"</td>
        <td>Experience</td>
        <td>SRM, novelty, spillover, multiple testing, Simpson's paradox</td>
      </tr>
      <tr>
        <td>"Results are flat, what now?"</td>
        <td>Pragmatism</td>
        <td>Check power, segment, don't ship (absence of evidence ≠ evidence of absence)</td>
      </tr>
    </table>
  </div>

  <div class="card">
    <h3>💬 Discussion Prompts</h3>
    <ol>
      <li><strong>"What's your process for choosing MDE?"</strong> — Share how you balance business needs with statistical feasibility.</li>
      <li><strong>"Describe a time an experiment surprised you"</strong> — Post your war stories for others to learn from.</li>
      <li><strong>"How do you handle stakeholders who want to peek?"</strong> — Share strategies for educating non-technical partners.</li>
    </ol>
  </div>

  <div class="card">
    <h3>✅ Self-Assessment</h3>
    <p>Before moving on, confirm you can:</p>
    <ul>
      <li>☐ Calculate sample size using the formula AND explain the intuition</li>
      <li>☐ Design an experiment with hypothesis, metrics, and randomization plan</li>
      <li>☐ Explain Type I and Type II errors to a non-technical PM</li>
      <li>☐ Identify at least 5 common A/B testing pitfalls</li>
      <li>☐ Recommend when NOT to run an A/B test</li>
    </ul>
  </div>

</div>

<div class="navigation-buttons">
  <a href="{{ '/foundational_knowledge/3/' | relative_url }}">Previous: Python for Data Analysis</a>
  <a href="{{ '/interview-preparation/technical-skills/' | relative_url }}">Next: Technical Skills Interview</a>
</div>

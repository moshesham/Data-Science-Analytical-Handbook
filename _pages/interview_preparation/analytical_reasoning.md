---
layout: default
title: "Analytical Reasoning / Product Sense"
permalink: /interview-preparation/analytical-reasoning/
difficulty: "Intermediate"
estimated_time: "45 mins"
tags: [Interview, Product Sense, Metrics, Strategy]
track: "Interview Preparation"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/interview-preparation/analytical-reasoning/' | relative_url }}">Interview Preparation</a> <span>&gt;</span>
  <span>Analytical Reasoning / Product Sense</span>
</div>

<div class="header">
  <h1>Analytical Reasoning / Product Sense Interview</h1>
  <p>Approaches to evaluating product decisions and metrics-driven reasoning.</p>
</div>

<div class="section">
  
  <div class="card">
    <h3>What to Expect</h3>
    <p>This interview assesses your product sense and ability to use data to inform product decisions. You'll be presented with ambiguous product questions or scenarios and asked to define relevant metrics, design experiments (with a focus on social network considerations), analyze potential trade-offs, and communicate your insights effectively. It emphasizes strategic product thinking and data-driven decision-making, not technical coding.</p>
  </div>

  <div class="card">
    <h3>Key Focus Areas</h3>
    
    <h4>1. Clarifying Ambiguous Problems</h4>
    <p>Can you bring clarity to vague or complex product problems? Practice breaking down open-ended problems using frameworks like MECE (Mutually Exclusive, Collectively Exhaustive).</p>
    
    <h4>2. Developing Strong Product Sense</h4>
    <p>Understanding user needs, market dynamics, and product strategy. Use user-centric approaches, product strategy frameworks (SWOT, Porter's Five Forces), and competitive analysis.</p>
    
    <h4>3. Defining Relevant Metrics</h4>
    <p>Key metric concepts:</p>
    <ul>
      <li><strong>North Star Metric:</strong> The single metric that best captures the product's core value (e.g., Facebook: DAU/MAU, Instagram: DAU/Time Spent)</li>
      <li><strong>Metric Trade-offs:</strong> Understanding potential conflicts between metrics</li>
      <li><strong>Leading vs. Lagging Indicators:</strong> Use both types for comprehensive analysis</li>
      <li><strong>Success Metrics:</strong> Directly measure the desired outcome</li>
      <li><strong>Counter Metrics:</strong> Monitor for unintended negative consequences</li>
      <li><strong>Ecosystem Stability Metrics:</strong> Ensure platform health</li>
    </ul>
    
    <h4>4. Designing Experiments in Social Networks</h4>
    <p><strong>Challenges:</strong></p>
    <ul>
      <li><strong>Interference/Contagion:</strong> Control users exposed to the treatment via connections</li>
      <li><strong>Clustering:</strong> Users cluster with similar users, hindering random sampling</li>
      <li><strong>Spillover Effects:</strong> Treatment "spills over" to the control group</li>
    </ul>
    <p><strong>Mitigation Strategies:</strong></p>
    <ul>
      <li>Cluster Randomized Trials: Randomize clusters (regions, communities)</li>
      <li>Egocentric Network Design: Focus on direct connections of treated users</li>
      <li>Graph Cluster Randomization: Partition the social graph to minimize connections between treatment and control</li>
      <li>"Ghost" or "Holdout" Accounts: Synthetic/isolated accounts for initial testing</li>
    </ul>
    
    <h4>5. Metric Frameworks</h4>
    <ul>
      <li><strong>AARRR Funnel:</strong> Acquisition, Activation, Retention, Referral, Revenue</li>
      <li><strong>HEART Framework:</strong> Happiness, Engagement, Adoption, Retention, Task success</li>
    </ul>
    
    <h4>6. Example Metrics</h4>
    <ul>
      <li><strong>Engagement:</strong> Likes, comments, shares, CTR, time spent, DAU/MAU, session duration, content creation rate</li>
      <li><strong>Growth:</strong> User acquisition, new user sign-ups, viral coefficient</li>
      <li><strong>Monetization:</strong> Ad revenue, conversion rates, ARPU, LTV, average order value</li>
      <li><strong>User Experience:</strong> User satisfaction scores, app store ratings, customer support tickets</li>
    </ul>
  </div>

  <div class="card">
    <h3>How to Prepare</h3>
    <ul>
      <li>Practice breaking down open-ended problems using structured frameworks</li>
      <li>Study successful products and understand their North Star metrics</li>
      <li>Learn about network effects and their impact on experimentation</li>
      <li>Practice designing A/B tests for social products considering spillover effects</li>
      <li>Develop stories using the STAR method that demonstrate product thinking</li>
      <li>Understand how to connect metrics to business outcomes</li>
    </ul>
  </div>

</div>

---

## 📊 Product Sense Problem-Solving Framework

<div class="section">
  <div class="card">
    <h3>The CIRCLES Framework for Product Questions</h3>
    <p>Use this structured approach for any product sense question:</p>
    
    <table class="comparison-table">
      <thead>
        <tr>
          <th>Step</th>
          <th>Description</th>
          <th>Key Questions</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>C</strong>omprehend</td>
          <td>Understand the situation</td>
          <td>What is the product? What's the context? What are constraints?</td>
        </tr>
        <tr>
          <td><strong>I</strong>dentify</td>
          <td>Identify the user</td>
          <td>Who are the users? What segments exist? Who do we focus on?</td>
        </tr>
        <tr>
          <td><strong>R</strong>eport</td>
          <td>Report user needs</td>
          <td>What are their pain points? Jobs to be done? Unmet needs?</td>
        </tr>
        <tr>
          <td><strong>C</strong>ut</td>
          <td>Cut through prioritization</td>
          <td>Which needs are most important? What's the impact vs effort?</td>
        </tr>
        <tr>
          <td><strong>L</strong>ist</td>
          <td>List solutions</td>
          <td>What are possible solutions? Be creative and comprehensive</td>
        </tr>
        <tr>
          <td><strong>E</strong>valuate</td>
          <td>Evaluate trade-offs</td>
          <td>What are pros/cons? Which solution best addresses needs?</td>
        </tr>
        <tr>
          <td><strong>S</strong>ummarize</td>
          <td>Summarize recommendation</td>
          <td>What's your recommendation and why? How would you measure success?</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

---

## 🎯 Practice Problems with Step-by-Step Solutions

### Problem 1: Metric Definition (Beginner)

<div class="card">
  <h4>📋 Problem Statement</h4>
  <p><strong>Question:</strong> You're a data scientist at Spotify. The product team wants to launch a new "collaborative playlist" feature where friends can add songs to shared playlists. How would you define success metrics for this feature?</p>
</div>

<details>
<summary><strong>🔍 Step-by-Step Solution</strong></summary>

<div class="solution-steps">

**Step 1: Clarify the Feature**
- What exactly is a collaborative playlist?
- How do users invite friends?
- Is there a limit on collaborators?
- What's the primary user goal? (Social connection, music discovery, or both?)

**Step 2: Identify User Segments**
- Power users (heavy playlist creators)
- Social users (many friends on platform)
- Casual listeners (mostly consume, rarely create)
- New users (onboarding opportunity)

**Step 3: Define the North Star Metric**

> **Recommendation:** Weekly Active Collaborative Playlists (WACP) - playlists with at least 2 contributors and 1 song added in the past 7 days.

**Rationale:** This captures sustained engagement with the core feature value proposition.

**Step 4: Build the Metrics Framework**

| Category | Metric | Formula | Why It Matters |
|----------|--------|---------|----------------|
| **Adoption** | Feature adoption rate | Users creating collab playlist / Total users | Are users discovering the feature? |
| **Adoption** | Invite acceptance rate | Accepted invites / Sent invites | Is the viral loop working? |
| **Engagement** | Songs added per playlist | Total songs / Total collab playlists | Is the feature being used meaningfully? |
| **Engagement** | Contributors per playlist | Unique contributors / Active playlists | Is collaboration happening? |
| **Retention** | 7-day return rate | Users returning to collab playlists / Total collab users | Is the feature sticky? |
| **Revenue** | Premium conversion from feature | New premium from collab users / Total collab users | Business impact |

**Step 5: Define Counter Metrics (Guardrails)**
- Personal playlist creation rate (shouldn't cannibalize)
- User listening time (shouldn't decrease)
- App performance (load times)
- Spam/abuse reports on collaborative playlists

**Step 6: Success Criteria**
For launch, we'd consider the feature successful if:
- 10%+ of active users try the feature within 30 days
- 40%+ of created collaborative playlists have 2+ contributors
- No negative impact on personal playlist creation (-5% threshold)
- 7-day retention for collab users ≥ overall retention rate

</div>
</details>

---

### Problem 2: Product Trade-offs (Intermediate)

<div class="card">
  <h4>📋 Problem Statement</h4>
  <p><strong>Question:</strong> Instagram is considering removing public like counts on posts. As a data scientist, how would you analyze the impact of this change and what would you recommend?</p>
</div>

<details>
<summary><strong>🔍 Step-by-Step Solution</strong></summary>

<div class="solution-steps">

**Step 1: Understand the "Why"**
- Mental health concerns about social comparison
- Reduce anxiety for content creators
- Focus on authentic content over popularity contests
- Regulatory pressure on social media's impact on youth

**Step 2: Stakeholder Analysis**

| Stakeholder | Current Value from Likes | Potential Impact |
|-------------|-------------------------|------------------|
| **Casual users** | Social validation, discovery signal | May feel less pressure, but less dopamine |
| **Creators/Influencers** | Public credibility, brand deals | Loss of social proof, negotiation challenges |
| **Brands** | Campaign measurement, partnership vetting | Reduced transparency for marketing ROI |
| **Instagram** | Engagement driver, ad targeting signal | May reduce engagement, but improve well-being metrics |

**Step 3: Define Hypotheses to Test**

**H1 (User Well-being):** Hiding likes will improve user sentiment and reduce anxiety
- Measure: In-app surveys, NPS, support tickets about mental health

**H2 (Content Creation):** Content creation may initially decrease but diversify
- Measure: Posts per user, content type diversity, new creator rate

**H3 (Engagement):** Overall engagement may decrease short-term
- Measure: DAU, time spent, likes given (private), comments

**H4 (Creator Retention):** Influencers may migrate to competing platforms
- Measure: Creator churn rate, content frequency for top creators

**Step 4: Experiment Design**

```
Design: Cluster Randomized Trial by geographic region
Duration: 8-12 weeks (account for novelty effects)
Treatment: Hide public like counts
Control: Current experience

Randomization Unit: DMA (Designated Market Area)
Rationale: Reduces contamination from users seeing both experiences
```

**Metrics Framework:**

| Category | Primary Metric | Threshold |
|----------|---------------|-----------|
| **Health** | Time spent | No more than -5% vs control |
| **Health** | DAU | No more than -3% vs control |
| **Success** | Content creation rate | No more than -10% |
| **Success** | User satisfaction (survey) | +5% improvement |
| **Guardrail** | Influencer churn | No more than +2% |
| **Guardrail** | Ad performance | No more than -5% CTR |

**Step 5: Recommendation Framework**

```
IF user_satisfaction improves > 10% AND engagement_drop < 3%:
    → Full rollout recommended
    
IF user_satisfaction improves > 5% AND engagement_drop 3-8%:
    → Consider hybrid approach (likes visible to post owner only)
    
IF engagement_drop > 8% OR influencer_churn > 5%:
    → Do not proceed, explore alternative solutions
```

**Step 6: Alternative Solutions to Consider**
1. Hide likes only for users under 18
2. Allow users to choose visibility per post
3. Show like counts only after 24 hours
4. Replace counts with ranges ("1K-5K likes")

</div>
</details>

---

### Problem 3: Root Cause Analysis (Intermediate)

<div class="card">
  <h4>📋 Problem Statement</h4>
  <p><strong>Question:</strong> You're at DoorDash and notice that the overall order completion rate dropped by 5% week-over-week. How would you investigate this?</p>
</div>

<details>
<summary><strong>🔍 Step-by-Step Solution</strong></summary>

<div class="solution-steps">

**Step 1: Clarify and Confirm the Data**

First, validate the metric:
- Is this a data quality issue? Check data pipelines
- Is this statistically significant? Calculate confidence intervals
- Is this part of normal seasonality? Compare YoY

```sql
-- Validate the drop
WITH weekly_orders AS (
    SELECT 
        DATE_TRUNC('week', order_date) AS week,
        COUNT(*) AS total_orders,
        SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed,
        ROUND(100.0 * SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) 
              / COUNT(*), 2) AS completion_rate
    FROM orders
    WHERE order_date >= CURRENT_DATE - INTERVAL '8 weeks'
    GROUP BY 1
)
SELECT *, 
       completion_rate - LAG(completion_rate) OVER (ORDER BY week) AS wow_change
FROM weekly_orders
ORDER BY week DESC;
```

**Step 2: Segment the Drop**

Break down by key dimensions:

| Dimension | Why It Matters |
|-----------|---------------|
| **Geography** | Regional issues (weather, supply) |
| **Order Type** | Restaurant vs. grocery vs. convenience |
| **Customer Segment** | New vs. returning, DashPass vs. non |
| **Restaurant Type** | Fast food vs. fine dining, chain vs. local |
| **Time of Day** | Lunch vs. dinner, weekday vs. weekend |
| **Platform** | iOS vs. Android vs. Web |
| **Dasher Supply** | Insufficient drivers in certain areas |

```sql
-- Identify which segments dropped most
WITH current_week AS (
    SELECT 
        city,
        restaurant_category,
        customer_type,
        COUNT(*) AS orders,
        AVG(CASE WHEN status = 'completed' THEN 1.0 ELSE 0 END) AS completion_rate
    FROM orders
    WHERE order_date >= CURRENT_DATE - INTERVAL '7 days'
    GROUP BY 1, 2, 3
),
prior_week AS (
    SELECT 
        city,
        restaurant_category,
        customer_type,
        COUNT(*) AS orders,
        AVG(CASE WHEN status = 'completed' THEN 1.0 ELSE 0 END) AS completion_rate
    FROM orders
    WHERE order_date >= CURRENT_DATE - INTERVAL '14 days'
      AND order_date < CURRENT_DATE - INTERVAL '7 days'
    GROUP BY 1, 2, 3
)
SELECT 
    c.city, c.restaurant_category, c.customer_type,
    c.orders AS current_orders,
    c.completion_rate AS current_rate,
    p.completion_rate AS prior_rate,
    c.completion_rate - p.completion_rate AS rate_change
FROM current_week c
JOIN prior_week p USING (city, restaurant_category, customer_type)
WHERE ABS(c.completion_rate - p.completion_rate) > 0.03
ORDER BY rate_change ASC;
```

**Step 3: Funnel Analysis**

Decompose where orders are failing:

```
Order Funnel:
1. Order Placed → 2. Restaurant Accepts → 3. Food Prepared → 
4. Dasher Assigned → 5. Picked Up → 6. Delivered → 7. Completed

Failure Points:
- Restaurant rejection rate
- Kitchen prep delay → customer cancel
- Dasher assignment failure (no drivers)
- Dasher decline rate
- Delivery failure (wrong address, not home)
- Customer cancellation (wait too long)
```

```sql
-- Funnel analysis
SELECT 
    DATE_TRUNC('week', order_date) AS week,
    COUNT(*) AS orders_placed,
    SUM(CASE WHEN restaurant_accepted THEN 1 ELSE 0 END) AS restaurant_accepted,
    SUM(CASE WHEN dasher_assigned THEN 1 ELSE 0 END) AS dasher_assigned,
    SUM(CASE WHEN picked_up THEN 1 ELSE 0 END) AS picked_up,
    SUM(CASE WHEN delivered THEN 1 ELSE 0 END) AS delivered,
    
    -- Calculate conversion rates
    ROUND(100.0 * SUM(CASE WHEN restaurant_accepted THEN 1 ELSE 0 END) 
          / COUNT(*), 2) AS accept_rate,
    ROUND(100.0 * SUM(CASE WHEN dasher_assigned THEN 1 ELSE 0 END) 
          / NULLIF(SUM(CASE WHEN restaurant_accepted THEN 1 ELSE 0 END), 0), 2) AS assign_rate
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '8 weeks'
GROUP BY 1
ORDER BY 1 DESC;
```

**Step 4: Generate Hypotheses**

Based on segmentation, prioritize investigation:

| Hypothesis | Supporting Evidence | Priority |
|------------|-------------------|----------|
| Dasher supply shortage | Assignment rate dropped | High |
| Restaurant capacity issues | Prep time increased, rejections up | High |
| App bug on iOS | iOS completion lower, Android stable | Medium |
| Weather event | Specific cities affected | Medium |
| Competitor promotion | New customer orders down | Low |

**Step 5: Validate Hypotheses**

For the top hypothesis (Dasher supply):

```sql
-- Check Dasher supply metrics
WITH dasher_metrics AS (
    SELECT 
        DATE_TRUNC('week', shift_date) AS week,
        market,
        COUNT(DISTINCT dasher_id) AS active_dashers,
        AVG(deliveries_per_hour) AS avg_throughput,
        AVG(time_to_assign_seconds) AS avg_assignment_time
    FROM dasher_shifts
    WHERE shift_date >= CURRENT_DATE - INTERVAL '8 weeks'
    GROUP BY 1, 2
)
SELECT 
    week,
    SUM(active_dashers) AS total_dashers,
    AVG(avg_throughput) AS avg_throughput,
    AVG(avg_assignment_time) AS avg_assignment_time
FROM dasher_metrics
GROUP BY 1
ORDER BY 1 DESC;
```

**Step 6: Present Findings and Recommendations**

**Root Cause Identified:** Dasher supply dropped 15% in top 10 markets due to competitor (Uber) running a sign-on bonus campaign.

**Recommendations:**
1. **Immediate:** Increase peak hour bonuses by 20% in affected markets
2. **Short-term:** Accelerate new Dasher onboarding in priority markets
3. **Long-term:** Improve Dasher retention through better scheduling flexibility

**Expected Impact:** Restoring Dasher supply should recover 3-4% of the 5% completion rate drop within 2 weeks.

</div>
</details>

---

### Problem 4: Experiment Design in Social Networks (Advanced)

<div class="card">
  <h4>📋 Problem Statement</h4>
  <p><strong>Question:</strong> LinkedIn wants to test a new "Endorsement Reminder" feature that prompts users to endorse skills of their connections who recently updated their profiles. How would you design this experiment considering network effects?</p>
</div>

<details>
<summary><strong>🔍 Step-by-Step Solution</strong></summary>

<div class="solution-steps">

**Step 1: Understand the Challenge**

This experiment faces significant network interference:
- Treatment users' endorsements affect control users' profiles
- Increased endorsements in treatment create visibility for control users
- Social proof effects cascade through the network

**Interference Diagram:**
```
Treatment User A ──endorses──▶ Control User B's profile
                                    ↓
                    Control User B appears "more endorsed"
                                    ↓
                    Control User C sees higher endorsement count
                                    ↓
                    Contaminates control group measurement
```

**Step 2: Choose Randomization Strategy**

| Strategy | Description | Pros | Cons |
|----------|-------------|------|------|
| **User-level** | Random users | Simple | High interference |
| **Ego-network** | User + their connections | Reduces spillover | Complex, smaller N |
| **Graph cluster** | Algorithm-defined communities | Best interference control | May not reflect user experience |
| **Geographic** | By region/country | Natural isolation | Confounds with location |

**Recommendation:** Hybrid approach using industry clusters:

```sql
-- Create industry-based clusters for randomization
WITH industry_clusters AS (
    SELECT 
        user_id,
        primary_industry,
        company_size,
        -- Create cluster based on industry + company size
        CONCAT(primary_industry, '_', 
               CASE 
                   WHEN company_size < 50 THEN 'small'
                   WHEN company_size < 500 THEN 'medium'
                   ELSE 'large'
               END) AS cluster_id
    FROM users
    WHERE last_active_date >= CURRENT_DATE - INTERVAL '30 days'
),
cluster_assignment AS (
    SELECT 
        cluster_id,
        -- Randomly assign clusters to treatment/control
        CASE WHEN RANDOM() < 0.5 THEN 'treatment' ELSE 'control' END AS assignment
    FROM (SELECT DISTINCT cluster_id FROM industry_clusters) clusters
)
SELECT ic.user_id, ic.cluster_id, ca.assignment
FROM industry_clusters ic
JOIN cluster_assignment ca ON ic.cluster_id = ca.cluster_id;
```

**Step 3: Define Metrics with Interference Awareness**

**Primary Metrics:**

| Metric | Definition | Network Consideration |
|--------|------------|----------------------|
| Endorsements given | Endorsements from treatment users | Direct effect |
| Endorsement received | Endorsements TO treatment users | May include control-to-treatment |
| Profile completeness | Skills added after endorsement | Second-order effect |

**Interference Metrics:**

| Metric | Purpose |
|--------|---------|
| Cross-group endorsement rate | Measure treatment → control spillover |
| Within-cluster endorsement % | Validate cluster isolation |
| Connection overlap | Check independence of clusters |

**Step 4: Statistical Methodology**

Given network effects, standard t-tests are invalid. Use:

**1. Cluster-robust standard errors:**
```python
import statsmodels.api as sm

# Fit model with cluster-robust SEs
model = sm.OLS(y, X).fit(cov_type='cluster', 
                          cov_kwds={'groups': cluster_id})
```

**2. Interference-adjusted estimator:**

The true Average Treatment Effect (ATE) needs to account for:
- Direct effect: Impact on treated users
- Spillover effect: Impact on control users from treated connections

```
ATE_adjusted = ATE_naive + Spillover_correction

Where:
Spillover_correction = β * (avg_treated_connections_control - 
                            avg_treated_connections_treatment)
```

**Step 5: Power Analysis with Clustering**

Standard power analysis underestimates required sample size:

```python
import numpy as np

def cluster_power_analysis(
    effect_size=0.05,    # 5% lift in endorsements
    baseline_rate=0.10,  # 10% weekly endorsement rate
    icc=0.02,            # Intra-cluster correlation
    cluster_size=100,    # Users per cluster
    alpha=0.05,
    power=0.80
):
    """
    Calculate clusters needed accounting for clustering effect
    """
    # Design effect for clustered design
    design_effect = 1 + (cluster_size - 1) * icc
    
    # Standard sample size
    z_alpha = 1.96
    z_beta = 0.84
    p1 = baseline_rate
    p2 = baseline_rate * (1 + effect_size)
    
    n_standard = (
        2 * ((z_alpha + z_beta) ** 2) * 
        (p1 * (1-p1) + p2 * (1-p2)) / 
        ((p2 - p1) ** 2)
    )
    
    # Adjusted for clustering
    n_adjusted = n_standard * design_effect
    
    # Number of clusters needed
    clusters_needed = np.ceil(n_adjusted / cluster_size)
    
    return int(clusters_needed * 2)  # Total clusters (treatment + control)

# Example: Need ~200 clusters for 80% power
print(cluster_power_analysis())
```

**Step 6: Analysis Plan**

**Primary Analysis:**
```sql
-- Compare endorsement rates by assignment
WITH user_metrics AS (
    SELECT 
        u.user_id,
        u.cluster_id,
        u.assignment,
        COUNT(e.endorsement_id) AS endorsements_given,
        SUM(CASE WHEN e.recipient_assignment = 'control' THEN 1 ELSE 0 END) 
            AS cross_group_endorsements
    FROM users u
    LEFT JOIN endorsements e ON u.user_id = e.giver_id
        AND e.created_at BETWEEN experiment_start AND experiment_end
    GROUP BY 1, 2, 3
)
SELECT 
    assignment,
    COUNT(*) AS users,
    AVG(endorsements_given) AS avg_endorsements,
    STDDEV(endorsements_given) AS std_endorsements,
    AVG(cross_group_endorsements) AS avg_spillover
FROM user_metrics
GROUP BY 1;
```

**Interference Check:**
```sql
-- Check if control users with treated connections behave differently
SELECT 
    CASE 
        WHEN treated_connections_pct > 0.5 THEN 'High exposure'
        WHEN treated_connections_pct > 0.2 THEN 'Medium exposure'
        ELSE 'Low exposure'
    END AS exposure_level,
    AVG(endorsements_received) AS avg_endorsements_received
FROM (
    SELECT 
        u.user_id,
        COUNT(c.connection_id) FILTER (WHERE c.assignment = 'treatment') * 1.0 / 
            NULLIF(COUNT(c.connection_id), 0) AS treated_connections_pct,
        COUNT(e.endorsement_id) AS endorsements_received
    FROM users u
    LEFT JOIN connections c ON u.user_id = c.user_id
    LEFT JOIN endorsements e ON u.user_id = e.recipient_id
    WHERE u.assignment = 'control'
    GROUP BY 1
) control_exposure
GROUP BY 1;
```

**Step 7: Decision Framework**

| Scenario | Result | Decision |
|----------|--------|----------|
| +10% endorsements, <5% spillover | Strong direct effect | Ship feature |
| +5% endorsements, >15% spillover | Network effect dominant | Consider full rollout (A/B may underestimate) |
| <3% endorsements, any spillover | Weak effect | Iterate on feature |
| Negative engagement signals | Harmful | Do not ship |

</div>
</details>

---

### Problem 5: Business Strategy & Metrics (Advanced)

<div class="card">
  <h4>📋 Problem Statement</h4>
  <p><strong>Question:</strong> Airbnb has seen a decline in bookings in European markets over the past quarter. The CEO asks: "Should we lower our service fees to be more competitive, or invest in improving the guest experience?" How would you structure this analysis?</p>
</div>

<details>
<summary><strong>🔍 Step-by-Step Solution</strong></summary>

<div class="solution-steps">

**Step 1: Structure the Problem**

This is a resource allocation decision with two competing hypotheses:
- **H1 (Price):** Bookings declined because we're too expensive vs. competitors
- **H2 (Experience):** Bookings declined because guest satisfaction is lower

**Framework: Decision Tree Analysis**

```
European Booking Decline
├── External Factors
│   ├── Economic conditions (recession, inflation)
│   ├── Regulatory changes (short-term rental laws)
│   ├── Competitor actions (Booking.com, VRBO)
│   └── Seasonality shifts
│
└── Internal Factors
    ├── Price Competitiveness
    │   ├── Service fee comparison
    │   ├── Total price vs. alternatives
    │   └── Price elasticity in market
    │
    └── Experience Quality
        ├── Search/discovery friction
        ├── Listing quality issues
        ├── Review sentiment trends
        └── Post-booking satisfaction
```

**Step 2: Gather Evidence for Each Hypothesis**

**Price Analysis:**

```sql
-- Compare our pricing to competitor data (if available)
WITH booking_analysis AS (
    SELECT 
        market,
        AVG(total_price) AS avg_airbnb_price,
        AVG(service_fee_rate) AS avg_fee_rate,
        AVG(competitor_price) AS avg_competitor_price,  -- from market research
        COUNT(*) AS bookings,
        LAG(COUNT(*)) OVER (PARTITION BY market ORDER BY quarter) AS prev_bookings
    FROM european_bookings
    WHERE booking_date >= '2024-01-01'
    GROUP BY market, quarter
)
SELECT 
    market,
    avg_airbnb_price,
    avg_competitor_price,
    (avg_airbnb_price - avg_competitor_price) / avg_competitor_price AS price_premium,
    (bookings - prev_bookings) * 1.0 / prev_bookings AS booking_change
FROM booking_analysis
ORDER BY booking_change ASC;

-- Price elasticity estimation
SELECT 
    market,
    CORR(price_percentile, conversion_rate) AS price_sensitivity,
    CORR(fee_rate, conversion_rate) AS fee_sensitivity
FROM search_sessions
WHERE region = 'Europe'
GROUP BY market;
```

**Experience Analysis:**

```sql
-- Review sentiment trends
SELECT 
    DATE_TRUNC('month', review_date) AS month,
    AVG(overall_rating) AS avg_rating,
    AVG(cleanliness_score) AS cleanliness,
    AVG(communication_score) AS communication,
    AVG(value_score) AS perceived_value,
    COUNT(*) AS review_count
FROM reviews
WHERE market_region = 'Europe'
GROUP BY 1
ORDER BY 1 DESC;

-- Support ticket analysis
SELECT 
    issue_category,
    COUNT(*) AS tickets,
    AVG(resolution_satisfaction) AS satisfaction
FROM support_tickets
WHERE market_region = 'Europe'
    AND created_date >= CURRENT_DATE - INTERVAL '6 months'
GROUP BY 1
ORDER BY tickets DESC;
```

**Step 3: Build the Business Case Model**

**Option A: Lower Service Fees**

```python
# Financial model for fee reduction
current_fee_rate = 0.14  # 14% service fee
proposed_fee_rate = 0.12  # 12% service fee

current_european_gmv = 2_000_000_000  # $2B
current_european_bookings = 5_000_000

# Assumptions (based on elasticity analysis)
price_elasticity = -1.2  # 1% price drop → 1.2% booking increase

fee_reduction_pct = (proposed_fee_rate - current_fee_rate) / current_fee_rate
total_price_impact = fee_reduction_pct * (current_fee_rate / 0.25)  # fee is ~25% of experience

expected_booking_lift = -price_elasticity * total_price_impact
new_bookings = current_european_bookings * (1 + expected_booking_lift)

# Revenue impact
current_fee_revenue = current_european_gmv * current_fee_rate
new_fee_revenue = (current_european_gmv * (1 + expected_booking_lift)) * proposed_fee_rate

revenue_change = new_fee_revenue - current_fee_revenue
print(f"Revenue change: ${revenue_change:,.0f}")  # Example: -$50M in year 1
```

**Option B: Invest in Guest Experience**

```python
# ROI model for experience investment
investment = 50_000_000  # $50M investment

# Experience improvements
initiatives = {
    'listing_quality_program': {
        'cost': 15_000_000,
        'expected_rating_lift': 0.1,  # +0.1 stars average
        'conversion_impact': 0.03    # 3% more bookings from search
    },
    'enhanced_support': {
        'cost': 20_000_000,
        'expected_nps_lift': 5,
        'rebooking_impact': 0.05     # 5% more repeat bookings
    },
    'search_improvement': {
        'cost': 15_000_000,
        'expected_conversion_lift': 0.04  # 4% more search-to-book
    }
}

# Combined impact estimate
total_booking_lift = 1.03 * 1.05 * 1.04 - 1  # ~12% booking increase
new_bookings = current_european_bookings * (1 + total_booking_lift)
new_revenue = new_bookings * avg_booking_value * current_fee_rate

roi = (new_revenue - current_fee_revenue - investment) / investment
print(f"3-year ROI: {roi:.1%}")
```

**Step 4: Comparative Analysis**

| Factor | Lower Fees | Invest in Experience |
|--------|------------|---------------------|
| **Year 1 Impact** | Immediate | 6-12 months lag |
| **Revenue Risk** | High (fee loss certain, volume uncertain) | Medium (investment, uncertain returns) |
| **Competitive Moat** | Low (easily matched) | High (hard to replicate) |
| **Customer LTV** | Neutral | Positive (better retention) |
| **Brand Impact** | May signal desperation | Signals quality focus |
| **Reversibility** | Hard to raise fees later | Can adjust investment |

**Step 5: Recommendation Framework**

**Decision Matrix:**

| Scenario | Evidence Profile | Recommendation |
|----------|-----------------|----------------|
| Price is 20%+ higher, elasticity > 1.5 | Strong price sensitivity | Fee reduction |
| Ratings declining, NPS dropping | Experience is root cause | Experience investment |
| Both factors present | Mixed evidence | Hybrid: modest fee cut + targeted experience investment |
| External factors dominant | Neither is root cause | Wait and monitor |

**Step 6: Structured Recommendation**

> **Recommendation:** Invest in guest experience with targeted fee adjustments
>
> **Rationale:**
> 1. Analysis shows guest ratings declined 0.2 points while competitor prices remained stable
> 2. "Value" rating dropped more than other dimensions, suggesting experience gap
> 3. Fee reduction would cost ~$100M annually with uncertain volume lift
> 4. Experience investment has higher long-term ROI and creates competitive moat
>
> **Proposed Action:**
> - Invest $50M in listing quality and guest support
> - Implement targeted fee discounts (5%) only in most price-sensitive markets
> - Monitor monthly: booking volume, review scores, conversion rates
> - Re-evaluate in 6 months

</div>
</details>

---

## 🧠 Quick Reference: Common Product Sense Questions

<div class="section">
  <div class="card">
    <h3>Question Types and Approaches</h3>
    
    <h4>Type 1: "How would you measure success for X feature?"</h4>
    <ul>
      <li>Define the goal of the feature</li>
      <li>Identify North Star metric</li>
      <li>Build metrics hierarchy (input → output → outcome)</li>
      <li>Include counter-metrics</li>
      <li>Set success criteria with thresholds</li>
    </ul>
    
    <h4>Type 2: "Metric X went up/down. Why?"</h4>
    <ul>
      <li>Confirm the change is real (data quality, significance)</li>
      <li>Segment by key dimensions</li>
      <li>Check for external events</li>
      <li>Analyze the funnel</li>
      <li>Generate and test hypotheses</li>
    </ul>
    
    <h4>Type 3: "Should we launch feature X?"</h4>
    <ul>
      <li>Clarify the goal and user need</li>
      <li>Define success metrics</li>
      <li>Identify trade-offs and risks</li>
      <li>Design experiment approach</li>
      <li>Set decision criteria</li>
    </ul>
    
    <h4>Type 4: "How would you improve product X?"</h4>
    <ul>
      <li>Understand current state and goals</li>
      <li>Identify user segments and pain points</li>
      <li>Brainstorm solutions</li>
      <li>Prioritize by impact vs. effort</li>
      <li>Recommend with measurement plan</li>
    </ul>
  </div>
</div>

---

## 📝 Practice Exercises

### Exercise 1: Define a North Star Metric

<div class="card">
  <p><strong>Task:</strong> For each product, define an appropriate North Star metric and explain why.</p>
  
  <ol>
    <li>Duolingo (language learning app)</li>
    <li>Uber Eats (food delivery)</li>
    <li>Slack (workplace communication)</li>
    <li>Robinhood (stock trading app)</li>
    <li>Peloton (fitness equipment + content)</li>
  </ol>
</div>

<details>
<summary><strong>Sample Answers</strong></summary>

| Product | North Star Metric | Rationale |
|---------|------------------|-----------|
| **Duolingo** | Daily Active Learners who complete a lesson | Captures engagement + learning progress |
| **Uber Eats** | Orders delivered within expected time | Combines reliability + volume |
| **Slack** | Daily Active Users who send 5+ messages | Active communication, not passive browsing |
| **Robinhood** | Monthly Active Traders | Trading activity = core value + revenue |
| **Peloton** | Monthly workouts per subscriber | Hardware + content usage = retention |

</details>

---

### Exercise 2: Metrics Trade-off Analysis

<div class="card">
  <p><strong>Scenario:</strong> Netflix is considering auto-playing trailers more aggressively on the home screen. What metrics might conflict?</p>
  
  <p>List 3-5 potential trade-offs and how you'd balance them.</p>
</div>

<details>
<summary><strong>Sample Answer</strong></summary>

| Metric A (May Increase) | Metric B (May Decrease) | Trade-off |
|------------------------|------------------------|-----------|
| Content discovery rate | User satisfaction score | Aggressive auto-play may annoy users |
| Watch time | Session starts | Users may watch fewer, longer sessions |
| New title sampling | Returning viewer rate | May frustrate users looking for specific content |
| Engagement (short-term) | Subscription retention (long-term) | Short-term gains may hurt loyalty |

**Balancing Approach:**
1. A/B test different aggressiveness levels
2. Segment by user type (explorers vs. goal-oriented)
3. Monitor long-term retention alongside short-term engagement
4. Provide user control (settings to disable)

</details>

---

### Exercise 3: Root Cause Diagnosis

<div class="card">
  <p><strong>Scenario:</strong> Twitter sees a 15% drop in tweets per day but DAU remains stable. What could explain this?</p>
  
  <p>List 5 hypotheses and how you'd validate each.</p>
</div>

<details>
<summary><strong>Sample Answer</strong></summary>

| Hypothesis | Validation Approach |
|------------|-------------------|
| **Shift to consumption** | Check ratio of tweets/retweets, time on feed vs. compose |
| **Content moderation increase** | Check rejected/filtered tweet rate |
| **Bot cleanup** | Segment by account age, activity patterns |
| **UI change made tweeting harder** | Check funnel: compose open → tweet sent |
| **Shift to other features** | Check DM volume, Spaces participation |
| **Power user drop** | Segment tweets by user percentile, check if top 10% dropped |

**Investigation Priority:** Start with UI funnel analysis (quickest), then user segmentation, then feature-level analysis.

</details>

</div>

<div class="navigation-buttons">
  <a href="{{ '/interview-preparation/analytical-execution/' | relative_url }}">Previous: Analytical Execution</a>
  <a href="{{ '/interview-preparation/behavioral-interview/' | relative_url }}">Next: Behavioral Interview</a>
</div>

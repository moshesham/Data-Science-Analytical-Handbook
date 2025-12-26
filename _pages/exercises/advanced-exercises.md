---
layout: page
title: "Advanced Exercises"
permalink: /exercises/advanced/
nav_order: 3
parent: "Exercises"
difficulty: "Advanced"
estimated_time: "4-6 hours"
tags: [Exercises, Practice, Advanced, Step-by-Step, Senior, Staff]
track: "Advanced Analytics & ML Prep"
---

# Advanced Exercises: Step-by-Step Problem Solving

These exercises simulate real-world complexity encountered at senior levels. Each problem requires synthesizing multiple concepts and making judgment calls.

---

## 📊 Advanced Statistics & Experimentation

### Exercise S7: Difference-in-Differences Analysis

**Scenario:** A ride-sharing company wants to measure the impact of a new driver bonus program. They can't run a clean A/B test because the program was rolled out to specific cities.

**Data:**
| City | Period | Type | Avg Rides/Driver |
|------|--------|------|------------------|
| Seattle | Before (Jan) | Treatment | 45 |
| Seattle | After (Feb) | Treatment | 58 |
| Portland | Before (Jan) | Control | 42 |
| Portland | After (Feb) | Control | 48 |

**Question:** Use Difference-in-Differences (DiD) to estimate the causal effect of the bonus program.

<details>
<summary>💡 Hint</summary>
DiD = (Treatment After - Treatment Before) - (Control After - Control Before)
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Understand the DiD Framework**

DiD controls for:
- Pre-existing differences between groups (Seattle vs Portland)
- Time trends affecting both groups (seasonal changes)

**Key Assumption:** Parallel trends - without treatment, both groups would have changed by the same amount.

**Step 2: Calculate Changes**
```
Seattle (Treatment):
  Change = 58 - 45 = +13 rides

Portland (Control):
  Change = 48 - 42 = +6 rides
```

**Step 3: Calculate Difference-in-Differences**
```
DiD Effect = Treatment Change - Control Change
DiD Effect = 13 - 6 = +7 rides per driver
```

**Step 4: Interpret the Result**

The bonus program is estimated to cause an increase of **7 additional rides per driver** beyond what would have happened naturally.

**Step 5: Validate the Parallel Trends Assumption**

Before trusting DiD, verify that trends were parallel before intervention:

```sql
-- Check historical trends
SELECT 
    city,
    month,
    avg_rides,
    avg_rides - LAG(avg_rides) OVER (
        PARTITION BY city ORDER BY month
    ) AS monthly_change
FROM historical_data
WHERE month < '2024-02-01'
ORDER BY city, month;
```

If Seattle was already growing faster than Portland before the bonus, DiD estimate is biased.

**Step 6: Statistical Significance (Regression Approach)**

For proper inference, run regression:
```
rides = β₀ + β₁(treatment) + β₂(after) + β₃(treatment × after) + ε
```

Where β₃ is the DiD estimator.

```python
import pandas as pd
import statsmodels.formula.api as smf

# Create dataset
data = pd.DataFrame({
    'city': ['Seattle', 'Seattle', 'Portland', 'Portland'],
    'period': ['before', 'after', 'before', 'after'],
    'treatment': [1, 1, 0, 0],
    'after': [0, 1, 0, 1],
    'rides': [45, 58, 42, 48]
})

# DiD regression
model = smf.ols('rides ~ treatment + after + treatment:after', data=data)
results = model.fit()
print(results.summary())

# The coefficient on treatment:after is the DiD estimate
```

**Answer:** The estimated treatment effect is +7 rides per driver. This represents the causal impact of the bonus program, controlling for time trends and city-level differences.

**Key Takeaways:**
1. DiD requires parallel trends assumption
2. Always check pre-treatment trends
3. Use regression for confidence intervals and p-values
4. Consider other confounders (e.g., different marketing campaigns)
</details>

---

### Exercise S8: Multi-Armed Bandit vs A/B Test Decision

**Scenario:** You're launching 4 different checkout flows. You have 2 options:
1. Run a traditional A/B/C/D test for 4 weeks
2. Use an epsilon-greedy multi-armed bandit

**Context:**
- 10,000 visitors per week
- Current conversion rate: 3%
- Expected best variant: ~3.5% conversion
- Revenue per conversion: $50

**Question:** Analyze the tradeoffs and recommend an approach.

<details>
<summary>💡 Hint</summary>
Consider regret, learning time, and when you need statistical rigor.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Define Evaluation Criteria**
```
1. Statistical rigor: Can we trust the results?
2. Regret: Revenue lost while exploring
3. Time to decision: When do we get actionable insights?
4. Complexity: Implementation and monitoring burden
```

**Step 2: Analyze A/B/C/D Test**

Equal traffic split (25% each):
```
Weekly visitors per variant: 2,500
Expected conversions at 3%: 75 per variant
Total 4-week sample: 10,000 per variant

Power calculation:
- Baseline: 3%, Expected improvement: 0.5% (to 3.5%)
- With 10,000 per variant, power ≈ 80% for detecting 0.5% difference
```

Regret calculation:
```
Assume best variant is 3.5%, others average 3.0%
Traffic to suboptimal variants: 75% of total
Weekly suboptimal conversions: 7,500 × 3.0% = 225
Weekly optimal conversions missed: 7,500 × 0.5% = 37.5
Weekly regret: 37.5 × $50 = $1,875
4-week regret: $7,500
```

**Step 3: Analyze Multi-Armed Bandit (ε-greedy, ε=0.1)**

Initially (exploration heavy):
- Week 1-2: ~40% to best, ~20% each to others (learning)
- Week 3-4: ~70% to best, ~10% each to others

Approximate regret:
```
More traffic flows to winner as it learns
Estimated total regret: ~$4,500 (better than A/B)
BUT: Less certainty in final result
```

**Step 4: Key Tradeoffs**

| Factor | A/B/C/D Test | Multi-Armed Bandit |
|--------|--------------|-------------------|
| Statistical rigor | High (p-values, CI) | Lower (estimates shift) |
| Regret | Higher (~$7,500) | Lower (~$4,500) |
| Time to decision | Fixed (4 weeks) | Continuous adaptation |
| Winner clarity | Clear at end | Can be ambiguous |
| Seasonality handling | Balanced by design | Can be fooled |
| Stakeholder trust | High (established) | May need education |

**Step 5: Decision Framework**

**Choose A/B Test when:**
- You need statistical proof (regulatory, high stakes)
- Results will inform long-term strategy
- Variants might have different performance over time (novelty effects)
- Stakeholders require p-values

**Choose Bandit when:**
- Minimizing regret is primary goal
- You have many variants (>4)
- Decision is reversible/low stakes
- You can accept "probably best" vs "statistically proven best"

**Step 6: Recommendation**

For checkout flow (high revenue impact, customer trust):

**Recommend: A/B/C/D Test** with these modifications:
1. Use sequential testing (group sequential design) to stop early if clear winner
2. Add guardrail metrics (cart abandonment, returns)
3. Run for 4 weeks but analyze weekly for early signals
4. Consider 40/20/20/20 split if you have a hypothesis about best variant

**Alternative hybrid approach:**
- Week 1-2: Bandit to quickly eliminate obvious losers
- Week 3-4: Equal split A/B between top 2 for statistical confirmation

**Key Takeaways:**
1. No universally "better" approach - context matters
2. Bandits minimize regret, A/B tests maximize certainty
3. Consider hybrid approaches for best of both worlds
4. Stakeholder expectations matter as much as statistics
</details>

---

### Exercise S9: Network Effects in Experiments

**Scenario:** You want to test a new "share with friends" feature on a social app. Users in the treatment group can share content, and their friends (who might be in control) will see those shares.

**Problem:** This violates the SUTVA (Stable Unit Treatment Value Assumption) - the control group is affected by treatment.

**Question:** How would you design this experiment to get valid causal estimates?

<details>
<summary>💡 Hint</summary>
Consider cluster randomization, ego-network randomization, or switchback designs.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Understand the Interference Problem**

```
Standard A/B test assumes:
- Treatment only affects treated users
- Control users are unaffected by treatment

With sharing feature:
- Control users see shared content from treatment friends
- Treatment effect "leaks" into control group
- Measured effect is biased downward (spillover)
```

**Step 2: Quantify Potential Bias**

If 30% of control users have treatment friends who share:
```
True treatment effect: +10% engagement
Spillover to control: +3% engagement (30% × partial exposure)
Measured effect: 10% - 3% = 7% (biased low)
```

**Step 3: Solution Options**

**Option A: Geographic Cluster Randomization**
```
Randomize at city/region level, not user level

Pros:
- Eliminates cross-group contamination within clusters
- Simple to implement

Cons:
- Fewer randomization units (lower power)
- Geographic differences are confounders
- Need many clusters (30+ recommended)
```

**Option B: Ego-Network Randomization**
```
Treat user AND their entire friend network together

Pros:
- Captures network effects
- Can measure direct + spillover effects

Cons:
- Complex assignment
- Some users in multiple networks (overlap)
- Reduced sample size
```

**Option C: Graph Cluster Randomization**
```
Use graph clustering algorithms to find disconnected communities
Randomize entire communities

Pros:
- Minimizes cross-cluster connections
- Natural randomization units

Cons:
- Perfectly isolated communities are rare
- Clusters may be different sizes
```

**Option D: Switchback Design**
```
Randomize over TIME instead of users
All users see treatment in period A, control in period B

Pros:
- Every user experiences both conditions
- No cross-user contamination

Cons:
- Carryover effects between periods
- Time-based confounders
- Feature must be reversible
```

**Step 4: Recommended Design**

For social sharing feature, use **Two-Stage Randomization**:

```
Stage 1: Cluster users into communities (Louvain algorithm)
Stage 2: Within some clusters, randomize individual users

This allows measurement of:
- Direct effect (treated vs control within treatment clusters)
- Spillover effect (control in treatment clusters vs pure control clusters)
- Total effect (treatment cluster avg vs control cluster avg)
```

**Implementation:**
```python
# Pseudo-code for two-stage design
import networkx as nx
from community import community_louvain

# Build friend network graph
G = nx.from_pandas_edgelist(friendships, 'user_a', 'user_b')

# Detect communities
communities = community_louvain.best_partition(G)

# Stage 1: Randomize clusters
cluster_ids = list(set(communities.values()))
treatment_clusters = random.sample(cluster_ids, len(cluster_ids) // 2)

# Stage 2: Within treatment clusters, randomize users
for user, cluster in communities.items():
    if cluster in treatment_clusters:
        user_treatment = random.random() < 0.5  # 50/50 within cluster
    else:
        user_treatment = False  # All control in control clusters
```

**Step 5: Analysis Framework**

```sql
-- Measure multiple effects
WITH user_conditions AS (
    SELECT 
        user_id,
        cluster_type,  -- 'treatment_cluster' or 'control_cluster'
        individual_treatment,  -- true/false
        engagement_metric
    FROM experiment_data
)
SELECT 
    cluster_type,
    individual_treatment,
    AVG(engagement_metric) AS avg_engagement,
    COUNT(*) AS n
FROM user_conditions
GROUP BY cluster_type, individual_treatment;
```

**Results interpretation:**
| Cluster Type | Individual Tx | Avg Engagement | Interpretation |
|--------------|---------------|----------------|----------------|
| Treatment | True | 10.5 | Direct treatment effect |
| Treatment | False | 8.2 | Spillover effect |
| Control | False | 7.5 | Pure baseline |

```
Direct Effect = 10.5 - 8.2 = 2.3
Spillover Effect = 8.2 - 7.5 = 0.7
Total Effect = 10.5 - 7.5 = 3.0
```

**Key Takeaways:**
1. Standard A/B tests fail with network effects
2. Cluster randomization reduces interference
3. Two-stage designs can measure both direct and spillover effects
4. Graph algorithms help identify natural clusters
5. Always consider: is the "spillover" actually part of the intended effect?
</details>

---

## 💻 Advanced SQL Exercises

### Exercise Q7: Sessionization Without Session IDs

**Schema:**
```sql
CREATE TABLE user_events (
    event_id SERIAL PRIMARY KEY,
    user_id INTEGER,
    event_type VARCHAR(50),
    event_time TIMESTAMP
);
```

**Question:** Group events into sessions where a session ends after 30 minutes of inactivity. Calculate session length and events per session.

<details>
<summary>💡 Hint</summary>
Use LAG to find time gaps, then SUM with CASE to create session boundaries.
</details>

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Find Time Since Previous Event**
```sql
WITH event_gaps AS (
    SELECT 
        event_id,
        user_id,
        event_type,
        event_time,
        LAG(event_time) OVER (
            PARTITION BY user_id 
            ORDER BY event_time
        ) AS prev_event_time,
        EXTRACT(EPOCH FROM (
            event_time - LAG(event_time) OVER (
                PARTITION BY user_id 
                ORDER BY event_time
            )
        )) / 60.0 AS minutes_since_last
    FROM user_events
)
SELECT * FROM event_gaps ORDER BY user_id, event_time;
```

**Step 2: Flag Session Starts**
```sql
WITH event_gaps AS (
    SELECT 
        event_id,
        user_id,
        event_type,
        event_time,
        EXTRACT(EPOCH FROM (
            event_time - LAG(event_time) OVER (
                PARTITION BY user_id 
                ORDER BY event_time
            )
        )) / 60.0 AS minutes_since_last
    FROM user_events
),
session_flags AS (
    SELECT 
        *,
        CASE 
            WHEN minutes_since_last IS NULL THEN 1  -- First event
            WHEN minutes_since_last > 30 THEN 1     -- Gap > 30 min
            ELSE 0 
        END AS is_session_start
    FROM event_gaps
)
SELECT * FROM session_flags ORDER BY user_id, event_time;
```

**Step 3: Create Session IDs Using Cumulative Sum**
```sql
WITH event_gaps AS (
    SELECT 
        event_id,
        user_id,
        event_type,
        event_time,
        EXTRACT(EPOCH FROM (
            event_time - LAG(event_time) OVER (
                PARTITION BY user_id 
                ORDER BY event_time
            )
        )) / 60.0 AS minutes_since_last
    FROM user_events
),
session_flags AS (
    SELECT 
        *,
        CASE 
            WHEN minutes_since_last IS NULL THEN 1
            WHEN minutes_since_last > 30 THEN 1
            ELSE 0 
        END AS is_session_start
    FROM event_gaps
),
sessionized AS (
    SELECT 
        *,
        SUM(is_session_start) OVER (
            PARTITION BY user_id 
            ORDER BY event_time
        ) AS session_num
    FROM session_flags
)
SELECT * FROM sessionized ORDER BY user_id, event_time;
```

**Step 4: Calculate Session Metrics**
```sql
WITH event_gaps AS (
    SELECT 
        event_id,
        user_id,
        event_type,
        event_time,
        EXTRACT(EPOCH FROM (
            event_time - LAG(event_time) OVER (
                PARTITION BY user_id 
                ORDER BY event_time
            )
        )) / 60.0 AS minutes_since_last
    FROM user_events
),
session_flags AS (
    SELECT 
        *,
        CASE 
            WHEN minutes_since_last IS NULL THEN 1
            WHEN minutes_since_last > 30 THEN 1
            ELSE 0 
        END AS is_session_start
    FROM event_gaps
),
sessionized AS (
    SELECT 
        *,
        SUM(is_session_start) OVER (
            PARTITION BY user_id 
            ORDER BY event_time
        ) AS session_num
    FROM session_flags
)
SELECT 
    user_id,
    session_num,
    MIN(event_time) AS session_start,
    MAX(event_time) AS session_end,
    EXTRACT(EPOCH FROM (MAX(event_time) - MIN(event_time))) / 60.0 AS session_duration_min,
    COUNT(*) AS events_in_session,
    ARRAY_AGG(event_type ORDER BY event_time) AS event_sequence
FROM sessionized
GROUP BY user_id, session_num
ORDER BY user_id, session_num;
```

**Sample Output:**
| user_id | session_num | session_start | session_end | session_duration_min | events_in_session | event_sequence |
|---------|-------------|---------------|-------------|---------------------|-------------------|----------------|
| 101 | 1 | 2024-01-01 09:00:00 | 2024-01-01 09:25:00 | 25.0 | 8 | {page_view,click,...} |
| 101 | 2 | 2024-01-01 14:30:00 | 2024-01-01 15:10:00 | 40.0 | 12 | {page_view,...} |

**Key Takeaway:** The cumulative sum of session_start flags creates incrementing session IDs.
</details>

---

### Exercise Q8: Efficient Deduplication with Window Functions

**Problem:** A large events table has duplicate rows. Find and keep only the most recent version of each event.

**Schema:**
```sql
CREATE TABLE raw_events (
    event_id VARCHAR(50),      -- Business key (not unique!)
    user_id INTEGER,
    event_data JSONB,
    created_at TIMESTAMP,
    updated_at TIMESTAMP       -- When this row was inserted/updated
);
```

**Question:** Write an efficient query to get the latest version of each event. Then write a DELETE statement to remove duplicates.

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Identify Duplicates**
```sql
SELECT 
    event_id,
    COUNT(*) AS duplicate_count
FROM raw_events
GROUP BY event_id
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
```

**Step 2: Use ROW_NUMBER to Rank Versions**
```sql
WITH ranked_events AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY event_id 
            ORDER BY updated_at DESC
        ) AS rn
    FROM raw_events
)
SELECT *
FROM ranked_events
WHERE rn = 1;  -- Keep only the latest version
```

**Step 3: Efficient DELETE Using ctid (PostgreSQL specific)**
```sql
-- First, identify rows to DELETE (not the latest)
WITH ranked_events AS (
    SELECT 
        ctid,  -- PostgreSQL physical row identifier
        event_id,
        updated_at,
        ROW_NUMBER() OVER (
            PARTITION BY event_id 
            ORDER BY updated_at DESC
        ) AS rn
    FROM raw_events
)
DELETE FROM raw_events
WHERE ctid IN (
    SELECT ctid 
    FROM ranked_events 
    WHERE rn > 1
);
```

**Step 4: Alternative Using Self-Join (Works on all DBs)**
```sql
DELETE FROM raw_events r1
USING raw_events r2
WHERE r1.event_id = r2.event_id
  AND r1.updated_at < r2.updated_at;
```

**Step 5: For Very Large Tables, Batch the Delete**
```sql
-- Delete in batches to avoid lock contention
DO $$
DECLARE
    batch_size INT := 10000;
    deleted_count INT;
BEGIN
    LOOP
        WITH to_delete AS (
            SELECT ctid
            FROM (
                SELECT 
                    ctid,
                    ROW_NUMBER() OVER (
                        PARTITION BY event_id 
                        ORDER BY updated_at DESC
                    ) AS rn
                FROM raw_events
            ) ranked
            WHERE rn > 1
            LIMIT batch_size
        )
        DELETE FROM raw_events
        WHERE ctid IN (SELECT ctid FROM to_delete);
        
        GET DIAGNOSTICS deleted_count = ROW_COUNT;
        
        IF deleted_count = 0 THEN
            EXIT;
        END IF;
        
        COMMIT;
        RAISE NOTICE 'Deleted % rows', deleted_count;
    END LOOP;
END $$;
```

**Step 6: Prevent Future Duplicates**
```sql
-- Add unique constraint (after dedup)
ALTER TABLE raw_events 
ADD CONSTRAINT unique_event_id UNIQUE (event_id);

-- Or create unique index for partial uniqueness
CREATE UNIQUE INDEX unique_latest_event 
ON raw_events (event_id, updated_at);
```

**Key Takeaway:** ROW_NUMBER is the standard pattern for deduplication. For large tables, batch deletes prevent lock issues.
</details>

---

### Exercise Q9: Recursive CTEs for Hierarchical Data

**Schema:**
```sql
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    manager_id INTEGER REFERENCES employees(employee_id),
    department VARCHAR(50),
    salary INTEGER
);
```

**Question:** 
1. Build the complete org chart showing each employee's level and full management chain
2. Calculate total salary cost under each manager (including all reports, recursively)

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Basic Recursive CTE Structure**
```sql
WITH RECURSIVE org_tree AS (
    -- Base case: Start with top-level managers (no manager)
    SELECT 
        employee_id,
        name,
        manager_id,
        department,
        salary,
        1 AS level,
        ARRAY[name] AS management_chain,
        ARRAY[employee_id] AS id_chain
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive case: Join employees to their managers
    SELECT 
        e.employee_id,
        e.name,
        e.manager_id,
        e.department,
        e.salary,
        ot.level + 1 AS level,
        ot.management_chain || e.name,
        ot.id_chain || e.employee_id
    FROM employees e
    JOIN org_tree ot ON e.manager_id = ot.employee_id
)
SELECT 
    employee_id,
    name,
    level,
    REPEAT('  ', level - 1) || name AS indented_name,
    ARRAY_TO_STRING(management_chain, ' → ') AS full_chain
FROM org_tree
ORDER BY id_chain;
```

**Sample Output:**
| employee_id | name | level | indented_name | full_chain |
|-------------|------|-------|---------------|------------|
| 1 | CEO Jane | 1 | CEO Jane | CEO Jane |
| 2 | VP Sales | 2 |   VP Sales | CEO Jane → VP Sales |
| 5 | Sales Rep | 3 |     Sales Rep | CEO Jane → VP Sales → Sales Rep |

**Step 2: Calculate Total Salary Under Each Manager**
```sql
WITH RECURSIVE org_tree AS (
    SELECT 
        employee_id,
        name,
        manager_id,
        salary,
        employee_id AS root_manager_id  -- Track the ancestor
    FROM employees
    
    UNION ALL
    
    SELECT 
        e.employee_id,
        e.name,
        e.manager_id,
        e.salary,
        ot.root_manager_id
    FROM employees e
    JOIN org_tree ot ON e.manager_id = ot.employee_id
),
manager_totals AS (
    SELECT 
        root_manager_id AS manager_id,
        SUM(salary) AS total_team_salary,
        COUNT(*) AS team_size
    FROM org_tree
    GROUP BY root_manager_id
)
SELECT 
    e.employee_id,
    e.name,
    e.salary AS own_salary,
    mt.team_size,
    mt.total_team_salary,
    mt.total_team_salary - e.salary AS reports_salary
FROM employees e
JOIN manager_totals mt ON e.employee_id = mt.manager_id
ORDER BY mt.total_team_salary DESC;
```

**Step 3: Find All Reports (Direct and Indirect)**
```sql
WITH RECURSIVE all_reports AS (
    -- Direct reports
    SELECT 
        manager_id,
        employee_id AS report_id,
        name AS report_name,
        1 AS distance
    FROM employees
    WHERE manager_id IS NOT NULL
    
    UNION ALL
    
    -- Indirect reports
    SELECT 
        ar.manager_id,
        e.employee_id,
        e.name,
        ar.distance + 1
    FROM employees e
    JOIN all_reports ar ON e.manager_id = ar.report_id
)
SELECT 
    e.name AS manager_name,
    COUNT(*) AS total_reports,
    COUNT(*) FILTER (WHERE distance = 1) AS direct_reports,
    COUNT(*) FILTER (WHERE distance > 1) AS indirect_reports,
    ARRAY_AGG(report_name ORDER BY distance, report_name) AS all_report_names
FROM all_reports ar
JOIN employees e ON ar.manager_id = e.employee_id
GROUP BY e.employee_id, e.name
ORDER BY total_reports DESC;
```

**Step 4: Detect Cycles (Safety Check)**
```sql
WITH RECURSIVE org_tree AS (
    SELECT 
        employee_id,
        manager_id,
        ARRAY[employee_id] AS path,
        FALSE AS has_cycle
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    SELECT 
        e.employee_id,
        e.manager_id,
        ot.path || e.employee_id,
        e.employee_id = ANY(ot.path)  -- Cycle if already in path
    FROM employees e
    JOIN org_tree ot ON e.manager_id = ot.employee_id
    WHERE NOT ot.has_cycle  -- Stop if cycle detected
)
SELECT * FROM org_tree WHERE has_cycle;
```

**Key Takeaways:**
1. Recursive CTEs have base case + recursive case joined by UNION ALL
2. Track the path to detect cycles and build chains
3. For aggregations up the tree, track the root ancestor
4. Always include cycle detection for safety
</details>

---

## 🎯 System Design Exercises

### Exercise SD1: Design an Analytics Pipeline

**Scenario:** You're the lead data engineer for a social media app with:
- 100M daily active users
- 5 billion events per day (posts, likes, comments, views)
- Need real-time dashboards (< 5 min latency)
- Need daily aggregated reports
- Must support ad-hoc queries from data scientists

**Question:** Design the data architecture. Include data flow, storage choices, and tradeoffs.

<details>
<summary>✅ Step-by-Step Solution</summary>

**Step 1: Identify Requirements**

| Requirement | Constraint |
|-------------|------------|
| Ingestion rate | ~58,000 events/second |
| Latency (real-time) | < 5 minutes |
| Latency (batch) | Daily |
| Query patterns | Real-time dashboards + Ad-hoc analysis |
| Data retention | ? (assume 2 years) |

**Step 2: Design the Architecture**

```
                    ┌─────────────────────────────────────────────────┐
                    │                    SOURCES                       │
                    │  Mobile App / Web / Backend Services             │
                    └───────────────────────┬─────────────────────────┘
                                            │
                                            ▼
                    ┌─────────────────────────────────────────────────┐
                    │              STREAMING INGESTION                 │
                    │           Apache Kafka / AWS Kinesis             │
                    │    (Partitioned by user_id for ordering)         │
                    └───────────────────────┬─────────────────────────┘
                                            │
              ┌─────────────────────────────┼─────────────────────────┐
              │                             │                         │
              ▼                             ▼                         ▼
┌──────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐
│    REAL-TIME PATH    │    │    RAW DATA LAKE     │    │  STREAM PROCESSING   │
│                      │    │                      │    │                      │
│  Apache Flink/Spark  │    │   S3/GCS (Parquet)   │    │   Flink (Aggregates) │
│  Streaming           │    │   Partitioned by     │    │                      │
│                      │    │   date/event_type    │    │   → Pre-aggregated   │
│  → ClickHouse/Druid  │    │                      │    │     metrics to       │
│    (OLAP for dash)   │    │   (Retain 2 years)   │    │     TimescaleDB      │
└──────────────────────┘    └──────────────────────┘    └──────────────────────┘
              │                             │                         │
              │                             │                         │
              ▼                             ▼                         ▼
┌──────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐
│   REAL-TIME DASH     │    │     BATCH ETL        │    │  REAL-TIME METRICS   │
│                      │    │                      │    │                      │
│  Grafana/Superset    │    │   Spark/dbt          │    │  Grafana + Alerts    │
│  < 5 min latency     │    │   Daily aggregations │    │                      │
└──────────────────────┘    │   → Snowflake/BQ     │    └──────────────────────┘
                            │   (Analytics DWH)    │
                            └──────────────────────┘
                                            │
                                            ▼
                            ┌──────────────────────┐
                            │   AD-HOC QUERIES     │
                            │                      │
                            │  Snowflake/BigQuery  │
                            │  Jupyter Notebooks   │
                            │  Looker/Tableau      │
                            └──────────────────────┘
```

**Step 3: Component Choices with Tradeoffs**

| Component | Choice | Why | Tradeoff |
|-----------|--------|-----|----------|
| Ingestion | Kafka | High throughput, ordering | Operational complexity |
| Real-time OLAP | ClickHouse | Fast aggregations, column-store | Less flexible than SQL DW |
| Data Lake | S3 + Parquet | Cheap, scalable, open format | Query latency |
| Batch DWH | Snowflake | Elastic, SQL-native, easy | Cost at scale |
| Stream Processing | Flink | Low latency, exactly-once | Learning curve |
| Orchestration | Airflow | Industry standard | Can be heavyweight |

**Step 4: Data Model Design**

**Raw Events (Data Lake):**
```sql
-- Partitioned by date and event_type
event_id        STRING
user_id         BIGINT
event_type      STRING
event_timestamp TIMESTAMP
properties      JSON
client_info     STRUCT
```

**Aggregated Metrics (DWH):**
```sql
-- Pre-aggregated for common queries
metric_date     DATE
user_segment    STRING
event_type      STRING
total_events    BIGINT
unique_users    BIGINT
```

**Step 5: Handling Scale**

```
5B events/day ÷ 86,400 seconds = ~58,000 events/second

Storage estimation:
- Avg event size: 500 bytes
- Daily raw: 5B × 500B = 2.5 TB
- With compression (5x): 500 GB/day
- 2 years: ~365 TB

Cost estimation (S3):
- Storage: $0.023/GB × 365,000 GB = ~$8,400/month
- Actual with tiering: ~$3,000/month (use Glacier for old data)
```

**Step 6: Failure Handling**

1. **Kafka retention:** 7 days for replay capability
2. **Idempotent writes:** Use event_id for deduplication
3. **Schema registry:** Avro schemas for evolution
4. **Dead letter queues:** Capture failed events for investigation
5. **Monitoring:** Track lag, throughput, error rates

**Key Takeaways:**
1. Lambda architecture: real-time + batch paths
2. Choose storage based on query patterns
3. Pre-aggregate for known high-frequency queries
4. Plan for scale from day 1
5. Build in failure recovery mechanisms
</details>

---

## 🎯 Final Checklist

After completing these exercises, you should be able to:

- [ ] Apply Difference-in-Differences for quasi-experiments
- [ ] Decide between A/B tests and multi-armed bandits
- [ ] Design experiments with network effects
- [ ] Sessionize event data with window functions
- [ ] Write efficient deduplication queries
- [ ] Use recursive CTEs for hierarchical data
- [ ] Design scalable analytics architectures
- [ ] Make justified technology tradeoff decisions

---

## 📈 What's Next?

You've completed the advanced exercises! Consider:
- [Return to Learning Tracks](/tracks/) to continue structured learning
- [SQL Interview Problems](/interview-preparation/sql-interview-problems/) for more practice
- [Best Practices: Strategy & Architecture](/best-practices/1-strategy-architecture/) for deep dives

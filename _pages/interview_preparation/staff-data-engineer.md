---
layout: default
title: "Meta Staff Data Engineer (E6) Interview Prep"
permalink: /interview-preparation/staff-data-engineer/
difficulty: "Advanced"
estimated_time: "90 mins"
tags: [Interview, Staff Engineer, Data Engineering, Meta, E6, SQL, Python, System Design, Data Modeling]
track: "Interview Preparation"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/interview-preparation/' | relative_url }}">Interview Preparation</a> <span>&gt;</span>
  <span>Staff Data Engineer (E6)</span>
</div>

<div class="header">
  <h1>Meta Staff Data Engineer (E6) Interview Prep</h1>
  <p>A granular, six-module syllabus covering the advanced architectural patterns, scale-optimization techniques, and leadership signals required to clear the Meta Staff Data Engineer bar.</p>
</div>

<div class="section">

  <div class="card">
    <h3>Overview</h3>
    <p>The Staff Data Engineer (E6) bar at Meta is materially higher than the senior bar. Candidates are evaluated not just on technical execution, but on their ability to <strong>lead through ambiguity</strong>, make defensible architectural trade-offs, and act as a <strong>technical force multiplier</strong> for those around them. SQL is treated as a <em>velocity filter</em> — expect up to five problems in 30 minutes in a plain-text editor with no auto-complete or execution environment.</p>
    <p>This guide covers six modules that mirror the actual interview rounds:</p>
    <ol>
      <li><a href="#module-1">SQL Proficiency at Exabyte Scale</a></li>
      <li><a href="#module-2">Python Coding &amp; ETL Logic</a></li>
      <li><a href="#module-3">Architectural Leadership — Data Modeling</a></li>
      <li><a href="#module-4">Distributed Systems Design</a></li>
      <li><a href="#module-5">Product Sense &amp; Metrics</a></li>
      <li><a href="#module-6">Leadership &amp; The "Ownership" Paradigm</a></li>
    </ol>
  </div>

  <!-- ================================================================ -->
  <!-- MODULE 1: SQL -->
  <!-- ================================================================ -->
  <div class="card" id="module-1">
    <h3>Module 1: SQL Proficiency at Exabyte Scale</h3>
    <p>At E6 the SQL round is a <em>velocity filter</em>. You must solve up to five problems in 30 minutes in a plain-text editor without auto-complete or execution capabilities. Speed, correctness, and the ability to reason about performance <em>while writing</em> are equally weighted.</p>

    <h4>1.1 Advanced Analytical Patterns</h4>
    <ul>
      <li><strong>Window Functions:</strong> Mastery of <code>RANK</code>, <code>DENSE_RANK</code>, <code>ROW_NUMBER</code>, <code>LAG</code>, and <code>LEAD</code> for sessionization, retention curves, and growth metrics.</li>
      <li><strong>CTEs:</strong> Use Common Table Expressions to decompose complex logic into named, readable steps — interviewers penalise monolithic, nested queries.</li>
    </ul>

    <h4>1.2 Scale Optimization Techniques</h4>
    <ul>
      <li><strong>Partition Pruning:</strong> Always filter on the partition key (e.g. <code>ds = '2024-01-01'</code>) before any JOIN or GROUP BY. Failing to do so forces a full-table scan across trillions of rows on Hive/Presto.</li>
      <li><strong>Salting:</strong> Append a random suffix (<code>CONCAT(user_id, '_', FLOOR(RAND()*10))</code>) to high-cardinality keys to redistribute "hot partitions" during an aggregation, then sum the partial aggregates in a second pass.</li>
      <li><strong>Broadcast Joins:</strong> When one side of a JOIN is a small dimension table (typically &lt;1 GB), explicitly hint the engine to broadcast it to all worker nodes, eliminating the expensive wide shuffle of the large fact table.</li>
    </ul>

    <h4>1.3 Production Guardrails</h4>
    <ul>
      <li>Use <code>COALESCE(col, default)</code> defensively — NULL propagation silently corrupts aggregations.</li>
      <li>Explicit <code>CAST()</code> prevents silent type coercions between <code>BIGINT</code> and <code>VARCHAR</code> that cause cross-join explosions.</li>
      <li>State your <code>EXPLAIN</code> reasoning out loud: tell the interviewer where you expect a full-scan vs. an index/partition scan.</li>
    </ul>

    <h4>1.4 Worked Examples</h4>

    <details>
    <summary><strong>Challenge 1 — Sessionization with LAG</strong> 🟡 Medium</summary>
    <p><strong>Tables:</strong> <code>page_events(user_id, event_ts, ds)</code></p>
    <p><strong>Task:</strong> Assign a session ID to each event. A new session starts when the gap since the previous event exceeds 30 minutes.</p>
    <details>
    <summary>✅ Solution</summary>
    <pre><code>-- Step 1: flag session starts
WITH lagged AS (
  SELECT
    user_id,
    event_ts,
    LAG(event_ts) OVER (
      PARTITION BY user_id
      ORDER BY event_ts
    ) AS prev_ts
  FROM page_events
  WHERE ds = '2024-01-01'          -- partition pruning
),
flagged AS (
  SELECT
    user_id,
    event_ts,
    CASE
      WHEN prev_ts IS NULL
        OR DATEDIFF('minute', prev_ts, event_ts) > 30
      THEN 1 ELSE 0
    END AS is_new_session
  FROM lagged
)
-- Step 2: cumulative sum produces a session counter per user
SELECT
  user_id,
  event_ts,
  SUM(is_new_session) OVER (
    PARTITION BY user_id
    ORDER BY event_ts
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS session_id
FROM flagged
ORDER BY user_id, event_ts;</code></pre>
    <p><strong>Key insight:</strong> <code>SUM(is_new_session) OVER (...)</code> acts as a running counter — it increments only when a new session boundary is crossed, giving each session a stable integer ID.</p>
    </details>
    </details>

    <details>
    <summary><strong>Challenge 2 — Salted Aggregation for a Skewed Key</strong> 🔴 Hard</summary>
    <p><strong>Context:</strong> <code>events(creator_id, action, ds)</code> where a handful of viral creators account for 90% of rows.</p>
    <p><strong>Task:</strong> Count actions per creator without hitting a hot-partition OOM error.</p>
    <details>
    <summary>✅ Solution</summary>
    <pre><code>-- Pass 1: add salt, partial aggregate
WITH salted AS (
  SELECT
    CONCAT(CAST(creator_id AS VARCHAR), '_',
           CAST(FLOOR(RAND() * 10) AS VARCHAR)) AS salted_key,
    creator_id,
    action,
    COUNT(*) AS partial_count
  FROM events
  WHERE ds = '2024-01-01'
  GROUP BY 1, 2, 3
)
-- Pass 2: strip salt, final aggregate
SELECT
  creator_id,
  action,
  SUM(partial_count) AS total_count
FROM salted
GROUP BY creator_id, action
ORDER BY total_count DESC;</code></pre>
    <p><strong>Key insight:</strong> Salting spreads the hot creator across 10 reducers in Pass 1. Pass 2 re-aggregates the 10 partial sums — cheap because there are at most <em>10 × distinct_creators × distinct_actions</em> rows.</p>
    </details>
    </details>

    <details>
    <summary><strong>Challenge 3 — Week-over-Week Retention with LEAD</strong> 🔴 Hard</summary>
    <p><strong>Table:</strong> <code>weekly_active(user_id, week_start, ds)</code></p>
    <p><strong>Task:</strong> For each week W, compute the fraction of W's active users who were also active in W+1.</p>
    <details>
    <summary>✅ Solution</summary>
    <pre><code>WITH next_week AS (
  SELECT
    user_id,
    week_start,
    LEAD(week_start) OVER (
      PARTITION BY user_id
      ORDER BY week_start
    ) AS next_active_week
  FROM weekly_active
  WHERE ds = '2024-01-01'
),
retention_flags AS (
  SELECT
    week_start,
    COUNT(DISTINCT user_id)                                  AS wau,
    COUNT(DISTINCT CASE
      WHEN DATEDIFF('day', week_start, next_active_week) = 7
      THEN user_id END)                                      AS retained_next_week
  FROM next_week
  GROUP BY week_start
)
SELECT
  week_start,
  wau,
  retained_next_week,
  ROUND(100.0 * retained_next_week / wau, 2) AS w1_retention_pct
FROM retention_flags
ORDER BY week_start;</code></pre>
    </details>
    </details>
  </div>

  <!-- ================================================================ -->
  <!-- MODULE 2: PYTHON / ETL -->
  <!-- ================================================================ -->
  <div class="card" id="module-2">
    <h3>Module 2: Python Coding &amp; ETL Logic</h3>
    <p>Python evaluation focuses on practical <strong>productionalization</strong> — not academic algorithms. Interviewers want to see that you write code that would survive a code review in a real data pipeline.</p>

    <h4>2.1 High-Performance Data Structures</h4>
    <ul>
      <li><strong>Dictionaries (hashmaps):</strong> Default to <code>dict</code>/<code>collections.defaultdict</code> for O(1) lookups; avoid repeated linear scans of lists.</li>
      <li><strong><code>collections.Counter</code>:</strong> One-liner for frequency counts; supports arithmetic (<code>+</code>, <code>-</code>, <code>&amp;</code>, <code>|</code>) between counters.</li>
      <li><strong><code>collections.defaultdict</code>:</strong> Eliminates <code>KeyError</code> guards and is faster than <code>dict.setdefault</code> in tight loops.</li>
    </ul>

    <h4>2.2 Complex Transformation Techniques</h4>
    <ul>
      <li><strong>Log Parsing:</strong> Use <code>re.compile</code> once outside the loop, then <code>.match()</code> / <code>.search()</code> per line. Name your capture groups (<code>(?P&lt;name&gt;...)</code>) to make downstream code self-documenting.</li>
      <li><strong>JSON Flattening:</strong> Use recursion with a <code>prefix</code> accumulator to produce column names like <code>user.address.city</code>. Guard against cycles with a <code>max_depth</code> parameter.</li>
      <li><strong>State Machine / Event Validation:</strong> Use an explicit <code>state</code> variable and a <code>transitions</code> dict (<code>{current_state: valid_next_states}</code>) to validate alternating event sequences (e.g. checkout → payment → confirmation).</li>
    </ul>

    <h4>2.3 Scalability Discussion</h4>
    <p>Proactively address what changes at 100× scale:</p>
    <ul>
      <li>Single-machine loop → distributed map with Spark/Beam</li>
      <li>In-memory dict → external KV store (Redis, DynamoDB) for state</li>
      <li>Batch file read → streaming consumer (Kafka) for real-time updates</li>
      <li>Always name the bottleneck: CPU, memory, I/O, or network</li>
    </ul>

    <h4>2.4 Worked Examples</h4>

    <details>
    <summary><strong>Challenge 1 — Parse Malformed Server Logs</strong> 🟡 Medium</summary>
    <p><strong>Input sample:</strong></p>
    <pre><code>2024-01-15T08:32:01Z | user=12345 | action=view | item_id=abc99 | latency_ms=142
2024-01-15T08:32:05Z | user=12345 | action=purchase | item_id=abc99 | amount=29.99
2024-01-15T08:32:07Z | MALFORMED LINE NO PIPE
2024-01-15T08:32:10Z | user=67890 | action=view | item_id=xyz01 | latency_ms=88</code></pre>
    <p><strong>Task:</strong> Parse into a list of dicts; skip and count malformed lines.</p>
    <details>
    <summary>✅ Solution</summary>
    <pre><code>import re
from typing import Iterator

LOG_PATTERN = re.compile(
    r"(?P&lt;ts&gt;\S+)\s+\|\s+user=(?P&lt;user_id&gt;\d+)\s+\|"
    r"\s+action=(?P&lt;action&gt;\w+)\s+\|(?P&lt;rest&gt;.*)"
)
KV_PATTERN = re.compile(r"(\w+)=(\S+)")


def parse_logs(lines: Iterator[str]) -> tuple[list[dict], int]:
    records, malformed = [], 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        m = LOG_PATTERN.match(line)
        if not m:
            malformed += 1
            continue
        record = {
            "ts": m.group("ts"),
            "user_id": int(m.group("user_id")),
            "action": m.group("action"),
        }
        # parse remaining key=value pairs
        record.update(
            {k: v for k, v in KV_PATTERN.findall(m.group("rest"))}
        )
        records.append(record)
    return records, malformed


# --- scalability note ---
# At 100x scale: stream lines from GCS/S3 via a generator (no full load),
# or distribute across Spark executors with sc.textFile().mapPartitions(parse_logs).</code></pre>
    </details>
    </details>

    <details>
    <summary><strong>Challenge 2 — Recursive JSON Flattener</strong> 🟡 Medium</summary>
    <p><strong>Task:</strong> Flatten nested JSON events into a single-level dict suitable for relational ingestion.</p>
    <details>
    <summary>✅ Solution</summary>
    <pre><code>from typing import Any


def flatten(obj: Any, prefix: str = "", sep: str = ".", max_depth: int = 10) -> dict:
    """
    Flatten a nested dict/list into {dotted.key: value} pairs.
    Lists are indexed: parent.0, parent.1, ...
    """
    if max_depth == 0:
        return {prefix: str(obj)}  # treat deep nodes as opaque strings

    items: dict = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{prefix}{sep}{k}" if prefix else k
            items.update(flatten(v, new_key, sep, max_depth - 1))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_key = f"{prefix}{sep}{i}" if prefix else str(i)
            items.update(flatten(v, new_key, sep, max_depth - 1))
    else:
        items[prefix] = obj
    return items


# Example
event = {
    "user": {"id": 123, "address": {"city": "NYC", "zip": "10001"}},
    "items": [{"sku": "A1", "qty": 2}, {"sku": "B3", "qty": 1}],
    "total": 49.99,
}
print(flatten(event))
# {
#   'user.id': 123, 'user.address.city': 'NYC', 'user.address.zip': '10001',
#   'items.0.sku': 'A1', 'items.0.qty': 2, 'items.1.sku': 'B3', 'items.1.qty': 1,
#   'total': 49.99
# }</code></pre>
    </details>
    </details>

    <details>
    <summary><strong>Challenge 3 — Event Sequence State Validator</strong> 🔴 Hard</summary>
    <p><strong>Task:</strong> Validate a stream of checkout events per user. Valid sequence: <code>cart_add → checkout_start → payment_submitted → order_confirmed</code>. Detect missing or out-of-order steps.</p>
    <details>
    <summary>✅ Solution</summary>
    <pre><code>from collections import defaultdict
from typing import NamedTuple

TRANSITIONS = {
    None:                 {"cart_add"},
    "cart_add":           {"cart_add", "checkout_start"},
    "checkout_start":     {"payment_submitted"},
    "payment_submitted":  {"order_confirmed"},
    "order_confirmed":    set(),  # terminal
}


class ValidationResult(NamedTuple):
    user_id: int
    invalid_transitions: list[tuple[str, str]]
    final_state: str | None


def validate_sequences(events: list[dict]) -> list[ValidationResult]:
    """events: sorted list of {user_id, action, ts}"""
    user_states: dict[int, str | None] = defaultdict(lambda: None)
    user_errors: dict[int, list] = defaultdict(list)

    for e in events:
        uid, action = e["user_id"], e["action"]
        current = user_states[uid]
        if action not in TRANSITIONS.get(current, set()):
            user_errors[uid].append((current, action))
        else:
            user_states[uid] = action

    all_users = set(user_states) | set(user_errors)
    return [
        ValidationResult(
            user_id=uid,
            invalid_transitions=user_errors[uid],
            final_state=user_states[uid],
        )
        for uid in sorted(all_users)
    ]


# --- scalability note ---
# At 100x scale: maintain state in Redis (HSET user:{id} state {action})
# so workers can be stateless and horizontally scaled.</code></pre>
    </details>
    </details>
  </div>

  <!-- ================================================================ -->
  <!-- MODULE 3: DATA MODELING -->
  <!-- ================================================================ -->
  <div class="card" id="module-3">
    <h3>Module 3: Architectural Leadership — Data Modeling</h3>
    <p>The modeling round is the <strong>defining round for Staff leveling</strong>. It assesses whether you can translate ambiguous business goals into durable technical systems that remain maintainable at Meta scale.</p>

    <h4>3.1 Dimensional Modeling Mastery</h4>

    <h5>Grain Definition</h5>
    <p>Before touching schema, always state the grain explicitly: <em>"One row represents one line item per order per day."</em> Getting grain wrong invalidates every downstream metric.</p>

    <h5>Fact Table Specialization</h5>
    <table>
      <tr>
        <th>Type</th>
        <th>Use When</th>
        <th>Example</th>
      </tr>
      <tr>
        <td><strong>Transactional</strong></td>
        <td>Discrete business events</td>
        <td>Ad clicks, purchases, messages sent</td>
      </tr>
      <tr>
        <td><strong>Periodic Snapshot</strong></td>
        <td>State captured at a regular cadence</td>
        <td>Daily account balances, weekly DAU</td>
      </tr>
      <tr>
        <td><strong>Accumulating Snapshot</strong></td>
        <td>Progress through a well-defined funnel</td>
        <td>Loan application stages, onboarding steps</td>
      </tr>
    </table>

    <h5>SCD Logic</h5>
    <ul>
      <li><strong>SCD Type 1 (Overwrite):</strong> Simple, no history. Use when history is irrelevant (e.g. phone number correction).</li>
      <li><strong>SCD Type 2 (New Row):</strong> Preserves full history via <code>effective_date</code> / <code>expiry_date</code> and a <code>is_current</code> flag. Required when historical accuracy is a business requirement (e.g. a customer's geographic region at time of purchase).</li>
      <li><strong>Defending your choice:</strong> State the business question that requires history. If no business question requires historical accuracy for that attribute, Type 1 is simpler and cheaper.</li>
    </ul>

    <h4>3.2 Advanced Schema Design</h4>

    <h5>Star Schema vs. One Big Table (OBT)</h5>
    <table>
      <tr>
        <th></th>
        <th>Star Schema</th>
        <th>OBT</th>
      </tr>
      <tr>
        <td><strong>Reads</strong></td>
        <td>Requires JOINs, slower for BI tools</td>
        <td>Single scan, fastest for BI tools</td>
      </tr>
      <tr>
        <td><strong>Storage</strong></td>
        <td>Compact (dimensions stored once)</td>
        <td>Denormalized — dimension columns duplicated</td>
      </tr>
      <tr>
        <td><strong>Maintenance</strong></td>
        <td>Update dimension once, propagated automatically</td>
        <td>Must rewrite entire OBT on dimension changes</td>
      </tr>
      <tr>
        <td><strong>Best for</strong></td>
        <td>Complex, flexible queries; large cardinality dimensions</td>
        <td>High-concurrency, fixed-query BI dashboards</td>
      </tr>
    </table>

    <h5>Mini-Dimensions</h5>
    <p>When a small subset of a large dimension (e.g. <code>dim_customer</code> with 500M rows) changes frequently (e.g. loyalty tier, credit score band), extract those attributes into a <strong>mini-dimension</strong> keyed by a hash of their values. This prevents the main dimension from "exploding" with SCD Type 2 rows on every status change.</p>

    <h5>Bridge Tables</h5>
    <p>Resolve many-to-many relationships (one patient → multiple diagnoses; one ad → multiple audience segments) with a <strong>bridge table</strong> that has a <code>group_key</code> linking rows in the fact table to a set of dimension members. Always define a <strong>weighting factor</strong> column (e.g. <code>1/count_of_diagnoses</code>) to prevent metric inflation when aggregating.</p>

    <h4>3.3 Schema Design Walkthrough</h4>

    <details>
    <summary><strong>Example — Ad Delivery Data Model at Meta Scale</strong></summary>
    <pre><code>-- Grain: one ad impression per user per ad per hour (partitioned by ds + hour)
CREATE TABLE fact_ad_impressions (
  impression_id   BIGINT,
  user_key        BIGINT,           -- FK to dim_user
  ad_key          BIGINT,           -- FK to dim_ad
  placement_key   INT,              -- FK to dim_placement
  user_demo_key   INT,              -- FK to mini_dim_user_demographics
  ds              DATE,             -- Hive partition key
  hour            TINYINT,          -- sub-partition
  impression_ts   BIGINT,           -- epoch ms
  is_click        BOOLEAN,
  revenue_usd     DECIMAL(12,6)
)
PARTITIONED BY (ds DATE, hour TINYINT)
STORED AS ORC TBLPROPERTIES ('orc.compress'='ZSTD');

-- SCD Type 2 dimension
CREATE TABLE dim_user (
  user_key        BIGINT,           -- surrogate key
  user_id         BIGINT,           -- natural key
  country_code    CHAR(2),
  age_band        VARCHAR(10),
  effective_date  DATE,
  expiry_date     DATE,             -- NULL means current
  is_current      BOOLEAN
);

-- Mini-dimension: rapidly changing demographics
CREATE TABLE mini_dim_user_demographics (
  user_demo_key   INT,
  income_band     VARCHAR(20),
  loyalty_tier    VARCHAR(10),
  valid_from      DATE,
  valid_to        DATE
);</code></pre>
    <p><strong>Interviewer follow-up you should anticipate:</strong></p>
    <ul>
      <li><em>"What changes if we need to support cross-device attribution?"</em> — Add a <code>device_key</code> and a bridge table mapping <code>device_id → user_id</code> resolved via identity graph.</li>
      <li><em>"How do you handle late-arriving data?"</em> — UPSERT (MERGE) on the surrogate key with a watermark column; re-partition the affected <code>ds</code> slices.</li>
    </ul>
    </details>
  </div>

  <!-- ================================================================ -->
  <!-- MODULE 4: DISTRIBUTED SYSTEMS -->
  <!-- ================================================================ -->
  <div class="card" id="module-4">
    <h3>Module 4: Distributed Systems Design</h3>
    <p>At E6 the system design round tests throughput, reliability, and correctness — <em>not</em> request/response latency. You are designing pipelines that process petabytes per day, not APIs that serve millisecond responses.</p>

    <h4>4.1 Architecture Comparison</h4>
    <table>
      <tr>
        <th>Pattern</th>
        <th>Core Idea</th>
        <th>When to Choose</th>
        <th>Key Trade-off</th>
      </tr>
      <tr>
        <td><strong>Lambda</strong></td>
        <td>Separate speed layer (stream) + batch layer; serving layer merges both</td>
        <td>When you need sub-minute latency AND historical accuracy</td>
        <td>Two codebases to maintain; data consistency at merge point</td>
      </tr>
      <tr>
        <td><strong>Kappa</strong></td>
        <td>Stream-only; replay from immutable log (Kafka) to reprocess history</td>
        <td>When stream semantics can handle all business questions</td>
        <td>Reprocessing at scale is expensive; requires durable log retention</td>
      </tr>
      <tr>
        <td><strong>Medallion (Bronze/Silver/Gold)</strong></td>
        <td>Tiered storage: raw → cleansed → aggregated</td>
        <td>Data lakehouse (Delta Lake / Iceberg); incremental refinement</td>
        <td>Storage amplification; staleness between tiers</td>
      </tr>
    </table>

    <h4>4.2 Reliability Techniques</h4>

    <h5>Exactly-Once Processing</h5>
    <p>True exactly-once delivery is impractical at Meta scale. The production pattern is:</p>
    <ol>
      <li><strong>At-least-once delivery</strong> from the message broker (Kafka/Scribe) — messages may be duplicated on retry.</li>
      <li><strong>Idempotent writes</strong> at the sink — use <code>MERGE INTO ... WHEN MATCHED THEN UPDATE</code> (Delta/Iceberg) or <code>INSERT OR REPLACE</code> keyed on a deterministic <code>event_id</code>.</li>
    </ol>

    <h5>Log-Based Change Data Capture (CDC)</h5>
    <ul>
      <li><strong>Log-based CDC (Debezium):</strong> Reads the database binary log (MySQL binlog, Postgres WAL) — zero additional load on the source database.</li>
      <li><strong>Query-based polling:</strong> <code>SELECT * WHERE updated_at > last_watermark</code> — simpler but adds read pressure and misses hard-deletes.</li>
      <li><strong>Prefer log-based</strong> at Staff level; polling is only acceptable for read-heavy sources that don't support CDC.</li>
    </ul>

    <h5>Operational Maturity: The Three Hard Problems</h5>
    <table>
      <tr>
        <th>Problem</th>
        <th>Definition</th>
        <th>Mitigation</th>
      </tr>
      <tr>
        <td><strong>Backpressure</strong></td>
        <td>A slow consumer lets the producer queue grow unboundedly</td>
        <td>Auto-scale consumers; expose consumer lag as a metric; use bounded queues with drop/DLQ policies</td>
      </tr>
      <tr>
        <td><strong>Schema Drift</strong></td>
        <td>Upstream adds/renames/removes fields without notice</td>
        <td>Schema registry (Confluent / AWS Glue) with compatibility rules; automated validation job that alerts on schema delta before writing to Silver</td>
      </tr>
      <tr>
        <td><strong>Small-File Problem</strong></td>
        <td>High-frequency streaming writes create millions of tiny Parquet/ORC files, crushing NameNode and slowing reads</td>
        <td>Micro-batch compaction job (e.g. Spark <code>OPTIMIZE</code> / Delta <code>ZORDER</code>) scheduled every 15 min; target 128–512 MB files</td>
      </tr>
    </table>

    <h4>4.3 System Design Walkthrough</h4>

    <details>
    <summary><strong>Example — Design a Real-Time Ad Spend Pipeline</strong></summary>
    <p><strong>Requirements:</strong></p>
    <ul>
      <li>Ingest 5M impression events/second from 200 countries</li>
      <li>Serve advertiser spend dashboards with &lt;5 min latency</li>
      <li>Guarantee spend figures are never double-counted</li>
      <li>Support 90-day historical reprocessing within 4 hours</li>
    </ul>
    <p><strong>Reference Architecture (Kappa on Medallion):</strong></p>
    <pre><code>Producers (mobile/web/server)
    │
    ▼
[Scribe / Kafka] — retention: 90 days, partitioned by advertiser_id
    │
    ├── Flink Job (streaming)
    │     • watermark: event_time + 2 min allowed lateness
    │     • aggregate spend per (advertiser, campaign, country, minute)
    │     • MERGE INTO delta_bronze.ad_spend_1min  (idempotent on event_minute + advertiser_id)
    │
    ▼
[Bronze — raw, immutable, Parquet/ORC on S3/GCS]
    │
[Silver — cleansed: deduped on impression_id, invalid creatives filtered out]
    │
[Gold — aggregated: daily/weekly rollups, pre-joined with dim_advertiser]
    │
    ▼
Advertiser Dashboard (Presto / internal BI tool reads Gold)</code></pre>
    <p><strong>How you handle double-counting:</strong> Flink assigns a deterministic <code>impression_id = SHA256(user_id + ad_id + event_ts_ms)</code>. The MERGE INTO on Bronze deduplicates on <code>impression_id</code> — replay is safe.</p>
    <p><strong>How you handle reprocessing:</strong> Replay 90 days of Kafka into the same Flink job with a historical mode flag. Bronze is append-only with partitioning on <code>event_date</code>; reprocessed partitions are overwritten atomically.</p>
    </details>
  </div>

  <!-- ================================================================ -->
  <!-- MODULE 5: PRODUCT SENSE & METRICS -->
  <!-- ================================================================ -->
  <div class="card" id="module-5">
    <h3>Module 5: Product Sense &amp; Metrics</h3>
    <p>Meta Data Engineers at E6 are expected to act as <strong>product partners</strong> who understand the "why" behind the data. The metrics round assesses whether you can design a measurement framework and debug anomalies independently.</p>

    <h4>5.1 Metric Engineering Framework</h4>
    <table>
      <tr>
        <th>Tier</th>
        <th>Purpose</th>
        <th>Example (Marketplace)</th>
      </tr>
      <tr>
        <td><strong>North Star</strong></td>
        <td>Single metric capturing the core product objective</td>
        <td>Weekly Gross Merchandise Value (GMV)</td>
      </tr>
      <tr>
        <td><strong>Leading Metrics</strong></td>
        <td>Early indicators that predict North Star movement</td>
        <td>Listing creation rate, search-to-detail-page CTR</td>
      </tr>
      <tr>
        <td><strong>Guardrail Metrics</strong></td>
        <td>Monitor for cannibalization or negative side effects</td>
        <td>Seller churn rate, buyer dispute rate, p50 latency</td>
      </tr>
    </table>
    <p><strong>Staff signal:</strong> Proactively name the guardrail metrics before the interviewer asks. This shows you think about second-order effects.</p>

    <h4>5.2 Structured Root Cause Analysis (RCA)</h4>
    <p>When asked <em>"Comments dropped 10% week-over-week — investigate,"</em> work through four layers <strong>in order</strong>:</p>
    <ol>
      <li><strong>Technical Integrity:</strong> Is the data trustworthy? Check for logging gaps, pipeline delays, instrumentation changes, or schema drift before drawing any business conclusions.</li>
      <li><strong>Population Specificity:</strong> Is the drop global or localized? Segment by platform (iOS/Android/web), geography, user cohort, and feature surface. A drop only on iOS 17.4 is an instrumentation bug, not a product regression.</li>
      <li><strong>External / Internal Events:</strong> Did a competitor launch? Was there a news event? Did Meta ship a related feature (e.g. Reacts) that may have substituted for comments? Check the launch calendar.</li>
      <li><strong>Metric Characteristics:</strong> Is this metric inherently seasonal (e.g. lower on weekends)? Did the denominator change (e.g. DAU grew, making per-user comment rate look flat even if total volume grew)?</li>
    </ol>
    <p><strong>Output format the interviewer expects:</strong></p>
    <ul>
      <li>State your hypothesis first, then describe the query you'd run to confirm or refute it.</li>
      <li>Give a recommendation: "If hypothesis A is confirmed, the action is X. If B, the action is Y."</li>
    </ul>

    <h4>5.3 RCA Practice</h4>

    <details>
    <summary><strong>Scenario — "DAU dropped 8% on Tuesday. Investigate."</strong></summary>
    <h5>Layer 1 — Technical Integrity</h5>
    <pre><code>-- Check: did the logging pipeline have a gap?
SELECT ds, COUNT(DISTINCT user_id) AS dau
FROM fact_daily_active
WHERE ds BETWEEN '2024-01-08' AND '2024-01-16'
GROUP BY ds
ORDER BY ds;</code></pre>
    <p>If the gap is Tuesday-only, check whether a pipeline incident affected that partition.</p>

    <h5>Layer 2 — Population Specificity</h5>
    <pre><code>-- Segment by platform
SELECT ds, platform, COUNT(DISTINCT user_id) AS dau
FROM fact_daily_active
WHERE ds IN ('2024-01-08', '2024-01-09')  -- Mon vs Tue
GROUP BY ds, platform;</code></pre>
    <p>If the drop is on Android only → likely an app crash or push notification failure.</p>

    <h5>Layer 3 — External Events</h5>
    <p>Check the release calendar: was there an Android app update on Monday night? Was there a Meta-wide outage reported by Downdetector?</p>

    <h5>Layer 4 — Metric Characteristics</h5>
    <pre><code>-- Check YoY: is Tuesday structurally lower?
SELECT DAYOFWEEK(ds) AS dow,
       AVG(dau) AS avg_dau
FROM fact_daily_active
WHERE ds BETWEEN '2023-01-01' AND '2024-01-01'
GROUP BY 1
ORDER BY 1;</code></pre>
    </details>
  </div>

  <!-- ================================================================ -->
  <!-- MODULE 6: LEADERSHIP -->
  <!-- ================================================================ -->
  <div class="card" id="module-6">
    <h3>Module 6: Leadership &amp; The "Ownership" Paradigm</h3>
    <p>At E6, the behavioral round assesses your ability to act as a <strong>technical force multiplier</strong> — someone who raises the output of every engineer around them through influence, mentorship, and clarity, not command authority.</p>

    <h4>6.1 Storytelling Frameworks</h4>

    <h5>STAR (Situation, Task, Action, Result)</h5>
    <p>The standard behavioral framework. At Staff level, the <strong>Action</strong> section must demonstrate cross-team influence, architectural decision-making, or mentorship — not individual execution.</p>

    <h5>SPSIL (Situation, Problem, Solution, Impact, Lessons)</h5>
    <p>Better suited for system design retrospectives because it surfaces <em>why</em> a technical choice was made, not just what was done. Use this when the interviewer asks: <em>"Walk me through a complex project you led."</em></p>

    <table>
      <tr>
        <th>Component</th>
        <th>Focus</th>
        <th>Time</th>
      </tr>
      <tr>
        <td><strong>Situation</strong></td>
        <td>Business context and scale (brief)</td>
        <td>15 sec</td>
      </tr>
      <tr>
        <td><strong>Problem</strong></td>
        <td>Technical root cause — be precise</td>
        <td>20 sec</td>
      </tr>
      <tr>
        <td><strong>Solution</strong></td>
        <td>Your architectural decision AND the alternatives you rejected</td>
        <td>60–90 sec</td>
      </tr>
      <tr>
        <td><strong>Impact</strong></td>
        <td>Quantified business or engineering outcome</td>
        <td>20 sec</td>
      </tr>
      <tr>
        <td><strong>Lessons</strong></td>
        <td>What you would do differently — shows intellectual honesty</td>
        <td>15 sec</td>
      </tr>
    </table>

    <h4>6.2 Staff Signal Techniques</h4>

    <h5>Leadership Without Authority</h5>
    <p>Prepare a story where you achieved a significant technical outcome without any direct reports. Strong signals include:</p>
    <ul>
      <li>Writing a design doc that became the standard adopted by multiple teams</li>
      <li>Running a cross-functional "data quality council" you initiated</li>
      <li>Convincing a partner team to change their schema by making the business case with data</li>
    </ul>

    <h5>Conflict Resolution</h5>
    <p>When disagreeing with a PM or Data Scientist, use the <em>de-risk and commit</em> pattern:</p>
    <ol>
      <li><strong>Quantify the risk</strong> of the disagreed-upon approach in business terms ($, latency, error rate).</li>
      <li><strong>Propose a middle ground</strong> that lets the business move forward while mitigating the risk.</li>
      <li><strong>Commit to a timeline</strong> and deliver on it — credibility is built in execution, not debate.</li>
    </ol>

    <h5>Architectural Defense (Project Retrospective)</h5>
    <p>Interviewers will probe your past systems looking for weaknesses. Prepare a <strong>granular retrospective</strong> for your most complex project:</p>
    <ul>
      <li>What were the three alternatives you considered for the critical architectural choice?</li>
      <li>What data did you use to make the final decision?</li>
      <li>What broke in production that your design did not anticipate?</li>
      <li>What would you change if you started today with the same constraints?</li>
    </ul>
    <p><strong>Why this matters:</strong> Shallow answers like "we chose Kafka because it's scalable" are E4 answers. E6 answers cite specific throughput numbers, specific failure modes observed, and specific trade-offs that informed the choice.</p>

    <h4>6.3 Example SPSIL Story</h4>

    <details>
    <summary><strong>"Walk me through a complex data pipeline you led"</strong></summary>

    <p><strong>Situation (15 sec):</strong></p>
    <p>I led the migration of our ads attribution pipeline from a daily Hive batch job to a near-real-time Flink pipeline processing 2M events/second. The pipeline was the source of truth for $800M/year in advertiser billing.</p>

    <p><strong>Problem (20 sec):</strong></p>
    <p>The batch pipeline produced billing figures 18–24 hours late, causing advertisers to pause campaigns mid-day when they couldn't see real spend. This was driving 15% of advertiser support tickets.</p>

    <p><strong>Solution (90 sec):</strong></p>
    <p>I considered three options:</p>
    <ol>
      <li><strong>Reduce batch frequency to hourly:</strong> Lowest risk, but still 60 min latency and didn't scale past 5× event volume growth.</li>
      <li><strong>Lambda architecture (stream + batch):</strong> Gave &lt;5 min latency, but two codebases to maintain and a complex merge layer. I prototyped it and found the merge logic introduced its own correctness bugs.</li>
      <li><strong>Kappa on Medallion (chosen):</strong> Single Flink codebase, immutable Bronze layer in Delta, idempotent MERGE on impression_id. Replay from Kafka for historical corrections.</li>
    </ol>
    <p>I wrote the design doc, got sign-off from three partner teams (Ads Infra, Billing Eng, Data Governance), and staffed a two-engineer sub-team for the 12-week build. I personally owned the idempotency guarantee and the schema migration playbook.</p>

    <p><strong>Impact (20 sec):</strong></p>
    <p>Latency dropped from 18 hours to 4 minutes. Advertiser support tickets related to spend visibility fell 60%. The pipeline handles 4× the original event volume without hardware changes.</p>

    <p><strong>Lessons (15 sec):</strong></p>
    <p>I underestimated the schema governance work — we had 12 upstream producers with inconsistent field naming. Next time I would invest in a schema contract and compatibility checks at the producer level before starting the pipeline build.</p>
    </details>

    <h4>6.4 Leadership Checklist</h4>
    <p>Before your behavioral round, confirm you can answer these with a concrete story:</p>
    <ul>
      <li>☐ A time you influenced a major technical decision without formal authority</li>
      <li>☐ A time you mentored a junior engineer and can quantify the outcome</li>
      <li>☐ A time you pushed back on a PM or leadership using data, and what happened</li>
      <li>☐ A project post-mortem where you can name three things you'd change</li>
      <li>☐ A time you drove alignment across &gt;3 teams on a shared technical standard</li>
    </ul>
  </div>

  <!-- ================================================================ -->
  <!-- INTERVIEW-DAY STRATEGY -->
  <!-- ================================================================ -->
  <div class="card">
    <h3>Interview-Day Strategy for E6</h3>
    <table>
      <tr>
        <th>Round</th>
        <th>First 2 Minutes</th>
        <th>Staff Signal</th>
      </tr>
      <tr>
        <td>SQL</td>
        <td>State the partition key you'll filter on before writing a single line</td>
        <td>Proactively mention salting or broadcast join if the schema implies skew</td>
      </tr>
      <tr>
        <td>Python/ETL</td>
        <td>Ask: "What's the expected input size and update frequency?"</td>
        <td>Conclude with a 100× scale discussion even if not prompted</td>
      </tr>
      <tr>
        <td>Data Modeling</td>
        <td>State the grain explicitly before drawing any table</td>
        <td>Name SCD type, fact type, and one alternative you rejected</td>
      </tr>
      <tr>
        <td>System Design</td>
        <td>Clarify SLA: latency, throughput, durability, and reprocessing requirements</td>
        <td>Proactively address exactly-once semantics and operational runbook</td>
      </tr>
      <tr>
        <td>Product/Metrics</td>
        <td>Define North Star and guardrail metrics before any analysis</td>
        <td>Structure RCA as four layers; state hypothesis before running queries</td>
      </tr>
      <tr>
        <td>Behavioral</td>
        <td>Confirm the competency the question is testing before answering</td>
        <td>Use SPSIL for technical stories; name alternatives you rejected</td>
      </tr>
    </table>
  </div>

</div>

<div class="navigation-buttons">
  <a href="{{ '/interview-preparation/behavioral-interview/' | relative_url }}">Previous: Behavioral Interview</a>
  <a href="{{ '/meta-specificity/' | relative_url }}">Next: Meta Specificity</a>
</div>

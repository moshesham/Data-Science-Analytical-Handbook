---
layout: page
title: "Data Architecture"
permalink: /best-practices/2-data-architecture/
difficulty: "Advanced"
estimated_time: "75 mins"
tags: [Data Architecture, Data Lake, Data Warehouse, Lakehouse, Data Mesh]
track: "Data Engineering Deep Dive"
nav_order: 2
parent: "Data Engineering Best Practices"
---

## II. Infrastructure & Development Practices

### Data Architecture

Data architecture is the strategic blueprint for managing and leveraging an organization's data assets. It defines how data is collected, stored, processed, integrated, and consumed to meet business objectives.  A robust data architecture goes beyond technology selection; it's a dynamic framework aligned with business strategy, data characteristics, organizational structure, and evolving needs.  In the era of high-velocity and high-volume data, a well-designed data architecture is paramount for ensuring scalability, performance, agility, data quality, and ultimately, the realization of data's strategic value. This section delves into critical data architecture patterns, modeling approaches, organizational considerations, and best practices for building resilient and future-proof data systems.

#### Architecture Patterns: Data Mesh, Data Fabric, Lakehouse, and Warehouse Approaches

**High-Level Pattern Explanation:**

Selecting the appropriate data architecture pattern is a foundational strategic decision.  The landscape has evolved significantly from solely relying on monolithic data warehouses to embracing distributed and specialized paradigms.  Understanding the strengths, weaknesses, and nuances of patterns like Data Mesh, Data Fabric, Lakehouse, and Data Warehouse is crucial for constructing data ecosystems capable of handling the scale, velocity, variety, and evolving nature of modern data. Each pattern embodies distinct principles and trade-offs, making them suitable for different organizational contexts, data challenges, and business priorities.  

For high-velocity and high-volume datasets, the chosen pattern profoundly influences ingestion efficiency, processing capabilities, analytical performance, data accessibility, and overall system resilience.

* **Data Warehouse: The Evolved Centralized Repository - Especially in the Cloud:**  The data warehouse, while often perceived as "traditional," has undergone significant evolution, *particularly in the cloud era*.  It remains a centralized repository of *structured* and *increasingly semi-structured* data, meticulously filtered, transformed, and optimized for analytical workloads – primarily business intelligence (BI) and reporting.  Historically built on relational databases, modern *cloud* data warehouses leverage cloud-native, massively parallel processing (MPP) columnar databases (e.g., Snowflake, Amazon Redshift, Google BigQuery). These modern iterations offer key *cloud-specific* features:
    * **Elastic Scalability:**  Cloud-based MPP architectures provide elastic scalability – scaling compute and storage independently based on demand.
    * **Serverless Options:** Many cloud DWs offer serverless consumption models, eliminating infrastructure management overhead.
    * **Pay-as-you-go Pricing:** Cost-effective pay-as-you-go pricing models optimize spending based on actual resource consumption.
    * **Separation of Compute and Storage:** Independent scaling and optimization of compute and storage resources.
    * **Semi-structured Data Handling:** Many modern data warehouses now support querying and integrating semi-structured data formats like JSON and XML, expanding their versatility.
    * **Advanced Analytics Integration:** Some platforms are incorporating in-database machine learning capabilities or seamless integration with cloud-based ML services.
    * **Mature Governance and Security:** Data warehouses typically offer robust data governance features, security controls, and compliance capabilities.
    * **Use Case:** Still ideal for organizations needing a single source of truth for structured business data, standardized reporting, and well-defined analytical queries.

* **Data Lake: The Flexible and Scalable Raw Data Hub:** A data lake is a centralized repository designed to store data in its *raw*, unprocessed form, typically in cost-effective object storage (e.g., AWS S3, Azure Blob Storage, Google Cloud Storage).  Its key characteristic is *schema-on-read*, meaning data is not transformed or structured upon ingestion, allowing for maximum flexibility in downstream consumption. Data lakes are designed to accommodate:
    * **Diverse Data Types:**  Handles structured, semi-structured, and unstructured data (text, images, video, audio) in their native formats.
    * **Variety of Analytical Workloads:** Supports data science exploration, machine learning model training, batch analytics, and ad-hoc querying.
    * **Scalability and Cost-Effectiveness:** Object storage provides massive scalability at a lower cost compared to traditional storage solutions.
    * **Data Discovery and Exploration:** Facilitates data exploration and discovery of new insights from raw data.
    * **Use Case:** Well-suited for organizations dealing with diverse data sources, requiring flexibility for various analytical use cases, and needing cost-effective storage for large volumes of raw data.

    **Crucially, Data Lake Governance is paramount.** Without robust governance, Data Lakes can quickly devolve into "data swamps" – unmanageable repositories of ungoverned, low-quality data.  Effective Data Lake governance requires:
    * **Metadata Management:** Comprehensive metadata cataloging to understand data lineage, schema, and semantics. **Tools:** Data Catalog tools like Apache Atlas, Collibra, Alation, Informatica Enterprise Data Catalog.
    * **Data Cataloging and Discovery Tools:**  Tools to enable users to find and understand available datasets. **Tools:** Data Catalog tools (mentioned above), cloud provider offerings.
    * **Access Control and Security:**  Fine-grained access control policies to protect sensitive data. **Tools:** Cloud IAM services, policy enforcement engines.
    * **Data Quality Frameworks:**  Processes and tools for monitoring and improving data quality within the lake. **Tools:** Data Quality tools like Great Expectations, Deequ, cloud provider data quality services.
    * **Data Lineage Tracking:**  Tracking data transformations and origins to ensure data trustworthiness and auditability. **Tools:** Data Lineage tools like Marquez, OpenLineage, lineage features within data integration platforms.

* **Lakehouse: Bridging the Gap with Transactional Data Lakes and Openness:** The Lakehouse architecture emerges as an attempt to unify the strengths of data lakes and data warehouses, directly on cost-effective data lake storage. It aims to bring the data management, governance, and performance capabilities of a data warehouse to the flexibility and scalability of a data lake.  Key enablers of the Lakehouse pattern are *open table formats* like **Delta Lake, Apache Iceberg, and Apache Hudi.** These are crucial because they:
    * **Enable Vendor Independence:**  Open formats prevent vendor lock-in, allowing portability across different compute engines and platforms.
    * **Ensure Data Portability:** Data stored in open formats can be accessed and processed by various tools and engines, promoting interoperability.
    * **Foster Community and Innovation:** Open source formats benefit from community-driven development and innovation.
    * **ACID Transactions:**  Ensuring data reliability and consistency with transactional guarantees within the data lake.
    * **Schema Enforcement and Governance:**  Enabling schema evolution, data versioning, and data quality enforcement directly on the lake.
    * **BI Performance Optimizations:**  Optimized storage formats (like Parquet), indexing, and query engines to improve performance for BI and analytical workloads.
    * **Unified Data Platform:**  A single platform for diverse workloads, from data science and machine learning to BI and reporting, eliminating data silos.
    * **Use Case:** Ideal for organizations seeking a unified platform for diverse analytical workloads, wanting to leverage cost-effective data lake storage while maintaining data warehouse-like governance and performance, and prioritizing openness and vendor independence.
    
    *   **Unified Governance with Unity Catalog (Databricks):** Within the Databricks ecosystem, Unity Catalog plays a central role in enabling the Lakehouse architecture. It provides a unified metadata management and data governance layer across all Databricks workspaces and clusters. Key features of Unity Catalog include:
        *   **Centralized Metadata Management:** A single, consistent catalog for all data assets (tables, views, files, models) across different Databricks workspaces.

---

## Dimensional Modeling

### The Foundation of Analytical Data Models

Dimensional modeling remains the gold standard for organizing data for analysis. Originally developed by Ralph Kimball, these principles translate well to modern cloud data warehouses.

#### Star Schema Design

The star schema consists of fact tables (measurements) surrounded by dimension tables (context):

```
                    ┌──────────────┐
                    │  dim_date    │
                    └──────┬───────┘
                           │
┌──────────────┐    ┌──────┴───────┐    ┌──────────────┐
│ dim_product  │────│ fact_sales   │────│ dim_customer │
└──────────────┘    └──────┬───────┘    └──────────────┘
                           │
                    ┌──────┴───────┐
                    │  dim_store   │
                    └──────────────┘
```

**Fact Table Design Principles:**

```sql
-- Fact table: Grain is one row per sales transaction line item
CREATE TABLE fact_sales (
    -- Keys (foreign keys to dimensions)
    date_key INTEGER REFERENCES dim_date(date_key),
    product_key INTEGER REFERENCES dim_product(product_key),
    customer_key INTEGER REFERENCES dim_customer(customer_key),
    store_key INTEGER REFERENCES dim_store(store_key),
    
    -- Degenerate dimension (no separate table)
    order_number VARCHAR(50),
    line_number INTEGER,
    
    -- Measures (aggregatable facts)
    quantity_sold INTEGER,
    unit_price DECIMAL(10,2),
    discount_amount DECIMAL(10,2),
    gross_amount DECIMAL(10,2),  -- quantity × unit_price
    net_amount DECIMAL(10,2),    -- gross - discount
    cost_amount DECIMAL(10,2),
    profit_amount DECIMAL(10,2), -- net - cost
    
    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Dimension Table Design:**

```sql
-- Dimension table with Type 2 Slowly Changing Dimension
CREATE TABLE dim_customer (
    -- Surrogate key (system-generated)
    customer_key INTEGER PRIMARY KEY,
    
    -- Natural key (from source system)
    customer_id VARCHAR(50) NOT NULL,
    
    -- Attributes
    customer_name VARCHAR(200),
    email VARCHAR(200),
    customer_segment VARCHAR(50),  -- e.g., 'Premium', 'Standard'
    acquisition_channel VARCHAR(100),
    
    -- SCD Type 2 tracking
    effective_date DATE NOT NULL,
    expiration_date DATE,  -- NULL for current record
    is_current BOOLEAN DEFAULT TRUE,
    
    -- Audit
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

#### Slowly Changing Dimensions (SCDs)

| Type | Behavior | Use Case | Storage Impact |
|------|----------|----------|----------------|
| Type 0 | Never change | Fixed attributes (birth date) | Minimal |
| Type 1 | Overwrite | Corrections, no history needed | Minimal |
| Type 2 | Add new row | Full history needed | High |
| Type 3 | Add column | Limited history (current + previous) | Medium |

**Type 2 SCD Implementation in dbt:**

```sql
-- dbt snapshot for Type 2 SCD
{% snapshot customer_snapshot %}

{{
    config(
      target_schema='snapshots',
      unique_key='customer_id',
      strategy='check',
      check_cols=['customer_name', 'customer_segment', 'email']
    )
}}

SELECT 
    customer_id,
    customer_name,
    email,
    customer_segment,
    acquisition_channel,
    updated_at
FROM {{ source('crm', 'customers') }}

{% endsnapshot %}
```

---

## Data Quality Framework

### Building Trust Through Validation

Data quality is not optional—it's the difference between insights and noise.

#### Quality Dimensions

| Dimension | Definition | Measurement Example |
|-----------|------------|---------------------|
| **Completeness** | Are all required values present? | % of rows with NULL in required fields |
| **Accuracy** | Do values match reality? | % of records matching source of truth |
| **Consistency** | Are values consistent across systems? | % of records with matching values across tables |
| **Timeliness** | Is data available when needed? | Data latency in minutes/hours |
| **Uniqueness** | Are there duplicate records? | % of duplicate primary keys |
| **Validity** | Do values conform to business rules? | % of values outside valid ranges |

#### Implementing Quality Checks with dbt Tests

```yaml
# schema.yml
version: 2

models:
  - name: fact_orders
    description: "One row per order line item"
    columns:
      - name: order_id
        tests:
          - not_null
          - unique
          
      - name: customer_id
        tests:
          - not_null
          - relationships:
              to: ref('dim_customers')
              field: customer_id
              
      - name: order_total
        tests:
          - not_null
          - dbt_utils.expression_is_true:
              expression: ">= 0"
              
      - name: order_date
        tests:
          - not_null
          - dbt_utils.expression_is_true:
              expression: "<= CURRENT_DATE"
              
    tests:
      # Table-level test
      - dbt_utils.equal_rowcount:
          compare_model: ref('stg_orders')
```

#### Great Expectations Integration

```python
# Example Great Expectations suite
import great_expectations as gx

context = gx.get_context()

# Define expectations
suite = context.add_expectation_suite("orders_suite")

# Column expectations
suite.add_expectation(
    expectation_type="expect_column_values_to_not_be_null",
    kwargs={"column": "order_id"}
)

suite.add_expectation(
    expectation_type="expect_column_values_to_be_between",
    kwargs={
        "column": "order_total",
        "min_value": 0,
        "max_value": 100000
    }
)

suite.add_expectation(
    expectation_type="expect_column_values_to_match_regex",
    kwargs={
        "column": "email",
        "regex": r"^[\w\.-]+@[\w\.-]+\.\w+$"
    }
)

# Row count expectations
suite.add_expectation(
    expectation_type="expect_table_row_count_to_be_between",
    kwargs={"min_value": 1000, "max_value": 10000000}
)
```

---

## ETL/ELT Pipeline Patterns

### Modern Data Pipeline Design

#### The Medallion Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    MEDALLION ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   BRONZE (Raw)         SILVER (Cleaned)      GOLD (Curated)     │
│   ─────────────        ───────────────       ──────────────     │
│   • Raw ingestion      • Deduplicated        • Business logic   │
│   • Schema evolution   • Type casting        • Aggregations     │
│   • Append-only        • Null handling       • Dimension tables │
│   • Full history       • Standardization     • Fact tables      │
│                                              • Ready for BI     │
│                                                                  │
│   Source → Bronze → Silver → Gold → Consumption                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Bronze Layer Example:**

```sql
-- Bronze: Raw data, minimal transformation
CREATE TABLE bronze.raw_orders (
    _raw_data VARIANT,  -- Store entire JSON payload
    _source_file STRING,
    _loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    _load_id STRING
);

-- Ingestion pattern
COPY INTO bronze.raw_orders
FROM @stage/orders/
FILE_FORMAT = (TYPE = JSON)
PATTERN = '.*\.json';
```

**Silver Layer Example:**

```sql
-- Silver: Cleaned, typed, deduplicated
CREATE TABLE silver.orders AS
SELECT DISTINCT
    _raw_data:order_id::VARCHAR AS order_id,
    _raw_data:customer_id::INTEGER AS customer_id,
    _raw_data:order_date::DATE AS order_date,
    _raw_data:total::DECIMAL(10,2) AS order_total,
    _raw_data:status::VARCHAR AS order_status,
    
    -- Standardization
    UPPER(TRIM(_raw_data:country::VARCHAR)) AS country,
    
    -- Null handling
    COALESCE(_raw_data:discount::DECIMAL(10,2), 0) AS discount_amount,
    
    -- Metadata
    _loaded_at AS bronze_loaded_at,
    CURRENT_TIMESTAMP AS silver_processed_at
FROM bronze.raw_orders
WHERE _raw_data:order_id IS NOT NULL  -- Data quality filter
QUALIFY ROW_NUMBER() OVER (
    PARTITION BY _raw_data:order_id 
    ORDER BY _loaded_at DESC
) = 1;  -- Deduplication: keep latest
```

**Gold Layer Example:**

```sql
-- Gold: Business-ready aggregations
CREATE TABLE gold.daily_sales_summary AS
SELECT 
    o.order_date,
    d.customer_segment,
    p.product_category,
    
    -- Measures
    COUNT(DISTINCT o.order_id) AS order_count,
    COUNT(DISTINCT o.customer_id) AS unique_customers,
    SUM(o.order_total) AS gross_revenue,
    SUM(o.discount_amount) AS total_discounts,
    SUM(o.order_total - o.discount_amount) AS net_revenue,
    
    -- Derived metrics
    AVG(o.order_total) AS avg_order_value,
    SUM(o.order_total) / COUNT(DISTINCT o.customer_id) AS revenue_per_customer
    
FROM silver.orders o
JOIN gold.dim_customers d ON o.customer_id = d.customer_id
JOIN gold.dim_products p ON o.product_id = p.product_id
GROUP BY 1, 2, 3;
```

---

## Exercises: Data Architecture

### Exercise 1: Schema Design Challenge

**Scenario:** Design a dimensional model for a subscription streaming service (like Netflix/Spotify) that needs to track:
- User viewing/listening history
- Subscription changes over time
- Content metadata
- User engagement metrics

**Question:** Create the fact and dimension tables with appropriate grain and SCD types.

<details>
<summary>✅ Solution</summary>

**Fact Tables:**

```sql
-- FACT: Stream Events (grain: one row per stream start)
CREATE TABLE fact_streams (
    stream_key BIGINT PRIMARY KEY,
    
    -- Dimension keys
    user_key INTEGER REFERENCES dim_users(user_key),
    content_key INTEGER REFERENCES dim_content(content_key),
    date_key INTEGER REFERENCES dim_date(date_key),
    time_key INTEGER REFERENCES dim_time(time_key),
    device_key INTEGER REFERENCES dim_device(device_key),
    subscription_key INTEGER REFERENCES dim_subscription(subscription_key),
    
    -- Degenerate dimensions
    session_id VARCHAR(100),
    
    -- Measures
    stream_duration_seconds INTEGER,
    content_duration_seconds INTEGER,
    completion_percentage DECIMAL(5,2),
    buffer_count INTEGER,
    quality_switches INTEGER,
    
    -- Flags
    is_completed BOOLEAN,
    is_first_stream_of_content BOOLEAN
);

-- FACT: Subscription Events (grain: one row per subscription change)
CREATE TABLE fact_subscription_events (
    event_key BIGINT PRIMARY KEY,
    
    -- Dimension keys
    user_key INTEGER,
    date_key INTEGER,
    
    -- Event details
    event_type VARCHAR(50), -- 'new', 'upgrade', 'downgrade', 'cancel', 'reactivate'
    from_plan VARCHAR(50),
    to_plan VARCHAR(50),
    
    -- Measures
    monthly_revenue_change DECIMAL(10,2),
    annual_revenue_impact DECIMAL(10,2)
);
```

**Dimension Tables:**

```sql
-- DIM: Users (SCD Type 2 for changing attributes)
CREATE TABLE dim_users (
    user_key INTEGER PRIMARY KEY,  -- Surrogate key
    user_id VARCHAR(100),          -- Natural key
    
    -- Attributes
    email VARCHAR(200),
    username VARCHAR(100),
    country VARCHAR(50),
    age_group VARCHAR(20),         -- Derived
    signup_source VARCHAR(50),
    
    -- SCD Type 2
    effective_date DATE,
    expiration_date DATE,
    is_current BOOLEAN
);

-- DIM: Content (SCD Type 1 for corrections, Type 2 for availability)
CREATE TABLE dim_content (
    content_key INTEGER PRIMARY KEY,
    content_id VARCHAR(100),
    
    -- Attributes
    title VARCHAR(500),
    content_type VARCHAR(50),  -- 'movie', 'series', 'episode'
    genre VARCHAR(100),
    release_year INTEGER,
    duration_seconds INTEGER,
    rating VARCHAR(10),
    
    -- Availability (SCD Type 2)
    is_available BOOLEAN,
    available_regions ARRAY,
    
    effective_date DATE,
    expiration_date DATE,
    is_current BOOLEAN
);

-- DIM: Subscription (SCD Type 2)
CREATE TABLE dim_subscription (
    subscription_key INTEGER PRIMARY KEY,
    user_id VARCHAR(100),
    
    plan_name VARCHAR(50),
    monthly_price DECIMAL(10,2),
    max_screens INTEGER,
    has_hd BOOLEAN,
    has_4k BOOLEAN,
    
    effective_date DATE,
    expiration_date DATE,
    is_current BOOLEAN
);

-- DIM: Device (SCD Type 0 - devices don't change)
CREATE TABLE dim_device (
    device_key INTEGER PRIMARY KEY,
    device_type VARCHAR(50),
    os_family VARCHAR(50),
    app_version VARCHAR(20)
);
```

**Design Decisions:**
1. Stream events at "stream start" grain for analysis flexibility
2. Subscription as separate fact for detailed churn analysis
3. Type 2 on subscription to track revenue over time
4. Device as Type 0 (lookup table only)
</details>

---

### Exercise 2: Data Quality Pipeline

**Scenario:** You're receiving order data from an upstream system with known quality issues:
- Duplicate orders (same order_id sent multiple times)
- Missing customer_ids (sometimes NULL)
- Future-dated orders (dates in the future)
- Negative order totals (rare but happens)

**Question:** Design a data quality pipeline that handles these issues.

<details>
<summary>✅ Solution</summary>

**Multi-Layer Quality Approach:**

```sql
-- LAYER 1: Bronze - Ingest everything, flag issues
CREATE TABLE bronze.orders_raw AS
SELECT 
    *,
    CURRENT_TIMESTAMP AS _ingested_at,
    
    -- Quality flags (don't filter, just flag)
    CASE WHEN order_id IS NULL THEN TRUE ELSE FALSE END AS _has_null_id,
    CASE WHEN customer_id IS NULL THEN TRUE ELSE FALSE END AS _has_null_customer,
    CASE WHEN order_date > CURRENT_DATE THEN TRUE ELSE FALSE END AS _has_future_date,
    CASE WHEN order_total < 0 THEN TRUE ELSE FALSE END AS _has_negative_total
FROM source_orders;

-- LAYER 2: Quarantine table for review
CREATE TABLE bronze.orders_quarantine AS
SELECT * FROM bronze.orders_raw
WHERE _has_null_id 
   OR _has_future_date 
   OR _has_negative_total;

-- LAYER 3: Silver - Clean data only
CREATE TABLE silver.orders AS
WITH deduplicated AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY order_id 
            ORDER BY _ingested_at DESC
        ) AS _rn
    FROM bronze.orders_raw
    WHERE NOT _has_null_id
      AND NOT _has_future_date
      AND NOT _has_negative_total
)
SELECT 
    order_id,
    customer_id,
    order_date,
    order_total,
    
    -- Handle missing customer_id
    COALESCE(customer_id, -1) AS customer_id_cleaned,  -- Unknown customer
    customer_id IS NULL AS _is_anonymous_order,
    
    _ingested_at
FROM deduplicated
WHERE _rn = 1;  -- Dedup: keep latest

-- LAYER 4: Quality monitoring table
CREATE TABLE monitoring.data_quality_log AS
SELECT 
    CURRENT_DATE AS check_date,
    'orders' AS table_name,
    
    COUNT(*) AS total_rows,
    SUM(CASE WHEN _has_null_id THEN 1 ELSE 0 END) AS null_id_count,
    SUM(CASE WHEN _has_null_customer THEN 1 ELSE 0 END) AS null_customer_count,
    SUM(CASE WHEN _has_future_date THEN 1 ELSE 0 END) AS future_date_count,
    SUM(CASE WHEN _has_negative_total THEN 1 ELSE 0 END) AS negative_total_count,
    
    -- Quality score
    100.0 * (COUNT(*) - SUM(
        CASE WHEN _has_null_id OR _has_future_date OR _has_negative_total 
        THEN 1 ELSE 0 END
    )) / COUNT(*) AS quality_score_pct
    
FROM bronze.orders_raw
WHERE _ingested_at >= CURRENT_DATE;
```

**Alerting Logic:**

```python
# Airflow task for quality alerts
def check_quality_metrics(**context):
    quality_score = get_latest_quality_score('orders')
    quarantine_count = get_quarantine_count('orders')
    
    if quality_score < 95:
        send_alert(
            channel='#data-alerts',
            message=f"⚠️ Orders quality score: {quality_score}%"
        )
    
    if quarantine_count > 1000:
        send_alert(
            channel='#data-oncall',
            message=f"🚨 {quarantine_count} orders in quarantine - investigate"
        )
```

**Key Principles:**
1. Never delete source data - quarantine instead
2. Flag issues at bronze, filter at silver
3. Log quality metrics for trending
4. Alert on thresholds, not individual records
</details>

---

## Key Takeaways

1. **Architecture patterns serve different needs**: Choose based on organization maturity and data characteristics
2. **Dimensional modeling endures**: Kimball's principles apply to modern cloud warehouses
3. **Data quality is a process, not a check**: Embed quality into every layer
4. **Medallion architecture scales**: Bronze → Silver → Gold provides clear separation
5. **Governance enables trust**: Catalogs, lineage, and contracts are not optional

---

## Further Reading

- [Strategy & Architecture](/best-practices/1-strategy-architecture/)
- [Advanced SQL Patterns](/analytical-engineering/advanced-sql-postgres/)
- [Advanced Exercises](/exercises/advanced/)
- [Data Engineering Track](/tracks/#advanced)
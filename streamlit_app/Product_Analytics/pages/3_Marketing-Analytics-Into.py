import random

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


def generate_website_dashboard_data(
    days=90,
    channels=["Organic", "Paid Ads", "Social", "Email"],
    devices=["Desktop", "Mobile", "Tablet"],
    countries=["USA", "Canada", "UK"],
):
    """Generates synthetic website dashboard data with channels, devices, and countries."""
    dates = pd.date_range(end="today", periods=days)
    data = []
    for date in dates:
        for channel in channels:
            for device in devices:
                for country in countries:
                    users = max(
                        0,
                        int(
                            100
                            + random.gauss(20, 30)
                            + (days - (dates.max() - date).days) * 2
                        ),
                    )  # Users increase over time
                    sessions = max(0, int(users * random.uniform(0.8, 0.95)))
                    page_views = max(0, int(sessions * random.uniform(2, 4)))
                    bounce_rate = (
                        min(100, max(20, int(random.gauss(60, 10)))) / 100
                    )  # Bounce rate around 60%
                    session_duration = max(
                        30, int(random.expovariate(1 / 180))
                    )  # Avg session duration ~ 3 mins
                    conversions = max(
                        0, int(users * random.uniform(0.01, 0.03))
                    )  # Conversion rate 1-3%
                    data.append(
                        [
                            date,
                            channel,
                            device,
                            country,
                            users,
                            sessions,
                            page_views,
                            bounce_rate,
                            session_duration,
                            conversions,
                        ]
                    )
    df = pd.DataFrame(
        data,
        columns=[
            "Date",
            "Channel",
            "Device",
            "Country",
            "Users",
            "Sessions",
            "Page Views",
            "Bounce Rate",
            "Session Duration (Seconds)",
            "Conversions",
        ],
    )
    return df


def generate_multi_channel_ads_data(
    num_campaigns=20,
    channels=["Google Ads", "Facebook Ads", "LinkedIn Ads", "Display Ads"],
):
    """Generates synthetic multi-channel advertising campaign data."""
    data = []
    for channel in channels:
        for i in range(1, num_campaigns + 1):
            campaign_name = f"{channel} Campaign {i}"
            impressions = int(
                random.expovariate(1 / 50000)
            )  # Avg impressions differ by channel
            clicks = int(impressions * random.uniform(0.01, 0.05))  # CTR varies
            spend = clicks * random.uniform(0.5, 2.5)  # CPC varies
            conversions = int(
                clicks * random.uniform(0.02, 0.08)
            )  # Conversion rate varies
            revenue = conversions * random.uniform(
                20, 150
            )  # Revenue per conversion varies
            data.append(
                [
                    campaign_name,
                    channel,
                    impressions,
                    clicks,
                    spend,
                    conversions,
                    revenue,
                ]
            )
    df_ads = pd.DataFrame(
        data,
        columns=[
            "Campaign",
            "Channel",
            "Impressions",
            "Clicks",
            "Spend",
            "Conversions",
            "Revenue",
        ],
    )
    df_ads["CTR"] = df_ads.apply(
        lambda row: (
            (row["Clicks"] / row["Impressions"]) * 100 if row["Impressions"] > 0 else 0
        ),
        axis=1,
    )
    df_ads["CPC"] = df_ads.apply(
        lambda row: row["Spend"] / row["Clicks"] if row["Clicks"] > 0 else 0, axis=1
    )
    df_ads["CPA"] = df_ads.apply(
        lambda row: row["Spend"] / row["Conversions"] if row["Conversions"] > 0 else 0,
        axis=1,
    )
    df_ads["ROAS"] = df_ads.apply(
        lambda row: row["Revenue"] / row["Spend"] if row["Spend"] > 0 else 0, axis=1
    )
    return df_ads


def generate_customer_segmentation_data(num_customers=1000):
    """Generates synthetic customer segmentation data."""
    np.random.seed(42)  # for reproducibility
    age = np.random.randint(18, 70, num_customers)
    gender = np.random.choice(
        ["Male", "Female", "Other"], num_customers, p=[0.45, 0.45, 0.1]
    )
    location = np.random.choice(
        ["USA", "Canada", "UK", "Germany", "France"], num_customers
    )
    website_visits_last_month = np.random.randint(0, 50, num_customers)
    time_on_site_minutes = np.random.randint(1, 120, num_customers)
    pages_visited = np.random.randint(1, 20, num_customers)
    purchase_frequency = np.random.choice(
        ["Low", "Medium", "High"], num_customers, p=[0.5, 0.3, 0.2]
    )
    avg_order_value = np.random.randint(25, 300, num_customers)
    email_engagement_score = np.random.randint(
        0, 100, num_customers
    )  # Higher score = more engagement
    social_media_engagement = np.random.choice(
        ["Low", "Medium", "High"], num_customers, p=[0.4, 0.4, 0.2]
    )

    df_customers = pd.DataFrame(
        {
            "Age": age,
            "Gender": gender,
            "Location": location,
            "Website Visits Last Month": website_visits_last_month,
            "Time on Site (Minutes)": time_on_site_minutes,
            "Pages Visited": pages_visited,
            "Purchase Frequency": purchase_frequency,
            "Average Order Value": avg_order_value,
            "Email Engagement Score": email_engagement_score,
            "Social Media Engagement": social_media_engagement,
        }
    )
    return df_customers


def generate_ab_test_detailed_data(sample_size=1000):
    """Generates more detailed A/B test data with more metrics."""
    group_a_conversions = np.random.binomial(
        1, 0.045, sample_size
    )  # Slightly lower conversion for A
    group_b_conversions = np.random.binomial(
        1, 0.055, sample_size
    )  # Slightly higher conversion for B
    group_a_aov = np.random.normal(45, 15, size=sample_size)  # Avg order value for A
    group_b_aov = np.random.normal(
        50, 18, size=sample_size
    )  # Avg order value for B is a bit higher
    group_a_bounce_rate = np.random.normal(
        0.65, 0.1, size=sample_size
    )  # Higher bounce for A
    group_b_bounce_rate = np.random.normal(
        0.55, 0.08, size=sample_size
    )  # Lower bounce for B
    group_a_time_on_page = np.random.normal(
        120, 40, size=sample_size
    )  # Less time on page for A
    group_b_time_on_page = np.random.normal(
        150, 50, size=sample_size
    )  # More time on page for B

    df_ab_detailed = pd.DataFrame(
        {
            "Group": ["A"] * sample_size + ["B"] * sample_size,
            "Converted": np.concatenate(
                [group_a_conversions, group_b_conversions]
            ).astype(bool),
            "Average Order Value": np.concatenate([group_a_aov, group_b_aov]),
            "Bounce Rate": np.concatenate([group_a_bounce_rate, group_b_bounce_rate]),
            "Time on Page (Seconds)": np.concatenate(
                [group_a_time_on_page, group_b_time_on_page]
            ),
        }
    )
    df_ab_detailed["Average Order Value"] = df_ab_detailed["Average Order Value"].clip(
        lower=10
    )  # Ensure AOV is not too low
    df_ab_detailed["Bounce Rate"] = df_ab_detailed["Bounce Rate"].clip(
        0, 1
    )  # Ensure bounce rate is between 0 and 1
    df_ab_detailed["Time on Page (Seconds)"] = df_ab_detailed[
        "Time on Page (Seconds)"
    ].clip(
        lower=30
    )  # Ensure time on page is not too low

    return df_ab_detailed


def generate_customer_journey_attribution_data(num_journeys=1000):
    """Generates customer journey data with conversion value for attribution."""
    channels = [
        "Organic Search",
        "Paid Ads",
        "Social Media",
        "Email Marketing",
        "Direct",
    ]
    journey_data = []
    for _ in range(num_journeys):
        journey_length = random.randint(1, 5)
        journey_path = random.choices(channels, k=journey_length)
        conversion = random.random() < 0.15  # 15% conversion rate
        conversion_value = 0
        if conversion:
            conversion_value = random.uniform(50, 500)  # Conversion value varies
        journey_data.append(
            {
                "Journey Path": journey_path,
                "Conversion": conversion,
                "Conversion Value": conversion_value,
            }
        )
    return pd.DataFrame(journey_data)


def last_click_attribution(journey_df):
    """Performs last-click attribution."""
    attributed_conversions = {}
    for index, row in journey_df.iterrows():
        if row["Conversion"]:
            last_touch_channel = row["Journey Path"][-1]
            attributed_conversions[last_touch_channel] = (
                attributed_conversions.get(last_touch_channel, 0)
                + row["Conversion Value"]
            )
    return attributed_conversions


def first_click_attribution(journey_df):
    """Performs first-click attribution."""
    attributed_conversions = {}
    for index, row in journey_df.iterrows():
        if row["Conversion"]:
            first_touch_channel = row["Journey Path"][0]
            attributed_conversions[first_touch_channel] = (
                attributed_conversions.get(first_touch_channel, 0)
                + row["Conversion Value"]
            )
    return attributed_conversions


def linear_attribution(journey_df):
    """Performs linear attribution."""
    attributed_conversions = {}
    for index, row in journey_df.iterrows():
        if row["Conversion"]:
            path_length = len(row["Journey Path"])
            value_per_touch = row["Conversion Value"] / path_length
            for channel in row["Journey Path"]:
                attributed_conversions[channel] = (
                    attributed_conversions.get(channel, 0) + value_per_touch
                )
    return attributed_conversions


def calculate_ctr(impressions, clicks):
    """Calculates Click-Through Rate (CTR)."""
    if impressions == 0:
        return 0
    return (clicks / impressions) * 100


def calculate_conversion_rate(clicks, conversions):
    """Calculates Conversion Rate."""
    if clicks == 0:
        return 0
    return (conversions / clicks) * 100


def calculate_roas(ad_spend, revenue):
    """Calculates Return on Ad Spend (ROAS)."""
    if ad_spend == 0:
        return 0
    return revenue / ad_spend


def generate_ab_test_data(sample_size=1000):
    """Generates synthetic A/B test data."""
    group_a_conversions = np.random.binomial(
        1, 0.05, sample_size
    )  # 5% conversion rate for group A
    group_b_conversions = np.random.binomial(
        1, 0.065, sample_size
    )  # 6.5% conversion rate for group B
    df = pd.DataFrame(
        {
            "Group": ["A"] * sample_size + ["B"] * sample_size,
            "Converted": np.concatenate([group_a_conversions, group_b_conversions]),
        }
    )
    df["Converted"] = df["Converted"].astype(bool)  # Convert to boolean for readability
    return df


def generate_customer_journey_data(num_journeys=100):
    """Generates synthetic customer journey data."""
    channels = [
        "Organic Search",
        "Paid Ads",
        "Social Media",
        "Email Marketing",
        "Direct",
    ]
    touchpoints_per_journey = random.choices(
        range(1, 6), k=num_journeys
    )  # Random number of touchpoints
    journey_data = []
    for i in range(num_journeys):
        journey = random.choices(channels, k=touchpoints_per_journey[i])
        converted = random.random() < 0.2  # 20% overall conversion rate
        journey_data.append({"Journey": journey, "Converted": converted})
    return pd.DataFrame(journey_data)


def show_fundamentals():
    st.header("1. Understanding the Fundamentals of Marketing Analytics")
    with st.expander("1.1 Defining Marketing Analytics", expanded=True):
        st.subheader("1.1 Defining Marketing Analytics")
        st.markdown(
            """
            **Definition:** Marketing analytics is the process of **measuring, managing, and analyzing marketing performance** to maximize its effectiveness and optimize return on investment (ROI). It's about using data and statistical techniques to understand marketing activities, gain customer insights, and make informed, data-driven decisions.

            **Core Objectives of Marketing Analytics:**
            *   **Measuring Marketing Performance:**  Track and evaluate the effectiveness of campaigns, channels, and initiatives.
            *   **Understanding Customer Behavior:** Gain insights into customer preferences, needs, journeys, and interactions.
            *   **Optimizing Marketing Strategies:** Identify improvements, refine tactics, and allocate resources efficiently.
            *   **Improving Marketing ROI:** Demonstrate marketing value and maximize returns on investments.
            *   **Predicting Future Trends:** Forecast market changes, customer behavior shifts, and campaign outcomes.
            *   **Personalizing Customer Experiences:** Tailor messages and offers to individual customer needs.
        """
        )

    with st.expander("1.2 The Importance of Marketing Analytics", expanded=True):
        st.subheader("1.2 The Importance of Marketing Analytics")
        st.markdown(
            """
            Marketing analytics is crucial in today's business environment for several reasons:

            *   **Data-Driven Decision Making:** Shift from guesswork to evidence-based strategies, leading to more effective decisions.
            *   **Improved Campaign Performance:** Optimize campaigns in real-time for better engagement, conversions, and results.
            *   **Enhanced Customer Understanding:** Gain deep insights into customer needs and behaviors for more effective targeting and messaging.
            *   **Increased Marketing ROI:** Justify marketing investments with measurable results and optimize resource allocation.
            *   **Competitive Advantage:** Leverage data to identify market opportunities and adapt to trends faster than competitors.
            *   **Personalized Customer Experiences:** Deliver relevant and personalized experiences to boost satisfaction and loyalty.
            *   **Accountability and Transparency:** Provide clear metrics and reports for accountability to stakeholders.
        """
        )


def show_core_components():
    st.header("2. Core Components of Marketing Analytics")
    with st.expander("2.1 Types of Marketing Data", expanded=True):
        st.subheader("2.1 Types of Marketing Data")
        st.markdown(
            """
            Effective marketing analytics relies on diverse data sources. Key types include:

            *   **Web Analytics Data:** Website interactions (traffic, page views, bounce rates) from tools like Google Analytics, Adobe Analytics.
            *   **Social Media Data:** Engagement metrics, follower growth, sentiment from platforms' analytics and tools.
            *   **CRM Data:** Customer demographics, purchase history, interactions from CRM systems (Salesforce, HubSpot).
            *   **Advertising Data:** Impressions, clicks, CTR, conversions, ad spend from platforms (Google Ads, Facebook Ads).
            *   **Email Marketing Data:** Open rates, CTR, bounce rates, conversions from platforms (Mailchimp, Marketo).
            *   **Sales Data:** Sales revenue, units sold, order value, product performance, sales cycle.
            *   **Customer Feedback Data:** Surveys, reviews, feedback forms, customer service interactions (qualitative and quantitative).
            *   **Market Research Data:** Surveys, focus groups, competitor analysis for broader market context.
            *   **Location Data:** Geolocation data for understanding customer movement and geographic targeting.
        """
        )

    with st.expander("2.2 Key Marketing Metrics and KPIs", expanded=True):
        st.subheader("2.2 Key Marketing Metrics and KPIs")
        st.markdown(
            """
            **Key Performance Indicators (KPIs)** and metrics are vital for measuring marketing success. Common categories include:

            *   **Website Traffic Metrics:** Unique Visitors, Page Views, Bounce Rate, Session Duration, Traffic Sources.
            *   **Social Media Metrics:** Engagement Rate, Reach, Impressions, Follower Growth, Social Sentiment.
            *   **Advertising Metrics:** Click-Through Rate (CTR), Conversion Rate, Cost Per Click (CPC), Cost Per Acquisition (CPA), Return on Ad Spend (ROAS).
            *   **Email Marketing Metrics:** Open Rate, Click-Through Rate (CTR), Conversion Rate, Bounce Rate, Unsubscribe Rate.
            *   **Sales and Revenue Metrics:** Sales Revenue, Overall Conversion Rate, Customer Acquisition Cost (CAC), Customer Lifetime Value (CLTV), Return on Marketing Investment (ROMI).
            *   **Customer-Centric Metrics:** Customer Satisfaction (CSAT), Net Promoter Score (NPS), Customer Retention Rate, Churn Rate.
        """
        )

    with st.expander("2.3 The Marketing Analytics Process", expanded=True):
        st.subheader("2.3 The Marketing Analytics Process")
        st.markdown(
            """
            A structured process is key to effective marketing analytics:

            1.  **Define Objectives and KPIs:** Clearly define marketing goals and metrics for success.
            2.  **Data Collection and Integration:** Gather data from various sources and unify it.
            3.  **Data Cleaning and Preparation:** Ensure data accuracy and consistency.
            4.  **Data Analysis and Exploration:** Apply techniques to find patterns and trends.
            5.  **Insight Generation and Interpretation:** Translate analysis into actionable insights.
            6.  **Reporting and Visualization:** Create dashboards and reports to communicate findings.
            7.  **Action and Implementation:** Apply insights to optimize marketing activities.
            8.  **Measurement and Iteration:** Monitor results and refine strategies continuously.

            This is a continuous cycle of improvement.
        """
        )


def show_types_of_analytics():
    st.header("3. Types of Marketing Analytics")
    with st.expander("3.1 By Analytical Approach", expanded=True):
        st.subheader("3.1 By Analytical Approach")
        st.markdown(
            """
            Marketing analytics can be categorized by the type of questions they answer:

            *   **Descriptive Analytics (What happened?):** Summarizes past performance. Examples: traffic reports, engagement summaries, sales dashboards.
            *   **Diagnostic Analytics (Why did it happen?):** Investigates reasons behind outcomes. Examples: analyzing traffic drops, poor campaign performance.
            *   **Predictive Analytics (What will happen?):** Forecasts future trends. Examples: predicting churn, sales forecasts, campaign conversion predictions.
            *   **Prescriptive Analytics (What should we do?):** Recommends optimal actions. Examples: personalized offers, ad spend optimization, content strategies.
        """
        )

    with st.expander("3.2 By Marketing Domain", expanded=True):
        st.subheader("3.2 By Marketing Domain")
        st.markdown(
            """
            Marketing analytics is also categorized by specific marketing areas:

            *   **Web Analytics:** Website user behavior and performance. Tools: Google Analytics, Adobe Analytics.
            *   **Social Media Analytics:** Social performance, engagement, sentiment. Tools: Sprout Social, Hootsuite, Brandwatch.
            *   **SEO Analytics:** Search rankings, organic traffic, keyword performance. Tools: SEMrush, Ahrefs, Google Search Console.
            *   **Content Analytics:** Content performance, engagement. Metrics: page views, time on page, shares.
            *   **Email Marketing Analytics:** Email campaign performance. Tools: Mailchimp, Marketo analytics.
            *   **CRM Analytics:** Customer behavior, segmentation. Tools: CRM platform analytics.
            *   **Customer Analytics:** Customer lifecycle, value, journey. Techniques: segmentation, cohort analysis, CLTV.
            *   **Mobile Analytics:** Mobile app usage and marketing performance. Tools: Firebase Analytics, Mixpanel.
            *   **Advertising Analytics:** Ad campaign performance. Tools: Ad platform dashboards.
        """
        )

    with st.expander("4. Business Use Cases of Marketing Analytics", expanded=False):
        st.header("4. Business Use Cases of Marketing Analytics")

        st.markdown(
            """
            Marketing analytics is applied across numerous business functions:

            *   **Campaign Optimization:** A/B testing, real-time adjustments, budget allocation.
            *   **Customer Segmentation and Targeting:** Identifying segments, targeted campaigns, personalized journeys.
            *   **Personalization:** Website, email, and dynamic content personalization.
            *   **Lead Scoring and Conversion Optimization:** Lead scoring models, funnel optimization.
            *   **Customer Lifetime Value (CLTV) Analysis:** Predicting CLTV, retention strategies.
            *   **Attribution Modeling:** Channel effectiveness, multi-touch attribution, channel mix optimization.
            *   **Market Basket Analysis:** Product associations, cross-selling, up-selling.
            *   **Sentiment Analysis:** Brand sentiment monitoring, issue detection.
            *   **Churn Prediction:** Identifying at-risk customers, proactive retention.
        """
        )


def show_challenges_and_best_practices():
    st.header("6. Challenges and Best Practices in Marketing Analytics")
    with st.expander("6.1 Challenges", expanded=True):
        st.subheader("6.1 Challenges")
        st.markdown(
            """
            Implementing marketing analytics effectively faces hurdles:

            *   **Data Quality Issues:** Inaccurate, incomplete, or inconsistent data.
            *   **Data Silos:** Disconnected data sources hindering a holistic view.
            *   **Lack of Data Literacy and Skills Gap:** Shortage of skilled analysts.
            *   **Privacy Concerns and Data Regulations (GDPR, CCPA):** Compliance and ethical data use.
            *   **Attribution Complexity:** Accurately crediting marketing efforts in complex journeys.
            *   **Actionable Insights vs. Data Overload:** Extracting meaningful insights from massive data.
            *   **Measuring ROI and Proving Marketing Value:** Demonstrating tangible marketing impact.
            *   **Keeping Up with Technology and Trends:** Rapidly evolving analytics landscape.
        """
        )

    with st.expander("6.2 Best Practices", expanded=True):
        st.subheader("6.2 Best Practices")
        st.markdown(
            """
            Overcome challenges by following best practices:

            *   **Establish Clear Objectives and KPIs (SMART):** Define specific, measurable goals.
            *   **Prioritize Data Quality and Governance:** Implement data management processes.
            *   **Integrate Data Sources:** Unify data from different channels.
            *   **Invest in Data Analytics Skills and Training:** Develop in-house capabilities.
            *   **Focus on Actionable Insights:** Go beyond reporting to strategic guidance.
            *   **Visualize Data Effectively:** Use dashboards for clear communication.
            *   **Embrace Experimentation and A/B Testing:** Foster a culture of continuous improvement.
            *   **Adopt a Customer-Centric Approach:** Focus on understanding customer needs.
            *   **Measure and Demonstrate Marketing ROI:** Track performance and communicate value.
            *   **Stay Updated on Industry Trends and Technologies:** Continuous learning.
        """
        )


def main():  # noqa: C901
    st.set_page_config(
        page_title="Marketing Analytics Guide", page_icon="📈", layout="wide"
    )
    st.title("Marketing Analytics: An In-Depth Guide 📈")
    st.write(
        """
        Unlock the power of data in marketing! This interactive guide will walk you through the essentials of marketing analytics,
        from fundamental concepts to real-world applications and future trends. Master data-driven marketing and elevate your strategies.
    """
    )

    show_fundamentals()
    show_core_components()
    show_types_of_analytics()
    show_challenges_and_best_practices()
    st.header("🕹️ Interactive Marketing Analytics Explorations")
    with st.expander(
        "📊 Website Traffic Dashboard (Descriptive Analytics)", expanded=True
    ):
        st.subheader("Interactive Website Traffic Dashboard")
        st.write(
            "Explore website performance across different dimensions and metrics. Use the filters below to investigate trends and patterns."
        )

        website_df = generate_website_dashboard_data()

        # Filters
        col1, col2 = st.columns(2)
        selected_channel_dashboard = col1.multiselect(
            "Filter by Channel:",
            website_df["Channel"].unique(),
            default=website_df["Channel"].unique(),
        )
        selected_device_dashboard = col2.multiselect(
            "Filter by Device:",
            website_df["Device"].unique(),
            default=website_df["Device"].unique(),
        )

        filtered_website_df = website_df[
            website_df["Channel"].isin(selected_channel_dashboard)
            & website_df["Device"].isin(selected_device_dashboard)
        ]

        # Metrics Selection
        metric_options_dashboard = [
            "Users",
            "Sessions",
            "Page Views",
            "Bounce Rate",
            "Session Duration (Seconds)",
            "Conversions",
        ]
        selected_metric_dashboard = st.selectbox(
            "Choose Metric to Visualize:", metric_options_dashboard, index=0
        )

        # Time Aggregation
        time_aggregation_dashboard = st.selectbox(
            "Time Aggregation:", ["Daily", "Weekly", "Monthly"], index=1
        )
        if time_aggregation_dashboard == "Weekly":
            filtered_website_df["Date"] = (
                filtered_website_df["Date"].dt.to_period("W").dt.to_timestamp()
            )
        elif time_aggregation_dashboard == "Monthly":
            filtered_website_df["Date"] = (
                filtered_website_df["Date"].dt.to_period("M").dt.to_timestamp()
            )

        aggregated_df_dashboard = (
            filtered_website_df.groupby("Date")[selected_metric_dashboard]
            .sum()
            .reset_index()
            if selected_metric_dashboard
            not in ["Bounce Rate", "Session Duration (Seconds)"]
            else filtered_website_df.groupby("Date")[selected_metric_dashboard]
            .mean()
            .reset_index()
        )  # Mean for rate/duration

        fig_website_dashboard = px.line(
            aggregated_df_dashboard,
            x="Date",
            y=selected_metric_dashboard,
            title=f"Website {selected_metric_dashboard} Trends ({time_aggregation_dashboard} Aggregation)",
        )
        st.plotly_chart(fig_website_dashboard, use_container_width=True)

        st.markdown("**Exploration Questions:**")
        st.markdown(
            "* What are the overall trends for **Users, Sessions, and Conversions** over time? Are they increasing, decreasing, or stable?"
        )
        st.markdown(
            "* How does the **Bounce Rate** fluctuate? Are there any spikes or dips that might correlate with specific dates or events?"
        )
        st.markdown(
            "* Investigate **Channel** performance: Filter by individual channels (e.g., 'Organic', 'Paid Ads') to compare their contribution to traffic and conversions."
        )
        st.markdown(
            "* Compare **Device** performance: How does website behavior differ between 'Desktop' and 'Mobile' users in terms of session duration or bounce rate?"
        )
        st.markdown(
            "* Try changing the **Time Aggregation** to 'Weekly' or 'Monthly' to smooth out daily fluctuations and see longer-term trends more clearly."
        )

    with st.expander(
        "💰 Multi-Channel Ad Campaign Analyzer (Performance & Diagnostic)",
        expanded=True,
    ):
        st.subheader("Multi-Channel Advertising Campaign Performance Analyzer")
        st.write(
            "Analyze and compare the performance of different ad campaigns across multiple channels. Sort and filter to identify top and bottom performers."
        )

        ads_df = generate_multi_channel_ads_data()

        # Channel Filter
        selected_channels_ads = st.multiselect(
            "Filter by Channel:",
            ads_df["Channel"].unique(),
            default=ads_df["Channel"].unique(),
        )
        filtered_ads_df = ads_df[ads_df["Channel"].isin(selected_channels_ads)]

        # Metric Selection & Sorting
        col_sort_metric, col_sort_order = st.columns(2)
        sort_metric_ads = col_sort_metric.selectbox(
            "Sort Campaigns By:",
            [
                "Impressions",
                "Clicks",
                "Spend",
                "Conversions",
                "Revenue",
                "ROAS",
                "CTR",
                "CPC",
                "CPA",
            ],
            index=5,
        )  # Default ROAS
        sort_ascending_ads = col_sort_order.selectbox(
            "Sort Order:",
            [False, True],
            format_func=lambda x: "Descending" if not x else "Ascending",
        )  # Descending as default

        sorted_ads_df = filtered_ads_df.sort_values(
            by=sort_metric_ads, ascending=sort_ascending_ads
        )

        st.dataframe(sorted_ads_df, use_container_width=True)

        # Channel Performance Bar Chart
        channel_performance_ads = (
            filtered_ads_df.groupby("Channel")[["Spend", "Revenue", "Conversions"]]
            .sum()
            .reset_index()
        )
        performance_metric_chart_ads = st.selectbox(
            "Visualize Channel Performance By:",
            ["Spend", "Revenue", "Conversions", "ROAS"],
            index=1,
        )  # Default Revenue

        if performance_metric_chart_ads == "ROAS":
            channel_performance_ads["ROAS"] = channel_performance_ads.apply(
                lambda row: row["Revenue"] / row["Spend"] if row["Spend"] > 0 else 0,
                axis=1,
            )
            fig_channel_ads = px.bar(
                channel_performance_ads,
                x="Channel",
                y="ROAS",
                title="Channel ROAS Comparison",
                labels={"ROAS": "Return on Ad Spend"},
            )
        else:
            fig_channel_ads = px.bar(
                channel_performance_ads,
                x="Channel",
                y=performance_metric_chart_ads,
                title=f"Channel {performance_metric_chart_ads} Comparison",
                labels={performance_metric_chart_ads: performance_metric_chart_ads},
            )

        st.plotly_chart(fig_channel_ads, use_container_width=True)

        st.markdown("**Exploration Questions:**")
        st.markdown(
            "* **Identify top-performing campaigns:** Sort by 'Revenue' or 'ROAS' in descending order. Which campaigns are generating the most revenue and return?"
        )
        st.markdown(
            "* **Find underperforming campaigns:** Sort by 'ROAS' in ascending order. Are there campaigns with low or even negative ROAS that need attention?"
        )
        st.markdown(
            "* **Compare channel efficiency:** Look at the 'Channel Performance' bar chart, visualizing 'ROAS' or 'CPA'. Which channels are most cost-effective in driving conversions and revenue?"
        )
        st.markdown(
            "* **Investigate high-spend vs. high-return:** Is there a correlation between 'Spend' and 'Revenue'? Are campaigns with higher spend always delivering proportionally higher returns? Sort by 'Spend' and then examine 'ROAS'."
        )
        st.markdown(
            "* **Examine CTR and CPC:** Sort by 'CTR' and 'CPC'. Are there channels or campaigns with unusually high or low click-through rates or cost per click? What might explain these differences?"
        )

    with st.expander(
        "👤 Customer Segmentation Explorer (Customer Analytics)", expanded=True
    ):
        st.subheader("Customer Segmentation Explorer")
        st.write(
            "Explore customer data to identify segments based on demographics, behavior, and engagement. Visualize segments and understand their characteristics."
        )

        customer_df = generate_customer_segmentation_data()

        segment_by_options = [
            "Gender",
            "Location",
            "Purchase Frequency",
            "Social Media Engagement",
        ]
        segment_by = st.selectbox("Segment Customers By:", segment_by_options, index=0)

        col_scatter_x, col_scatter_y = st.columns(2)
        scatter_x_metric = col_scatter_x.selectbox(
            "Scatter Plot - X-axis:",
            [
                "Age",
                "Website Visits Last Month",
                "Time on Site (Minutes)",
                "Pages Visited",
                "Average Order Value",
                "Email Engagement Score",
            ],
            index=0,
        )
        scatter_y_metric = col_scatter_y.selectbox(
            "Scatter Plot - Y-axis:",
            [
                "Age",
                "Website Visits Last Month",
                "Time on Site (Minutes)",
                "Pages Visited",
                "Average Order Value",
                "Email Engagement Score",
            ],
            index=4,
        )  # Default AOV

        fig_segmentation = px.scatter(
            customer_df,
            x=scatter_x_metric,
            y=scatter_y_metric,
            color=segment_by,
            title=f"Customer Segmentation by {segment_by}",
            labels={
                scatter_x_metric: scatter_x_metric,
                scatter_y_metric: scatter_y_metric,
                "color": segment_by,
            },
        )
        st.plotly_chart(fig_segmentation, use_container_width=True)

        segment_summary = (
            customer_df.groupby(segment_by)[
                [
                    "Age",
                    "Website Visits Last Month",
                    "Time on Site (Minutes)",
                    "Pages Visited",
                    "Average Order Value",
                    "Email Engagement Score",
                ]
            ]
            .mean()
            .reset_index()
        )
        st.dataframe(segment_summary, use_container_width=True)

        st.markdown("**Exploration Questions:**")
        st.markdown(
            "* **Identify segments with high Average Order Value:** Segment by 'Purchase Frequency' or 'Social Media Engagement' and examine the 'Average Order Value' in the summary table. Which segments have the highest AOV?"
        )
        st.markdown(
            "* **Explore engagement differences:** Segment by 'Gender' or 'Location' and compare the 'Website Visits Last Month' or 'Email Engagement Score'. Are there noticeable differences in engagement levels across segments?"
        )
        st.markdown(
            "* **Visualize segment clusters:** Use the scatter plot, plotting 'Average Order Value' vs. 'Website Visits Last Month' and color by different segmentation variables (e.g., 'Purchase Frequency', 'Gender'). Do you see distinct clusters forming for different segments?"
        )
        st.markdown(
            "* **Analyze segment profiles:** For each segment (e.g., 'High' Purchase Frequency customers), look at the average values in the summary table for 'Age', 'Time on Site', 'Email Engagement Score'. Can you describe the typical profile of customers within each segment?"
        )
        st.markdown(
            "* **Consider actionable segments:** Based on your exploration, which segments might be most valuable to target with personalized marketing campaigns? Why?"
        )

    with st.expander(
        "🔬 A/B Test Deep Dive Analyzer (Diagnostic & Statistical)", expanded=True
    ):
        st.subheader("Detailed A/B Test Result Analyzer")
        st.write(
            "Analyze A/B test results across multiple metrics to determine the winning variant and understand the impact beyond just conversion rates."
        )

        ab_detailed_df = generate_ab_test_detailed_data()

        st.dataframe(
            ab_detailed_df.describe().T, use_container_width=True
        )  # Summary statistics

        metric_options_ab_detailed = [
            "Converted",
            "Average Order Value",
            "Bounce Rate",
            "Time on Page (Seconds)",
        ]
        for metric in metric_options_ab_detailed:
            fig_box = px.box(
                ab_detailed_df,
                x="Group",
                y=metric,
                color="Group",
                title=f"Distribution of {metric} by Group",
                labels={metric: metric},
            )
            st.plotly_chart(fig_box, use_container_width=True)

        st.markdown("**Analysis & Exploration Questions:**")
        st.markdown(
            "* **Compare Conversion Rates:** Examine the 'Converted' box plot and the summary statistics. Is there a noticeable and practically significant difference in conversion rates between Group A and Group B?"
        )
        st.markdown(
            "* **Analyze Average Order Value (AOV):** Look at the 'Average Order Value' box plot. Does one group have a significantly higher AOV? If so, this could contribute to overall revenue increase even if conversion rate difference is small."
        )
        st.markdown(
            "* **Investigate Bounce Rate:** Compare 'Bounce Rate' distributions. A lower bounce rate in one group (like Group B potentially) suggests a better user experience on that variant."
        )
        st.markdown(
            "* **Examine Time on Page:** Analyze 'Time on Page' distributions. Higher time on page for a variant could indicate more engaging content, even if it doesn't directly translate to much higher conversions immediately."
        )
        st.markdown(
            "* **Overall Winner?**: Considering all metrics (Conversion Rate, AOV, Bounce Rate, Time on Page), which group (A or B) appears to be the more successful variant overall? Is the 'winner' clear-cut, or are there trade-offs?"
        )
        st.markdown(
            "* **Statistical Significance (Conceptual):** While this demo doesn't perform formal statistical tests, visually inspect the box plots. Are the medians and distributions clearly separated, suggesting a potentially meaningful difference? For a real A/B test, you would perform statistical significance tests to confirm if the observed differences are not just due to random chance."
        )

    with st.expander(
        "🔄 Customer Journey Attribution Modeler (Attribution Modeling)", expanded=True
    ):
        st.subheader("Customer Journey Attribution Modeling")
        st.write(
            "Explore how different attribution models can change the perceived value of marketing channels. Select an attribution model and compare channel performance."
        )

        attribution_df = generate_customer_journey_attribution_data(num_journeys=500)

        attribution_model_options = ["Last Click", "First Click", "Linear"]
        selected_attribution_model = st.selectbox(
            "Choose Attribution Model:", attribution_model_options, index=0
        )

        if selected_attribution_model == "Last Click":
            attributed_conversions_data = last_click_attribution(attribution_df)
        elif selected_attribution_model == "First Click":
            attributed_conversions_data = first_click_attribution(attribution_df)
        elif selected_attribution_model == "Linear":
            attributed_conversions_data = linear_attribution(attribution_df)
        else:
            attributed_conversions_data = {}

        attributed_channels = list(attributed_conversions_data.keys())
        attributed_values = list(attributed_conversions_data.values())
        attribution_results_df = pd.DataFrame(
            {"Channel": attributed_channels, "Attributed Value": attributed_values}
        )

        fig_attribution = px.bar(
            attribution_results_df,
            x="Channel",
            y="Attributed Value",
            title=f"{selected_attribution_model} Attribution Model - Channel Performance",
            labels={"Attributed Value": "Attributed Conversion Value"},
        )
        st.plotly_chart(fig_attribution, use_container_width=True)
        st.dataframe(attribution_results_df, use_container_width=True)

        st.markdown("**Exploration Questions:**")
        st.markdown(
            "* **Compare Channel Rankings:** Switch between 'Last Click', 'First Click', and 'Linear' attribution models. How does the ranking of channels by 'Attributed Value' change across models? Which channels gain or lose value depending on the model?"
        )
        st.markdown(
            "* **Last-Click Bias:** Observe the results under 'Last Click' attribution. Is 'Direct' traffic always the top channel? Why might last-click attribution overemphasize 'Direct' and under value earlier touchpoints?"
        )
        st.markdown(
            "* **First-Click Emphasis:** Examine 'First Click' attribution. Which channels are now valued more highly? How does first-click attribution shift the focus to top-of-funnel channels that initiate customer journeys?"
        )
        st.markdown(
            "* **Linear Distribution:** Analyze 'Linear' attribution. How does it distribute value across all touchpoints in the journey? Is the channel value distribution more even compared to last-click or first-click?"
        )
        st.markdown(
            "* **Strategic Implications:** If you were making budget allocation decisions based on these attribution models, how might your channel investment strategy differ depending on whether you used last-click, first-click, or linear attribution?"
        )
        st.markdown(
            "* **Model Choice Considerations:**  Which attribution model do you think might be most appropriate for different marketing objectives (e.g., brand awareness vs. direct response)? What are the limitations of each model?"
        )

    st.header("✅ Knowledge Check Quiz: Test Your Understanding of Marketing Analytics")
    quiz_questions = [
        {
            "question": "What is the primary goal of marketing analytics?",
            "options": [
                "To increase marketing spend",
                "To make marketing decisions based on intuition",
                "To measure and optimize marketing performance using data",
                "To automate all marketing activities",
            ],
            "answer": "To measure and optimize marketing performance using data",
            "solution": "Marketing analytics is fundamentally about using data to improve marketing effectiveness and ROI.",
        },
        {
            "question": "Which of the following is an example of descriptive analytics in marketing?",
            "options": [
                "Predicting customer churn",
                "Analyzing website traffic trends over the past year",
                "Recommending products to customers",
                "Optimizing ad spend allocation",
            ],
            "answer": "Analyzing website traffic trends over the past year",
            "solution": "Descriptive analytics focuses on summarizing and describing past data, like website traffic trends.",
        },
        {
            "question": "What does KPI stand for in marketing analytics?",
            "options": [
                "Key Process Improvement",
                "Knowledge Performance Indicator",
                "Key Performance Indicator",
                "Keep Promoting Initiatives",
            ],
            "answer": "Key Performance Indicator",
            "solution": "KPIs are crucial metrics to measure the success of marketing activities against objectives.",
        },
        {
            "question": "Which type of marketing data is typically collected from CRM systems?",
            "options": [
                "Website traffic data",
                "Social media engagement data",
                "Customer demographics and purchase history",
                "Advertising campaign performance data",
            ],
            "answer": "Customer demographics and purchase history",
            "solution": "CRM systems are designed to store and manage customer-related data, including demographics and transaction history.",
        },
        {
            "question": "What is the purpose of diagnostic analytics in marketing?",
            "options": [
                "To describe past marketing performance",
                "To predict future marketing outcomes",
                "To understand why certain marketing outcomes occurred",
                "To recommend optimal marketing actions",
            ],
            "answer": "To understand why certain marketing outcomes occurred",
            "solution": "Diagnostic analytics aims to investigate the reasons and causes behind observed marketing results.",
        },
        {
            "question": "Which metric directly measures the profitability of advertising spend?",
            "options": [
                "Click-Through Rate (CTR)",
                "Conversion Rate",
                "Cost Per Click (CPC)",
                "Return on Ad Spend (ROAS)",
            ],
            "answer": "Return on Ad Spend (ROAS)",
            "solution": "ROAS calculates the revenue generated for every dollar spent on advertising, directly indicating profitability.",
        },
        {
            "question": "What is 'data integration' in the marketing analytics process?",
            "options": [
                "Cleaning and preparing data",
                "Analyzing data for insights",
                "Combining data from different sources into a unified view",
                "Visualizing data in dashboards",
            ],
            "answer": "Combining data from different sources into a unified view",
            "solution": "Data integration is essential to overcome data silos and get a holistic view of marketing performance.",
        },
        {
            "question": "Which future trend in marketing analytics involves using AI to automatically surface insights and recommendations?",
            "options": [
                "Predictive Customer Journeys",
                "Hyper-Personalization at Scale",
                "Augmented Analytics",
                "Voice and Conversational Analytics",
            ],
            "answer": "Augmented Analytics",
            "solution": "Augmented analytics leverages AI to make analytics more accessible and insightful even for non-experts.",
        },
        {
            "question": "What is a key challenge related to 'attribution complexity' in marketing analytics?",
            "options": [
                "Ensuring data quality",
                "Measuring the ROI of marketing activities",
                "Accurately crediting marketing touchpoints in multi-channel journeys",
                "Keeping up with technology trends",
            ],
            "answer": "Accurately crediting marketing touchpoints in multi-channel journeys",
            "solution": "Attribution complexity arises from the need to understand the contribution of each marketing channel and touchpoint in the customer journey.",
        },
        {
            "question": "Which best practice is crucial for ensuring marketing analytics leads to strategic actions?",
            "options": [
                "Focusing solely on data collection",
                "Prioritizing data visualization above all else",
                "Focusing on generating actionable insights",
                "Ignoring data privacy regulations",
            ],
            "answer": "Focusing on generating actionable insights",
            "solution": "The ultimate goal of marketing analytics is to drive better decisions and actions, so focusing on actionable insights is key.",
        },
    ]

    user_answers = []
    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i + 1}. {question['question']}**")
        user_answer = st.radio(
            "Select an answer:", question["options"], key=f"quiz_{i}"
        )
        user_answers.append(user_answer)

    if st.button("Submit Quiz", key="quiz_submit_button"):
        correct_count = 0
        for i, (user_answer, question) in enumerate(zip(user_answers, quiz_questions)):
            if user_answer == question["answer"]:
                correct_count += 1
                st.success(f"Question {i+1}: Correct! 🎉")
            else:
                st.error(
                    f"Question {i+1}: Incorrect. Let's review the solution below. 🧐"
                )

        st.write(
            f"You scored **{correct_count} out of {len(quiz_questions)}** questions correctly."
        )

        if correct_count < len(
            quiz_questions
        ):  # Optionally show solutions only if not perfect score
            with st.expander("Show Detailed Solutions"):
                for i, question in enumerate(quiz_questions):
                    st.markdown(f"**Question {i+1}:** {question['question']}")
                    st.markdown(f"**Your Answer:** {user_answers[i]}")
                    st.markdown(f"**Correct Answer:** {question['answer']}")
                    st.markdown(f"**Solution:** {question['solution']}")
                    if user_answers[i] == question["answer"]:
                        st.success("Correct!")
                    else:
                        st.error("Incorrect.")


if __name__ == "__main__":
    main()

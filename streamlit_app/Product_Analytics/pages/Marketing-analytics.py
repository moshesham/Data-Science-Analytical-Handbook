import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import chi2_contingency

# --- Data Generation Functions ---

def generate_campaign_data(n_customers=1000, conversion_rate=0.05, avg_order_value=50, cost_per_click=1, random_state=42):
    """Generates synthetic marketing campaign data."""
    np.random.seed(random_state)
    customer_ids = np.arange(1, n_customers + 1)
    impressions = np.random.randint(1, 5, n_customers)  # 1-4 impressions
    clicks = (np.random.rand(n_customers) < 0.2).astype(int)  # Assume 20% click-through rate
    converted = (np.random.rand(n_customers) < conversion_rate).astype(int)
    revenue = np.where(converted == 1, np.random.normal(avg_order_value, 10, n_customers), 0)
    cost = clicks * cost_per_click

    df = pd.DataFrame({
        'CustomerID': customer_ids,
        'Impressions': impressions,
        'Clicks': clicks,
        'Converted': converted,
        'Revenue': revenue,
        'Cost': cost
    })
    return df

def generate_segmentation_data(n_customers=1000, random_state=42):
    np.random.seed(random_state)
    customer_ids = np.arange(1, n_customers + 1)
    age = np.random.randint(18, 65, n_customers)
    income = np.random.normal(50000, 20000, n_customers).astype(int)
    income = np.maximum(income, 10000)  # Ensure income >= 10000
    location = np.random.choice(['Urban', 'Suburban', 'Rural'], n_customers)
    past_purchases = np.random.randint(0, 10, n_customers)

    df = pd.DataFrame({
        'CustomerID': customer_ids,
        'Age': age,
        'Income': income,
        'Location': location,
        'PastPurchases': past_purchases
    })
    return df

def generate_ab_test_data(n_variants=2, n_users_per_variant=500, conversion_rates=[0.10, 0.12], random_state=42):
    np.random.seed(random_state)
    data = []
    for i in range(n_variants):
        variant = chr(65 + i)  # A, B, C...
        users = np.arange(1, n_users_per_variant + 1)
        converted = (np.random.rand(n_users_per_variant) < conversion_rates[i]).astype(int)
        data.extend(list(zip([variant] * n_users_per_variant, users, converted)))

    df = pd.DataFrame(data, columns=['Variant', 'UserID', 'Converted'])
    return df

def generate_clv_data(n_customers=1000, avg_revenue=100, retention_rate=0.7, discount_rate=0.1, periods=5, random_state=42):
    np.random.seed(random_state)
    customer_ids = np.arange(1, n_customers + 1)
    # Simulate more realistic revenue with some variation
    initial_revenue = np.random.normal(avg_revenue, avg_revenue * 0.3, n_customers)
    initial_revenue = np.maximum(initial_revenue, 10)  # Ensure revenue is not too low

    data = {'CustomerID': customer_ids, 'InitialRevenue': initial_revenue}
    for period in range(1, periods + 1):
        retained = (np.random.rand(n_customers) < retention_rate).astype(int)
        # Revenue changes year-to-year, but is correlated with previous year
        if period == 1:
            revenue = initial_revenue * (1 + np.random.normal(0, 0.1, n_customers))  # 10% variation
        else:
            revenue = data[f'Revenue_Year{period-1}'] * (1 + np.random.normal(0, 0.1, n_customers))
        revenue = np.where(retained == 1, revenue, 0) # zero if not retained.
        data[f'Revenue_Year{period}'] = revenue

    df = pd.DataFrame(data)

    #Calculate CLV
    df['CLV'] = 0
    for period in range(1, periods + 1):
        df['CLV'] += df[f'Revenue_Year{period}'] / ((1 + discount_rate) ** period)
    return df



def perform_chi2_test(df, group_col, outcome_col):
    """Performs a Chi-Square test of independence and returns results."""
    contingency_table = pd.crosstab(df[group_col], df[outcome_col])
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    results = {
        "Chi-Square Statistic": chi2,
        "P-value": p,
        "Degrees of Freedom": dof,
        "Contingency Table": contingency_table,
        "Expected Frequencies": expected
    }
    return results

def calculate_metrics(df):
    """Calculates key marketing metrics."""
    total_impressions = df['Impressions'].sum()
    total_clicks = df['Clicks'].sum()
    total_conversions = df['Converted'].sum()
    total_revenue = df['Revenue'].sum()
    total_cost = df['Cost'].sum()

    ctr = (total_clicks / total_impressions) * 100 if total_impressions > 0 else 0
    conversion_rate = (total_conversions / total_clicks) * 100 if total_clicks > 0 else 0
    cpa = total_cost / total_conversions if total_conversions > 0 else 0
    roas = total_revenue / total_cost if total_cost > 0 else 0
    avg_order_value = total_revenue / total_conversions if total_conversions > 0 else 0

    metrics = {
        'Total Impressions': total_impressions,
        'Total Clicks': total_clicks,
        'Total Conversions': total_conversions,
        'Total Revenue': total_revenue,
        'Total Cost': total_cost,
        'Click-Through Rate (CTR) (%)': ctr,
        'Conversion Rate (%)': conversion_rate,
        'Cost per Acquisition (CPA)': cpa,
        'Return on Ad Spend (ROAS)': roas,
        'Average Order Value (AOV)': avg_order_value
    }
    return metrics


def main():
    st.set_page_config(page_title="Marketing Analytics Dashboard", page_icon="📊", layout="wide")

    st.title("Marketing Analytics Dashboard")
    st.write("Explore key marketing metrics, customer segmentation, A/B testing, and CLV analysis.")

    with st.expander("📖 Theoretical Concepts"):
        st.markdown("""
        Marketing analytics involves analyzing marketing data to measure performance, identify trends, and optimize campaigns.

        ### 1. Key Marketing Metrics

        *   **Click-Through Rate (CTR):** `(Clicks / Impressions) * 100%` - Measures the percentage of people who click on an ad after seeing it.
        *   **Conversion Rate:** `(Conversions / Clicks) * 100%` - Measures the percentage of people who complete a desired action (e.g., purchase) after clicking on an ad.
        *   **Cost per Acquisition (CPA):** `Total Cost / Conversions` - Measures the cost of acquiring a new customer.
        *   **Return on Ad Spend (ROAS):** `Revenue / Cost` - Measures the revenue generated for every dollar spent on advertising.
        *   **Average Order Value (AOV):**  `Total Revenue / Number of Orders`
        * **Customer Lifetime Value (CLV)** `Sum of (Revenue - cost) / (1 + Discount Rate)^t for period t`

        ### 2. Customer Segmentation

        *   **Purpose:** Dividing customers into groups based on shared characteristics (demographics, behavior, etc.).
        *   **Benefits:** Targeted marketing, personalized messaging, improved customer engagement.
        *   **Techniques:**  Clustering (k-means, hierarchical), RFM analysis (Recency, Frequency, Monetary Value).

        ### 3. A/B Testing

        *   **Purpose:** Comparing two or more versions of a marketing element (e.g., ad copy, landing page) to see which performs better.
        *   **Methodology:**  Randomly assign users to different variants and measure a key metric (e.g., conversion rate).
        *   **Statistical Significance:**  Use statistical tests (e.g., Chi-Square test) to determine if the observed differences are likely due to the changes made or just random chance.

        ### 4. Customer Lifetime Value (CLV)
        *   **Definition:**  A prediction of the net profit attributed to the entire future relationship with a customer.
        * **Importance:** Helps businesses understand the long-term value of their customers and make informed decisions about customer acquisition and retention.
        * **Calculation:** Various methods, often involving factors like average revenue, retention rate, and discount rate.

        **Further Reading:**
            *   [Google Digital Marketing & E-commerce Professional Certificate](https://grow.google/certificates/digital-marketing-ecommerce/#?modal_active=none)
            *   [HubSpot Marketing Blog](https://blog.hubspot.com/marketing)

        """)


    # --- Sidebar for Data Selection ---
    st.sidebar.header("Data Selection")
    analysis_type = st.sidebar.selectbox("Select Analysis Type:", ["Campaign Performance", "Customer Segmentation", "A/B Testing", "Customer Lifetime Value (CLV)"])


    # --- Main Content ---
    if analysis_type == "Campaign Performance":
        st.header("Campaign Performance Analysis")
        data_source = st.sidebar.radio("Data Source:", ["Generate Synthetic Data", "Upload CSV"]) #Moved to sidebar

        if data_source == "Generate Synthetic Data":
            n_customers = st.sidebar.number_input("Number of Customers:", min_value=100, max_value=10000, value=1000, step=100)
            conversion_rate = st.sidebar.slider("Conversion Rate (%):", min_value=0.01, max_value=0.2, value=0.05, step=0.01)
            avg_order_value = st.sidebar.number_input("Average Order Value:", min_value=10, max_value=500, value=50, step=10)
            cost_per_click = st.sidebar.number_input("Cost per Click:", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            df_campaign = generate_campaign_data(n_customers, conversion_rate, avg_order_value, cost_per_click)
            st.write("Generated Campaign Data:")
            st.dataframe(df_campaign)
        else:
            uploaded_file = st.sidebar.file_uploader("Upload CSV for Campaign Data", type=["csv"])
            if uploaded_file is not None:
                try:
                    df_campaign = pd.read_csv(uploaded_file)
                    st.write("Uploaded Campaign Data:")
                    st.dataframe(df_campaign)
                except Exception as e:
                    st.error(f"Error reading CSV: {e}")
                    df_campaign = None # Ensure df isn't used
            else:
                df_campaign = None


        if df_campaign is not None: # Only proceed if df is valid
            metrics = calculate_metrics(df_campaign)
            st.subheader("Key Marketing Metrics")
            col1, col2, col3, col4, col5 = st.columns(5)  # Create columns for layout
            with col1:
                st.metric("Total Impressions", f"{metrics['Total Impressions']:,}")
                st.metric("CTR (%)", f"{metrics['Click-Through Rate (CTR) (%)']:.2f}")
            with col2:
                st.metric("Total Clicks", f"{metrics['Total Clicks']:,}")
                st.metric("Conversion Rate (%)", f"{metrics['Conversion Rate (%)']:.2f}")
            with col3:
                st.metric("Total Conversions", f"{metrics['Total Conversions']:,}")
                st.metric("CPA", f"${metrics['Cost per Acquisition (CPA)']:.2f}")
            with col4:
                st.metric("Total Revenue", f"${metrics['Total Revenue']:.2f}")
                st.metric("ROAS", f"{metrics['Return on Ad Spend (ROAS)']:.2f}")
            with col5:
                st.metric("Total Cost", f"${metrics['Total Cost']:.2f}")
                st.metric("AOV", f"${metrics['Average Order Value (AOV)']:.2f}")

            # Visualizations
            st.subheader("Campaign Performance Visualizations")

            # Impressions, Clicks, Conversions over Time (Simulated)
            df_time = df_campaign.copy()
            df_time['Date'] = pd.to_datetime('2024-01-01') + pd.to_timedelta(np.random.randint(0, 30, len(df_time)), unit='D')  # Simulate daily data
            df_time = df_time.groupby('Date').agg({'Impressions': 'sum', 'Clicks': 'sum', 'Converted': 'sum'}).reset_index()
            fig_time = px.line(df_time, x='Date', y=['Impressions', 'Clicks', 'Converted'], title='Impressions, Clicks, and Conversions Over Time')
            st.plotly_chart(fig_time)

            # Revenue Distribution
            fig_revenue = px.histogram(df_campaign, x='Revenue', nbins=20, title='Revenue Distribution')
            st.plotly_chart(fig_revenue)

            # Cost vs. Revenue
            fig_cost_revenue = px.scatter(df_campaign, x='Cost', y='Revenue', color='Converted', title='Cost vs. Revenue')
            st.plotly_chart(fig_cost_revenue)


    elif analysis_type == "Customer Segmentation":
        st.header("Customer Segmentation Analysis")

        data_source = st.sidebar.radio("Data Source:", ["Generate Synthetic Data", "Upload CSV"]) #moved to sidebar

        if data_source == "Generate Synthetic Data":
            n_customers = st.sidebar.number_input("Number of Customers:", min_value=100, max_value=10000, value=1000, step=100)
            df_segmentation = generate_segmentation_data(n_customers)
            st.write("Generated Segmentation Data:")
            st.dataframe(df_segmentation)

        else:
            uploaded_file = st.sidebar.file_uploader("Upload CSV for Segmentation Data", type=["csv"])
            if uploaded_file is not None:
                try:
                    df_segmentation = pd.read_csv(uploaded_file)
                    st.write("Uploaded Segmentation Data")
                    st.dataframe(df_segmentation)
                except Exception as e:
                    st.error(f"Error reading CSV: {e}")
                    df_segmentation = None
            else:
                df_segmentation = None

        if df_segmentation is not None: # Proceed only if df is valid
            st.subheader("Customer Segmentation Visualizations")

            # Age Distribution
            fig_age = px.histogram(df_segmentation, x='Age', nbins=20, title='Age Distribution')
            st.plotly_chart(fig_age)

            # Income Distribution
            fig_income = px.histogram(df_segmentation, x='Income', nbins=20, title='Income Distribution')
            st.plotly_chart(fig_income)

            # Location Breakdown
            fig_location = px.pie(df_segmentation, names='Location', title='Customer Location Breakdown')
            st.plotly_chart(fig_location)

            # Scatter Plot: Income vs. Past Purchases
            fig_scatter = px.scatter(df_segmentation, x='Income', y='PastPurchases', color='Location', title='Income vs. Past Purchases')
            st.plotly_chart(fig_scatter)

            # Correlation Heatmap
            st.subheader("Correlation Heatmap")
            corr_matrix = df_segmentation[['Age', 'Income', 'PastPurchases']].corr()
            fig_heatmap = px.imshow(corr_matrix, text_auto=True, aspect="auto", color_continuous_scale='RdBu', title='Correlation Heatmap')
            st.plotly_chart(fig_heatmap)

    elif analysis_type == "A/B Testing":
        st.header("A/B Testing Analysis")

        data_source = st.sidebar.radio("Data Source:", ["Generate Synthetic Data", "Upload CSV"])

        if data_source == "Generate Synthetic Data":
           n_variants = st.sidebar.number_input("Number of Variants:", min_value=2, max_value=5, value=2, step=1)
           n_users_per_variant = st.sidebar.number_input("Users per Variant:", min_value=100, max_value=5000, value=500, step=100)
           conversion_rates = [st.sidebar.slider(f"Conversion Rate for Variant {chr(65 + i)} (%):", min_value=0.01, max_value=0.30, value=0.10 + i*0.02, step=0.01) for i in range(n_variants)]
           df_ab_test = generate_ab_test_data(n_variants, n_users_per_variant, conversion_rates)
           st.write("Generated AB Test Data:")
           st.dataframe(df_ab_test)

        else:
            uploaded_file = st.sidebar.file_uploader("Upload CSV for A/B Test Data", type=["csv"])
            if uploaded_file is not None:
                try:
                    df_ab_test = pd.read_csv(uploaded_file)
                    st.write("Uploaded AB Test Data")
                    st.dataframe(df_ab_test)
                except Exception as e:
                    st.error(f"Error reading CSV file: {e}")
                    df_ab_test = None
            else:
                df_ab_test = None

        if df_ab_test is not None: #Proceed only with valid dataframe
            st.subheader("A/B Test Results")

            # Summary Table
            summary_table = df_ab_test.groupby('Variant')['Converted'].agg(['count', 'sum', 'mean']).reset_index()
            summary_table.columns = ['Variant', 'Users', 'Conversions', 'Conversion Rate']
            summary_table['Conversion Rate'] = summary_table['Conversion Rate'] * 100
            st.dataframe(summary_table)

            # Visualization
            fig_conversion = px.bar(summary_table, x='Variant', y='Conversion Rate', title='Conversion Rate by Variant', text_auto='.2f')
            st.plotly_chart(fig_conversion)

            # Statistical Significance (Chi-Square Test)
            st.subheader("Statistical Significance (Chi-Square Test)")
            chi2_results = perform_chi2_test(df_ab_test, 'Variant', 'Converted')
            st.write(f"Chi-Square Statistic: {chi2_results['Chi-Square Statistic']:.2f}")
            st.write(f"P-value: {chi2_results['P-value']:.4f}")
            st.write(f"Degrees of Freedom: {chi2_results['Degrees of Freedom']}")

            if chi2_results['P-value'] < 0.05:
                st.success("The difference in conversion rates is statistically significant.")
            else:
                st.warning("The difference in conversion rates is not statistically significant.")

            with st.expander("Show Contingency Table and Expected Frequencies"):
                st.write("Contingency Table:")
                st.dataframe(chi2_results['Contingency Table'])
                st.write("Expected Frequencies:")
                st.dataframe(pd.DataFrame(chi2_results['Expected Frequencies'], index=chi2_results['Contingency Table'].index, columns=chi2_results['Contingency Table'].columns))

    elif analysis_type == "Customer Lifetime Value (CLV)":
        st.header("Customer Lifetime Value (CLV) Analysis")
        data_source = st.sidebar.radio("Data Source:", ["Generate Synthetic Data", "Upload CSV"])

        if data_source == "Generate Synthetic Data":
            n_customers = st.sidebar.number_input("Number of Customers:", min_value=100, max_value=5000, value=1000, step=100, key="clv_n_cust") #key added
            avg_revenue = st.sidebar.number_input("Average Initial Revenue:", min_value=20, max_value=500, value=100, step=10, key='clv_rev')
            retention_rate = st.sidebar.slider("Retention Rate (%):", min_value=0.1, max_value=0.99, value=0.7, step=0.01, key='clv_retention')
            discount_rate = st.sidebar.slider("Discount Rate (%):", min_value=0.01, max_value=0.2, value=0.1, step=0.01, key='clv_discount')
            periods = st.sidebar.number_input("Number of Periods (Years):", min_value=1, max_value=10, value=5, step=1, key='clv_periods')
            df_clv = generate_clv_data(n_customers, avg_revenue, retention_rate, discount_rate, periods)
            st.write("Generated CLV Data:")
            st.dataframe(df_clv)
        else:
            uploaded_file = st.sidebar.file_uploader("Upload CSV for CLV Data", type=["csv"])
            if uploaded_file is not None:
                try:
                    df_clv = pd.read_csv(uploaded_file)
                    st.write("Uploaded CLV data")
                    st.dataframe(df_clv)
                except Exception as e:
                    st.error(f"Error reading CSV: {e}")
                    df_clv = None
            else:
                df_clv = None

        if df_clv is not None: # Proceed if valid
            st.subheader("CLV Analysis Results")

            # Summary Statistics
            st.write(f"Average CLV: ${df_clv['CLV'].mean():.2f}")
            st.write(f"Median CLV: ${df_clv['CLV'].median():.2f}")
            st.write(f"Total CLV: ${df_clv['CLV'].sum():.2f}")

            # CLV Distribution
            fig_clv_hist = px.histogram(df_clv, x='CLV', nbins=30, title='Customer Lifetime Value (CLV) Distribution')
            st.plotly_chart(fig_clv_hist)

            # Top Customers by CLV
            st.subheader("Top 10 Customers by CLV")
            top_customers = df_clv.sort_values('CLV', ascending=False).head(10)
            st.dataframe(top_customers[['CustomerID', 'CLV']])


    st.header("💪 Practice Exercises")
    st.markdown("""
        1. **Analyze a real-world marketing campaign dataset.** Calculate key metrics (CTR, conversion rate, CPA, ROAS) and interpret the results.
        2. **Perform customer segmentation on a dataset.** Use different criteria (demographics, behavior) to group customers and identify valuable segments.
        3.  **Design and analyze an A/B test.** Compare two versions of an ad or landing page and determine if there's a statistically significant difference in performance.
        4.  **Calculate CLV for a customer cohort.** Use historical data or make assumptions about future revenue and retention to estimate CLV.
        5.  **Explore different visualization techniques.**  Create charts and graphs to effectively communicate marketing insights.
    """)

    st.header("🌍 Real-world Applications")
    st.markdown("""
    Marketing analytics is used across various industries and functions:

    *   **Digital Marketing:** Optimizing online advertising campaigns, improving website performance, and measuring social media engagement.
    *   **E-commerce:** Understanding customer behavior, personalizing recommendations, and improving conversion rates.
    *   **Retail:** Analyzing sales data, optimizing pricing and promotions, and managing inventory.
    *   **Customer Relationship Management (CRM):** Identifying high-value customers, predicting churn, and improving customer retention.
    *   **Market Research:** Understanding consumer preferences, identifying market trends, and assessing the effectiveness of marketing strategies.
    """)
    st.header("✅ Knowledge Check")
    quiz_questions = [
    {
        "question": "What does CTR stand for in marketing?",
        "options": ["Click-Total Ratio", "Click-Through Rate", "Conversion-Total Ratio", "Cost-Through Rate"],
        "answer": "Click-Through Rate",
        "solution": "CTR measures the percentage of people who click on an ad after seeing it."
    },
    {
        "question": "What is the formula for calculating Return on Ad Spend (ROAS)?",
        "options": ["Revenue / Cost", "Cost / Revenue", "(Revenue - Cost) / Cost", "Clicks / Impressions"],
        "answer": "Revenue / Cost",
        "solution": "ROAS indicates how much revenue is generated for every dollar spent on advertising."
    },
    {
        "question": "What is the purpose of customer segmentation?",
        "options": ["To increase advertising costs", "To divide customers into groups based on shared characteristics", "To reduce the number of marketing channels", "To make all marketing messages the same for everyone"],
        "answer": "To divide customers into groups based on shared characteristics",
        "solution": "Segmentation allows for more targeted and personalized marketing efforts."
    },
    {
        "question": "In A/B testing, what does a statistically significant result (e.g., p-value < 0.05) indicate?",
        "options": ["The observed difference between variants is likely due to random chance.",
                    "The observed difference is likely due to the changes made between variants.",
                    "The experiment was poorly designed.",
                    "The sample size was too small."],
        "answer": "The observed difference is likely due to the changes made between variants.",
        "solution": "Statistical significance suggests that the results are not just due to random variation."
    },
    {
        "question": "What is Customer Lifetime Value (CLV)?",
        "options": ["The total revenue a customer has generated to date",
                    "A prediction of the net profit attributed to the entire future relationship with a customer",
                    "The cost of acquiring a new customer",
                    "The average order value of a customer"],
        "answer": "A prediction of the net profit attributed to the entire future relationship with a customer",
        "solution": "CLV is a forward-looking metric that helps businesses understand the long-term value of their customers."
    },
    {
        "question": "Which of the following is NOT a typical input for calculating CLV?",
        "options": ["Average revenue per customer", "Customer retention rate", "Discount rate", "Number of marketing emails sent"],
        "answer": "Number of marketing emails sent",
        "solution": "While marketing emails might influence retention, the number sent is not a direct input for calculating CLV. The other options are common inputs."
    },
    {
        "question": "What statistical test is commonly used to analyze the results of A/B tests with categorical outcomes (e.g., conversion/no conversion)?",
        "options": ["t-test", "ANOVA", "Chi-Square test", "Regression analysis"],
        "answer": "Chi-Square test",
        "solution": "The Chi-Square test of independence is used to determine if there's a statistically significant association between two categorical variables (e.g., variant and conversion)."
    },
    {
        "question": "What does CPA stand for in marketing?",
        "options": ["Cost Per Acquisition", "Click Per Action", "Cost Per Action", "Clicks Per Acquisition"],
        "answer": "Cost Per Acquisition",
        "solution": "CPA measures the cost of acquiring a *new customer*."
    },
    {
       "question": "What is the primary goal of RFM analysis in customer segmentation?",
        "options": ["To predict future revenue.",
                    "To identify high-value customers based on recency, frequency, and monetary value of purchases.",
                    "To determine the optimal pricing strategy.",
                    "To measure website traffic."],
        "answer": "To identify high-value customers based on recency, frequency, and monetary value of purchases.",
        "solution": "RFM analysis focuses on past customer behavior to segment customers."
    },
    {
        "question": "Which metric would you primarily use to assess the effectiveness of an email marketing campaign aimed at driving immediate sales?",
        "options": ["Open rate", "Click-through rate", "Conversion rate", "Bounce rate"],
        "answer": "Conversion rate",
        "solution": "While open and click-through rates are important, the conversion rate directly measures the percentage of recipients who completed the desired action (a purchase)."
    }
]

    user_answers = []
    for i, question in enumerate(quiz_questions):
        st.markdown(f"**{i + 1}. {question['question']}**")
        user_answer = st.radio(f"Select an answer:", question["options"], key=f"quiz_{i}")
        user_answers.append(user_answer)

    if st.button("Submit Quiz"):
        correct_count = 0
        for i, (user_answer, question) in enumerate(zip(user_answers, quiz_questions)):
            if user_answer == question["answer"]:
                correct_count += 1

        st.write(f"You got {correct_count} out of {len(quiz_questions)} questions correct.")

        with st.expander("Show Detailed Solutions"):
            for i, question in enumerate(quiz_questions):
                st.markdown(f"**Question {i+1}:** {question['question']}")
                st.markdown(f"**Your Answer:** {user_answers[i]}")
                st.markdown(f"**Correct Answer:** {question['answer']}")
                st.markdown(f"**Solution:** {question['solution']}")
                if user_answers[i] == question['answer']:
                    st.success("Correct!")
                else:
                    st.error("Incorrect.")

if __name__ == "__main__":
    main()

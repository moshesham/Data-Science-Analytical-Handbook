import random

import folium
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from streamlit_folium import folium_static


def generate_transaction_data(
    num_transactions,
    anomaly_rate=0.05,
    geographic_anomalies=False,
    merchant_category_anomalies=False,
):
    """Generates simulated transaction data with optional anomalies."""
    categories = [
        "Grocery",
        "Electronics",
        "Clothing",
        "Restaurant",
        "Travel",
        "Home Goods",
        "Entertainment",
    ]
    locations = [
        {"city": "New York", "lat": 40.7128, "lon": -74.0060},
        {"city": "London", "lat": 51.5074, "lon": 0.1278},
        {"city": "Tokyo", "lat": 35.6895, "lon": 139.6917},
        {"city": "Sydney", "lat": -33.8688, "lon": 151.2093},
        {"city": "Paris", "lat": 48.8566, "lon": 2.3522},
        {"city": "Rio de Janeiro", "lat": -22.9068, "lon": -43.1729},
        {"city": "Cairo", "lat": 30.0444, "lon": 31.2357},
    ]
    data = []
    for i in range(num_transactions):
        amount = np.random.normal(50, 15)
        is_anomaly = np.random.rand() < anomaly_rate
        category = random.choice(categories)
        location = random.choice(locations)
        timestamp = (
            pd.to_datetime("now")
            - pd.to_timedelta(np.random.randint(0, 30), unit="days")
            + pd.to_timedelta(np.random.randint(0, 24 * 60), unit="minutes")
        )

        if is_anomaly:
            amount = np.random.uniform(150, 400)  # Higher amounts for anomalies
            if merchant_category_anomalies:
                category = "Luxury Goods"  # Unusual category
            if geographic_anomalies:
                location = {
                    "city": "Dubai",
                    "lat": 25.2048,
                    "lon": 55.2708,
                }  # Unusual location

        data.append(
            {
                "Transaction ID": i + 1,
                "Timestamp": timestamp,
                "Amount": amount,
                "Category": category,
                "Location": location["city"],
                "Latitude": location["lat"],
                "Longitude": location["lon"],
                "Is Anomaly": is_anomaly,
            }
        )
    return pd.DataFrame(data)


def generate_transaction_data_interactive(
    num_transactions, anomaly_rate=0.05, anomaly_type="amount"
):
    """Generates simulated transaction data with different types of anomalies."""
    categories = [
        "Grocery",
        "Electronics",
        "Clothing",
        "Restaurant",
        "Travel",
        "Home Goods",
        "Entertainment",
    ]
    locations = [
        {"city": "New York", "lat": 40.7128, "lon": -74.0060},
        {"city": "London", "lat": 51.5074, "lon": 0.1278},
        {"city": "Tokyo", "lat": 35.6895, "lon": 139.6917},
        {"city": "Sydney", "lat": -33.8688, "lon": 151.2093},
        {"city": "Paris", "lat": 48.8566, "lon": 2.3522},
        {"city": "Rio de Janeiro", "lat": -22.9068, "lon": -43.1729},
        {"city": "Cairo", "lat": 30.0444, "lon": 31.2357},
    ]
    data = []
    for i in range(num_transactions):
        amount = np.random.normal(50, 15)
        is_anomaly = np.random.rand() < anomaly_rate
        category = random.choice(categories)
        location = random.choice(locations)
        timestamp = (
            pd.to_datetime("now")
            - pd.to_timedelta(np.random.randint(0, 30), unit="days")
            + pd.to_timedelta(np.random.randint(0, 24 * 60), unit="minutes")
        )

        if is_anomaly:
            if anomaly_type == "amount":
                amount = np.random.uniform(150, 400)  # Higher amounts for anomalies
            elif anomaly_type == "location":
                location = {
                    "city": "Dubai",
                    "lat": 25.2048,
                    "lon": 55.2708,
                }  # Unusual location
            elif anomaly_type == "category":
                category = "Luxury Goods"  # Unusual category
            elif anomaly_type == "velocity":
                timestamp = pd.to_datetime(
                    "now"
                )  # Recent timestamp for velocity simulation

        data.append(
            {
                "Transaction ID": i + 1,
                "Timestamp": timestamp,
                "Amount": amount,
                "Category": category,
                "Location": location["city"],
                "Latitude": location["lat"],
                "Longitude": location["lon"],
                "Is Anomaly": is_anomaly,
            }
        )
    return pd.DataFrame(data)


def main():
    st.set_page_config(
        page_title="Fraud & Risk Data Analytics", page_icon="🛡️", layout="wide"
    )

    st.title("🛡️ Data Analytics for Fraud and Risk Detection")
    st.write(
        "Explore how data analytics empowers organizations to proactively combat fraud and manage risks effectively in today's digital age."
    )

    with st.expander("📖 1. Understanding Fraud and Risk", expanded=False):
        st.markdown(
            """
        ### 1.1 Defining Fraud in Business 🎭

        **Definition:** Fraud is an intentional act of deception for unlawful gain or to deprive another of something valuable. In business, fraud can manifest in various forms causing financial, operational, and reputational damage. It's crucial to understand that fraud is not accidental; it's a deliberate action.

        **Types of Fraud:**

        *   **Financial Statement Fraud:** Manipulating financial records to present a misleading financial picture to stakeholders.
            *   *Examples:* Revenue inflation, expense understatement, asset manipulation, *concealing liabilities*.
        *   **Asset Misappropriation (Employee Fraud):**  Theft or misuse of company assets by employees for personal gain.
            *   *Examples:* Embezzlement, theft of inventory, misuse of company credit cards, *payroll fraud*.
        *   **Corruption:** Abuse of entrusted power for private benefit, often involving bribery or conflicts of interest.
            *   *Examples:* Bribery, kickbacks, undisclosed conflicts of interest, *extortion*.
        *   **Customer Fraud:** Deceptive actions by customers that harm the business.
            *   *Examples:* Credit card fraud, insurance claim fraud, return fraud, *friendly fraud (chargebacks)*.
        *   **Cyber Fraud:** Fraudulent activities conducted through digital channels, often leveraging technology for illicit gains.
            *   *Examples:* Phishing, ransomware, data breaches for financial gain, *identity theft*, *malware attacks for financial data theft*.
        *   **Vendor Fraud:** Fraudulent schemes involving suppliers or vendors, often targeting procurement processes.
            *   *Examples:* Inflated invoicing, bid rigging, collusion, *shell company schemes*.

        <div style="background-color:#f0f2f6;padding:10px;border-radius:5px;">
        <p style="font-weight: bold;">Key Takeaway:</p>
        <p>Fraud is intentional deception aimed at personal or organizational gain at the expense of others. Understanding the diverse types of fraud is the first step in effective detection and prevention.</p>
        </div>
        """
        )

        st.markdown(
            """
        ### 1.2 Defining Risk in Business ⚠️

        **Definition:** Risk is the potential for negative outcomes or losses due to internal or external events. Business risks span a wide range of uncertainties that can impact organizational objectives. Risk implies uncertainty and the possibility of loss.

        **Types of Business Risks:**

        *   **Financial Risk:** Risks associated with financial losses and instability.
            *   *Examples:* Credit risk (loan defaults), market risk (market volatility), liquidity risk (cash flow issues), operational failures leading to financial losses, *interest rate risk*, *currency risk*.
        *   **Operational Risk:** Risks arising from day-to-day operations and internal processes, including process failures and human error.
            *   *Examples:* Process failures, human errors, system outages, internal fraud, *supply chain disruptions*, *regulatory breaches due to operational lapses*.
        *   **Compliance Risk:** Risk of legal or regulatory penalties due to non-compliance with laws, regulations, or internal policies.
            *   *Examples:* Data privacy violations (GDPR, CCPA), anti-money laundering (AML) failures, breach of industry regulations, *tax compliance failures*, *environmental regulation violations*.
        *   **Reputational Risk:** Risk of damage to brand image and public perception, impacting stakeholder trust.
            *   *Examples:* Scandals, negative publicity, customer data breaches, *product recalls*, *ethical lapses*.
        *   **Strategic Risk:** Risks related to business strategy and major decisions, impacting long-term goals.
            *   *Examples:* Failed market entry, unsuccessful mergers and acquisitions, ineffective product strategies, *disruptive technologies*, *changing customer preferences*.
        *   **Cybersecurity Risk:** Risks from cyberattacks and digital threats that can compromise data and operations.
            *   *Examples:* Data breaches, ransomware attacks, cyber espionage, *denial-of-service attacks*, *insider threats leading to cyber incidents*.
        *   **Credit Risk:** Specifically the risk that borrowers may not repay debts, impacting lending institutions and credit providers.

         <div style="background-color:#f0f2f6;padding:10px;border-radius:5px;">
        <p style="font-weight: bold;">Key Takeaway:</p>
        <p>Risk is inherent in all business operations. Identifying, assessing, and mitigating various types of risks is crucial for organizational resilience and sustainability.</p>
        </div>
        """
        )

        st.markdown(
            """
        ### 1.3 The Fraud-Risk Interconnection 🔗

        Fraud is often categorized as a significant subset of **operational risk**. Fraudulent activities are a major source of operational losses and can quickly escalate into broader financial and reputational risks, creating a cascading effect across the organization.

        **Cascading Risk Example:** Employee embezzlement (fraud - operational risk failure) can lead to:
        *   **Direct Financial Loss:** Embezzled funds directly reduce profits (financial risk).
        *   **Investigation Costs:** Expenses for audits and investigations (financial risk).
        *   **Reputational Damage:** Loss of customer and investor trust if the fraud becomes public (reputational risk).
        *   **Compliance Penalties:** Fines and regulatory sanctions if internal controls were inadequate (compliance risk).
        *   **Strategic Impact:** In severe cases, loss of investor confidence can hinder future growth plans (strategic risk).

        Therefore, effective risk management strategies must inherently include robust fraud detection and prevention mechanisms as a core component. Addressing fraud proactively is not just about preventing direct financial losses, but also about protecting against a wider spectrum of interconnected business risks.

         <div style="background-color:#f0f2f6;padding:10px;border-radius:5px;">
        <p style="font-weight: bold;">Key Takeaway:</p>
        <p>Fraud acts as a key trigger and amplifier of broader business risks.  A strong fraud defense is integral to overall risk management and organizational stability.</p>
        </div>
        """
        )

    with st.expander("📖 2. Data Analytics Fundamentals 📊", expanded=False):
        st.markdown(
            """
        ### 2.1 Data Types for Fraud and Risk Detection 🗂️

        Effective data analytics starts with identifying and leveraging relevant data sources. In fraud and risk detection, diverse data types play crucial and often complementary roles:

        *   **Transactional Data:** Records of core business activities – the bedrock for many fraud and risk detection efforts, reflecting the flow of business.
            *   *Examples:* Sales transactions, payment records, insurance claims, fund transfers, credit card purchases, banking transactions.
            *   *Value:* **Fraud Detection:** Reveals patterns, anomalies, and deviations in normal business flow that are indicative of fraudulent activities. **Risk Detection:** Helps in assessing operational and financial risks linked to transaction volumes and patterns. *Specifically useful for detecting transaction fraud, payment fraud, and money laundering.*

        *   **Customer/User Data:** Information about individuals or entities interacting with the business, providing context and behavioral insights.
            *   *Examples:* Demographics, account details, interaction history, behavior patterns, KYC (Know Your Customer) information, customer profiles, user login details.
            *   *Value:* **Fraud Detection:** Enables user profiling, behavior analysis, and personalized risk assessment, helping identify unusual user behavior indicative of account takeover or identity theft. **Risk Detection:** Aids in customer segmentation for differentiated risk management and targeted interventions. *Crucial for application fraud, account takeover, and customer risk assessment.*

        *   **Log Data:** System, network, and application logs tracking system events and digital footprints, essential for cybersecurity and internal monitoring.
            *   *Examples:* Login attempts, access logs, error logs, network traffic logs, system event logs, audit trails.
            *   *Value:* **Fraud Detection:** Essential for cybersecurity fraud detection, identifying unauthorized access attempts, system anomalies, and potential data breaches indicative of cyber fraud. **Risk Detection:** Crucial for monitoring cybersecurity risks, system health, and compliance with security protocols. *Directly used for cybersecurity risk, insider threat detection, and system integrity monitoring.*

        *   **Sensor Data (IoT):** Data from connected devices and sensors, providing real-time operational data for risk assessment in physical contexts.
            *   *Examples:* Telematics data from vehicles (speed, location, driving behavior), sensor readings from industrial equipment (temperature, pressure), security system data (alarms, access events).
            *   *Value:* **Fraud Detection:** Provides real-time operational data for anomaly detection in physical assets and processes, useful in insurance fraud (telematics for car accidents), and industrial fraud (equipment tampering). **Risk Detection:** Enables real-time monitoring of operational risks, predictive maintenance, and risk assessment of physical assets and processes. *Applicable to insurance fraud, operational risk in manufacturing, and logistics.*

        *   **External Data:** Data from sources outside the organization, enriching internal data and providing a broader context for validation and risk assessment.
            *   *Examples:* Credit bureau data, social media activity, news feeds, public records, sanctions lists, watchlists, geolocation data, weather data.
            *   *Value:* **Fraud Detection:** Contextual enrichment, validation, and identification of external risks, crucial for verifying customer information, identifying links to fraudulent entities, and detecting external threats. **Risk Detection:** Aids in assessing macroeconomic risks, geopolitical risks, and external compliance risks. *Valuable in application fraud, KYC/AML compliance, and external threat intelligence.*

        *   **Unstructured Data:** Text, images, videos, and audio data, offering rich contextual insights when analyzed with advanced techniques.
            *   *Examples:* Emails, customer service interactions (text/voice), document scans (ID cards, invoices), images from claims (accident photos), social media posts, contracts.
            *   *Value:* **Fraud Detection:** Rich insights through NLP and image/video analysis for sentiment analysis (customer service interactions for complaint patterns), document verification (ID and invoice fraud detection), and contextual understanding in claims processing (insurance fraud). **Risk Detection:** Analysis of customer feedback, social media sentiment for reputational risk, and contract analysis for legal and compliance risks. *Increasingly important in insurance claim fraud, document fraud, and customer sentiment analysis.*

        <div style="background-color:#f0f2f6;padding:10px;border-radius:5px;">
        <p style="font-weight: bold;">Key Takeaway:</p>
        <p>A diverse range of data types, from transactional records to unstructured content, is essential for comprehensive fraud and risk detection. The key is to select and integrate data sources relevant to the specific fraud and risk scenarios being addressed.</p>
        </div>
        """
        )

        st.markdown(
            """
        ### 2.2 Data Preprocessing and Feature Engineering ⚙️

        Raw data is rarely directly usable for effective analysis. Preprocessing is essential to transform data into an analysis-ready format, and feature engineering extracts valuable information to enhance model performance.

        *   **Data Cleaning:** Addressing data quality issues to ensure reliability and accuracy of analysis.
            *   *Tasks:* Handling missing values (imputation, removal), error correction (data validation, standardization), duplicate removal (deduplication techniques), data standardization (format consistency). *Example: Correcting inconsistent date formats, handling typos in names, imputing missing address information.*

        *   **Data Transformation:** Converting data into suitable formats and structures optimized for analytical techniques.
            *   *Tasks:* Normalization (scaling numerical features), standardization (zero-centering and scaling), aggregation (summarizing data at different levels), data type conversion (numeric to categorical, etc.), encoding categorical variables (one-hot encoding, label encoding). *Example: Converting timestamps to time intervals, aggregating transactions by customer, scaling transaction amounts to a 0-1 range.*

        *   **Feature Engineering:** Creating new variables (features) from existing data that can significantly improve the performance and interpretability of analytical models for fraud and risk detection. This is a crucial step and often requires domain expertise.
            *   *Examples for Fraud/Risk:*
                *   **Frequency Features:** Transaction counts per customer per day, login attempts per hour, claims filed in the last month. *Captures activity volume and intensity.*
                *   **Ratio Features:** Claim amount to premium ratios, transaction amount to average spending ratios, loan amount to income ratio. *Indicates proportionality and deviation from norms.*
                *   **Time-Based Features:** Time since last transaction, time of day/week of transactions, days since account opening, seasonality flags (weekend/weekday, holiday). *Exploits temporal patterns and deviations.*
                *   **Geographic Features:** Transaction locations (country, city), IP address geolocation, distance between transaction location and home address, geographic risk scores of locations. *Highlights location-based anomalies and risks.*
                *   **Behavioral Features:** Deviation from user's typical spending patterns, unusual transaction sequences, changes in login behavior, abnormal browsing patterns. *Focuses on deviations from established user behavior.*

         <div style="background-color:#f0f2f6;padding:10px;border-radius:5px;">
        <p style="font-weight: bold;">Key Takeaway:</p>
        <p>Data preprocessing and feature engineering are critical foundations for effective data analytics in fraud and risk. Well-engineered features, derived from clean and transformed data, are often more impactful than just choosing sophisticated algorithms.</p>
        </div>
        """
        )

        st.markdown(
            """
        ### 2.3 Key Data Analytics Techniques 🧮

        Data analytics techniques for fraud and risk detection can be categorized into four progressively advanced types, each serving different analytical purposes:

        *   **Descriptive Analytics:** Understanding *what* happened in the past, providing a historical view of fraud and risk events.
            *   *Techniques:* Data visualization (dashboards, charts - bar charts, histograms, geographical maps, time series plots), summary statistics (mean, median, mode, standard deviation, percentiles), basic reporting, data aggregation.
            *   *Use Cases:* Trend identification in fraud types, visualizing risk exposures across departments or business units, monitoring Key Risk Indicators (KRIs) and performance metrics, creating baseline understanding of data patterns. *Example: Dashboard showing monthly fraud counts by type, geographical heat map of high-risk areas, trend chart of average claim amounts over time.*

        *   **Diagnostic Analytics:** Understanding *why* events happened, investigating the root causes of fraud incidents or risk escalations.
            *   *Techniques:* Drill-down analysis (exploring data at granular levels), root cause analysis (identifying underlying factors), correlation analysis (relationship between variables), basic anomaly detection (statistical methods like Z-score, IQR for outlier detection), hypothesis testing, comparative analysis.
            *   *Use Cases:* Investigating specific fraud cases to understand the modus operandi, identifying factors contributing to high-risk situations (e.g., process weaknesses, system vulnerabilities), understanding the sequence of events leading to a security breach, diagnosing reasons for increased claim frequencies. *Example: Investigating a spike in fraudulent transactions by drilling down into merchant categories, time of day, and customer demographics to find common factors.*

        *   **Predictive Analytics:** Forecasting *what might happen* in the future, anticipating potential fraud and risk events before they occur. This is where Machine Learning (ML) plays a significant role.
            *   *Techniques:*
                *   **Classification Models:** Predicting categorical outcomes (Fraud/Not Fraud, High Risk/Low Risk, Approve/Reject) - *Algorithms:* Logistic Regression, Decision Trees, Random Forests, Gradient Boosting Machines (GBM), Support Vector Machines (SVM), Neural Networks (including Deep Learning).
                *   **Regression Models:** Predicting numerical values (loss amounts, risk scores, probability of default) - *Algorithms:* Linear Regression, Polynomial Regression, Regression Trees, Neural Networks.
                *   **Advanced Anomaly Detection:** Identifying outliers and unusual patterns that deviate significantly from the norm, potentially indicating new or evolving fraud types - *Algorithms:* Isolation Forest, One-Class SVM, Autoencoders (Deep Learning), Clustering-based anomaly detection (e.g., DBSCAN), statistical anomaly detection models.
                *   **Time Series Analysis & Forecasting:** Analyzing time-dependent data to detect patterns, seasonality, and anomalies, and forecast future risk trends - *Algorithms:* ARIMA, Prophet, Exponential Smoothing, LSTM Recurrent Neural Networks.
            *   *Use Cases:* Real-time fraud transaction prediction, identifying high-risk customers or accounts, forecasting potential cyber threats, predicting loan default probabilities, predicting equipment failures (predictive maintenance for operational risk). *Example: Building a model to predict the probability of a credit card transaction being fraudulent based on transaction features and past fraud patterns.*

        *   **Prescriptive Analytics:** Recommending *what actions to take* to prevent or mitigate fraud and risk, going beyond prediction to suggest optimal interventions.
            *   *Techniques:* Optimization algorithms (linear programming, integer programming), simulation (Monte Carlo simulation, agent-based modeling), rule-based expert systems (decision rules, business rules), recommendation engines, reinforcement learning (emerging for adaptive security measures).
            *   *Use Cases:* Recommending optimal fraud prevention strategies (e.g., dynamically adjusting security protocols), suggesting risk mitigation actions (e.g., adjusting credit limits), automating responses to detected threats (e.g., triggering alerts, blocking transactions), dynamically adjusting security controls based on real-time risk levels, optimizing resource allocation for fraud investigations. *Example: A system that not only predicts a transaction as high-risk but also automatically triggers a two-factor authentication challenge and recommends a temporary spending limit reduction.*

         <div style="background-color:#f0f2f6;padding:10px;border-radius:5px;">
        <p style="font-weight: bold;">Key Takeaway:</p>
        <p>Data analytics techniques progress from describing past events to diagnosing causes, predicting future outcomes, and finally, prescribing optimal actions. A comprehensive fraud and risk management strategy often utilizes a combination of these techniques, moving towards more proactive and automated approaches.</p>
        </div>
        """
        )

        st.markdown(
            """
        ### 2.4 Deep Dive into Key Algorithms 🚀

        Let's delve deeper into some of the most commonly used algorithms in data analytics for fraud and risk detection, highlighting their strengths and applications:

        *   **Logistic Regression:** A fundamental statistical method primarily used for **binary classification** problems. It predicts the probability of an event occurring (e.g., probability of a transaction being fraudulent).
            *   *Strengths:* Highly **interpretable** (easy to understand feature importance), computationally **efficient**, good baseline model, provides probability scores.
            *   *Applications:* Initial fraud screening, risk scoring, binary outcome prediction when interpretability is key. *Example: Predicting if a loan application is high-risk or low-risk.*

        *   **Decision Trees and Random Forests:** **Tree-based models** that partition data based on feature values to make decisions (classification or regression). **Random Forests** are ensembles of multiple decision trees, improving accuracy and robustness and reducing overfitting.
            *   *Strengths:* **Non-linear relationships** handling, **feature importance** ranking, relatively **interpretable** (especially single decision trees), robust to outliers (Random Forests), versatile for classification and regression.
            *   *Applications:* Fraud classification, risk categorization, feature selection, rule extraction. *Example: Identifying key factors that lead to fraudulent insurance claims.*

        *   **Support Vector Machines (SVM):** Powerful algorithms effective for both **classification and regression**. SVMs find an optimal hyperplane that best separates different classes in high-dimensional space. **Kernel functions** allow SVMs to model non-linear decision boundaries.
            *   *Strengths:* Effective in **high-dimensional spaces**, versatile with different **kernel functions** for non-linear data, good generalization capability, robust to margin maximization.
            *   *Applications:* Complex fraud classification, anomaly detection, image-based fraud detection, text classification for risk assessment. *Example: Detecting fraudulent transactions with complex patterns that are not linearly separable.*

        *   **Neural Networks (Deep Learning):**  Complex and powerful models inspired by the structure of the human brain. Capable of learning extremely complex patterns from very large datasets. Especially effective for image recognition, natural language processing, and complex anomaly detection.
            *   *Types relevant to fraud/risk:*
                *   **Multilayer Perceptrons (MLPs):** Basic **feedforward networks** suitable for tabular data.
                *   **Recurrent Neural Networks (RNNs) and LSTMs:** Designed for **sequential data** like time series and transaction sequences, capturing temporal dependencies. *Ideal for transaction sequence analysis and time-series anomaly detection.*
                *   **Autoencoders:** For **anomaly detection** by learning compressed representations of "normal" data and identifying deviations from this learned norm as anomalies. *Effective for unsupervised anomaly detection in various data types.*
                *   **Convolutional Neural Networks (CNNs):** Primarily for **image and pattern recognition**, potentially useful in areas like document fraud detection (analyzing scanned documents for forgeries) and image-based claim assessment (insurance).
            *   *Strengths:* **High accuracy** for complex patterns, ability to learn from **unstructured data** (images, text), feature learning (automatic feature extraction), scalability with large datasets, representation learning for complex features.
            *   *Applications:* Advanced fraud detection, image-based document fraud analysis, natural language processing for risk assessment from text data, complex anomaly detection, real-time fraud detection in high-velocity data streams. *Example: Real-time analysis of high-volume transaction streams to detect subtle fraud patterns that traditional models might miss.*

        *   **Clustering Algorithms (e.g., K-Means, DBSCAN):** **Unsupervised learning** algorithms that group similar data points together based on inherent data patterns. Useful for **anomaly detection** (outliers as anomalies) and customer segmentation for risk profiling. **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) is particularly good for finding clusters of arbitrary shapes and identifying noise points as anomalies without pre-defining the number of clusters.
            *   *Strengths:* **Unsupervised anomaly detection**, customer/risk **segmentation**, pattern discovery, no need for labeled fraud data (for anomaly detection in some cases). *DBSCAN excels at finding clusters of varying shapes and handling noisy data.*
            *   *Applications:* Anomaly detection in transaction data, customer segmentation based on risk behavior, identifying unusual groups of transactions. *Example: Clustering transactions to identify unusual groups or outliers that deviate from typical transaction clusters.*

        *   **Anomaly Detection Algorithms (Isolation Forest, One-Class SVM):** Algorithms specifically designed to **identify rare and unusual data points** that deviate significantly from the majority of the data. **Isolation Forest** isolates anomalies by randomly partitioning data; anomalies are easier to isolate (require fewer partitions). **One-Class SVM** learns a boundary around "normal" data and flags data points outside this boundary as anomalous.
            *   *Strengths:* **Specialized for anomaly detection**, effective in **high-dimensional data**, robust to class imbalance (anomaly detection context), unsupervised anomaly detection (Isolation Forest can be unsupervised). *Isolation Forest is computationally efficient and effective for high-dimensional data.*
            *   *Applications:* Fraud anomaly detection, outlier detection in risk indicators, identifying unusual system behavior, detecting rare events. *Example: Detecting highly unusual transactions that stand out as anomalies compared to the vast majority of normal transactions.*

        *   **Graph Analytics:** Analyzing **relationships and networks in data**. Particularly useful for detecting complex fraud schemes like **fraud rings**, **money laundering networks**, and **social network analysis for risk assessment**. Graph databases and algorithms are used to explore connections and patterns.
            *   *Algorithms include:* Centrality measures (identifying key nodes), community detection (finding clusters of connected entities), pathfinding algorithms (shortest paths, network traversal).
            *   *Strengths:* Detecting **complex relationships and networks**, identifying **hidden connections**, visualizing and analyzing interconnected data, powerful for network-based fraud schemes.
            *   *Applications:* Fraud ring detection, anti-money laundering (AML) compliance, social network risk analysis, supply chain risk assessment. *Example: Identifying a network of interconnected accounts involved in a coordinated fraud scheme by analyzing transaction flows and account relationships in a graph database.*

         <div style="background-color:#f0f2f6;padding:10px;border-radius:5px;">
        <p style="font-weight: bold;">Key Takeaway:</p>
        <p>The choice of algorithm depends heavily on the specific fraud/risk problem, data characteristics, and desired outcome (interpretability, accuracy, speed). Often, a combination of algorithms and techniques is used for a robust and comprehensive fraud and risk detection system. Deep Learning and Graph Analytics are increasingly important for handling complex and evolving fraud scenarios.</p>
        </div>
        """
        )

    with st.expander("📖 3. Business Use Cases Across Industries 🏢", expanded=False):
        st.markdown(
            """
        ### 3. Business Use Cases Across Industries 🏢

        Data analytics for fraud and risk detection is not confined to a single industry; its principles and techniques are broadly applicable across diverse sectors. Here are key use cases highlighting industry-specific applications:

        *   **3.1 Financial Services:** Industry at the forefront of fraud and risk analytics due to high stakes and regulatory scrutiny.

            *   **Banking:**
                *   **Retail Banking:**
                    *   **Credit Card Fraud Detection:** Real-time transaction monitoring, ML models on transaction features and user behavior for immediate fraud prevention. *Focus: Minimizing transaction-level fraud and customer impact.*
                    *   **Anti-Money Laundering (AML):** Transaction pattern and network analysis for illicit financial flows, compliance-driven. *Focus: Regulatory compliance and preventing financial crime.*
                    *   **Loan Application Fraud:** Analysis of application data, credit history, and external data to identify fraudulent loan attempts. *Focus: Preventing loan losses at origination.*
                    *   **Account Takeover (ATO) Detection:** Login and behavior pattern monitoring, device fingerprinting, and anomaly detection for unauthorized account access. *Focus: Protecting customer accounts and funds from unauthorized access.*
                *   **Insurance:**
                    *   **Claims Fraud Detection:** Claim details, medical records, and historical data analysis for suspicious patterns and anomalies in insurance claims. *Focus: Reducing fraudulent payouts and controlling claim costs.*
                    *   **Application Fraud:** Applicant data and external database analysis to detect misrepresentation or fraud in insurance applications. *Focus: Preventing adverse selection and fraudulent policy issuance.*
                    *   **Premium Fraud:** Detection of policyholders intentionally underreporting risk factors to lower premiums, impacting revenue integrity. *Focus: Ensuring fair premium collection and accurate risk pricing.*
                *   **Investment Management:**
                    *   **Market Manipulation Detection:** Suspicious trading pattern analysis for market manipulation schemes (pump and dump, insider trading). *Focus: Maintaining market integrity and regulatory compliance.*
                    *   **Risk Management in Trading:** Assessing and managing various financial risks (market risk, credit risk, operational risk) associated with trading activities using predictive models and risk dashboards. *Focus: Ensuring portfolio stability and regulatory compliance.*

        *   **3.2 E-commerce and Retail:** Critical for protecting online revenue and customer trust in digital commerce.

            *   **Online Retail:**
                *   **Payment Fraud Detection:** Real-time online payment monitoring, similar to credit card fraud but adapted for e-commerce transactions. *Focus: Minimizing payment processing fraud and chargebacks.*
                *   **Account Takeover (E-commerce):** Prevention of unauthorized access to customer accounts on e-commerce platforms, protecting customer data and loyalty points. *Focus: Customer account security and data protection.*
                *   **Return Fraud:** Analysis of return patterns for suspicious activities, preventing losses from fraudulent returns of merchandise. *Focus: Reducing losses from fraudulent return schemes.*
                *   **Promotion Abuse:** Identifying customers violating promotional terms, abusing discounts and offers unfairly, impacting promotional ROI. *Focus: Optimizing promotional campaign effectiveness and preventing unfair discount abuse.*
            *   **Digital Services:**
                *   **Subscription Fraud:** Detection of fraudulent subscriptions to digital services, trial abuse, and unauthorized access. *Focus: Protecting revenue from fraudulent subscriptions and service misuse.*
                *   **Digital Goods Fraud:** Transaction and device verification, behavior analysis for fraudulent transactions involving digital goods (e.g., software, digital content). *Focus: Securing digital asset transactions and preventing digital piracy related fraud.*

        *   **3.3 Healthcare:** Vital for cost containment and protecting against fraudulent claims in healthcare systems.

            *   **Healthcare Fraud Detection:** Medical claim analysis for billing fraud, upcoding, and unnecessary procedures, impacting healthcare costs. *Focus: Reducing healthcare costs and ensuring appropriate medical billing practices.*
            *   **Medical Identity Theft:** Detection of stolen medical identities used to obtain healthcare services or prescription drugs, impacting patient safety and healthcare system integrity. *Focus: Patient safety and preventing fraudulent access to healthcare services.*
            *   **Prescription Drug Fraud:** Identifying fraudulent prescriptions and illegal distribution of controlled substances, addressing drug diversion and misuse. *Focus: Preventing drug abuse and ensuring legitimate prescription practices.*

        *   **3.4 Telecommunications:** Protecting revenue streams and service integrity in telecom operations.

            *   **Subscription Fraud:** Detecting fraudulent subscriptions to telecommunication services (mobile, internet, cable), preventing unpaid service usage. *Focus: Revenue protection from fraudulent subscriptions.*
                *   **Toll Fraud:** Detecting unauthorized use of telecommunication services, often through hacking or social engineering, preventing service abuse. *Focus: Preventing unauthorized service usage and toll revenue losses.*
                *   **Roaming Fraud:** Detecting fraudulent use of roaming services by subscribers, minimizing international roaming revenue losses. *Focus: Roaming revenue assurance and fraud prevention in international telecom services.*

        *   **3.5 Government and Public Sector:** Ensuring efficient use of public funds and preventing fraud in government programs.

            *   **Tax Fraud Detection:** Identifying fraudulent tax returns and tax evasion, maximizing tax revenue collection and fairness. *Focus: Maximizing tax revenue and ensuring tax system integrity.*
                *   **Benefit Fraud Detection:** Detecting fraudulent claims for government benefits (unemployment, social security, welfare), ensuring public fund integrity. *Focus: Protecting public funds and ensuring fair distribution of benefits.*
                *   **Public Procurement Fraud:** Detecting fraud in government procurement processes (bid rigging, inflated invoices, corruption), ensuring fair government spending. *Focus: Ensuring fair and transparent government procurement processes.*

        *   **3.6 Cybersecurity:** Integral to protecting digital assets and infrastructure across all industries, often intersecting with financial fraud.

            *   **Intrusion Detection and Prevention:** Network and system log analysis for unauthorized access, detecting and preventing cyber intrusions. *Focus: Protecting digital infrastructure and data from cyberattacks.*
                *   **Insider Threat Detection:** Monitoring employee activities for malicious actions from insiders with legitimate access, preventing data breaches and internal fraud. *Focus: Preventing insider-driven security incidents and data leaks.*
                *   **Phishing Detection:** Analyzing emails and websites for phishing attempts, blocking phishing attacks and protecting user credentials. *Focus: User protection from phishing attacks and credential theft.*
                *   **Malware Detection:** Identifying and removing malicious software from systems and networks, preventing malware infections and related data compromise. *Focus: System security and malware threat mitigation.*

         <div style="background-color:#f0f2f6;padding:10px;border-radius:5px;">
        <p style="font-weight: bold;">Key Takeaway:</p>
        <p>Data analytics is a versatile tool applicable across industries for fraud and risk detection.  Industry-specific use cases demonstrate the broad applicability and tailored approaches needed to address diverse fraud and risk challenges in each sector. The underlying principles of data analysis and algorithm application, however, remain consistent across these diverse applications.</p>
        </div>
        """
        )

    with st.expander("📖 4. Tools and Technologies 🛠️", expanded=False):
        st.markdown(
            """
        ### 4. Tools and Technologies for Data Analytics in Fraud and Risk Detection 🛠️

        A robust technology stack is indispensable for building and deploying effective data analytics solutions for fraud and risk detection. The landscape includes a variety of tools, each with specific strengths and purposes:

        *   **Programming Languages:** Foundation for data manipulation, algorithm development, and system integration.
            *   **Python:** The dominant language in data science and machine learning. Offers a rich ecosystem of libraries:
                *   **Pandas:** For efficient data manipulation and analysis (DataFrames).
                *   **NumPy:** For numerical computing, array operations, and mathematical functions.
                *   **Scikit-learn:** Comprehensive library for classical machine learning algorithms (classification, regression, clustering).
                *   **TensorFlow & PyTorch:** Leading deep learning frameworks for building and training neural networks.
            *   **R:** Another popular language for statistical computing, data visualization, and specialized statistical analysis. Strong in statistical modeling.
            *   **SQL (Structured Query Language):** Essential for interacting with databases, querying, and manipulating structured data stored in relational databases.

        *   **Data Visualization Tools:** Critical for exploratory data analysis, building dashboards, and communicating insights effectively.
            *   **Tableau:** Powerful and user-friendly data visualization platform, known for its interactive dashboards and ease of use.
            *   **Power BI (Microsoft Power Business Intelligence):** Microsoft's data visualization and business intelligence tool, tightly integrated with Microsoft ecosystem.
            *   **Qlik Sense:** Another leading data visualization and analytics platform, known for its associative data engine and flexible visualizations.
            *   **Python Libraries (Matplotlib, Seaborn, Plotly):** For creating custom visualizations within Python environments, offering fine-grained control and integration with analytical workflows. *Plotly is especially useful for interactive and web-based visualizations within Streamlit applications.*

        *   **Machine Learning Platforms and Libraries:** Provide the algorithms, frameworks, and infrastructure for building, training, and deploying machine learning models.
            *   **Scikit-learn (Python):** Comprehensive library for classical machine learning algorithms (classification, regression, clustering, dimensionality reduction, model selection, preprocessing). *Excellent for a wide range of traditional ML tasks.*
            *   **TensorFlow (Python, Java, C++):** Google's open-source deep learning framework, widely adopted in industry and research, supports distributed computing and GPU acceleration. *Powerful for complex deep learning models.*
            *   **PyTorch (Python):** Facebook's open-source deep learning framework, popular in research and increasingly in industry, known for its flexibility and dynamic computation graphs. *Favored for research and rapid prototyping in deep learning.*
            *   **Cloud-based ML Platforms (AWS SageMaker, Google AI Platform, Azure Machine Learning):** Managed platforms provided by cloud providers (Amazon, Google, Microsoft) for building, training, and deploying ML models in scalable and cost-effective cloud environments. *Simplify ML lifecycle management and offer pre-built services.*

        *   **Big Data Technologies:**  Essential for handling the massive datasets common in fraud and risk analytics, enabling distributed storage and processing.
            *   **Hadoop:** Framework for distributed storage (Hadoop Distributed File System - HDFS) and processing (MapReduce) of large datasets across clusters of computers. *Foundation for big data processing.*
            *   **Spark:** Fast, general-purpose distributed computing system, often used in conjunction with Hadoop or other data storage systems. Offers in-memory processing and supports various data processing tasks (SQL, streaming, MLlib for machine learning). *Faster alternative to MapReduce for many workloads.*
            *   **Cloud Data Warehouses (Amazon Redshift, Google BigQuery, Snowflake):** Scalable and cost-effective data warehouses hosted in the cloud for storing and analyzing large volumes of structured and semi-structured data. Offer SQL-based querying and integration with data analytics tools. *Scalable data warehousing solutions in the cloud.*

        *   **Databases and Data Warehouses:** Systems for storing, managing, and retrieving data, ranging from traditional relational databases to NoSQL and specialized graph databases.
            *   **Relational Databases (MySQL, PostgreSQL, Oracle, SQL Server):** Traditional databases for structured data storage and management, using SQL for querying and manipulation. *Well-established for transactional data and structured information.*
            *   **NoSQL Databases (MongoDB, Cassandra):** Databases designed for handling unstructured and semi-structured data (documents, key-value pairs, wide-column stores). Offer scalability and flexibility for diverse data types. *Suitable for flexible data models and high-volume data.*
            *   **Graph Databases (Neo4j, Amazon Neptune):** Databases specialized in storing and analyzing network data, representing data as nodes and relationships. Crucial for fraud ring detection, social network analysis, and relationship-centric data analysis. *Optimized for network data and relationship queries.*

        *   **Specialized Fraud Detection and Risk Management Software:** Commercial software solutions purpose-built for fraud detection and risk management, often offering pre-built models, rules engines, and case management systems.
            *   **SAS Fraud Management:** Enterprise-level fraud detection and prevention software suite, offering comprehensive fraud analytics and rule-based systems. *Established solution for large organizations.*
            *   **Nice Actimize:** Financial crime, risk, and compliance solutions specifically designed for financial institutions, covering AML, fraud, and market abuse detection. *Focus on financial crime compliance and risk management in finance.*
            *   **FICO Falcon Fraud Manager:** Widely used credit card fraud detection system, known for its real-time transaction scoring and adaptive analytics. *Industry-standard for credit card fraud detection.*
            *   **IBM Security QRadar:** Security information and event management (SIEM) system for cybersecurity risk management, providing real-time threat detection and security event analysis. *Focus on cybersecurity threat detection and incident response.*

         <div style="background-color:#f0f2f6;padding:10px;border-radius:5px;">
        <p style="font-weight: bold;">Key Takeaway:</p>
        <p>A comprehensive technology stack for fraud and risk analytics encompasses programming languages, visualization tools, machine learning platforms, big data technologies, and specialized databases. The selection of tools depends on the scale of data, complexity of analysis, and specific requirements of the fraud and risk detection use cases.</p>
        </div>
        """
        )

    with st.expander("📖 5. Challenges and Best Practices 🚧", expanded=False):
        st.markdown(
            """
        ### 5. Challenges and Best Practices in Implementation 🚧

        Implementing effective data analytics for fraud and risk detection is not without its challenges. Addressing these challenges requires adherence to best practices across data management, model development, and deployment:

        *   **5.1 Challenges:** Common hurdles faced during the implementation process.
            *   **Data Quality and Availability:** Fraud detection models are critically reliant on high-quality and comprehensive data. Issues like missing data, inaccurate data, inconsistencies, and data silos can severely hinder model performance and reliability. *Challenge: Ensuring data is accurate, complete, consistent, and accessible across silos is a major undertaking.*
            *   **Evolving Fraud Tactics:** Fraudsters are constantly adapting their methods to evade detection mechanisms. Models trained on historical data may become less effective as fraud patterns change. Continuous model updates and adaptation are essential. *Challenge: Maintaining model effectiveness against evolving fraud tactics requires ongoing monitoring, adaptation, and potentially, real-time learning capabilities.*
            *   **Class Imbalance:** Fraudulent transactions or risky events are often rare compared to normal, legitimate transactions. This significant class imbalance can bias machine learning models towards predicting the majority class (non-fraudulent), leading to poor detection of actual fraud cases. *Challenge: Addressing class imbalance requires specialized techniques like oversampling, undersampling, cost-sensitive learning, and using appropriate evaluation metrics beyond accuracy.*
            *   **Model Interpretability and Explainability:** In highly regulated industries (e.g., finance, healthcare), interpretability and explainability of model decisions are paramount. "Black box" models like deep neural networks can be challenging to interpret, making it difficult to understand *why* a particular transaction was flagged as fraudulent, which is crucial for regulatory compliance and auditability. *Challenge: Balancing model accuracy with interpretability and explainability, especially when using complex models in regulated environments.*
            *   **Privacy and Data Security:** Handling sensitive customer data (financial, personal) in fraud detection requires strict adherence to data privacy regulations (GDPR, CCPA, HIPAA, etc.) and robust data security measures to prevent data breaches and misuse. *Challenge: Implementing analytics while ensuring data privacy compliance and robust security is a critical responsibility.*
            *   **Ethical Considerations and Bias:** Machine learning models can inadvertently perpetuate or even amplify biases present in the training data. This can lead to unfair or discriminatory outcomes in fraud and risk detection, disproportionately impacting certain demographic groups. *Challenge: Ensuring fairness, mitigating bias, and addressing ethical considerations in AI-driven fraud and risk detection is crucial for responsible AI implementation.*
            *   **Integration with Existing Systems:** Implementing new data analytics solutions often requires seamless integration with complex and often legacy existing IT infrastructure and operational processes. Compatibility issues, data integration challenges, and system interoperability need to be addressed. *Challenge: Seamlessly integrating new analytics solutions into existing complex IT ecosystems can be technically and organizationally challenging.*

        *   **5.2 Best Practices:** Recommended approaches to mitigate challenges and build robust systems.
            *   **Data Governance and Quality Management:** Establish robust data governance frameworks and data quality management processes to ensure data accuracy, completeness, consistency, and timely availability. Implement data validation, data lineage tracking, and data quality monitoring procedures. *Best Practice: Invest in data quality initiatives and establish data governance policies from the outset.*
            *   **Feature Engineering and Selection:** Invest in effective feature engineering to create informative features that capture relevant patterns for fraud and risk detection. Select the most relevant features to improve model performance, reduce dimensionality, and enhance interpretability. Involve domain experts in feature engineering. *Best Practice: Prioritize feature engineering as a key driver of model performance; domain expertise is invaluable.*
            *   **Model Selection and Evaluation:** Choose appropriate machine learning algorithms based on the specific use case, data characteristics, interpretability requirements, and performance needs. Rigorously evaluate model performance using appropriate metrics beyond accuracy (precision, recall, F1-score, AUC, lift charts) and robust validation techniques (cross-validation, hold-out testing, backtesting). *Best Practice: Select models thoughtfully based on problem requirements and thoroughly evaluate performance using relevant metrics and validation methods.*
            *   **Continuous Model Monitoring and Retraining:** Implement continuous model performance monitoring in production environments. Track key metrics, detect model drift (performance degradation over time), and retrain models periodically with new data to adapt to evolving fraud patterns and maintain accuracy. Establish model retraining pipelines and version control. *Best Practice: Treat models as dynamic entities requiring continuous monitoring and adaptive retraining.*
            *   **Explainable AI (XAI) and Interpretability Techniques:** Employ Explainable AI (XAI) techniques to understand model decisions, especially for complex models like neural networks. Use techniques like feature importance analysis, SHAP values, LIME, and rule extraction to gain insights into model behavior and decision-making processes. *Best Practice: Prioritize model interpretability, especially in regulated domains; use XAI techniques to understand model decisions.*
            *   **Privacy-Preserving Analytics:** Implement privacy-enhancing technologies (e.g., differential privacy, federated learning, anonymization techniques) to analyze sensitive data while preserving user privacy and complying with data protection regulations. *Best Practice: Embed privacy by design and utilize privacy-preserving techniques when handling sensitive data.*
            *   **Collaboration and Information Sharing:** Foster close collaboration between data scientists, fraud investigators, risk managers, compliance officers, and business stakeholders. Encourage information sharing and insights exchange across departments to improve overall fraud and risk detection capabilities. Establish cross-functional teams and communication channels. *Best Practice: Promote interdisciplinary collaboration and knowledge sharing to enhance effectiveness.*
            *   **Ethical AI Development and Deployment:** Incorporate ethical considerations into all stages of AI development and deployment lifecycle. Conduct bias audits of data and models, ensure fairness and non-discrimination, promote transparency and accountability in AI systems. Establish ethical AI guidelines and oversight mechanisms. *Best Practice: Embed ethical principles into AI development and deployment; prioritize fairness, transparency, and accountability.*

         <div style="background-color:#f0f2f6;padding:10px;border-radius:5px;">
        <p style="font-weight: bold;">Key Takeaway:</p>
        <p>Implementing data analytics for fraud and risk detection is a complex undertaking requiring careful planning and execution. Addressing challenges proactively through best practices in data management, model development, ethical considerations, and collaboration is crucial for building robust and effective systems.</p>
        </div>
        """
        )

        st.markdown(
            """
        ### 6. Future Trends in Data Analytics for Fraud and Risk Detection 🔮

        The field of data analytics for fraud and risk detection is continuously evolving, driven by rapid technological advancements and the increasingly sophisticated nature of fraud and risk. Key future trends shaping the field include:

        *   **Real-time Fraud Detection and Prevention:** A growing emphasis on real-time analytics capabilities to detect and block fraudulent activities *as they happen*, minimizing potential losses and immediate damage. Expect increased adoption of streaming data analytics and ultra-low latency models for immediate action. *Trend: Shift towards proactive, real-time fraud intervention rather than reactive detection.*

        *   **AI and Machine Learning Advancements:** Continued and rapid advancements in Artificial Intelligence (AI) and Machine Learning (ML) algorithms, particularly in deep learning, are set to significantly enhance fraud and risk detection capabilities. Anticipate more sophisticated:
            *   **Anomaly Detection Techniques:**  Moving beyond basic statistical methods to advanced deep learning-based anomaly detection for subtle and evolving anomalies.
            *   **Natural Language Processing (NLP) for Unstructured Data Analysis:** Increased use of NLP to analyze unstructured data sources (text, voice) for sentiment analysis, fraud clues in communications, and risk assessment from textual content.
            *   **Reinforcement Learning for Adaptive Security Measures:** Exploring reinforcement learning for dynamic and adaptive security systems that learn and optimize their responses to evolving threats in real-time.
            *   **Explainable AI (XAI) by Design:**  Newer AI models will increasingly incorporate explainability directly into their architecture, addressing the "black box" challenge. *Trend: More powerful and nuanced AI techniques pushing the boundaries of detection accuracy and proactive intervention.*

        *   **Federated Learning and Privacy-Preserving AI:** Growth of federated learning techniques, allowing model training across decentralized data sources (multiple banks, institutions) without direct sharing of raw sensitive data. Enhances privacy and enables collaborative model building while adhering to data protection regulations. Expect increased use of privacy-preserving AI methodologies. *Trend: Collaborative model building while maintaining data privacy, addressing data sharing limitations and regulatory requirements.*

        *   **Graph Analytics for Complex Fraud Schemes:** Increased utilization of graph analytics and graph databases to uncover complex fraud schemes involving intricate networks of individuals, entities, and transactions. Particularly relevant for detecting fraud rings, money laundering networks, organized crime, and complex financial crime schemes that are difficult to detect with traditional methods. *Trend: Focus on network-based fraud detection, uncovering hidden relationships and complex schemes.*

        *   **Explainable and Trustworthy AI (XAI and Trustworthy AI):**  A greater emphasis on **explainable and trustworthy AI systems** in fraud and risk detection, driven by increasing regulatory requirements, ethical considerations, and the need for human oversight and auditability. Transparency, fairness, and accountability will be critical aspects of future AI deployments in this domain. *Trend: Demanding transparency, fairness, accountability, and human oversight in AI-driven systems for regulatory compliance and ethical considerations.*

        *   **Integration of Cybersecurity and Fraud Analytics (Cyber-Fraud Convergence):**  Closer integration of cybersecurity analytics and fraud analytics to create a holistic and unified approach to risk management. Recognizing the significant overlap and convergence between cyber threats and financial fraud, expect integrated platforms and strategies that address both domains synergistically. *Trend: Unified security and fraud detection strategies, recognizing the cyber-financial crime nexus.*

        *   **Use of Biometrics and Behavioral Biometrics for Enhanced Security:** Growing adoption of biometric authentication (fingerprint, facial recognition) and behavioral biometrics (typing patterns, mouse movements, gait analysis) to enhance security and fraud prevention. Leveraging unique individual characteristics for stronger identity verification, continuous authentication, and anomaly detection based on behavioral patterns. *Trend: Stronger identity verification and continuous authentication using biometrics and behavioral data, reducing reliance on traditional passwords.*

        *   **Quantum Computing for Risk Analysis (Long-term Perspective):** While still in early stages, quantum computing holds the potential to revolutionize risk analysis and fraud detection in the long term. Quantum computers could enable faster and more complex computations, breaking current encryption methods and enabling more sophisticated risk modeling. However, practical applications in this domain are still further in the future. *Trend (Long-term): Potential for quantum computing to transform risk analysis and break current cryptographic standards in the distant future.*

         <div style="background-color:#f0f2f6;padding:10px;border-radius:5px;">
        <p style="font-weight: bold;">Key Takeaway:</p>
        <p>The future of data analytics in fraud and risk detection is characterized by a move towards real-time, AI-driven, privacy-conscious, and network-centric approaches. Explainable and trustworthy AI will be paramount, and emerging technologies like quantum computing hold long-term potential to reshape the landscape. Staying ahead requires continuous learning and adaptation to these evolving trends.</p>
        </div>
        """
        )

    # interactive_section removed (was assigned but unused)

    with st.expander(" 📈 Interactive Transaction Anomaly Simulation", expanded=True):
        st.subheader("Interactive Transaction Anomaly Simulation")
        num_transactions_sim = st.slider(
            "Number of Transactions:",
            min_value=100,
            max_value=1000,
            value=500,
            key="num_trans_slider",
        )
        anomaly_rate_sim = (
            st.slider(
                "Anomaly Rate (%):",
                min_value=0,
                max_value=20,
                value=5,
                key="anom_rate_slider",
            )
            / 100.0
        )
        anomaly_type_sim = st.selectbox(
            "Anomaly Type:",
            ["amount", "location", "category", "velocity"],
            index=0,
            key="anom_type_selectbox",
        )

        if st.button("Simulate Transactions", key="sim_button"):
            df_sim = generate_transaction_data_interactive(
                num_transactions_sim, anomaly_rate_sim, anomaly_type_sim
            )
            fig_scatter = px.scatter(
                df_sim,
                x="Transaction ID",
                y="Amount",
                color="Is Anomaly",
                title="Simulated Transactions with Anomalies",
                color_discrete_map={False: "blue", True: "red"},
            )
            st.plotly_chart(fig_scatter)
            st.write(
                "This simulation visualizes transaction amounts. Red points indicate anomalies. Anomalies are introduced based on the 'Anomaly Type' selected. In a real-world scenario, anomaly detection algorithms would automatically flag these deviations."
            )

            time_hist = px.histogram(
                df_sim,
                x=df_sim["Timestamp"].dt.hour,
                nbins=24,
                title="Transaction Time Distribution (Hour of Day)",
            )
            st.plotly_chart(time_hist)
            st.write(
                "Transaction Time Distribution: Observe the typical hours for transactions. Anomalous transactions might occur outside normal hours, especially with velocity anomalies."
            )

            if anomaly_type_sim == "location":
                st.subheader("Geographic Transaction Visualization")
                m = folium.Map(location=[0, 0], zoom_start=2)  # World map centered
                for index, row in df_sim.iterrows():
                    folium.Marker(
                        [row["Latitude"], row["Longitude"]],
                        popup=f"Transaction ID: {row['Transaction ID']}, Location: {row['Location']}, Anomaly: {row['Is Anomaly']}",
                    ).add_to(m)
                folium_static(m)
                st.write(
                    "Geographic Anomalies: Red markers might represent transactions in unusual or high-risk locations when 'location' anomaly type is selected."
                )

            category_bar = px.bar(
                df_sim["Category"].value_counts(),
                title="Merchant Category Distribution",
                labels={
                    "value": "Number of Transactions",
                    "index": "Merchant Category",
                },
            )
            st.plotly_chart(category_bar)
            st.write(
                "Merchant Category Distribution: View the distribution of transactions across different merchant categories. Anomalous transactions might disproportionately occur in unusual or high-risk categories when 'category' anomaly type is selected."
            )

            amount_box = px.box(
                df_sim, y="Amount", title="Transaction Amount Distribution (Box Plot)"
            )
            st.plotly_chart(amount_box)
            st.write(
                "Transaction Amount Distribution: A box plot provides a view of the distribution of transaction amounts, highlighting potential outliers (anomalies) with unusually high amounts, especially when 'amount' anomaly type is selected."
            )

    with st.expander(" 🚦 Interactive Rule-Based Fraud Detection", expanded=False):
        st.subheader("Interactive Rule-Based Fraud Detection System")
        st.write("Define and test your own fraud rules on simulated transactions.")

        rule_amount_threshold = st.slider(
            "Amount Threshold for Rule 1:", min_value=100, max_value=500, value=300
        )
        rule_category_options = [
            "Luxury Goods",
            "Entertainment",
            "Travel",
            "Electronics",
            "Restaurant",
            "Clothing",
            "Grocery",
            "Home Goods",
        ]
        rule_category = st.multiselect(
            "Merchant Categories for Rule 1:",
            rule_category_options,
            default=["Luxury Goods", "Entertainment"],
        )
        rule_location_options = [
            "Dubai",
            "New York",
            "London",
            "Tokyo",
            "Sydney",
            "Paris",
            "Rio de Janeiro",
            "Cairo",
        ]
        rule_location = st.multiselect(
            "Locations for Rule 2 (High-Risk Locations):",
            rule_location_options,
            default=["Dubai"],
        )
        st.slider(
            "Velocity Threshold (Transactions per Hour) for Rule 3:",
            min_value=1,
            max_value=10,
            value=3,
        )
        time_of_day_rule3 = st.select_slider(
            "Time of Day for Rule 3 (Night Hours):",
            options=["Night", "Morning", "Afternoon", "Evening"],
            value=("Night"),
        )

        if st.button("Apply Rules and Detect Fraud"):
            rule_based_df = generate_transaction_data_interactive(
                num_transactions=500
            )  # Generate data for rule testing

            # Rule 1: High Amount in Specific Categories
            rule1_mask = (rule_based_df["Amount"] > rule_amount_threshold) & (
                rule_based_df["Category"].isin(rule_category)
            )
            rule_based_df["Rule 1 Flag"] = rule1_mask

            # Rule 2: Transactions in High-Risk Locations
            rule2_mask = rule_based_df["Location"].isin(rule_location)
            rule_based_df["Rule 2 Flag"] = rule2_mask

            # Rule 3: High Velocity Transactions at Night (Conceptual - requires more complex velocity calculation in real-time)
            # For simplicity, we'll flag all transactions in 'Night' time for demonstration in this simplified interactive example
            rule_based_df["Hour"] = rule_based_df["Timestamp"].dt.hour

            def categorize_time(hour):
                if 22 <= hour or hour < 6:
                    return "Night"  # Simplified night definition
                else:
                    return "Day"

            rule_based_df["Time Category"] = rule_based_df["Hour"].apply(
                categorize_time
            )
            rule3_mask = (
                rule_based_df["Time Category"] == time_of_day_rule3
            )  # Simplified time based rule - velocity requires more complex logic
            rule_based_df["Rule 3 Flag"] = rule3_mask

            # Combine Rules: Flag if ANY rule is triggered
            rule_based_df["Rule-Based Fraud Flag"] = rule_based_df[
                ["Rule 1 Flag", "Rule 2 Flag", "Rule 3 Flag"]
            ].any(axis=1)

            st.dataframe(
                rule_based_df[
                    [
                        "Transaction ID",
                        "Amount",
                        "Category",
                        "Location",
                        "Timestamp",
                        "Rule 1 Flag",
                        "Rule 2 Flag",
                        "Rule 3 Flag",
                        "Rule-Based Fraud Flag",
                    ]
                ]
            )

            fraud_count = rule_based_df["Rule-Based Fraud Flag"].sum()
            total_transactions = len(rule_based_df)
            fraud_percentage = (
                (fraud_count / total_transactions) * 100
                if total_transactions > 0
                else 0
            )

            st.write(
                f"Transactions Flagged as Potentially Fraudulent by Rules: **{fraud_count} out of {total_transactions} ({fraud_percentage:.2f}%)**"
            )
            st.info(
                "Experiment with different rule parameters (thresholds, categories, locations, velocity) to see how the number of flagged transactions changes. Rule-based systems are effective for known fraud patterns but may miss new or subtle fraud schemes."
            )

    with st.expander(" 🔍 Interactive Feature Importance Exploration", expanded=False):
        st.subheader("Interactive Feature Importance Exploration with a Simple Model")
        st.write(
            "Explore how different features contribute to fraud prediction in a basic Logistic Regression model."
        )

        feature_importance_df = generate_transaction_data_interactive(
            num_transactions=500, anomaly_rate=0.1
        )  # Higher anomaly rate for better demonstration
        feature_importance_df["time_of_day"] = feature_importance_df[
            "Timestamp"
        ].dt.hour
        feature_importance_df["is_weekend"] = (
            feature_importance_df["Timestamp"].dt.dayofweek >= 5
        ).astype(
            int
        )  # Weekend Feature
        feature_importance_df["location_risk"] = feature_importance_df[
            "Location"
        ].apply(
            lambda loc: 1 if loc in ["Dubai", "Cairo"] else 0
        )  # Example location risk

        features_for_model = [
            "Amount",
            "time_of_day",
            "is_weekend",
            "location_risk",
        ]  # Features for Logistic Regression
        X = feature_importance_df[features_for_model]
        y = feature_importance_df["Is Anomaly"].astype(int)

        from sklearn.linear_model import LogisticRegression

        model = LogisticRegression()
        model.fit(X, y)

        importance_scores = model.coef_[
            0
        ]  # Coefficients from Logistic Regression as feature importance
        feature_importance_plot_df = pd.DataFrame(
            {"Feature": features_for_model, "Importance Score": importance_scores}
        )
        feature_importance_plot_df = feature_importance_plot_df.sort_values(
            by="Importance Score", ascending=False
        )

        fig_importance = px.bar(
            feature_importance_plot_df,
            x="Feature",
            y="Importance Score",
            title="Feature Importance Scores from Logistic Regression",
            labels={
                "Importance Score": "Coefficient Value (Magnitude indicates Importance)"
            },
        )
        st.plotly_chart(fig_importance)
        st.write(
            "Feature Importance from Logistic Regression: This chart shows the coefficients from a Logistic Regression model trained to predict 'Is Anomaly'. The magnitude of the coefficient indicates the feature's importance in the model's decision. Positive or negative sign indicates the direction of the feature's impact (though sign interpretation can be complex in Logistic Regression)."
        )
        st.info(
            "Observe which features the simple Logistic Regression model deems most important for fraud detection based on the simulated data. In real-world models, feature importance analysis helps understand model behavior and refine feature engineering."
        )

    with st.expander(
        " 🗺️ Interactive Anomaly Detection with Clustering", expanded=False
    ):
        st.subheader("Interactive Anomaly Detection using Clustering (DBSCAN)")
        st.write(
            "Visualize how clustering algorithms like DBSCAN can identify anomalies (outliers) in transaction data."
        )

        num_samples_cluster = st.slider(
            "Number of Data Points for Clustering:",
            min_value=200,
            max_value=1000,
            value=500,
            key="cluster_slider",
        )
        epsilon_dbscan = st.slider(
            "DBSCAN Epsilon (ε - Radius):",
            min_value=0.1,
            max_value=2.0,
            value=0.5,
            step=0.1,
            key="epsilon_slider",
        )
        min_samples_dbscan = st.slider(
            "DBSCAN Min Samples:",
            min_value=2,
            max_value=20,
            value=5,
            step=1,
            key="min_samples_slider",
        )

        if st.button("Run DBSCAN Clustering for Anomaly Detection"):
            cluster_df = generate_transaction_data_interactive(
                num_transactions=num_samples_cluster,
                anomaly_rate=0.1,
                anomaly_type="amount",
            )  # Amount anomalies for visual clarity
            cluster_df["time_of_day"] = cluster_df["Timestamp"].dt.hour
            cluster_data = cluster_df[
                ["Amount", "time_of_day"]
            ].copy()  # Using Amount and time_of_day for 2D clustering

            scaler = StandardScaler()  # Standardize features for DBSCAN
            scaled_data = scaler.fit_transform(cluster_data)

            dbscan = DBSCAN(eps=epsilon_dbscan, min_samples=min_samples_dbscan)
            clusters = dbscan.fit_predict(scaled_data)
            cluster_df["Cluster"] = clusters  # Add cluster labels to dataframe

            fig_cluster = px.scatter(
                cluster_df,
                x="time_of_day",
                y="Amount",
                color="Cluster",
                title="DBSCAN Clustering for Anomaly Detection (Anomalies in Cluster -1)",
                labels={"Cluster": "Cluster ID (-1 = Anomalies/Noise)"},
                color_continuous_scale=px.colors.qualitative.Set1,
            )  # Color scale for clusters
            st.plotly_chart(fig_cluster)

            st.write(
                "DBSCAN Clustering Results: DBSCAN has clustered transactions based on 'Amount' and 'Time of Day'. Points in Cluster '-1' are considered noise or anomalies by DBSCAN (outliers that do not belong to any dense cluster). Experiment with different 'Epsilon' (radius) and 'Min Samples' parameters to see how cluster formation and anomaly detection changes. Higher epsilon expands cluster radius, lower min_samples makes clusters easier to form (more noise/anomalies might be classified as clusters)."
            )
            st.info(
                "Clustering-based anomaly detection is useful for identifying outliers without pre-defined labels. DBSCAN is effective in finding clusters of arbitrary shapes and identifying noise points as anomalies."
            )

    with st.expander("💪 3. Practice Exercises", expanded=False):
        st.subheader("Practice Exercises to Apply Your Knowledge")

        st.markdown(
            """
        **Exercise 3.1: Feature Engineering for Transaction Data (Conceptual)**

        Imagine you have transaction data with columns: `transaction_id`, `customer_id`, `timestamp`, `amount`, `location`, `merchant_category`.

        1.  **Create a 'time_of_day' feature:** Conceptually explain how you would extract the hour from the `timestamp` and categorize it into 'Morning', 'Afternoon', 'Evening', 'Night' using Python (Pandas). Provide a code snippet example.
        2.  **Create a 'transaction_frequency' feature:**  Conceptually explain how you would calculate the number of transactions for each `customer_id` in the last 7 days *before* each transaction using Pandas. Provide a code snippet outline.
        3.  **Create a 'location_risk' feature:** Assume you have an external dataset `location_risk_data` (e.g., CSV) with columns `location` and `risk_score`.  Explain how you would merge this risk score into your transaction data based on the `location` column using Pandas. Provide conceptual steps.

        *Hint:* Consider using Pandas library in Python for these exercises. Focus on the *conceptual steps and code outlines* rather than fully executable code within Streamlit for these feature engineering exercises due to complexity.*

        ```python
        # Example code snippets (Conceptual outlines)

        # 1. Time of Day Feature (Conceptual)
        # df['hour'] = df['timestamp'].dt.hour
        # def categorize_time(hour):
        #     if 6 <= hour < 12: return 'Morning'
        #     elif 12 <= hour < 17: return 'Afternoon'
        #     elif 17 <= hour < 22: return 'Evening'
        #     else: return 'Night'
        # df['time_of_day'] = df['hour'].apply(categorize_time)
        # st.code(...) # Show code snippet in Streamlit

        # 2. Transaction Frequency Feature (Conceptual - outline)
        # def calculate_frequency(customer_transactions): # Function operating on customer's transactions
        #     frequencies = []
        #     for i, trans in enumerate(customer_transactions):
        #         past_week_transactions = customer_transactions[(customer_transactions['timestamp'] < trans['timestamp']) & (customer_transactions['timestamp'] >= trans['timestamp'] - pd.Timedelta(days=7))]
        #         frequencies.append(len(past_week_transactions))
        #     return frequencies
        # # df.groupby('customer_id').apply(calculate_frequency) # Apply per customer

        # 3. Location Risk Feature (Conceptual - outline - assuming location_risk_df loaded)
        # # df = pd.merge(df, location_risk_df, on='location', how='left') # Merge based on 'location' column
        ```
        """
        )

        st.markdown(
            """
        **Exercise 3.2: Rule-Based Fraud Detection (Design Exercise)**

        Design a more nuanced rule-based system to flag potentially fraudulent transactions. Consider these factors:

        1.  **Rule 1: Amount Threshold with Category Context:** Flag transactions where `amount` > $200 *AND* `merchant_category` is 'Luxury Goods' or 'Entertainment' (higher threshold for certain categories).
        2.  **Rule 2: Geographic Distance Rule:** Flag transactions where the `location` is more than 500 miles away from the customer's 'home_location' (assume you have 'home_location' data).
        3.  **Rule 3: Velocity and Time of Day:** Flag transactions if `transaction_frequency` (from Exercise 3.1) > 5 transactions in the last hour *AND* `time_of_day` is 'Night'.

        Combine these rules: A transaction is flagged as potentially fraudulent if it satisfies *any* of these *combined* rules.

        *Challenge:*  Describe in detail how you would implement this rule-based system.  Focus on the *logic and steps* for checking each rule and combining them. Discuss scenarios where such rule-based systems are effective, and where they might fall short compared to machine learning models.*
        """
        )

        st.markdown(
            """
        **Exercise 3.3: Understanding Class Imbalance (Conceptual)**

        Revisit the concept of class imbalance in fraud detection.

        1.  Explain *in your own words* why training a standard classification model on a dataset with extreme class imbalance (e.g., 99% non-fraudulent, 1% fraudulent) can lead to misleadingly high accuracy but poor fraud detection.  Focus on what the model *actually learns* in such scenarios.
        2.  Describe *two different techniques* (oversampling and undersampling) to mitigate class imbalance. Explain *how each technique works* and what their potential drawbacks are.
        3.  Beyond accuracy, list *three evaluation metrics* that are more appropriate for assessing the performance of fraud detection models in imbalanced datasets. Explain *why* these metrics are better suited than accuracy in this context.
        """
        )

    with st.expander("🏢 4. Real-World Applications - Case Studies", expanded=False):
        st.subheader("Real-World Case Studies of Data Analytics in Fraud and Risk")

        st.markdown(
            """
        **Case Study 4.1: Credit Card Fraud Detection in Retail Banking (Enhanced Detail)**

        *   **Industry:** Retail Banking
        *   **Problem:**  High volumes of credit card transaction fraud resulting in significant financial losses from chargebacks and direct fraud, as well as customer dissatisfaction due to fraudulent charges and card misuse. The bank needed a system to reduce fraud losses and improve customer experience.
        *   **Solution:** Implemented a real-time fraud detection system using machine learning to analyze transactions and identify likely fraudulent activities *before authorization*.
            *   **Approach:**
                *   **Data Sources:** Integrated transactional features (amount, time, merchant, location, transaction channel), customer behavior patterns (historical spending habits, typical locations, purchase frequency), and device information (device ID, IP address).
                *   **Feature Engineering:** Engineered features like transaction velocity (transactions per hour), geographic deviation (distance from home location), unusual merchant category patterns, and spending amount ratios.
                *   **Model Selection:** Compared various classification models and selected a hybrid approach using **Random Forest** for initial fast scoring and **Deep Neural Networks (LSTMs)** for more complex, sequential pattern recognition, especially for account takeover scenarios.
                *   **Real-time System:** Deployed models in a real-time transaction processing pipeline. Transactions were scored within milliseconds before authorization, and high-risk transactions triggered immediate actions.
            *   **Actions Triggered by High-Risk Scores:**
                *   **Transaction Blocking:**  High probability fraud transactions were automatically blocked.
                *   **Step-Up Authentication:** Customers prompted for additional verification (OTP, biometric) for medium-risk transactions.
                *   **Fraud Alerts:** Fraud analysts received alerts for high-risk transactions for manual review and investigation.
            *   **Outcome:**
                *   **Fraud Reduction:** Achieved a significant reduction in fraudulent transactions (estimated 70-80% reduction in fraud losses).
                *   **Improved Customer Experience:** Reduced false positives compared to previous rule-based systems, minimizing inconvenience for legitimate customers.
                *   **Cost Savings:** Substantial cost savings from reduced fraud losses, lower chargeback rates, and improved operational efficiency in fraud investigations.
        *   **Key Technologies:** Python, Pandas, Scikit-learn, TensorFlow/Keras, Cloud-based infrastructure (AWS) for real-time processing, Kafka for streaming data, real-time scoring engine.

        ---

        **Case Study 4.2: Business Email Compromise (BEC) Prevention in Commercial Banking**

        *   **Industry:** Commercial Banking
        *   **Problem:**  Sophisticated Business Email Compromise (BEC) attacks targeting corporate accounts. Fraudsters impersonated company executives via email to trick employees into transferring large sums of money to attacker-controlled accounts, resulting in massive financial losses and reputational damage for corporate clients and the bank.
        *   **Solution:** Developed a multi-layered security approach, significantly enhanced by advanced data analytics and AI, to detect and prevent BEC attacks proactively.
            *   **Approach:**
                *   **Email Content Analysis using NLP:** Implemented Natural Language Processing (NLP) models to analyze email content in real-time:
                    *   **Phishing Indicators:** Detection of keywords, phrases, and linguistic patterns commonly associated with phishing and BEC attempts (urgency, threats, unusual requests).
                    *   **Sentiment Analysis:** Assessing email sentiment for manipulative language or emotional cues.
                    *   **Domain and Sender Analysis:** Verifying email domain authenticity, sender reputation, and detecting spoofed email addresses.
                *   **Behavioral Analysis of User Activity:** Monitoring user login patterns, transaction initiation behavior, and communication patterns for anomalies:
                    *   **Unusual Login Locations/Times:** Flagging logins from unusual IPs or geographic locations, or outside of normal business hours.
                    *   **Deviations from Transaction Patterns:** Detecting unusual transaction amounts, beneficiaries, or frequencies compared to historical patterns for the specific user and corporate account.
                    *   **Communication Network Analysis:** Analyzing email communication patterns within the organization to identify suspicious communication flows or unusual external contacts.
                *   **Integration with Security Information and Event Management (SIEM):** Integrated the analytics platform with the bank's SIEM system for centralized security monitoring and alerting.
            *   **Technologies Deployed:** Advanced NLP libraries in Python (NLTK, SpaCy, Transformers), Machine Learning for anomaly detection, Graph databases for communication network analysis, Real-time email scanning gateways, Security Information and Event Management (SIEM) platform.
            *   **Outcomes Achieved:**
                *   **Enhanced BEC Detection Rate:** Significant improvement in detection rate of BEC attempts (estimated >90% detection of targeted BEC attacks).
                *   **Proactive Alerts and Intervention:** Real-time alerts triggered for suspicious emails and user behavior, enabling security teams to intervene proactively and prevent fraudulent transactions.
                *   **Reduced Financial Losses:** Substantial reduction in successful BEC fraud incidents and associated financial losses for corporate clients.
                *   **Improved Client Trust:** Enhanced security measures improved client confidence in the bank's ability to protect corporate accounts from sophisticated cyber-financial threats like BEC.
        """
        )

        st.markdown(
            """
        **Case Study 4.3: Claims Fraud Detection in Auto Insurance**

        *   **Industry:** Auto Insurance
        *   **Problem:**  High incidence of fraudulent insurance claims, particularly in auto insurance, leading to inflated payouts, increased operational costs for claims processing and investigations, and higher premiums for all customers.  The insurance company aimed to implement a system to more effectively detect and prevent fraudulent claims early in the claims lifecycle.
        *   **Solution:** Implemented an advanced claims fraud detection system leveraging data analytics, machine learning, and image analysis to identify and flag potentially fraudulent claims for further investigation.
            *   **Approach:**
                *   **Comprehensive Data Integration:** Integrated diverse data sources related to claims:
                    *   **Claims Data:** Detailed claim information (accident reports, damage descriptions, injury reports, claimant details, policy information, claim history).
                    *   **External Data:** Public records, weather data (for accident context), police reports, social media data (where ethically and legally permissible).
                    *   **Image Data:** Images of damaged vehicles submitted by claimants (accident scene photos, repair estimates with images).
                    *   **Provider Data:** Data on repair shops, medical providers, and their historical claim patterns.
                *   **Advanced Analytics and Machine Learning Models:**
                    *   **Anomaly Detection:** Models to detect anomalies in claim amounts, repair costs, injury types, claimant behavior, and provider billing patterns.
                    *   **Network Analysis:** Graph-based analysis to identify potential fraud rings by analyzing relationships between claimants, repair shops, medical providers, witnesses, and other entities involved in claims.
                    *   **Text Mining and NLP:** Natural Language Processing to analyze textual descriptions in accident reports, police reports, and claimant statements for inconsistencies, red flags, and linguistic indicators of fraud.
                    *   **Image Analysis with Computer Vision:** Deep learning-based computer vision models to analyze images of damaged vehicles:
                        *   **Damage Assessment:** Automated assessment of vehicle damage severity from images, comparing it to repair estimates and claim descriptions.
                        *   **Inconsistency Detection:** Identifying inconsistencies between reported damage, image evidence, and accident circumstances (e.g., staged accidents, pre-existing damage).
                *   **Risk Scoring and Alerting:**  Developed a risk scoring engine that combined outputs from various models to generate a comprehensive fraud risk score for each claim. High-risk claims automatically flagged and routed for manual review by fraud investigators.
            *   **Technologies Utilized:** Machine learning libraries (Scikit-learn, TensorFlow, PyTorch) for anomaly detection and classification, Graph databases (Neo4j) for network analysis, Computer vision libraries (OpenCV, TensorFlow/Keras for image analysis), NLP libraries, Cloud-based data platform, Rule-based engine for integrating diverse analytics outputs and setting risk thresholds.
            *   **Impact and Outcomes:**
                *   **Improved Fraud Detection Accuracy:** Significantly improved accuracy in identifying fraudulent claims compared to traditional rule-based and manual review processes.
                *   **Faster Claim Processing for Legitimate Claims:** Automation of initial fraud screening allowed for faster processing of legitimate claims, improving customer satisfaction.
                *   **Significant Cost Savings:** Substantial reduction in fraudulent payouts and operational costs associated with fraud investigations.
                *   **Enhanced Investigative Efficiency:** Fraud investigators could focus their efforts on genuinely high-risk claims, improving efficiency and resource allocation.
        """
        )

    with st.expander("❓ 5. Knowledge Check Quiz", expanded=False):
        st.subheader("Knowledge Check Quiz: Test Your Understanding")

        quiz_questions = [
            {
                "question": "Which type of fraud primarily involves intentional misrepresentation of a company's financial statements?",
                "options": [
                    "Asset Misappropriation",
                    "Financial Statement Fraud",
                    "Customer Fraud",
                    "Cyber Fraud",
                ],
                "answer": "Financial Statement Fraud",
            },
            {
                "question": "Diagnostic analytics is best suited for answering which of the following questions in fraud and risk detection?",
                "options": [
                    "What fraud or risks might occur in the future?",
                    "What actions should be taken to prevent fraud?",
                    "Why did a particular fraud or risk event happen?",
                    "What types of fraud and risks have occurred in the past?",
                ],
                "answer": "Why did a particular fraud or risk event happen?",
            },
            {
                "question": "Which anomaly detection algorithm is known for its efficiency in isolating anomalies by random data partitioning, especially in high-dimensional data?",
                "options": [
                    "Logistic Regression",
                    "K-Means Clustering",
                    "Isolation Forest",
                    "One-Class SVM",
                ],
                "answer": "Isolation Forest",
            },
            {
                "question": "In credit card fraud detection, identifying 'deviation from typical spending location' for a customer is an example of leveraging a:",
                "options": [
                    "Transaction-based feature",
                    "Merchant-related feature",
                    "Time-based feature",
                    "Behavioral feature",
                ],
                "answer": "Behavioral feature",
            },
            {
                "question": "What primary challenge arises when building machine learning models for fraud detection due to the inherent nature of fraud incidents being rare?",
                "options": [
                    "Data scarcity",
                    "Evolving fraud tactics",
                    "Class imbalance",
                    "Lack of relevant features",
                ],
                "answer": "Class imbalance",
            },
            {
                "question": "For real-time credit card fraud detection requiring immediate transaction scoring, which algorithm type would generally be preferred due to its speed and interpretability?",
                "options": [
                    "Deep Neural Networks",
                    "Random Forests",
                    "Logistic Regression",
                    "Support Vector Machines",
                ],
                "answer": "Logistic Regression",
            },
            {
                "question": "Analyzing relationships between claimants, repair shops, and medical providers to detect potential fraud rings in auto insurance claims is a use case for:",
                "options": [
                    "Time Series Analysis",
                    "Regression Analysis",
                    "Graph Analytics",
                    "Clustering Algorithms",
                ],
                "answer": "Graph Analytics",
            },
            {
                "question": "Which ethical consideration is most critical in deploying AI-driven fraud detection systems to ensure fairness and avoid discrimination?",
                "options": [
                    "Data Security",
                    "Model Interpretability",
                    "Bias Mitigation",
                    "Privacy Preservation",
                ],
                "answer": "Bias Mitigation",
            },
            {
                "question": "Federated learning is emerging as a key trend in fraud analytics primarily to address which challenge?",
                "options": [
                    "Evolving fraud tactics",
                    "Data quality issues",
                    "Class imbalance",
                    "Privacy and data sharing limitations",
                ],
                "answer": "Privacy and data sharing limitations",
            },
            {
                "question": "Which future trend in fraud detection focuses on analyzing unstructured data like emails and voice interactions to identify fraud clues?",
                "options": [
                    "Real-time Analytics",
                    "Behavioral Biometrics",
                    "Natural Language Processing",
                    "Quantum Computing",
                ],
                "answer": "Natural Language Processing",
            },
        ]

        user_answers = {}
        for i, question_data in enumerate(quiz_questions):
            question_num = i + 1
            st.markdown(f"**Question {question_num}:** {question_data['question']}")
            user_answer = st.radio(
                f"Select your answer for Q{question_num}",
                question_data["options"],
                key=f"q{question_num}",
            )
            user_answers[question_num] = user_answer

        if st.button("Submit Quiz", key="quiz_submit_button"):
            correct_count = 0
            for i, question_data in enumerate(quiz_questions):
                question_num = i + 1
                if user_answers[question_num] == question_data["answer"]:
                    correct_count += 1
                    st.success(f"Question {question_num}: Correct! ✅")
                else:
                    st.error(
                        f"Question {question_num}: Incorrect. ❌ Correct answer is: **{question_data['answer']}**"
                    )

            st.write(
                f"\n**Quiz Result: You scored {correct_count} out of {len(quiz_questions)}.**"
            )


if __name__ == "__main__":
    main()

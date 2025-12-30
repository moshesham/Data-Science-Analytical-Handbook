# Analytical Hands-On Projects

This folder provides practical, hands-on experience in data analysis using open-source tools and data. By working through these real-world examples, you'll solidify understanding of key concepts covered in the [2026 Analytics Challenge](../supplementary/2026-new-year-challenge.md) and develop essential skills in data manipulation, analysis, visualization, and interpretation.

## 🎯 Project Portfolio

Each project is designed to build specific skills aligned with the 2026 Analytics Challenge:

| Project | Challenge Week | Key Skills |
|---------|---------------|------------|
| [A/B Testing](./AB_Test_Project/) | Week 4 | Experiment design, statistical testing, guardrails |
| [Cohort Analysis](./Cohort_Analysis_Project/) | Week 2 | Window functions, retention metrics, heatmaps |
| [Customer Churn](./Customer_Churn_Project/) | Week 5-6 | EDA, classification, feature engineering |
| [Demand Forecasting](./Demand_Forecasting_Project/) | Capstone | Time series, Prophet, business recommendations |
| [Fraud Detection](./Fraud_Detection_Project/) | Advanced | Imbalanced data, precision-recall, thresholds |
| [Pricing Elasticity](./Pricing_Elasticity_Project/) | Week 6 | Regression, elasticity, revenue simulation |
| [Movie Reviews](./Movie_Reviews_Project/) | Beginner | Basic EDA, visualization |

## 🆕 2026 Enhancements

All projects now include:
- **One-click environments:** Open directly in Google Colab or GitHub Codespaces
- **Polars examples:** High-performance alternative to Pandas
- **AI-augmented challenges:** Learn to use LLMs as analysis co-pilots
- **Video walkthrough requirement:** Practice explaining technical work

## 📁 Project Structure

Each project follows a consistent Jupyter Notebook structure:

### 1. Introduction
- **Project Overview:** Goals and objectives
- **Dataset Description:** Source, format, and key variables
- **Business Context:** Why this analysis matters

### 2. Data Acquisition and Cleaning
- **Data Loading:** Code for downloading and loading data
- **Exploration:** Descriptive statistics, data types, missing values
- **Cleaning:** Handling nulls, duplicates, inconsistencies

### 3. Exploratory Data Analysis
- **Visualizations:** Charts using Matplotlib, Seaborn, Plotly
- **Statistical Analysis:** Hypothesis testing, correlations

### 4. Modeling and Analysis
- **Model Selection:** Appropriate techniques for the problem
- **Implementation:** Using scikit-learn, statsmodels, etc.
- **Evaluation:** Relevant metrics (AUC, RMSE, precision, etc.)

### 5. Business Recommendations
- **Key Findings:** Top 3-5 actionable insights
- **Recommendations:** What should the business do?
- **Next Steps:** Follow-up experiments or analyses

### 6. Communication (NEW for 2026)
- **5-Slide Summary:** Presentation-ready slides
- **3-Minute Video:** Loom walkthrough explaining the analysis

## 🚀 Getting Started

1. **Choose a project** based on your skill level and interests
2. **Read the project README** for learning objectives and setup
3. **Open the notebook** in Colab or locally
4. **Work through the analysis** step by step
5. **Complete the challenges** and share in [GitHub Discussions](https://github.com/moshesham/Data-Science-Analytical-Handbook/discussions)

## 📊 Free Dataset Suggestions

**1. Analyzing Movie Ratings:**

* **Dataset:** IMDB movie dataset (available on Kaggle).
* **Description:** Explore the relationship between movie ratings, genres, release year, and other factors.
* **Learning Outcomes:** Data cleaning, exploratory data analysis, visualization, basic statistical analysis.
* **Example Analysis:**

    * Analyze the distribution of movie ratings across different genres.
    * Identify trends in movie ratings over time.
    * Explore the relationship between movie budget and rating.

**2. Predicting Customer Churn:**

* **Dataset:** Telecom customer churn dataset (available on Kaggle).
* **Description:** Build a predictive model to identify customers at risk of churn based on their usage patterns and demographics.
* **Learning Outcomes:** Data preprocessing, feature engineering, classification modeling, model evaluation.
* **Example Analysis:**

    * Build a logistic regression model to predict churn probability.
    * Evaluate the model's performance using metrics like accuracy, precision, and recall.
    * Identify key factors contributing to customer churn.
    * **Deployment Considerations:** Discuss the ethical implications of using a churn prediction model, such as potential bias against certain customer segments. Explore techniques for making the model more transparent and explainable.

**3. Analyzing Global Health Trends:**

* **Dataset:** World Health Organization (WHO) Global Health Observatory data.
* **Description:** Explore trends in disease prevalence, mortality rates, and healthcare access across different countries and regions.
* **Learning Outcomes:** Data manipulation, time series analysis, geospatial visualization, data storytelling.
* **Example Analysis:**

    * Analyze the prevalence of specific diseases over time.
    * Compare healthcare access indicators across different countries.
    * Create interactive maps to visualize global health trends.

**4. Sentiment Analysis of Social Media Data:**

* **Dataset:** Twitter API data on a specific topic or event.
* **Description:** Analyze the sentiment expressed in tweets using natural language processing techniques.
* **Learning Outcomes:** Text preprocessing, sentiment analysis, topic modeling, data visualization.
* **Example Analysis:**

    * Classify tweets as positive, negative, or neutral.
    * Identify key topics and themes discussed in the tweets.
    * Visualize sentiment trends over time.
    * **Deployment Considerations:** Discuss the challenges of deploying a sentiment analysis model in a real-world setting, such as handling sarcasm, irony, and cultural nuances. Explore techniques for mitigating bias and ensuring fairness.

**5. Building a Recommendation System:**

* **Dataset:** MovieLens movie ratings dataset.
* **Description:** Develop a movie recommendation system based on user ratings and movie characteristics.
* **Learning Outcomes:** Collaborative filtering, matrix factorization, recommender system evaluation.
* **Example Analysis:**

    * Implement a collaborative filtering algorithm to recommend movies to users.
    * Evaluate the recommendation system's performance using metrics like precision and recall.
    * Explore different recommendation strategies and compare their effectiveness.
    * **Deployment Considerations:** Discuss the importance of user privacy and data security when deploying a recommendation system. Explore techniques for providing users with control over their data and recommendations.



By working through these projects, students will gain valuable hands-on experience in data analysis, develop essential skills, and build a portfolio of projects to showcase their abilities.
---
layout: default
title: "Hands-On Analytical Projects"
permalink: /analytical-projects/
difficulty: "All Levels"
estimated_time: "Variable"
tags: [Projects, Portfolio, Hands-On]
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <span>Hands-On Projects</span>
</div>

<div class="header">
  <h1>Hands-On Analytical Projects</h1>
  <p>Build portfolio-ready projects to practice the concepts from this handbook.</p>
</div>

<div class="section">
  <div class="card">
    <h3>How This Works</h3>
    <p>Each project folder contains a Jupyter Notebook (or placeholder) plus a README with scope and next steps. Our CI converts notebooks to Markdown in <code>notebooks_md/</code> so they render nicely on GitHub.</p>
  </div>

  <div class="card" id="customer-churn">
    <h3>Customer Churn Project</h3>
    <p>Predict churn and identify key drivers with logistic regression or tree-based models.</p>
    <ul>
      <li>Location: <code>Analytical-HandsOn-Projects/Customer_Churn_Project/</code></li>
      <li>Outputs: Notebook (EDA, modeling), evaluation plots, recommendations</li>
      <li>Status: Placeholder README ready; add data + notebook</li>
    </ul>
  </div>

  <div class="card" id="cohort-analysis">
    <h3>Cohort Analysis Project</h3>
    <p>Build cohorts and retention curves to understand user engagement over time.</p>
    <ul>
      <li>Location: <code>Analytical-HandsOn-Projects/Cohort_Analysis_Project/</code></li>
      <li>Outputs: Notebook (cohort labeling, retention), heatmaps/curves</li>
      <li>Status: Placeholder README ready; add data + notebook</li>
    </ul>
  </div>

  <div class="card" id="ab-testing">
    <h3>A/B Testing Project</h3>
    <p>Design, size, and analyze an experiment with guardrail metrics and uplift visualization.</p>
    <ul>
      <li>Location: <code>Analytical-HandsOn-Projects/AB_Test_Project/</code></li>
      <li>Outputs: Notebook (design, analysis), visuals, checklist</li>
      <li>Status: Placeholder README ready; add data + notebook</li>
    </ul>
  </div>

  <div class="card" id="demand-forecasting">
    <h3>Demand Forecasting Project</h3>
    <p>Forecast weekly demand with seasonality and holiday effects; compare statistical and ML models.</p>
    <ul>
      <li>Location: <code>Analytical-HandsOn-Projects/Demand_Forecasting_Project/</code></li>
      <li>Outputs: Notebook (EDA, baselines, Prophet/ARIMA/GBM), backtests, forecast visuals</li>
      <li>Status: Placeholder README ready; add data + notebook</li>
    </ul>
  </div>

  <div class="card" id="fraud-detection">
    <h3>Fraud Detection Project</h3>
    <p>Detect anomalous transactions with imbalance-aware modeling and threshold tuning.</p>
    <ul>
      <li>Location: <code>Analytical-HandsOn-Projects/Fraud_Detection_Project/</code></li>
      <li>Outputs: Notebook (feature engineering, PR AUC, recall@k, threshold curves), cost/benefit notes</li>
      <li>Status: Placeholder README ready; add data + notebook</li>
    </ul>
  </div>

  <div class="card" id="pricing-elasticity">
    <h3>Pricing Elasticity Project</h3>
    <p>Estimate price and cross-elasticity, simulate revenue scenarios, and propose price moves.</p>
    <ul>
      <li>Location: <code>Analytical-HandsOn-Projects/Pricing_Elasticity_Project/</code></li>
      <li>Outputs: Notebook (elasticity modeling, demand curves, scenario sims), revenue impact summary</li>
      <li>Status: Placeholder README ready; add data + notebook</li>
    </ul>
  </div>

  <div class="card">
    <h3>Notebook Publishing</h3>
    <p>On push/PR, <code>.github/workflows/notebooks-to-markdown.yml</code> converts <code>.ipynb</code> files to Markdown in <code>notebooks_md/</code> and uploads them as an artifact (and commits on push). This keeps rendered copies in sync.</p>
  </div>
</div>

<div class="navigation-buttons">
  <a href="{{ '/tracks/' | relative_url }}">Previous: Learning Tracks</a>
  <a href="{{ '/tools/' | relative_url }}">Next: Interactive Tools</a>
</div>

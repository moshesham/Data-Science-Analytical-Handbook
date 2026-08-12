---
layout: default
title: "Product Analytics Streamlit App"
permalink: /streamlit-app/
difficulty: "All Levels"
estimated_time: "5 mins"
tags: [Streamlit, Product Analytics, App]
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <span>Streamlit App</span>
</div>

<div class="header">
  <h1>Product Analytics Streamlit App</h1>
  <p>Live app showcasing interactive analytics demos from this handbook.</p>
</div>

<div class="section">
  <div class="card">
    <h3>Run Locally</h3>
    <p>This app is not currently deployed to a public URL. To run it locally:</p>
    <ol>
      <li>Clone the repository: <code>git clone https://github.com/moshesham/Data-Science-Analytical-Handbook.git</code></li>
      <li>Install dependencies: <code>pip install -r streamlit_app/Product_Analytics/requirements.txt</code></li>
      <li>Launch: <code>cd streamlit_app/Product_Analytics &amp;&amp; streamlit run streamlit_app.py</code></li>
      <li>Open <code>http://localhost:8501</code> in your browser</li>
    </ol>
    <p>See <a href="https://github.com/moshesham/Data-Science-Analytical-Handbook/blob/main/streamlit_app/README.md">streamlit_app/README.md</a> for optional Streamlit Cloud deployment instructions.</p>
  </div>

  <div class="card">
    <h3>What's Inside</h3>
    <ul>
      <li>Code: <code>streamlit_app/Product_Analytics/</code></li>
      <li>Data sources: <code>streamlit_app/Product_Analytics/data/</code></li>
      <li>Utilities: <code>streamlit_app/Product_Analytics/utils/</code></li>
      <li>Features: A/B testing, time series, economic dashboard, and more</li>
    </ul>
  </div>
</div>

<div class="navigation-buttons">
  <a href="{{ '/tools/' | relative_url }}">Previous: Interactive Tools</a>
  <a href="{{ '/meta-specificity/' | relative_url }}">Next: Meta Specificity</a>
</div>

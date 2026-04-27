---
layout: default
title: "Foundational Knowledge Overview"
permalink: /foundational-knowledge/
difficulty: "Beginner"
estimated_time: "10 mins"
tags: [Overview, Foundations]
track: "Foundational Knowledge"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <span>Foundational Knowledge & Skills</span>
</div>

<div class="header">
  <h1>Foundational Knowledge & Skills</h1>
  <p>The Building Blocks of Data Science Excellence</p>
</div>

<div class="section">
  
  <div class="card">
    <h3>Overview</h3>
    <p>This section covers the fundamental concepts and skills required for a Data Science (Analytical) role at Meta. These building blocks form the foundation for all technical and analytical work you'll do.</p>
    <p>At Meta, Data Scientists play a crucial role in driving product development and business strategy through rigorous data analysis and statistical reasoning. Working at scale with billions of users and petabytes of data, statistical rigor and technical proficiency are paramount.</p>
    <h4>Why This Order?</h4>
    <p>The four topics are sequenced deliberately:</p>
    <ol>
      <li><strong>Statistics & Probability</strong> — the conceptual foundation. Everything else (SQL queries, Python analysis, A/B tests) is meaningless without understanding what you're measuring and why.</li>
      <li><strong>SQL & Data Manipulation</strong> — how you access and shape data. In interviews and on the job, SQL is the first tool you reach for to explore a dataset or answer a product question.</li>
      <li><strong>Python for Analysis</strong> — how you go deeper than SQL allows: cleaning messy data, building models, running simulations. Python extends what SQL can do.</li>
      <li><strong>A/B Testing & Experimentation</strong> — how you prove an effect is real. A/B testing brings together statistics (hypothesis tests), SQL (pulling experiment data), and Python (analysis) into a complete decision-making workflow.</li>
    </ol>
    <p>If you are short on time, prioritize <strong>Statistics → SQL → A/B Testing</strong> as these three topics appear most frequently in Meta DS interviews.</p>
  </div>

  <div class="card">
    <h3><a href="{{ '/foundational_knowledge/1/' | relative_url }}">1. Statistics & Probability</a></h3>
    <p>Master the statistical foundations essential for data-driven decision making at Meta. Learn descriptive statistics, probability distributions, hypothesis testing, regression analysis, and experimental design.</p>
    <p><strong>Key Topics:</strong> Mean, median, mode, normal distribution, A/B testing, p-values, confidence intervals, statistical power</p>
    <p><a href="{{ '/foundational_knowledge/1/' | relative_url }}" class="button">Learn More →</a></p>
  </div>

  <div class="card">
    <h3><a href="{{ '/foundational_knowledge/2-SQL/' | relative_url }}">2. SQL & Data Manipulation</a></h3>
    <p>Develop proficiency in SQL for querying, joining, and aggregating data. Master window functions and query optimization techniques.</p>
    <p><strong>Key Topics:</strong> JOINs, GROUP BY, window functions, CTEs, subqueries, query optimization</p>
    <p><a href="{{ '/foundational_knowledge/2-SQL/' | relative_url }}" class="button">Learn More →</a></p>
  </div>

  <div class="card">
    <h3><a href="{{ '/analytical-engineering/' | relative_url }}">2a. Analytical Engineering</a></h3>
    <p>Turn raw data into trustworthy analytics tables with versioned SQL models, tests, and clear definitions.</p>
    <p><strong>Key Topics:</strong> facts/dims, incremental loads, SCD2, QA checks, semantic definitions</p>
    <p><a href="{{ '/analytical-engineering/' | relative_url }}" class="button">Learn More →</a></p>
  </div>

  <div class="card">
    <h3><a href="{{ '/foundational_knowledge/3/' | relative_url }}">3. Programming (Python/R) for Data Analysis</a></h3>
    <p>Learn to use Python and R for data manipulation, analysis, and visualization. Master core libraries like Pandas, NumPy, Matplotlib, and Seaborn.</p>
    <p><strong>Key Topics:</strong> Pandas DataFrames, NumPy arrays, data cleaning, visualization, statistical modeling</p>
    <p><a href="{{ '/foundational_knowledge/3/' | relative_url }}" class="button">Learn More →</a></p>
  </div>

</div>

<div class="navigation-buttons">
  <a href="{{ '/introduction/' | relative_url }}">Previous: Introduction</a>
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Next: Statistics & Probability</a>
</div>

---
layout: default
title: "SQL & Data Manipulation"
permalink: /foundational_knowledge/2-SQL/
difficulty: "Beginner"
estimated_time: "30 mins"
tags: [SQL, Data Manipulation, Query Optimization]
track: "Foundational Knowledge"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Foundational Knowledge & Skills</a> <span>&gt;</span>
  <span>SQL & Data Manipulation</span>
</div>

<div class="header">
  <h1>SQL & Data Manipulation</h1>
  <p>Core SQL syntax, advanced techniques, query optimization, and data cleaning with SQL.</p>
</div>

<div class="section">
  
  <div class="card">
    <h3>What Can You Expect?</h3>
    <p>You can expect SQL coding questions that involve:</p>
    <ul>
      <li>Writing complex queries, joining tables, aggregating data</li>
      <li>Using window functions and optimizing query performance</li>
      <li>Analyzing a large dataset or solving a business problem using SQL</li>
    </ul>
  </div>

  <div class="card">
    <h3>How to Prep</h3>
    <ul>
      <li>Practice writing SQL queries regularly and focus on efficiency.</li>
      <li>Be prepared to explain your code and its logic.</li>
      <li><strong>Resources:</strong>
        <ul>
          <li><a href="https://sqlzoo.net/" target="_blank">SQLZOO</a></li>
          <li><a href="https://www.hackerrank.com/domains/sql" target="_blank">HackerRank SQL</a></li>
          <li><a href="https://leetcode.com/problemset/database/" target="_blank">LeetCode Database</a></li>
          <li><a href="https://www.stratascratch.com/" target="_blank">StrataScratch</a></li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="card">
    <h3>Key SQL Concepts</h3>
    <ul>
      <li><strong>SELECT, FROM, WHERE:</strong> Basic query structure.</li>
      <li><strong>JOINs (INNER, LEFT, RIGHT, FULL):</strong> Combining data from multiple tables.</li>
      <li><strong>GROUP BY and Aggregate Functions (COUNT, SUM, AVG, MIN, MAX):</strong> Summarizing data.</li>
      <li><strong>Window Functions (ROW_NUMBER, RANK, LAG, LEAD):</strong> Performing calculations across rows related to the current row.</li>
      <li><strong>Subqueries and CTEs (Common Table Expressions):</strong> Creating reusable query blocks.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Example SQL Problem</h3>
    <p>Given two tables: <code>Users</code> (user_id, signup_date) and <code>Orders</code> (order_id, user_id, order_date, amount), write a query to find the total amount spent by each user who signed up in January 2023.</p>
    
    <pre><code>SELECT u.user_id, SUM(o.amount) AS total_spent
FROM Users u
JOIN Orders o ON u.user_id = o.user_id
WHERE u.signup_date BETWEEN '2023-01-01' AND '2023-01-31'
GROUP BY u.user_id;</code></pre>
  </div>

</div>

<div class="navigation-buttons">
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Previous: Statistics & Probability</a>
  <a href="{{ '/foundational_knowledge/3/' | relative_url }}">Next: Programming (Python/R) for Data Analysis</a>
</div>

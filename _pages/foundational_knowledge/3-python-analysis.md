---
layout: default
title: "Programming (Python/R) for Data Analysis"
permalink: /foundational_knowledge/3/
difficulty: "Intermediate"
estimated_time: "45 mins"
tags: [Python, Data Analysis, Pandas, NumPy]
track: "Foundational Knowledge"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Foundational Knowledge & Skills</a> <span>&gt;</span>
  <span>Programming (Python/R) for Data Analysis</span>
</div>

<div class="header">
  <h1>Programming (Python/R) for Data Analysis</h1>
  <p>Python fundamentals, Pandas, NumPy, visualization, and optional modeling libraries.</p>
</div>

<div class="section">
  
  <div class="card">
    <h3>Overview</h3>
    <p>While SQL is often the primary focus in data science interviews, demonstrating proficiency in Python or R is crucial for data manipulation, analysis, and visualization. You may be asked to write code snippets, explain code logic, or discuss how you would approach a data-related problem using these languages. Expect questions involving:</p>
    <ul>
      <li><strong>Core Libraries:</strong> Pandas, NumPy, data visualization libraries (Matplotlib, Seaborn)</li>
      <li><strong>Potentially:</strong> Statistical modeling libraries (Statsmodels, scikit-learn), and other specialized libraries depending on the role (e.g., NLP libraries like NLTK or spaCy).</li>
    </ul>
  </div>

  <div class="card">
    <h3>How to Prep</h3>
    <ul>
      <li><strong>Practice Regularly:</strong> Consistent practice is key. Work through coding exercises on platforms like HackerRank, LeetCode (Database section), and StrataScratch, focusing on data manipulation and analysis problems.</li>
      <li><strong>Focus on Fundamentals:</strong> Ensure you have a solid understanding of data structures (lists, dictionaries, arrays), control flow (loops, conditional statements), and functions.</li>
      <li><strong>Master Core Libraries:</strong> Become proficient in using Pandas for data manipulation, NumPy for numerical operations, and Matplotlib/Seaborn for visualization.</li>
      <li><strong>Understand Data Cleaning and Transformation:</strong> Practice techniques for handling missing values, data type conversions, and data aggregation.</li>
      <li><strong>Be Comfortable Explaining Your Code:</strong> Be prepared to walk through your code line by line, explaining the logic and reasoning behind your choices. Consider time and space complexity of your solutions.</li>
      <li><strong>Think About Edge Cases:</strong> When designing solutions, consider potential edge cases and how your code handles them.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Resources</h3>
    <ul>
      <li><strong>Pandas:</strong>
        <ul>
          <li><a href="https://pandas.pydata.org/docs/" target="_blank">Official Documentation</a></li>
          <li><a href="https://pandas.pydata.org/docs/user_guide/10min.html" target="_blank">10 Minutes to pandas</a></li>
        </ul>
      </li>
      <li><strong>NumPy:</strong>
        <ul>
          <li><a href="https://numpy.org/doc/" target="_blank">Official Documentation</a></li>
          <li><a href="https://numpy.org/doc/stable/user/quickstart.html" target="_blank">NumPy Quickstart Tutorial</a></li>
        </ul>
      </li>
      <li><strong>Matplotlib:</strong>
        <ul>
          <li><a href="https://matplotlib.org/stable/contents.html" target="_blank">Official Documentation</a></li>
          <li><a href="https://matplotlib.org/stable/tutorials/index.html" target="_blank">Matplotlib Tutorials</a></li>
        </ul>
      </li>
      <li><strong>Seaborn:</strong>
        <ul>
          <li><a href="https://seaborn.pydata.org/" target="_blank">Official Documentation</a></li>
          <li><a href="https://seaborn.pydata.org/tutorial.html" target="_blank">Seaborn Tutorials</a></li>
        </ul>
      </li>
      <li><a href="https://jakevdp.github.io/PythonDataScienceHandbook/" target="_blank">Python Data Science Handbook</a></li>
    </ul>
  </div>

  <div class="card">
    <h3>Key Libraries and Functionalities</h3>
    
    <h4>Pandas</h4>
    <ul>
      <li><strong>DataFrames:</strong> Two-dimensional labeled data structures with columns of potentially different types.</li>
      <li><strong>Series:</strong> One-dimensional labeled array.</li>
      <li><strong>Data Cleaning:</strong> Handling missing values (e.g., <code>df.fillna()</code>, <code>df.dropna()</code>), removing duplicates (<code>df.drop_duplicates()</code>).</li>
      <li><strong>Data Transformation:</strong> Filtering (<code>df[df['Age'] > 25]</code>), sorting (<code>df.sort_values('Age')</code>), adding/removing columns.</li>
      <li><strong>Data Aggregation:</strong> Grouping data and applying aggregate functions (e.g., <code>df.groupby('City')['Age'].mean()</code>).</li>
      <li><strong>Reading and Writing Data:</strong> Reading data from CSV, Excel, and other formats (<code>pd.read_csv()</code>, <code>pd.read_excel()</code>).</li>
    </ul>

    <h4>NumPy</h4>
    <ul>
      <li><strong>Arrays:</strong> N-dimensional arrays for efficient numerical operations.</li>
      <li><strong>Mathematical Functions:</strong> Performing mathematical operations on arrays (e.g., <code>np.mean()</code>, <code>np.std()</code>, <code>np.sum()</code>).</li>
      <li><strong>Linear Algebra:</strong> Matrix operations, dot products, etc.</li>
    </ul>

    <h4>Matplotlib/Seaborn</h4>
    <ul>
      <li><strong>Matplotlib:</strong> Creating basic plots like line plots, scatter plots, bar charts, histograms.</li>
      <li><strong>Seaborn:</strong> Building on top of Matplotlib to create more visually appealing and informative statistical graphics.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Example: Creating a DataFrame</h3>
    <pre><code>import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 
        'Age': [25, 30, 28], 
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print(df)</code></pre>
  </div>

  <div class="card">
    <h3>Example: NumPy Array</h3>
    <pre><code>import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(f"Mean: {np.mean(arr)}")
print(f"Std: {np.std(arr)}")</code></pre>
  </div>

</div>

<div class="section">
  <h2>Test Your Knowledge</h2>
  {% include quiz_widget.html quiz_id="python_data_analysis" %}
</div>

<div class="navigation-buttons">
  <a href="{{ '/foundational_knowledge/2-SQL/' | relative_url }}">Previous: SQL & Data Manipulation</a>
  <a href="{{ '/interview-preparation/technical-skills/' | relative_url }}">Next: Interview Preparation</a>
</div>

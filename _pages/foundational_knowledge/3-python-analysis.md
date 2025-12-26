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
    <h3>Interview-Grade Python: What "Good" Looks Like</h3>
    <ul>
      <li><strong>Correctness first:</strong> handle missing values, duplicate keys, timezone/date quirks, and edge cases.</li>
      <li><strong>Readable & modular:</strong> small functions, clear variable names, explicit assumptions.</li>
      <li><strong>Vectorized when it matters:</strong> prefer pandas operations over Python loops for large data.</li>
      <li><strong>Reproducible:</strong> fixed seeds, deterministic sorts, and saved intermediate outputs when useful.</li>
      <li><strong>Communicates insight:</strong> code answers a question; narrative explains why the result matters.</li>
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
    <h3>Core Pandas Patterns (Most Frequently Tested)</h3>
    <ul>
      <li><strong>Join/merge:</strong> <code>pd.merge(left, right, on=..., how='left')</code> + verify key uniqueness.</li>
      <li><strong>Groupby aggregates:</strong> <code>groupby(...).agg(...)</code> for multi-metric tables.</li>
      <li><strong>Reshape:</strong> <code>pivot_table</code>, <code>melt</code>, wide-to-long and long-to-wide.</li>
      <li><strong>Time series:</strong> <code>dt</code> accessors, resampling, rolling windows.</li>
      <li><strong>Conditional logic:</strong> <code>np.where</code>, boolean masks, and <code>DataFrame.assign</code>.</li>
      <li><strong>Safe counts:</strong> <code>nunique</code>, <code>value_counts(dropna=False)</code>, and explicit denominators.</li>
    </ul>

    <p><strong>Key-check pattern (prevents silent join explosions):</strong></p>
    <pre><code>def assert_unique(df, cols, name="df"):
    dupes = df.duplicated(cols).sum()
    if dupes:
        raise ValueError(f"{name}: {dupes} duplicate keys on {cols}")

assert_unique(users, ["user_id"], "users")
assert_unique(orders, ["order_id"], "orders")

df = users.merge(orders, on="user_id", how="left")</code></pre>
  </div>

  <div class="card">
    <h3>Data Cleaning Checklist (Fast + Practical)</h3>
    <ul>
      <li><strong>Schema:</strong> <code>df.info()</code>, dtypes, parse dates at read time.</li>
      <li><strong>Missingness:</strong> quantify per column; decide <em>drop</em>, <em>impute</em>, or <em>model as signal</em>.</li>
      <li><strong>Duplicates:</strong> define a primary key; dedupe with a rule (latest timestamp wins).</li>
      <li><strong>Outliers:</strong> define a rule (winsorize, cap, remove) and justify it.</li>
      <li><strong>Units:</strong> verify currency, percent vs fraction, and timezones.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Example: EDA Template You Can Reuse</h3>
    <pre><code>import pandas as pd
import numpy as np

def quick_eda(df: pd.DataFrame, target: str | None = None) -> None:
    print("shape:", df.shape)
    display(df.head(3))
    display(df.describe(include="all").T)
    missing = df.isna().mean().sort_values(ascending=False)
    display(missing[missing &gt; 0].to_frame("missing_rate"))
    if target and target in df.columns:
        display(df[target].value_counts(dropna=False).head(20))

quick_eda(df, target=None)</code></pre>
  </div>

  <div class="card">
    <h3>Example: Cohort Retention in Pandas (Interview Favorite)</h3>
    <p><em>Input:</em> events with <code>user_id</code> and <code>event_date</code>. <em>Output:</em> retention table by cohort month.</p>
    <pre><code>import pandas as pd

events = events.copy()
events["event_date"] = pd.to_datetime(events["event_date"], errors="coerce")
events = events.dropna(subset=["event_date"])
events["event_month"] = events["event_date"].dt.to_period("M")

cohort = events.groupby("user_id")["event_month"].min().rename("cohort")
events = events.join(cohort, on="user_id")
events["period"] = (events["event_month"] - events["cohort"]).apply(lambda p: p.n)

active = events.drop_duplicates(["user_id", "period"])
ret = active.pivot_table(index="cohort", columns="period", values="user_id", aggfunc="nunique")
ret_rate = ret.div(ret[0], axis=0)

ret_rate</code></pre>
  </div>

  <div class="card">
    <h3>Example: A/B Test Metric + Bootstrap CI</h3>
    <p><em>Input:</em> user-level table with <code>group</code> and numeric <code>metric</code>.</p>
    <pre><code>import numpy as np

control = df.loc[df["group"] == "control", "metric"].astype(float)
treat = df.loc[df["group"] == "treatment", "metric"].astype(float)

ate = treat.mean() - control.mean()

rng = np.random.default_rng(42)
boot = []
for _ in range(3000):
    boot.append(rng.choice(treat, len(treat), replace=True).mean() - rng.choice(control, len(control), replace=True).mean())

ci = np.percentile(boot, [2.5, 97.5])
print({"ate": ate, "ci_low": ci[0], "ci_high": ci[1]})</code></pre>
    <p><strong>Tip:</strong> In interviews, say whether your CI is for the mean difference and what assumptions you are making (IID users, stable assignment, etc.).</p>
  </div>

  <div class="card">
    <h3>Common Pitfalls (And How to Avoid Them)</h3>
    <ul>
      <li><strong>Chained assignment:</strong> prefer <code>df = df.assign(...)</code> or <code>df.loc[mask, col] = ...</code>.</li>
      <li><strong>SettingWithCopy warnings:</strong> use <code>.copy()</code> when subsetting.</li>
      <li><strong>Silent type issues:</strong> parse numerics with <code>pd.to_numeric(..., errors='coerce')</code>.</li>
      <li><strong>Timezone bugs:</strong> standardize to UTC before grouping by day.</li>
      <li><strong>Speed:</strong> avoid row-wise <code>apply</code> when vectorization exists.</li>
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

  <div class="card">
    <h3>Practice Drills (Try Without Looking)</h3>
    <ul>
      <li><strong>Groupby:</strong> compute DAU by day and platform from an events table.</li>
      <li><strong>Join:</strong> left-join orders to users and compute conversion rate by signup week.</li>
      <li><strong>Time series:</strong> compute a 7-day rolling average of revenue.</li>
      <li><strong>Outliers:</strong> cap metric at 99th percentile per country, then recompute mean.</li>
      <li><strong>Debugging:</strong> fix a merge that unexpectedly triples row count.</li>
    </ul>
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

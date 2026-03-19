---
layout: default
title: "Analytical Execution Interview"
permalink: /interview-preparation/analytical-execution/
difficulty: "Intermediate"
estimated_time: "45 mins"
tags: [Interview, Case Study, Analytical Execution, A/B Testing]
track: "Interview Preparation"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/interview-preparation/analytical-execution/' | relative_url }}">Interview Preparation</a> <span>&gt;</span>
  <span>Analytical Execution</span>
</div>

<div class="header">
  <h1>Analytical Execution Interview (Data Analysis/Case Study)</h1>
  <p>Frameworks and practice for real-world case studies and data analysis problems.</p>
</div>

<div class="section">
  
  <div class="card">
    <h3>What to Expect</h3>
    <p>This interview assesses your ability to conduct quantitative analysis, draw meaningful conclusions from data, and communicate your findings effectively. You'll typically be presented with a business problem or a dataset and asked to analyze it, focusing on hypothesis generation, quantitative analysis, goal setting aligned with business objectives, and adaptability to dynamic situations.</p>
  </div>

  <div class="card">
    <h3>Key Areas</h3>
    <ul>
      <li><strong>Crafting Hypotheses and Statistical Knowledge:</strong> Formulating strong, testable hypotheses, particularly for new features or data-driven decisions. Understanding null (H0) and alternative (H1) hypotheses, framing hypotheses with quantifiable metrics, and prioritizing based on business impact.</li>
      <li><strong>Proficiency in Quantitative Analysis:</strong> Quantifying trade-offs, understanding the impact of features on relevant metrics, and using data to support your arguments.</li>
      <li><strong>Goal Setting Aligned with Business Objectives:</strong> Defining clear goals and success metrics that directly contribute to broader business objectives. Consider success metrics, counter metrics, and overall ecosystem stability metrics.</li>
      <li><strong>Adapting Analytical Approaches in Dynamic Situations:</strong> Demonstrating flexibility when facing data challenges, changing requirements, or confounding factors.</li>
    </ul>
  </div>

  <div class="card">
    <h3>How to Prepare</h3>
    <ul>
      <li><strong>Master Foundational Statistical Concepts:</strong> Focus on defining, applying, and explaining the limitations of statistical concepts.</li>
      <li><strong>Practice with Case Studies:</strong> Focus on hypothesis generation, quantitative analysis, and structured problem-solving.</li>
      <li><strong>Develop a Structured Approach to Trade-offs:</strong> Use a structured framework (see table below).</li>
      <li><strong>Clear and Concise Communication:</strong> Explain the \"why\" behind decisions, provide context, and use visualizations.</li>
      <li><strong>Share Behavioral Stories Demonstrating Adaptability:</strong> Use the STAR method.</li>
      <li><strong>Familiarize Yourself with Meta's Context:</strong> Research Meta's products, user base, and business objectives.</li>
      <li><strong>A/B Testing Deep Dive:</strong> Understand sample size calculation, statistical significance, power, metrics to track, and interpreting results.</li>
      <li><strong>Asking Clarifying Questions:</strong> Practice asking clarifying questions to fully understand the problem.</li>
    </ul>
  </div>

  <div class="card">
    <h3>Trade-off Evaluation Framework</h3>
    <table>
      <tr>
        <th>Option</th>
        <th>Metric A</th>
        <th>Impact on Metric A</th>
        <th>Metric B</th>
        <th>Impact on Metric B</th>
        <th>Overall Assessment</th>
      </tr>
      <tr>
        <td>A</td>
        <td>CTR</td>
        <td>+5%</td>
        <td>Load Time</td>
        <td>+20ms</td>
        <td>Acceptable Trade-off</td>
      </tr>
      <tr>
        <td>B</td>
        <td>CTR</td>
        <td>+10%</td>
        <td>Load Time</td>
        <td>+100ms</td>
        <td>Unacceptable Trade-off</td>
      </tr>
    </table>
  </div>

  <div class="card">
    <h3>Example Scenario (Brief)</h3>
    <p><strong>Problem:</strong> A social media platform has seen a recent decline in user engagement. How would you investigate the cause?</p>
    
    <h4>Possible Approach:</h4>
    <ol>
      <li><strong>Clarifying Questions:</strong>
        <ul>
          <li>What is the timeframe of the decline?</li>
          <li>Is the decline observed across all regions/markets?</li>
          <li>Is the decline observed across all user segments or only specific ones?</li>
          <li>Have there been any recent product changes or marketing campaigns?</li>
          <li>Have DAU and MAU metrics also been declining?</li>
        </ul>
      </li>
      <li><strong>Define Key Metrics and Business Objectives:</strong> Define \"user engagement\" with specific, measurable metrics (DAU, MAU, session duration, content creation rate, etc.).</li>
      <li><strong>Craft Hypotheses:</strong> Formulate testable hypotheses about potential causes.</li>
      <li><strong>Analyze Trends and Segment Users:</strong> Analyze trends, segmenting by demographics, behavior, and platform.</li>
      <li><strong>Quantitative Analysis and Trade-off Evaluation:</strong> Use A/B testing, cohort analysis, or regression.</li>
      <li><strong>Adapt to Dynamic Situations:</strong> Discuss how you'd adapt if data quality issues arose.</li>
      <li><strong>Communicate Findings and Recommendations:</strong> Present findings clearly with visualizations.</li>
    </ol>
  </div>

  <div class="card">
    <h3>📊 Full Worked Case Study: "Instagram Reels Engagement Drop"</h3>
    
    <details>
    <summary><strong>Click to expand the complete case study walkthrough</strong></summary>
    
    <h4>🎯 The Prompt</h4>
    <p><em>Interviewer: "Reels watch time per user dropped 15% week-over-week. Walk me through how you'd investigate."</em></p>
    
    <hr>
    
    <h4>Step 1: Clarifying Questions (2-3 minutes)</h4>
    <p><strong>Always ask before diving in.</strong> This shows structured thinking and prevents wasted effort.</p>
    
    <table>
      <tr>
        <th>Question</th>
        <th>Why You're Asking</th>
        <th>Hypothetical Answer</th>
      </tr>
      <tr>
        <td>"Is this global or specific regions?"</td>
        <td>Localize the problem</td>
        <td>"It's global, but worse in NA and EU"</td>
      </tr>
      <tr>
        <td>"New users, existing, or both?"</td>
        <td>Acquisition vs retention issue</td>
        <td>"Existing users are driving the drop"</td>
      </tr>
      <tr>
        <td>"Any product launches or bugs last week?"</td>
        <td>Rule out obvious causes</td>
        <td>"We launched a new recommendation algo"</td>
      </tr>
      <tr>
        <td>"Is this just watch time, or also opens/sessions?"</td>
        <td>Understand where in funnel the problem is</td>
        <td>"Opens are flat; watch time per session is down"</td>
      </tr>
      <tr>
        <td>"How are we measuring watch time?"</td>
        <td>Rule out measurement issues</td>
        <td>"Total seconds watched / DAU"</td>
      </tr>
    </table>
    
    <p><strong>What we learned:</strong> The issue is global, affecting existing users, watch time per session is down (not opens), and there was a new recommendation algorithm launch.</p>
    
    <hr>
    
    <h4>Step 2: Hypothesis Generation (2 minutes)</h4>
    <p><strong>Generate multiple hypotheses, then prioritize.</strong></p>
    
    <table>
      <tr>
        <th>#</th>
        <th>Hypothesis</th>
        <th>How We'd Test</th>
        <th>Priority</th>
      </tr>
      <tr>
        <td>1</td>
        <td>New algo is recommending less engaging content</td>
        <td>Compare avg video completion rate pre/post launch</td>
        <td>🔴 High</td>
      </tr>
      <tr>
        <td>2</td>
        <td>New algo shows less variety, causing fatigue</td>
        <td>Measure content diversity score per session</td>
        <td>🔴 High</td>
      </tr>
      <tr>
        <td>3</td>
        <td>Bug in video player (buffering, crashes)</td>
        <td>Check error rates, buffer time metrics</td>
        <td>🟡 Medium</td>
      </tr>
      <tr>
        <td>4</td>
        <td>Seasonal effect (holiday week, exams)</td>
        <td>Compare to same period last year</td>
        <td>🟡 Medium</td>
      </tr>
      <tr>
        <td>5</td>
        <td>Competition (TikTok launched new feature)</td>
        <td>External research; less actionable</td>
        <td>🟢 Low</td>
      </tr>
    </table>
    
    <p><strong>Prioritization logic:</strong> Start with the algo change since it's the most likely cause given timing. Rule out bugs quickly. Seasonal and competition are backup hypotheses.</p>
    
    <hr>
    
    <h4>Step 3: Data Analysis (5-7 minutes)</h4>
    
    <h5>Analysis 1: Algo Impact on Engagement</h5>
    <pre><code>-- Compare key metrics pre/post algo launch
WITH weekly_metrics AS (
  SELECT 
    CASE 
      WHEN event_date < '2025-12-15' THEN 'pre_launch'
      ELSE 'post_launch'
    END AS period,
    user_id,
    SUM(watch_time_seconds) AS total_watch_time,
    COUNT(DISTINCT video_id) AS videos_watched,
    AVG(completion_rate) AS avg_completion
  FROM reels_events
  WHERE event_date BETWEEN '2025-12-08' AND '2025-12-22'
  GROUP BY 1, 2
)
SELECT 
  period,
  COUNT(DISTINCT user_id) AS users,
  AVG(total_watch_time) AS avg_watch_time,
  AVG(videos_watched) AS avg_videos,
  AVG(avg_completion) AS avg_completion_rate
FROM weekly_metrics
GROUP BY period;</code></pre>
    
    <p><strong>Finding:</strong></p>
    <table>
      <tr>
        <th>Period</th>
        <th>Avg Watch Time</th>
        <th>Avg Videos</th>
        <th>Completion Rate</th>
      </tr>
      <tr>
        <td>Pre-launch</td>
        <td>420 sec</td>
        <td>28</td>
        <td>45%</td>
      </tr>
      <tr>
        <td>Post-launch</td>
        <td>357 sec (-15%)</td>
        <td>24 (-14%)</td>
        <td>38% (-16%)</td>
      </tr>
    </table>
    
    <p><strong>Insight:</strong> Completion rate dropped significantly—users are swiping away faster. The algo is showing content users don't want to finish.</p>
    
    <h5>Analysis 2: Content Diversity</h5>
    <pre><code>-- Measure content diversity: unique creators per session
WITH session_diversity AS (
  SELECT 
    period,
    user_id,
    session_id,
    COUNT(DISTINCT creator_id) AS unique_creators,
    COUNT(DISTINCT content_category) AS unique_categories
  FROM reels_events
  GROUP BY 1, 2, 3
)
SELECT 
  period,
  AVG(unique_creators) AS avg_creators_per_session,
  AVG(unique_categories) AS avg_categories_per_session
FROM session_diversity
GROUP BY period;</code></pre>
    
    <p><strong>Finding:</strong></p>
    <table>
      <tr>
        <th>Period</th>
        <th>Creators/Session</th>
        <th>Categories/Session</th>
      </tr>
      <tr>
        <td>Pre-launch</td>
        <td>18</td>
        <td>6</td>
      </tr>
      <tr>
        <td>Post-launch</td>
        <td>12 (-33%)</td>
        <td>4 (-33%)</td>
      </tr>
    </table>
    
    <p><strong>Insight:</strong> New algo is over-optimizing for a narrow set of creators/categories. Users get bored faster.</p>
    
    <h5>Analysis 3: Segment Deep-Dive</h5>
    <pre><code>-- Which user segments are most affected?
SELECT 
  user_tenure_bucket,
  period,
  AVG(watch_time_seconds) AS avg_watch_time
FROM reels_events
JOIN users USING (user_id)
GROUP BY 1, 2
ORDER BY user_tenure_bucket, period;</code></pre>
    
    <p><strong>Finding:</strong></p>
    <table>
      <tr>
        <th>Tenure</th>
        <th>Pre-Launch</th>
        <th>Post-Launch</th>
        <th>Change</th>
      </tr>
      <tr>
        <td>0-30 days</td>
        <td>380 sec</td>
        <td>350 sec</td>
        <td>-8%</td>
      </tr>
      <tr>
        <td>31-180 days</td>
        <td>420 sec</td>
        <td>340 sec</td>
        <td>-19%</td>
      </tr>
      <tr>
        <td>180+ days</td>
        <td>450 sec</td>
        <td>370 sec</td>
        <td>-18%</td>
      </tr>
    </table>
    
    <p><strong>Insight:</strong> Veteran users are hit hardest. They have more refined tastes; the algo's lack of diversity bothers them most.</p>
    
    <hr>
    
    <h4>Step 4: Root Cause Identification (1 minute)</h4>
    
    <p><strong>The Story:</strong></p>
    <blockquote>
      The new recommendation algorithm is over-indexing on short-term engagement signals (e.g., "user watched 80% of this video, show more like it"). This creates a "filter bubble" that reduces content diversity by 33%. Users, especially veterans, experience content fatigue faster, leading to lower completion rates (-16%) and shorter sessions (-15%).
    </blockquote>
    
    <hr>
    
    <h4>Step 5: Recommendations (2 minutes)</h4>
    
    <table>
      <tr>
        <th>Recommendation</th>
        <th>Expected Impact</th>
        <th>Effort</th>
        <th>Priority</th>
      </tr>
      <tr>
        <td><strong>Immediate:</strong> Roll back to previous algo while we fix</td>
        <td>Recover 15% watch time</td>
        <td>Low</td>
        <td>🔴 Do now</td>
      </tr>
      <tr>
        <td><strong>Short-term:</strong> Add diversity constraint to algo (min 15 unique creators per session)</td>
        <td>Improve completion rate</td>
        <td>Medium</td>
        <td>🟡 This sprint</td>
      </tr>
      <tr>
        <td><strong>Medium-term:</strong> A/B test diversity parameter levels</td>
        <td>Find optimal balance</td>
        <td>Medium</td>
        <td>🟢 Next month</td>
      </tr>
      <tr>
        <td><strong>Long-term:</strong> Build content fatigue model</td>
        <td>Proactive diversity adjustment</td>
        <td>High</td>
        <td>🟢 Roadmap</td>
      </tr>
    </table>
    
    <h5>Trade-off Discussion</h5>
    <p><em>Interviewer: "But the new algo increased ad revenue per session by 5%. How do you think about that trade-off?"</em></p>
    
    <p><strong>Answer framework:</strong></p>
    <ol>
      <li><strong>Quantify both sides:</strong>
        <ul>
          <li>+5% ad revenue per session</li>
          <li>-15% sessions per user (watch time proxy)</li>
          <li>Net impact: 0.95 × 1.05 = 0.9975... roughly breakeven short-term</li>
        </ul>
      </li>
      <li><strong>Consider long-term effects:</strong>
        <ul>
          <li>Fatigued users may churn or reduce frequency</li>
          <li>Short-term ad revenue ≠ long-term DAU health</li>
        </ul>
      </li>
      <li><strong>Recommendation:</strong> The 5% ad revenue gain is likely a short-term boost at the cost of user experience. I'd prioritize watch time recovery to protect long-term engagement, and explore ad optimization separately.</li>
    </ol>
    
    <hr>
    
    <h4>Step 6: Summarize for Interviewer (30 seconds)</h4>
    
    <blockquote>
      <strong>"To summarize:</strong> The 15% watch time drop is caused by the new recommendation algorithm reducing content diversity by 33%. Users, especially veterans, are completing fewer videos and ending sessions earlier. My recommendation is to roll back immediately, then add a diversity constraint before re-launching. I'd also run an A/B test to find the optimal diversity level that balances engagement and ad revenue."
    </blockquote>
    
    </details>
  </div>

  <div class="card">
    <h3>🧠 More Practice Case Studies</h3>
    
    <details>
    <summary><strong>Case 2: "Facebook Marketplace listing volume dropped 20%"</strong></summary>
    
    <h4>Clarifying Questions to Ask:</h4>
    <ul>
      <li>Is this new listings, or total active listings?</li>
      <li>Is this sellers listing less, or fewer unique sellers?</li>
      <li>Is this specific to certain categories?</li>
      <li>Any changes to listing flow or policies?</li>
    </ul>
    
    <h4>Hypotheses to Generate:</h4>
    <ol>
      <li>Listing flow has more friction (new verification step?)</li>
      <li>Sellers are migrating to other platforms</li>
      <li>Fewer buyers → sellers see less value</li>
      <li>Category-specific issue (e.g., auto listings down)</li>
      <li>Seasonality (post-holiday cleanup is done)</li>
    </ol>
    
    <h4>Analysis Approach:</h4>
    <pre><code>-- Decompose: Is it fewer sellers or fewer listings per seller?
SELECT 
  date_trunc('week', listed_at) AS week,
  COUNT(DISTINCT seller_id) AS unique_sellers,
  COUNT(*) AS total_listings,
  COUNT(*) / COUNT(DISTINCT seller_id)::float AS listings_per_seller
FROM marketplace_listings
WHERE listed_at >= CURRENT_DATE - 60
GROUP BY 1
ORDER BY 1;</code></pre>
    
    <h4>Key Insight (Hypothetical):</h4>
    <p>Unique sellers is flat; listings per seller dropped. A new "enhanced photos" requirement is adding friction—sellers with phones that don't support it are dropping off.</p>
    
    <h4>Recommendation:</h4>
    <p>Make enhanced photos optional with a "recommended" badge; A/B test impact on buyer engagement.</p>
    </details>
    
    <details>
    <summary><strong>Case 3: "WhatsApp message send failure rate increased"</strong></summary>
    
    <h4>Clarifying Questions:</h4>
    <ul>
      <li>What's the failure rate now vs baseline?</li>
      <li>Is this specific to certain message types (text, media, voice)?</li>
      <li>Is this regional or global?</li>
      <li>Any infra changes or deployments?</li>
    </ul>
    
    <h4>Hypotheses:</h4>
    <ol>
      <li>Server-side issue (deployment, capacity)</li>
      <li>Client-side issue (app update, device compatibility)</li>
      <li>Network issues (carrier, ISP)</li>
      <li>Media-specific issue (image/video sending)</li>
    </ol>
    
    <h4>Analysis Approach:</h4>
    <pre><code>-- Segment by message type and region
SELECT 
  message_type,
  region,
  COUNT(*) AS attempts,
  SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) AS failures,
  SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS failure_rate
FROM message_events
WHERE event_date >= CURRENT_DATE - 7
GROUP BY 1, 2
ORDER BY failure_rate DESC;</code></pre>
    
    <h4>Key Insight (Hypothetical):</h4>
    <p>Image messages in India have 25% failure rate (vs 2% baseline). A new image compression library in the latest Android app update is crashing on older devices.</p>
    
    <h4>Recommendation:</h4>
    <p>Rollback the library for devices below Android 10; push a hotfix within 24 hours.</p>
    </details>
    
    <details>
    <summary><strong>Case 4: "LinkedIn connection acceptance rate dropped"</strong></summary>
    
    <h4>Clarifying Questions:</h4>
    <ul>
      <li>Is this overall or for cold outreach specifically?</li>
      <li>Is the drop in sends, accepts, or both?</li>
      <li>Any changes to the connection request UI?</li>
    </ul>
    
    <h4>Hypotheses:</h4>
    <ol>
      <li>New UI makes "Ignore" easier than "Accept"</li>
      <li>Increase in spam/recruiter requests</li>
      <li>People are more selective (behavior change)</li>
      <li>Measurement changed (definition of "accept")</li>
    </ol>
    
    <h4>Analysis Approach:</h4>
    <pre><code>-- Funnel analysis: request → view → action
SELECT 
  week,
  COUNT(*) AS requests_sent,
  SUM(CASE WHEN viewed THEN 1 ELSE 0 END) AS viewed,
  SUM(CASE WHEN accepted THEN 1 ELSE 0 END) AS accepted,
  SUM(CASE WHEN ignored THEN 1 ELSE 0 END) AS ignored,
  AVG(CASE WHEN accepted THEN 1 ELSE 0 END) AS accept_rate
FROM connection_requests
GROUP BY week;</code></pre>
    
    <h4>Key Insight (Hypothetical):</h4>
    <p>View rate is flat; accept rate dropped 10%, ignore rate up 10%. New mobile UI made "Ignore" the default swipe gesture.</p>
    
    <h4>Recommendation:</h4>
    <p>A/B test reversing the swipe direction; if validated, ship the fix.</p>
    </details>
  </div>

  <div class="card">
    <h3>📈 Descriptive Analytics Deep Dive</h3>
    <p>Descriptive analytics is the foundation of every analytical execution interview. Before forming hypotheses or running experiments, you must <strong>describe what the data looks like</strong>. Interviewers test whether you reach for the right summary statistics and whether you understand when each one is appropriate.</p>

    <details>
    <summary><strong>Click to expand the full Descriptive Analytics guide</strong></summary>

    <h4>The Five-Number Summary + Beyond</h4>
    <p>For any metric you encounter in an interview, your first instinct should be to characterize its distribution:</p>

    <table>
      <tr>
        <th>Statistic</th>
        <th>What It Tells You</th>
        <th>When to Use</th>
        <th>Watch Out For</th>
      </tr>
      <tr>
        <td><strong>Mean</strong></td>
        <td>Average level</td>
        <td>Symmetric distributions, aggregated metrics</td>
        <td>Sensitive to outliers — one whale user can skew it</td>
      </tr>
      <tr>
        <td><strong>Median</strong></td>
        <td>Typical value</td>
        <td>Skewed data (revenue, session length)</td>
        <td>Ignores tail behavior entirely</td>
      </tr>
      <tr>
        <td><strong>Mode</strong></td>
        <td>Most common value</td>
        <td>Categorical data, discrete counts</td>
        <td>May not be unique; not useful for continuous data</td>
      </tr>
      <tr>
        <td><strong>Standard Deviation</strong></td>
        <td>Spread around the mean</td>
        <td>Normal-ish distributions</td>
        <td>Meaningless for highly skewed data</td>
      </tr>
      <tr>
        <td><strong>IQR (Q3 − Q1)</strong></td>
        <td>Spread of the middle 50%</td>
        <td>Skewed distributions, outlier detection</td>
        <td>Ignores tails by design</td>
      </tr>
      <tr>
        <td><strong>Skewness</strong></td>
        <td>Asymmetry direction</td>
        <td>Assessing if mean or median is appropriate</td>
        <td>Positive = right tail; most product metrics are right-skewed</td>
      </tr>
      <tr>
        <td><strong>Kurtosis</strong></td>
        <td>Tail heaviness</td>
        <td>Assessing outlier risk</td>
        <td>High kurtosis = more extreme outliers than normal</td>
      </tr>
      <tr>
        <td><strong>Coefficient of Variation (CV)</strong></td>
        <td>Relative variability (σ/μ)</td>
        <td>Comparing variability across metrics with different scales</td>
        <td>Undefined when mean is 0</td>
      </tr>
    </table>

    <h4>Practical SQL for Descriptive Analytics</h4>
    <pre><code>-- Comprehensive descriptive stats for any metric
SELECT
  COUNT(*)                                    AS n,
  AVG(metric_value)                           AS mean,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY metric_value) AS median,
  STDDEV(metric_value)                        AS stddev,
  VARIANCE(metric_value)                      AS variance,
  MIN(metric_value)                           AS min_val,
  PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY metric_value) AS p25,
  PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY metric_value) AS p75,
  PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY metric_value) AS p90,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY metric_value) AS p95,
  PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY metric_value) AS p99,
  MAX(metric_value)                           AS max_val,
  -- Skewness approximation
  AVG(POWER((metric_value - sub.mu) / sub.sd, 3)) AS skewness,
  -- Coefficient of variation
  STDDEV(metric_value) / NULLIF(AVG(metric_value), 0) AS cv
FROM my_table
CROSS JOIN (
  SELECT AVG(metric_value) AS mu, STDDEV(metric_value) AS sd FROM my_table
) sub;</code></pre>

    <h4>When Mean vs. Median Matters: A Concrete Example</h4>
    <p>Suppose you're analyzing <strong>revenue per user per month</strong> for a freemium app:</p>
    <table>
      <tr><th>User</th><th>Revenue ($)</th></tr>
      <tr><td>User 1</td><td>0</td></tr>
      <tr><td>User 2</td><td>0</td></tr>
      <tr><td>User 3</td><td>0</td></tr>
      <tr><td>User 4</td><td>5</td></tr>
      <tr><td>User 5</td><td>10</td></tr>
      <tr><td>User 6</td><td>12</td></tr>
      <tr><td>User 7</td><td>15</td></tr>
      <tr><td>User 8</td><td>20</td></tr>
      <tr><td>User 9</td><td>50</td></tr>
      <tr><td>User 10</td><td>2,500</td></tr>
    </table>
    <ul>
      <li><strong>Mean:</strong> $261.20 — dominated by the whale user</li>
      <li><strong>Median:</strong> $11.00 — represents the "typical" paying experience</li>
      <li><strong>P90:</strong> $50 — what a high-spending (but not extreme) user looks like</li>
      <li><strong>P99:</strong> $2,500 — whale territory</li>
    </ul>
    <p><strong>Interview tip:</strong> Always state which central tendency you're using and why. Saying "I'd look at the median here because revenue is heavily right-skewed" shows distribution awareness.</p>

    <h4>Segmented Descriptive Analytics</h4>
    <p>Raw descriptive stats across all users can mask important patterns. Always segment:</p>
    <pre><code>-- Descriptive stats segmented by user cohort
SELECT
  user_segment,
  COUNT(*)                                     AS n,
  AVG(metric)                                  AS mean,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY metric) AS median,
  PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY metric) AS p90,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY metric) AS p95,
  STDDEV(metric)                               AS stddev
FROM user_events
GROUP BY user_segment
ORDER BY mean DESC;</code></pre>

    <p><strong>Common segmentations:</strong></p>
    <ul>
      <li>New vs. returning users</li>
      <li>Platform (iOS / Android / Web)</li>
      <li>Geography / market maturity</li>
      <li>Subscription tier (free / premium)</li>
      <li>Power users vs. casual users (e.g., top 10% by activity)</li>
    </ul>

    </details>
  </div>

  <div class="card">
    <h3>📊 Estimating P90, P95, and P99 from Limited Data</h3>
    <p>In interviews (and in practice) you often have <strong>limited data</strong> — maybe 20-50 observations, a summary table, or just a mean and standard deviation. You still need to estimate extreme percentiles like the 90th, 95th, or 99th. Here's how.</p>

    <details>
    <summary><strong>Click to expand Percentile Estimation Techniques</strong></summary>

    <h4>Method 1: Parametric Estimation (Assume a Distribution)</h4>
    <p>If you can assume a distribution family, you can estimate any percentile from just the mean (μ) and standard deviation (σ).</p>

    <h5>For Normal Data</h5>
    <p>Use the z-score formula: <strong>Percentile = μ + z × σ</strong></p>
    <table>
      <tr>
        <th>Percentile</th>
        <th>z-score</th>
        <th>Formula</th>
        <th>Example (μ=100, σ=15)</th>
      </tr>
      <tr>
        <td>P90</td>
        <td>1.282</td>
        <td>μ + 1.282σ</td>
        <td>100 + 1.282 × 15 = <strong>119.2</strong></td>
      </tr>
      <tr>
        <td>P95</td>
        <td>1.645</td>
        <td>μ + 1.645σ</td>
        <td>100 + 1.645 × 15 = <strong>124.7</strong></td>
      </tr>
      <tr>
        <td>P99</td>
        <td>2.326</td>
        <td>μ + 2.326σ</td>
        <td>100 + 2.326 × 15 = <strong>134.9</strong></td>
      </tr>
    </table>
    <p><strong>When to use:</strong> Aggregated metrics (sample means), measurement data, anything you've confirmed is approximately symmetric.</p>
    <p><strong>When NOT to use:</strong> Revenue, session duration, time-to-event — these are almost never normal.</p>

    <h5>For Log-Normal Data (Most Product Metrics)</h5>
    <p>Most product metrics (revenue, session duration, time on page, purchase amounts) are right-skewed and follow a log-normal distribution. The trick: <strong>take the log, estimate percentiles as if normal, then exponentiate back</strong>.</p>

    <p><strong>Step-by-step:</strong></p>
    <ol>
      <li>Compute μ_log = mean of ln(x) and σ_log = stddev of ln(x)</li>
      <li>Estimate log-space percentile: P_log = μ_log + z × σ_log</li>
      <li>Convert back: P = exp(P_log)</li>
    </ol>

    <p><strong>Worked example — Revenue per user:</strong></p>
    <table>
      <tr><th>Statistic</th><th>Raw ($)</th><th>Log-transformed</th></tr>
      <tr><td>Mean</td><td>$45.20</td><td>μ_log = 3.12</td></tr>
      <tr><td>Std Dev</td><td>$120.50</td><td>σ_log = 1.45</td></tr>
    </table>
    <table>
      <tr>
        <th>Percentile</th>
        <th>Log-space Calculation</th>
        <th>Result</th>
      </tr>
      <tr>
        <td>P90</td>
        <td>exp(3.12 + 1.282 × 1.45) = exp(4.98)</td>
        <td><strong>$145.47</strong></td>
      </tr>
      <tr>
        <td>P95</td>
        <td>exp(3.12 + 1.645 × 1.45) = exp(5.51)</td>
        <td><strong>$246.61</strong></td>
      </tr>
      <tr>
        <td>P99</td>
        <td>exp(3.12 + 2.326 × 1.45) = exp(6.49)</td>
        <td><strong>$660.52</strong></td>
      </tr>
    </table>

    <p><strong>Interview tip:</strong> If you're told "revenue per user has mean $45 and std dev $120," immediately note that σ >> μ, which signals a right-skewed distribution. State: "This looks log-normal. I'd estimate percentiles in log-space."</p>

    <h5>For Exponential Data (Time-to-Event)</h5>
    <p>Time between events (purchases, support tickets, logins) often follows an exponential distribution with rate λ = 1/mean.</p>
    <p><strong>Percentile = −ln(1 − p) / λ</strong> or equivalently <strong>−mean × ln(1 − p)</strong></p>

    <table>
      <tr>
        <th>Percentile</th>
        <th>Formula (mean = 7 days)</th>
        <th>Result</th>
      </tr>
      <tr>
        <td>P90</td>
        <td>−7 × ln(0.10)</td>
        <td><strong>16.1 days</strong></td>
      </tr>
      <tr>
        <td>P95</td>
        <td>−7 × ln(0.05)</td>
        <td><strong>21.0 days</strong></td>
      </tr>
      <tr>
        <td>P99</td>
        <td>−7 × ln(0.01)</td>
        <td><strong>32.2 days</strong></td>
      </tr>
    </table>
    <p><strong>When to use:</strong> Days between purchases, time to first action, inter-arrival times, server response times.</p>

    <hr>

    <h4>Method 2: Non-Parametric (Order Statistics)</h4>
    <p>When you have limited raw data (say, n = 20-50 observations) but no distribution assumption:</p>
    <ul>
      <li><strong>Sort the data</strong></li>
      <li><strong>P90 ≈ value at rank ceiling(0.90 × n)</strong></li>
      <li>For n=20: P90 = value at rank 18, P95 = value at rank 19</li>
      <li>For n=50: P90 = value at rank 45, P95 = rank 48, P99 = rank 50</li>
    </ul>
    <p><strong>Limitations:</strong> With small n, you can't reliably estimate P99 (you'd need ~100+ observations for a single P99 data point). State this limitation in interviews.</p>

    <hr>

    <h4>Method 3: Chebyshev's Inequality (Distribution-Free Bound)</h4>
    <p>When you <strong>know nothing</strong> about the distribution shape, Chebyshev gives a worst-case upper bound:</p>
    <p><strong>At most 1/k² of data lies beyond k standard deviations from the mean.</strong></p>

    <table>
      <tr>
        <th>Target</th>
        <th>k</th>
        <th>Chebyshev Bound</th>
        <th>Normal Actual</th>
        <th>Use Case</th>
      </tr>
      <tr>
        <td>P90</td>
        <td>3.16</td>
        <td>μ ± 3.16σ</td>
        <td>μ ± 1.28σ</td>
        <td>Very conservative; safety-critical</td>
      </tr>
      <tr>
        <td>P95</td>
        <td>4.47</td>
        <td>μ ± 4.47σ</td>
        <td>μ ± 1.65σ</td>
        <td>SLA guarantees with unknown distributions</td>
      </tr>
      <tr>
        <td>P99</td>
        <td>10.0</td>
        <td>μ ± 10σ</td>
        <td>μ ± 2.33σ</td>
        <td>Extreme worst-case budgeting</td>
      </tr>
    </table>
    <p><strong>Interview tip:</strong> Mention Chebyshev when the interviewer says "assume nothing about the distribution." It shows depth. But immediately note it's very conservative and offer to refine if you can assume log-normal or similar.</p>

    <hr>

    <h4>Method 4: Bootstrapping (Small Sample, No Assumptions)</h4>
    <p>When you have limited data and can't assume a distribution, bootstrapping gives confidence intervals for percentile estimates:</p>
    <pre><code>import numpy as np

# Your limited data (e.g., 30 page load times in seconds)
data = np.array([0.8, 1.1, 1.2, 1.3, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0,
                 2.1, 2.2, 2.3, 2.5, 2.7, 2.9, 3.0, 3.2, 3.5, 3.8,
                 4.0, 4.2, 4.5, 5.0, 5.5, 6.0, 7.0, 8.5, 10.0, 15.0])

n_bootstrap = 10000
p90_estimates = []
p95_estimates = []
p99_estimates = []

for _ in range(n_bootstrap):
    sample = np.random.choice(data, size=len(data), replace=True)
    p90_estimates.append(np.percentile(sample, 90))
    p95_estimates.append(np.percentile(sample, 95))
    p99_estimates.append(np.percentile(sample, 99))

print(f"P90: {np.median(p90_estimates):.1f} "
      f"[{np.percentile(p90_estimates, 2.5):.1f}, "
      f"{np.percentile(p90_estimates, 97.5):.1f}]")
print(f"P95: {np.median(p95_estimates):.1f} "
      f"[{np.percentile(p95_estimates, 2.5):.1f}, "
      f"{np.percentile(p95_estimates, 97.5):.1f}]")
print(f"P99: {np.median(p99_estimates):.1f} "
      f"[{np.percentile(p99_estimates, 2.5):.1f}, "
      f"{np.percentile(p99_estimates, 97.5):.1f}]")</code></pre>
    <p><strong>Interview tip:</strong> You won't code this live, but mentioning "I'd bootstrap percentile estimates and report a confidence interval" shows sophistication and practical awareness of uncertainty.</p>

    <hr>

    <h4>Decision Framework: Which Method to Use</h4>
    <table>
      <tr>
        <th>Situation</th>
        <th>Best Method</th>
        <th>Example</th>
      </tr>
      <tr>
        <td>Large sample, symmetric data</td>
        <td>Normal parametric (z-score)</td>
        <td>NPS scores, satisfaction ratings</td>
      </tr>
      <tr>
        <td>Right-skewed metric, any sample size</td>
        <td>Log-normal parametric</td>
        <td>Revenue, session duration, purchase amount</td>
      </tr>
      <tr>
        <td>Time-to-event data</td>
        <td>Exponential parametric</td>
        <td>Days between purchases, time to churn</td>
      </tr>
      <tr>
        <td>Small sample (n < 50), no assumptions</td>
        <td>Bootstrap or order statistics</td>
        <td>Pilot test results, early A/B test data</td>
      </tr>
      <tr>
        <td>Unknown distribution, worst-case bound</td>
        <td>Chebyshev inequality</td>
        <td>SLA commitments, safety budgets</td>
      </tr>
      <tr>
        <td>Only summary stats given (mean, σ)</td>
        <td>Parametric with stated assumption</td>
        <td>"The mean load time is 2s with σ = 1.5s"</td>
      </tr>
    </table>

    </details>
  </div>

  <div class="card">
    <h3>🔬 Real-World Data: Distributions, Behavior, and Assumptions</h3>
    <p>Different product metrics follow different distributions. Knowing which distribution applies — and why — is critical for choosing the right analysis technique and communicating results accurately.</p>

    <details>
    <summary><strong>Click to expand Real-World Data Distribution Examples</strong></summary>

    <h4>1. Page Load Times → Log-Normal (Right-Skewed)</h4>
    <table>
      <tr><th>Property</th><th>Value</th></tr>
      <tr><td>Typical range</td><td>0.5s – 3s</td></tr>
      <tr><td>Mean</td><td>~2.1s</td></tr>
      <tr><td>Median</td><td>~1.6s</td></tr>
      <tr><td>P90</td><td>~4.5s</td></tr>
      <tr><td>P95</td><td>~6.0s</td></tr>
      <tr><td>P99</td><td>~12s</td></tr>
      <tr><td>Skewness</td><td>~2.5 (strongly right-skewed)</td></tr>
    </table>
    <p><strong>Why log-normal:</strong> Most requests are fast, but network retries, cold starts, and database timeouts create a long right tail. There's a hard lower bound (can't be < 0) but no practical upper bound.</p>
    <p><strong>Assumption to state:</strong> "Page load times are typically log-normal. I'd report the median and P95/P99 rather than the mean, since the mean is inflated by tail latencies."</p>
    <p><strong>P95 estimation with limited data:</strong> If you have mean_log = 0.47 and sd_log = 0.80, then P95 = exp(0.47 + 1.645 × 0.80) = exp(1.79) ≈ 5.98 seconds.</p>

    <hr>

    <h4>2. Daily Revenue per User → Zero-Inflated Log-Normal</h4>
    <table>
      <tr><th>Property</th><th>Value</th></tr>
      <tr><td>% of zeros</td><td>85-95% (non-paying users)</td></tr>
      <tr><td>Mean (all users)</td><td>$0.15</td></tr>
      <tr><td>Mean (payers only)</td><td>$3.00</td></tr>
      <tr><td>Median (payers)</td><td>$1.50</td></tr>
      <tr><td>P90 (payers)</td><td>$8.00</td></tr>
      <tr><td>P99 (payers)</td><td>$150</td></tr>
    </table>
    <p><strong>Why zero-inflated:</strong> Most users never pay. Among payers, amounts follow a log-normal pattern. This two-part structure requires special handling.</p>
    <p><strong>Assumption to state:</strong> "Revenue is zero-inflated. I'd analyze it as a two-part model: (1) probability of paying (binomial) and (2) amount given paying (log-normal). Reporting a single mean across all users is misleading."</p>

    <pre><code>-- Two-part decomposition for revenue
SELECT
  segment,
  COUNT(*) AS total_users,
  SUM(CASE WHEN revenue > 0 THEN 1 ELSE 0 END) AS payers,
  AVG(CASE WHEN revenue > 0 THEN 1.0 ELSE 0.0 END) AS payer_rate,
  AVG(CASE WHEN revenue > 0 THEN revenue END) AS avg_revenue_payers,
  PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY CASE WHEN revenue > 0 THEN revenue END) AS p90_payers,
  PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY CASE WHEN revenue > 0 THEN revenue END) AS p99_payers
FROM user_daily_revenue
GROUP BY segment;</code></pre>

    <hr>

    <h4>3. Session Duration → Log-Normal / Weibull</h4>
    <table>
      <tr><th>Property</th><th>Value</th></tr>
      <tr><td>Typical range</td><td>10s – 15 min</td></tr>
      <tr><td>Mean</td><td>~5.2 min</td></tr>
      <tr><td>Median</td><td>~3.1 min</td></tr>
      <tr><td>P90</td><td>~12 min</td></tr>
      <tr><td>P95</td><td>~18 min</td></tr>
      <tr><td>P99</td><td>~45 min</td></tr>
      <tr><td>Skewness</td><td>~3.0</td></tr>
    </table>
    <p><strong>Why:</strong> Quick bounces create a mass near zero; deep engagement creates the right tail. The Weibull distribution can model a decreasing hazard rate (users who stay longer tend to stay even longer).</p>
    <p><strong>Assumption to state:</strong> "Session duration is right-skewed with a floor at 0. I'd use median and percentiles rather than mean. If I need to model it, log-normal or Weibull fit well."</p>

    <hr>

    <h4>4. Daily Active Users (DAU) → Approximately Normal (Aggregated Count)</h4>
    <table>
      <tr><th>Property</th><th>Value</th></tr>
      <tr><td>Mean</td><td>2.1M</td></tr>
      <tr><td>Std Dev</td><td>150K</td></tr>
      <tr><td>CV</td><td>~7%</td></tr>
      <tr><td>Skewness</td><td>~0.1 (near symmetric)</td></tr>
    </table>
    <p><strong>Why normal:</strong> DAU is a <strong>count of independent events</strong> aggregated over millions of users. By the Central Limit Theorem, it's approximately normal. Day-of-week seasonality creates predictable humps, not skew.</p>
    <p><strong>Assumption to state:</strong> "DAU is a large aggregate count, so by CLT it's approximately normal. I can use z-scores for percentile estimation. But I'd detrend for day-of-week effects first."</p>

    <hr>

    <h4>5. Number of Events per User per Day → Poisson / Negative Binomial</h4>
    <table>
      <tr><th>Property</th><th>Value</th></tr>
      <tr><td>Mean (likes per user/day)</td><td>4.2</td></tr>
      <tr><td>Variance</td><td>18.5</td></tr>
      <tr><td>% with 0 events</td><td>40%</td></tr>
      <tr><td>P90</td><td>12</td></tr>
      <tr><td>P99</td><td>28</td></tr>
    </table>
    <p><strong>Why negative binomial over Poisson:</strong> Poisson assumes mean = variance. When variance >> mean (overdispersion), which is typical in user event counts, the negative binomial is more appropriate.</p>
    <p><strong>Assumption to state:</strong> "Event counts are overdispersed — the variance is 4× the mean. A Poisson model would underestimate the tails. I'd use negative binomial, or if I just need percentiles, I'd use the empirical distribution."</p>

    <hr>

    <h4>6. Time Between Purchases → Exponential / Gamma</h4>
    <table>
      <tr><th>Property</th><th>Value</th></tr>
      <tr><td>Mean</td><td>14 days</td></tr>
      <tr><td>Median</td><td>9.7 days</td></tr>
      <tr><td>P90</td><td>32.2 days</td></tr>
      <tr><td>P95</td><td>41.9 days</td></tr>
      <tr><td>P99</td><td>64.5 days</td></tr>
    </table>
    <p><strong>Why exponential:</strong> If purchases are memoryless (constant hazard rate), inter-purchase time is exponential. In practice, the Gamma distribution fits better when users have a "warming up" period or increasing purchase propensity.</p>
    <p><strong>Quick estimation:</strong> With exponential assumption and mean = 14 days:</p>
    <ul>
      <li>P90 = −14 × ln(0.10) = 32.2 days</li>
      <li>P95 = −14 × ln(0.05) = 41.9 days</li>
      <li>P99 = −14 × ln(0.01) = 64.5 days</li>
    </ul>

    <hr>

    <h4>7. Conversion Rates (per user segment) → Beta Distribution</h4>
    <table>
      <tr><th>Property</th><th>Value</th></tr>
      <tr><td>Overall rate</td><td>3.2%</td></tr>
      <tr><td>Range across segments</td><td>0.5% – 12%</td></tr>
      <tr><td>Distribution of segment rates</td><td>Right-skewed (most segments have low conversion)</td></tr>
    </table>
    <p><strong>Why Beta:</strong> Conversion rates are bounded [0, 1] and represent proportions. The Beta distribution naturally models proportions and is the conjugate prior for binomial data, making it useful in Bayesian A/B testing.</p>
    <p><strong>Assumption to state:</strong> "Conversion rates follow a Beta distribution. For A/B testing with low conversion rates, I need larger sample sizes because the variance of a proportion is p(1-p)/n, which is maximized near p = 0.5."</p>

    <hr>

    <h4>Quick Reference: Distribution Cheat Sheet for Interviews</h4>
    <table>
      <tr>
        <th>Metric Type</th>
        <th>Likely Distribution</th>
        <th>Use Mean?</th>
        <th>Key Percentile Method</th>
      </tr>
      <tr>
        <td>Load time, latency</td>
        <td>Log-normal</td>
        <td>No — use median + P95</td>
        <td>Log-transform, then z-score</td>
      </tr>
      <tr>
        <td>Revenue per user</td>
        <td>Zero-inflated log-normal</td>
        <td>Conditional on payers</td>
        <td>Separate payers; log-normal for payers</td>
      </tr>
      <tr>
        <td>Session duration</td>
        <td>Log-normal / Weibull</td>
        <td>No — use median</td>
        <td>Log-transform, then z-score</td>
      </tr>
      <tr>
        <td>DAU / MAU</td>
        <td>Normal (CLT)</td>
        <td>Yes</td>
        <td>z-score directly</td>
      </tr>
      <tr>
        <td>Events per user</td>
        <td>Negative binomial</td>
        <td>Yes, but report variance too</td>
        <td>Empirical or parametric NB</td>
      </tr>
      <tr>
        <td>Time between events</td>
        <td>Exponential / Gamma</td>
        <td>Mean is valid</td>
        <td>Exponential formula: −μ ln(1−p)</td>
      </tr>
      <tr>
        <td>Conversion rate</td>
        <td>Beta (Bayesian) / Binomial</td>
        <td>Yes (it IS the mean)</td>
        <td>Beta quantile function</td>
      </tr>
      <tr>
        <td>NPS / Satisfaction</td>
        <td>Bimodal or discrete</td>
        <td>Depends on shape</td>
        <td>Empirical percentiles only</td>
      </tr>
    </table>

    </details>
  </div>

  <div class="card">
    <h3>🎯 Full Mock Interview: "Uber Eats Delivery Time Optimization"</h3>
    <p>This is a complete, realistic 35-minute mock interview for an analytical execution round. It demonstrates every skill an interviewer evaluates: structured thinking, descriptive analytics, distribution awareness, percentile estimation, hypothesis generation, SQL analysis, and clear recommendations.</p>

    <details>
    <summary><strong>Click to expand the complete mock interview walkthrough</strong></summary>

    <h4>🎬 Setting the Scene</h4>
    <p><em>Interviewer: "You're a data scientist at Uber Eats. Our operations team has flagged that customer satisfaction scores dropped from 4.2 to 3.8 (out of 5) over the past month. They suspect delivery times are the issue. You have access to all delivery, order, and customer data. Walk me through how you'd investigate this and what you'd recommend."</em></p>

    <hr>

    <h4>Step 1: Clarifying Questions (3 minutes)</h4>
    <p><strong>Candidate:</strong> "Before I dive in, I'd like to understand the problem space better."</p>

    <table>
      <tr>
        <th>#</th>
        <th>Question</th>
        <th>Why I'm Asking</th>
        <th>Interviewer's Answer</th>
      </tr>
      <tr>
        <td>1</td>
        <td>"Is the CSAT drop consistent across all markets, or concentrated in specific cities?"</td>
        <td>Localize the problem</td>
        <td>"It's worse in large cities like NYC, LA, and Chicago. Smaller markets are relatively stable."</td>
      </tr>
      <tr>
        <td>2</td>
        <td>"Is this across all restaurant types, or specific categories like fast food vs. fine dining?"</td>
        <td>Segment the problem</td>
        <td>"Seems to be across the board, but we haven't dug into that yet."</td>
      </tr>
      <tr>
        <td>3</td>
        <td>"What's the CSAT survey methodology? Is it post-delivery, and what's the response rate?"</td>
        <td>Rule out measurement changes</td>
        <td>"Post-delivery push notification, ~15% response rate, methodology hasn't changed."</td>
      </tr>
      <tr>
        <td>4</td>
        <td>"Have there been any operational changes — new driver onboarding, batched deliveries, routing algorithm updates?"</td>
        <td>Identify potential root causes</td>
        <td>"We launched batched deliveries (2 orders per trip) in large markets 5 weeks ago to reduce driver costs."</td>
      </tr>
      <tr>
        <td>5</td>
        <td>"What does 'delivery time' mean here — from order placed, or from restaurant pickup?"</td>
        <td>Define the metric precisely</td>
        <td>"We track both. Total time = order_placed → delivered. Let's focus on total time."</td>
      </tr>
      <tr>
        <td>6</td>
        <td>"Do we show an estimated delivery time to the customer? And how does actual compare?"</td>
        <td>Expectation vs. reality is key to satisfaction</td>
        <td>"Yes, we show an ETA. Great question — that's probably relevant."</td>
      </tr>
    </table>

    <p><strong>Key insight from clarifying questions:</strong> Batched deliveries launched 5 weeks ago in the same markets where CSAT dropped. This is our primary suspect. But I also want to check whether the issue is absolute delivery time or delivery time <em>relative to the ETA shown</em>.</p>

    <hr>

    <h4>Step 2: Define Metrics & Descriptive Analytics (5 minutes)</h4>
    <p><strong>Candidate:</strong> "Let me first understand the delivery time distribution before and after the batching launch."</p>

    <h5>Key Metrics to Examine</h5>
    <ul>
      <li><strong>Total delivery time</strong> (order_placed → delivered)</li>
      <li><strong>ETA accuracy</strong> = (actual_time − estimated_time) — positive means late</li>
      <li><strong>Late delivery rate</strong> = % of orders where actual > ETA</li>
      <li><strong>Delivery time percentiles</strong> — P50, P90, P95, P99</li>
      <li><strong>CSAT score distribution</strong> — not just the mean</li>
    </ul>

    <h5>Descriptive Analysis Query</h5>
    <pre><code>-- Delivery time distribution: pre vs post batching launch
WITH delivery_stats AS (
  SELECT
    CASE
      WHEN order_date < '2026-02-15' THEN 'pre_batch'
      ELSE 'post_batch'
    END AS period,
    market,
    total_delivery_minutes,
    actual_delivery_minutes - estimated_delivery_minutes AS eta_miss_minutes
  FROM orders o
  JOIN deliveries d ON o.order_id = d.order_id
  WHERE order_date BETWEEN '2026-01-15' AND '2026-03-15'
    AND market IN ('NYC', 'LA', 'Chicago')
)
SELECT
  period,
  COUNT(*) AS orders,
  -- Central tendency
  AVG(total_delivery_minutes) AS mean_delivery,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY total_delivery_minutes) AS median_delivery,
  -- Spread
  STDDEV(total_delivery_minutes) AS stddev_delivery,
  -- Tail behavior (critical for customer experience)
  PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY total_delivery_minutes) AS p90_delivery,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY total_delivery_minutes) AS p95_delivery,
  PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY total_delivery_minutes) AS p99_delivery,
  -- ETA accuracy
  AVG(eta_miss_minutes) AS avg_eta_miss,
  PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY eta_miss_minutes) AS p90_eta_miss,
  AVG(CASE WHEN eta_miss_minutes > 0 THEN 1.0 ELSE 0.0 END) AS late_rate,
  AVG(CASE WHEN eta_miss_minutes > 10 THEN 1.0 ELSE 0.0 END) AS very_late_rate
FROM delivery_stats
GROUP BY period;</code></pre>

    <h5>Hypothetical Results</h5>
    <table>
      <tr>
        <th>Metric</th>
        <th>Pre-Batch</th>
        <th>Post-Batch</th>
        <th>Change</th>
      </tr>
      <tr>
        <td>Median delivery (min)</td>
        <td>32</td>
        <td>35</td>
        <td>+9%</td>
      </tr>
      <tr>
        <td>Mean delivery (min)</td>
        <td>36</td>
        <td>42</td>
        <td>+17%</td>
      </tr>
      <tr>
        <td>Std Dev (min)</td>
        <td>12</td>
        <td>19</td>
        <td>+58% ⚠️</td>
      </tr>
      <tr>
        <td>P90 delivery (min)</td>
        <td>52</td>
        <td>68</td>
        <td>+31% ⚠️</td>
      </tr>
      <tr>
        <td>P95 delivery (min)</td>
        <td>58</td>
        <td>82</td>
        <td>+41% ⚠️</td>
      </tr>
      <tr>
        <td>P99 delivery (min)</td>
        <td>72</td>
        <td>105</td>
        <td>+46% ⚠️</td>
      </tr>
      <tr>
        <td>Avg ETA miss (min)</td>
        <td>-2 (early)</td>
        <td>+8 (late)</td>
        <td>⚠️ Expectation gap</td>
      </tr>
      <tr>
        <td>Late rate (&gt; ETA)</td>
        <td>28%</td>
        <td>55%</td>
        <td>+27pp ⚠️</td>
      </tr>
      <tr>
        <td>Very late rate (&gt;10min)</td>
        <td>8%</td>
        <td>31%</td>
        <td>+23pp ⚠️</td>
      </tr>
    </table>

    <p><strong>Candidate:</strong> "There are two critical findings here:"</p>
    <ol>
      <li><strong>The tails exploded.</strong> The median only went up 9%, but P90 went up 31% and P99 went up 46%. Batching is creating high-variance outcomes. This tells me delivery time is becoming more right-skewed — likely shifting from a log-normal with σ_log ≈ 0.3 to σ_log ≈ 0.5. The mean is misleading here; P95 is the metric that matters for customer experience.</li>
      <li><strong>The ETA model isn't calibrated for batching.</strong> We went from 2 minutes early on average to 8 minutes late. More than half of orders are now arriving after the promised time. That expectation gap is likely what's driving CSAT down more than the absolute time increase."</li>
    </ol>

    <hr>

    <h4>Step 3: Hypothesis Generation & Prioritization (2 minutes)</h4>

    <table>
      <tr>
        <th>#</th>
        <th>Hypothesis</th>
        <th>Evidence So Far</th>
        <th>How to Test</th>
        <th>Priority</th>
      </tr>
      <tr>
        <td>H1</td>
        <td>Batched deliveries increase tail delivery times, and the ETA model doesn't account for the second stop</td>
        <td>Strong: P90/P95 ballooned; late rate doubled</td>
        <td>Compare batched vs. single deliveries</td>
        <td>🔴 High</td>
      </tr>
      <tr>
        <td>H2</td>
        <td>The second customer in a batch is getting cold food (long sit time after restaurant pickup)</td>
        <td>Plausible: second stop adds 10-15 min</td>
        <td>Compare CSAT for 1st vs. 2nd delivery in batch</td>
        <td>🔴 High</td>
      </tr>
      <tr>
        <td>H3</td>
        <td>Batching algorithm pairs distant restaurants or delivery addresses</td>
        <td>Unknown</td>
        <td>Analyze distance between paired orders</td>
        <td>🟡 Medium</td>
      </tr>
      <tr>
        <td>H4</td>
        <td>Drivers are rejecting batched orders, causing reassignment delays</td>
        <td>Unknown</td>
        <td>Check driver acceptance rates pre/post</td>
        <td>🟡 Medium</td>
      </tr>
      <tr>
        <td>H5</td>
        <td>CSAT survey timing/selection bias — unhappy users respond more</td>
        <td>Unlikely: methodology unchanged, response rate stable</td>
        <td>Check response rate trends</td>
        <td>🟢 Low</td>
      </tr>
    </table>

    <hr>

    <h4>Step 4: Deep-Dive Analysis (7 minutes)</h4>

    <h5>Analysis 1: Batched vs. Single Delivery Comparison</h5>
    <pre><code>-- Compare batched vs single deliveries
SELECT
  delivery_type,     -- 'single' or 'batched'
  batch_position,    -- NULL for single, 1 or 2 for batched
  COUNT(*) AS orders,
  AVG(total_delivery_minutes) AS mean_delivery,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY total_delivery_minutes) AS p50,
  PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY total_delivery_minutes) AS p90,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY total_delivery_minutes) AS p95,
  AVG(actual_delivery_minutes - estimated_delivery_minutes) AS avg_eta_miss,
  AVG(CASE WHEN actual_delivery_minutes > estimated_delivery_minutes THEN 1.0 ELSE 0.0 END) AS late_rate,
  AVG(csat_score) AS avg_csat
FROM orders o
JOIN deliveries d ON o.order_id = d.order_id
LEFT JOIN csat_surveys c ON o.order_id = c.order_id
WHERE order_date >= '2026-02-15'
  AND market IN ('NYC', 'LA', 'Chicago')
GROUP BY delivery_type, batch_position;</code></pre>

    <h5>Hypothetical Results</h5>
    <table>
      <tr>
        <th>Delivery Type</th>
        <th>Orders</th>
        <th>P50 (min)</th>
        <th>P90 (min)</th>
        <th>P95 (min)</th>
        <th>Avg ETA Miss</th>
        <th>Late Rate</th>
        <th>Avg CSAT</th>
      </tr>
      <tr>
        <td>Single</td>
        <td>180K</td>
        <td>31</td>
        <td>48</td>
        <td>55</td>
        <td>-1 min</td>
        <td>26%</td>
        <td>4.1</td>
      </tr>
      <tr>
        <td>Batch — 1st drop</td>
        <td>90K</td>
        <td>33</td>
        <td>55</td>
        <td>65</td>
        <td>+5 min</td>
        <td>48%</td>
        <td>3.8</td>
      </tr>
      <tr>
        <td>Batch — 2nd drop</td>
        <td>90K</td>
        <td>45</td>
        <td>78</td>
        <td>92</td>
        <td>+18 min</td>
        <td>72%</td>
        <td>3.2</td>
      </tr>
    </table>

    <p><strong>Candidate:</strong> "This confirms Hypotheses H1 and H2. The second customer in a batch is getting hit hardest: P95 is 92 minutes (vs. 55 for single), the average ETA miss is 18 minutes, and CSAT is 3.2. That 3.2 for 2nd-drop customers is dragging the overall CSAT from 4.1 down to 3.8."</p>

    <h5>Analysis 2: Quantify the CSAT-Lateness Relationship</h5>
    <pre><code>-- CSAT as a function of ETA miss
SELECT
  CASE
    WHEN actual_minutes - estimated_minutes <= -5  THEN '5+ min early'
    WHEN actual_minutes - estimated_minutes <= 0   THEN '0-5 min early'
    WHEN actual_minutes - estimated_minutes <= 5   THEN '0-5 min late'
    WHEN actual_minutes - estimated_minutes <= 10  THEN '5-10 min late'
    WHEN actual_minutes - estimated_minutes <= 20  THEN '10-20 min late'
    ELSE '20+ min late'
  END AS lateness_bucket,
  COUNT(*) AS orders,
  AVG(csat_score) AS avg_csat,
  STDDEV(csat_score) AS sd_csat
FROM orders o
JOIN deliveries d ON o.order_id = d.order_id
JOIN csat_surveys c ON o.order_id = c.order_id
WHERE order_date >= '2026-02-15'
GROUP BY 1
ORDER BY MIN(actual_minutes - estimated_minutes);</code></pre>

    <h5>Hypothetical Results</h5>
    <table>
      <tr>
        <th>Lateness Bucket</th>
        <th>Orders</th>
        <th>Avg CSAT</th>
        <th>"Threshold Effect"</th>
      </tr>
      <tr>
        <td>5+ min early</td>
        <td>45K</td>
        <td>4.5</td>
        <td></td>
      </tr>
      <tr>
        <td>0-5 min early</td>
        <td>70K</td>
        <td>4.3</td>
        <td></td>
      </tr>
      <tr>
        <td>0-5 min late</td>
        <td>55K</td>
        <td>4.0</td>
        <td>Small dip — tolerable</td>
      </tr>
      <tr>
        <td>5-10 min late</td>
        <td>40K</td>
        <td>3.5</td>
        <td>⚠️ Sharp drop — the pain threshold</td>
      </tr>
      <tr>
        <td>10-20 min late</td>
        <td>30K</td>
        <td>2.8</td>
        <td>🔴 Severe impact</td>
      </tr>
      <tr>
        <td>20+ min late</td>
        <td>20K</td>
        <td>2.1</td>
        <td>🔴 Nearly guaranteed bad review</td>
      </tr>
    </table>

    <p><strong>Candidate:</strong> "There's a clear non-linear threshold: CSAT drops sharply once a delivery is more than 5 minutes late. This suggests that <strong>CSAT is driven more by expectation violation than absolute delivery time</strong>. A 45-minute delivery that arrives on time scores better than a 35-minute delivery that's 10 minutes late."</p>

    <h5>Analysis 3: Estimating the Cost of Batching with Percentile Modeling</h5>
    <p><strong>Candidate:</strong> "Let me estimate the P95 delivery time for batched orders using the distribution properties. The post-batch delivery time data shows:"</p>
    <ul>
      <li>Mean_log (2nd drop) ≈ ln(45) ≈ 3.81</li>
      <li>From the spread, σ_log ≈ 0.55</li>
      <li>P95 estimate = exp(3.81 + 1.645 × 0.55) = exp(4.71) ≈ <strong>111 minutes</strong></li>
    </ul>
    <p>"This means about 5% of 2nd-drop customers are waiting nearly <strong>2 hours</strong>. Those customers will likely churn. If we can tighten the distribution by improving routing (reducing σ_log from 0.55 to 0.35), the estimated P95 drops to exp(3.81 + 1.645 × 0.35) = exp(4.39) ≈ 80 minutes — still long, but a 28% improvement at the tail."</p>

    <hr>

    <h4>Step 5: Root Cause Summary (1 minute)</h4>
    <blockquote>
      <p><strong>Root cause:</strong> The batched delivery program launched 5 weeks ago is creating two problems:</p>
      <ol>
        <li><strong>The 2nd-drop customer experiences 40% longer delivery times</strong> (P50: 45 vs. 31 min), with extreme tail cases — P95 of 92 minutes.</li>
        <li><strong>The ETA model was not recalibrated for batching</strong>, creating an expectation gap: 72% of 2nd-drop orders arrive late. Since CSAT drops sharply once lateness exceeds 5 minutes, this expectation gap — not the absolute time — is the primary driver of the CSAT decline.</li>
      </ol>
      <p>In aggregate, the 90K 2nd-drop orders per month with a 3.2 CSAT are pulling the blended average from 4.1 to 3.8.</p>
    </blockquote>

    <hr>

    <h4>Step 6: Recommendations (3 minutes)</h4>

    <table>
      <tr>
        <th>Timeframe</th>
        <th>Recommendation</th>
        <th>Expected Impact</th>
        <th>Effort</th>
        <th>Trade-off</th>
      </tr>
      <tr>
        <td><strong>Immediate (this week)</strong></td>
        <td>Recalibrate ETA model to add estimated batching delay for 2nd-drop customers. Show "Your order is part of a multi-stop delivery" with adjusted ETA.</td>
        <td>Reduce late rate from 72% → ~35% for 2nd-drop; CSAT recovery ~0.2-0.3 points</td>
        <td>Low</td>
        <td>Showing longer ETAs may reduce order volume slightly</td>
      </tr>
      <tr>
        <td><strong>Short-term (2 weeks)</strong></td>
        <td>Add distance/time constraints to batching algorithm: only batch if 2nd drop adds &lt;10 min and distance &lt;1.5 miles</td>
        <td>Reduce 2nd-drop P90 from 78 → ~55 min</td>
        <td>Medium</td>
        <td>Reduces % of eligible batches, partially reducing cost savings</td>
      </tr>
      <tr>
        <td><strong>Medium-term (1 month)</strong></td>
        <td>A/B test dynamic batching rules: batch only during low-demand hours when driver supply is ample; single delivery during peak hours when speed matters most</td>
        <td>Optimize cost savings vs. CSAT trade-off</td>
        <td>Medium</td>
        <td>Requires demand forecasting model</td>
      </tr>
      <tr>
        <td><strong>Long-term (quarter)</strong></td>
        <td>Build a real-time delivery experience score model that predicts CSAT from (estimated time, actual time, food type, weather) and uses it to gate batching decisions — only batch when model predicts CSAT ≥ 4.0</td>
        <td>Systematic quality floor for all deliveries</td>
        <td>High</td>
        <td>Model complexity; needs continuous retraining</td>
      </tr>
    </table>

    <hr>

    <h4>Step 7: Handling the Follow-Up (Trade-off Discussion)</h4>
    <p><em>Interviewer: "The operations team says batching saves $2.50 per delivery in driver costs. That's $225K/month in the three cities. How do you think about the trade-off?"</em></p>

    <p><strong>Candidate:</strong></p>
    <ol>
      <li><strong>Quantify the CSAT cost:</strong>
        <ul>
          <li>90K 2nd-drop orders per month with avg CSAT 3.2 (vs. 4.1 baseline)</li>
          <li>Research shows a 1-point CSAT drop increases churn rate by ~15%</li>
          <li>If these users have LTV of $200 and churn rate increases by 15%: 90K × 0.15 × $200 = <strong>$2.7M at risk annually</strong></li>
        </ul>
      </li>
      <li><strong>Compare to savings:</strong>
        <ul>
          <li>Cost savings: $225K/month = $2.7M/year</li>
          <li>CSAT-driven churn risk: ~$2.7M/year</li>
          <li>Roughly breakeven, <strong>but the churn effect compounds</strong> — lost customers don't come back</li>
        </ul>
      </li>
      <li><strong>Recommendation:</strong> "The batching savings roughly equal the churn risk, but churn is irreversible while cost savings can be optimized. I'd keep batching but with the tighter constraints I suggested — limit the 2nd-drop penalty. A constrained batching model might save $1.80 per delivery (vs $2.50) while keeping CSAT for 2nd-drop orders above 3.8. That's $162K/month in savings with much lower churn risk — a better long-term outcome."</li>
    </ol>

    <hr>

    <h4>Step 8: Closing Summary (30 seconds)</h4>
    <blockquote>
      <p><strong>"To wrap up:</strong> The CSAT decline from 4.2 to 3.8 is primarily driven by the batched delivery program. The 2nd-drop customer experiences 40% longer delivery times and 72% of their orders arrive late because the ETA model wasn't updated. The non-linear relationship between lateness and CSAT means even small improvements in ETA accuracy will have outsized effects. My recommendation is a three-pronged approach: (1) immediately fix the ETA model, (2) tighten batching constraints over the next two weeks, and (3) A/B test dynamic batching rules to find the cost-quality sweet spot. The batching program can be profitable without destroying customer experience."</p>
    </blockquote>

    <hr>

    <h4>📝 Interviewer Scorecard: What This Candidate Demonstrated</h4>
    <table>
      <tr>
        <th>Evaluation Criterion</th>
        <th>Rating</th>
        <th>Evidence</th>
      </tr>
      <tr>
        <td>Problem structuring</td>
        <td>✅ Strong</td>
        <td>Asked 6 clarifying questions; identified batching immediately as the likely cause</td>
      </tr>
      <tr>
        <td>Descriptive analytics</td>
        <td>✅ Strong</td>
        <td>Used median + percentiles (not just mean); noted distribution shift; explained mean vs. median choice</td>
      </tr>
      <tr>
        <td>Distribution awareness</td>
        <td>✅ Strong</td>
        <td>Identified delivery time as log-normal; estimated P95 parametrically; explained tail behavior</td>
      </tr>
      <tr>
        <td>Hypothesis generation</td>
        <td>✅ Strong</td>
        <td>5 hypotheses with prioritization and testing approach</td>
      </tr>
      <tr>
        <td>SQL & quantitative analysis</td>
        <td>✅ Strong</td>
        <td>3 well-structured queries; segmented by delivery type and lateness bucket</td>
      </tr>
      <tr>
        <td>Insight generation</td>
        <td>✅ Strong</td>
        <td>Key insight: CSAT driven by expectation gap, not absolute time — non-obvious finding</td>
      </tr>
      <tr>
        <td>Recommendations</td>
        <td>✅ Strong</td>
        <td>4 prioritized recommendations with trade-offs; quantified cost vs. churn risk</td>
      </tr>
      <tr>
        <td>Communication</td>
        <td>✅ Strong</td>
        <td>Clear narrative arc; concise summary; used data to support every claim</td>
      </tr>
    </table>

    </details>
  </div>

  <div class="card">
    <h3>📱 Social Media Metrics: Expected Behavior & Distributions</h3>
    <p>In interviews you'll often be asked: <em>"A social media metric changed — is that expected?"</em> or <em>"How would you model this metric?"</em>. Answering well requires knowing how each metric <strong>typically behaves</strong>, what distribution it follows, and what assumptions are safe to make.</p>

    <details>
    <summary><strong>Click to expand Social Media Metrics Deep Dive</strong></summary>

    <h4>Quick Reference: Social Media Metric Distributions</h4>
    <table>
      <tr>
        <th>Metric</th>
        <th>Distribution</th>
        <th>Typical Shape</th>
        <th>Use Mean?</th>
        <th>Key Percentiles to Watch</th>
      </tr>
      <tr>
        <td>DAU / MAU</td>
        <td>Normal (CLT)</td>
        <td>Symmetric with day-of-week seasonality</td>
        <td>Yes</td>
        <td>Not applicable — it's a single aggregate</td>
      </tr>
      <tr>
        <td>DAU/MAU ratio (stickiness)</td>
        <td>Beta</td>
        <td>Bounded [0,1], often left-skewed for healthy products</td>
        <td>Yes</td>
        <td>P10 (floor of engagement)</td>
      </tr>
      <tr>
        <td>Likes per post</td>
        <td>Log-normal / Power-law</td>
        <td>Most posts get few; viral posts get orders of magnitude more</td>
        <td>No — use median</td>
        <td>P90, P99 (viral threshold)</td>
      </tr>
      <tr>
        <td>Comments per post</td>
        <td>Zero-inflated negative binomial</td>
        <td>50-70% of posts get 0 comments; heavy right tail</td>
        <td>No — use median or % with ≥1 comment</td>
        <td>P75, P90</td>
      </tr>
      <tr>
        <td>Shares/Reshares per post</td>
        <td>Zero-inflated power-law</td>
        <td>90%+ posts get 0 shares; extreme outliers</td>
        <td>No — use share rate (% with ≥1 share)</td>
        <td>P95, P99 (virality)</td>
      </tr>
      <tr>
        <td>Time spent per session</td>
        <td>Log-normal</td>
        <td>Right-skewed; most sessions are short</td>
        <td>No — use median</td>
        <td>P90, P95</td>
      </tr>
      <tr>
        <td>Time spent per day (total)</td>
        <td>Log-normal / Gamma</td>
        <td>Right-skewed; power users dominate the tail</td>
        <td>No — use median</td>
        <td>P90, P95</td>
      </tr>
      <tr>
        <td>Sessions per user per day</td>
        <td>Poisson / Negative binomial</td>
        <td>Discrete counts, overdispersed</td>
        <td>Yes (as rate)</td>
        <td>P90</td>
      </tr>
      <tr>
        <td>CTR (click-through rate)</td>
        <td>Beta</td>
        <td>Bounded [0,1], usually low (1-5%), right-skewed</td>
        <td>Yes (it IS the proportion)</td>
        <td>Segment by position/content type</td>
      </tr>
      <tr>
        <td>Follow/connection requests per day</td>
        <td>Poisson (well-behaved users) / Power-law (spammers)</td>
        <td>Most send 0-2; bot/spam accounts send hundreds</td>
        <td>Report median + P99</td>
        <td>P99 (spam detection)</td>
      </tr>
      <tr>
        <td>Impressions per piece of content</td>
        <td>Log-normal / Power-law</td>
        <td>Extreme right skew; algo-boosted content dominates</td>
        <td>No — use median</td>
        <td>P90, P99</td>
      </tr>
      <tr>
        <td>Video watch time per view</td>
        <td>Bimodal / Beta</td>
        <td>Spike at 0-3 seconds (scroll-past) and near completion (engaged)</td>
        <td>No — use completion rate</td>
        <td>P25 (quick-abandon), P75</td>
      </tr>
      <tr>
        <td>Ad revenue per user (ARPU)</td>
        <td>Zero-inflated log-normal</td>
        <td>Many users see no ads or don't click; heavy right tail</td>
        <td>Conditional on exposure</td>
        <td>P90, P99 (high-value users)</td>
      </tr>
      <tr>
        <td>Notification open rate</td>
        <td>Beta</td>
        <td>Bounded [0,1]; varies heavily by notification type</td>
        <td>Yes</td>
        <td>P10 (worst-performing types)</td>
      </tr>
      <tr>
        <td>Friend/follower count</td>
        <td>Power-law (Pareto)</td>
        <td>Most users have tens-hundreds; influencers have millions</td>
        <td>No — use median</td>
        <td>P90, P99, P99.9</td>
      </tr>
    </table>

    <hr>

    <h4>Case Study Questions: "How Should This Metric Behave?"</h4>

    <h5>Case A: "Likes per post on Instagram dropped 8% week-over-week. Should we be concerned?"</h5>
    
    <p><strong>Expected distribution:</strong> Likes per post follow a <strong>log-normal / power-law</strong> distribution. Most posts receive a small number of likes, while a few viral posts receive orders of magnitude more.</p>

    <p><strong>Why the distribution matters here:</strong></p>
    <ul>
      <li>Because of the extreme right skew, the <strong>mean likes per post</strong> is heavily influenced by viral outliers. A single viral post (or the absence of one) can swing the mean by 5-10%.</li>
      <li>An 8% drop in the <strong>mean</strong> could simply mean there were fewer viral posts this week — not a systemic problem.</li>
      <li>The <strong>median</strong> likes per post is the better signal for "typical" post performance.</li>
    </ul>
    
    <p><strong>How to investigate:</strong></p>
    <pre><code>-- Decompose: Is the drop in the body or the tail?
SELECT
  period,
  COUNT(*) AS posts,
  AVG(likes) AS mean_likes,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY likes) AS median_likes,
  PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY likes) AS p90_likes,
  PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY likes) AS p99_likes,
  -- What % of posts drove &gt; 50% of all likes?
  COUNT(*) FILTER (WHERE likes > (SELECT PERCENTILE_CONT(0.95) 
    WITHIN GROUP (ORDER BY likes) FROM posts)) * 100.0 / COUNT(*) AS pct_viral
FROM posts
WHERE posted_at BETWEEN '2026-03-02' AND '2026-03-15'
GROUP BY CASE WHEN posted_at < '2026-03-09' THEN 'prev_week' ELSE 'this_week' END AS period;</code></pre>

    <table>
      <tr>
        <th>Period</th>
        <th>Mean Likes</th>
        <th>Median Likes</th>
        <th>P90</th>
        <th>P99</th>
        <th>Interpretation</th>
      </tr>
      <tr>
        <td>Previous week</td>
        <td>142</td>
        <td>28</td>
        <td>310</td>
        <td>8,500</td>
        <td>Baseline</td>
      </tr>
      <tr>
        <td>This week (Scenario 1)</td>
        <td>131</td>
        <td>27</td>
        <td>290</td>
        <td>5,200</td>
        <td>⚠️ Tail shrank — fewer viral posts; body is stable. Likely algorithmic or content-mix issue.</td>
      </tr>
      <tr>
        <td>This week (Scenario 2)</td>
        <td>131</td>
        <td>22</td>
        <td>250</td>
        <td>8,100</td>
        <td>🔴 Body AND tail dropped — systemic engagement decline. Investigate feed ranking, app bugs, or external factors.</td>
      </tr>
    </table>
    
    <p><strong>Key interview insight:</strong> "An 8% drop in mean likes doesn't tell me much on its own because the distribution is extremely right-skewed. I'd look at the median and the P90/P99 separately to determine if this is a tail phenomenon or a systemic shift."</p>

    <hr>

    <h5>Case B: "Time spent per session on TikTok increased by 12%. The PM is celebrating. Is this good?"</h5>

    <p><strong>Expected distribution:</strong> Session duration follows a <strong>log-normal</strong> distribution. Most sessions are 1-5 minutes (quick scrolls), with a long right tail of 30+ minute deep-engagement sessions.</p>

    <p><strong>Why an increase might NOT be good:</strong></p>
    <ul>
      <li>An increase in <strong>mean</strong> session time can be driven by the right tail growing (power users spending even longer) while casual users stay flat or churn.</li>
      <li>If the <strong>median</strong> didn't move but the <strong>P90/P95</strong> jumped — a small group is spending much more time. This can indicate addictive loops rather than broad engagement improvement.</li>
      <li>If total sessions per user <strong>decreased</strong> while time per session increased — users might be coming less often but getting "stuck" when they do. Net time spent per day could be flat or down.</li>
    </ul>

    <p><strong>How to investigate:</strong></p>
    <pre><code>-- Decompose time spent: Per session vs. daily total
SELECT
  period,
  -- Per-session metrics
  AVG(session_duration_min) AS mean_session_min,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY session_duration_min) AS median_session,
  PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY session_duration_min) AS p90_session,
  -- Daily totals per user
  AVG(daily_total_min) AS avg_daily_total,
  -- Frequency
  AVG(sessions_per_day) AS avg_sessions_per_day
FROM (
  SELECT
    user_id,
    session_id,
    CASE WHEN session_date < '2026-03-09' THEN 'prev_week' ELSE 'this_week' END AS period,
    session_duration_min,
    SUM(session_duration_min) OVER (PARTITION BY user_id, session_date) AS daily_total_min,
    COUNT(*) OVER (PARTITION BY user_id, session_date) AS sessions_per_day
  FROM sessions
  WHERE session_date BETWEEN '2026-03-02' AND '2026-03-15'
) sub
GROUP BY period;</code></pre>

    <table>
      <tr>
        <th>Metric</th>
        <th>Prev Week</th>
        <th>This Week</th>
        <th>Change</th>
        <th>Signal</th>
      </tr>
      <tr>
        <td>Mean session (min)</td>
        <td>8.2</td>
        <td>9.2</td>
        <td>+12%</td>
        <td>The headline number</td>
      </tr>
      <tr>
        <td>Median session (min)</td>
        <td>4.5</td>
        <td>4.6</td>
        <td>+2%</td>
        <td>Typical user barely changed</td>
      </tr>
      <tr>
        <td>P90 session (min)</td>
        <td>22</td>
        <td>28</td>
        <td>+27%</td>
        <td>⚠️ Heavy users are going deeper</td>
      </tr>
      <tr>
        <td>Sessions per day</td>
        <td>5.1</td>
        <td>4.6</td>
        <td>-10%</td>
        <td>⚠️ Users are opening the app less</td>
      </tr>
      <tr>
        <td>Total daily time (min)</td>
        <td>42</td>
        <td>42</td>
        <td>0%</td>
        <td>🔴 Net engagement is flat</td>
      </tr>
    </table>

    <p><strong>Key interview insight:</strong> "A 12% increase in mean session time is misleading here. The median barely moved (+2%), meaning typical users aren't more engaged. The increase is driven by the P90 tail — power users going deeper while coming back less often. Total daily engagement is flat. I wouldn't celebrate; I'd investigate whether the longer sessions are healthy engagement or whether users are having trouble finding content quickly."</p>

    <hr>

    <h5>Case C: "Comments per post on Facebook dropped 15%. How would you investigate?"</h5>

    <p><strong>Expected distribution:</strong> Comments per post follow a <strong>zero-inflated negative binomial</strong> distribution. Most posts (50-70%) get <strong>zero</strong> comments. Among posts that do get comments, counts are overdispersed (variance >> mean).</p>

    <p><strong>Why this distribution matters:</strong></p>
    <ul>
      <li>A 15% drop in mean comments could mean: (a) more posts getting zero comments (rate shift) or (b) commented posts getting fewer comments (intensity shift) — these have different causes.</li>
      <li>Because of zero-inflation, the <strong>mean is driven by the fraction of posts that get any comments at all</strong> more than by comment depth.</li>
    </ul>

    <p><strong>Two-part decomposition:</strong></p>
    <pre><code>-- Decompose: Is it fewer posts getting comments, or fewer comments per post?
SELECT
  period,
  COUNT(*) AS total_posts,
  -- Part 1: Comment incidence
  AVG(CASE WHEN comment_count > 0 THEN 1.0 ELSE 0.0 END) AS pct_with_comments,
  -- Part 2: Intensity (among commented posts)
  AVG(CASE WHEN comment_count > 0 THEN comment_count END) AS avg_comments_given_any,
  PERCENTILE_CONT(0.50) WITHIN GROUP (
    ORDER BY CASE WHEN comment_count > 0 THEN comment_count END
  ) AS median_comments_given_any,
  -- Combined
  AVG(comment_count) AS mean_comments_overall
FROM posts_with_engagement
GROUP BY period;</code></pre>

    <table>
      <tr>
        <th>Metric</th>
        <th>Prev Month</th>
        <th>This Month</th>
        <th>Change</th>
      </tr>
      <tr>
        <td>% posts with ≥1 comment</td>
        <td>38%</td>
        <td>30%</td>
        <td>-8pp ⚠️</td>
      </tr>
      <tr>
        <td>Avg comments (given any)</td>
        <td>6.2</td>
        <td>6.0</td>
        <td>-3%</td>
      </tr>
      <tr>
        <td>Mean comments (overall)</td>
        <td>2.4</td>
        <td>1.8</td>
        <td>-25%</td>
      </tr>
    </table>

    <p><strong>Key interview insight:</strong> "The drop is almost entirely in comment <em>incidence</em>, not intensity. Fewer posts are sparking conversations at all, but posts that do get comments are performing similarly. I'd investigate changes to the feed algorithm that may be deprioritizing conversation-starter content, or look at whether content mix shifted toward Stories/Reels (which have lower comment rates by format)."</p>

    <hr>

    <h5>Case D: "DAU/MAU ratio (stickiness) declined from 0.55 to 0.48 over 3 months. What's happening?"</h5>

    <p><strong>Expected distribution:</strong> At the product level, DAU/MAU is a single ratio. But across user segments or markets, the stickiness values follow a <strong>Beta distribution</strong> — bounded between 0 and 1, often left-skewed for healthy apps (most segments have decent stickiness) or right-skewed for apps with retention issues.</p>

    <p><strong>Why this matters:</strong></p>
    <ul>
      <li>DAU/MAU = 0.55 means a typical user opens the app ~17 days per month. Dropping to 0.48 means ~14 days. That's 3 fewer days of engagement per user per month — significant.</li>
      <li>This ratio can decline due to: (a) MAU growing faster than DAU (acquisition without activation), (b) DAU declining (engagement loss), or (c) both.</li>
    </ul>

    <p><strong>How to decompose:</strong></p>
    <pre><code>-- Is DAU falling, MAU rising, or both?
SELECT
  month,
  dau_avg,
  mau,
  dau_avg * 1.0 / mau AS stickiness,
  -- Decompose: new vs returning DAU
  new_user_dau_avg,
  returning_user_dau_avg,
  new_user_dau_avg * 1.0 / dau_avg AS pct_dau_new
FROM monthly_metrics
WHERE month >= '2025-12-01'
ORDER BY month;</code></pre>

    <table>
      <tr>
        <th>Month</th>
        <th>DAU (M)</th>
        <th>MAU (M)</th>
        <th>Stickiness</th>
        <th>% DAU from New Users</th>
        <th>Interpretation</th>
      </tr>
      <tr>
        <td>Dec 2025</td>
        <td>18.7</td>
        <td>34.0</td>
        <td>0.55</td>
        <td>12%</td>
        <td>Baseline</td>
      </tr>
      <tr>
        <td>Jan 2026</td>
        <td>19.1</td>
        <td>36.5</td>
        <td>0.52</td>
        <td>18%</td>
        <td>⚠️ MAU growing from marketing push; new users are less sticky</td>
      </tr>
      <tr>
        <td>Feb 2026</td>
        <td>19.0</td>
        <td>38.2</td>
        <td>0.50</td>
        <td>22%</td>
        <td>⚠️ Acquisition continues but activation/retention lagging</td>
      </tr>
      <tr>
        <td>Mar 2026</td>
        <td>18.5</td>
        <td>38.5</td>
        <td>0.48</td>
        <td>20%</td>
        <td>🔴 DAU starting to decline; new users not converting to daily habit</td>
      </tr>
    </table>

    <p><strong>Key interview insight:</strong> "The stickiness decline isn't because existing users are disengaging — it's driven by rapid MAU growth from acquisition campaigns bringing in users who don't form a daily habit. The existing user base's stickiness is stable. The fix isn't an engagement feature; it's improving the new user onboarding and activation flow. I'd look at D1, D7, D30 retention curves for the new cohorts to find where they drop off."</p>

    <hr>

    <h5>Case E: "Shares per post on LinkedIn are way up — does that mean content quality improved?"</h5>

    <p><strong>Expected distribution:</strong> Shares per post follow a <strong>zero-inflated power-law</strong>. 90%+ of posts get zero shares. Among shared posts, the distribution follows a power law — a tiny fraction account for the vast majority of total shares.</p>

    <p><strong>Why this is tricky:</strong></p>
    <ul>
      <li>Because of the extreme zero-inflation and heavy tail, small changes in the <strong>viral tail</strong> can massively shift the mean.</li>
      <li>"Shares are way up" could mean: (a) a few posts went mega-viral (noise), (b) share rate (% of posts shared at least once) increased (signal), or (c) the share button got repositioned in the UI (behavior change).</li>
    </ul>

    <p><strong>How to decompose:</strong></p>
    <pre><code>-- Separate share rate from share intensity
SELECT
  period,
  COUNT(*) AS total_posts,
  AVG(CASE WHEN shares > 0 THEN 1.0 ELSE 0.0 END) AS share_rate,
  AVG(shares) AS mean_shares_all,
  AVG(CASE WHEN shares > 0 THEN shares END) AS mean_shares_shared,
  PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY shares) AS p99_shares,
  -- Concentration: what % of total shares come from top 1% of posts?
  SUM(CASE WHEN shares >= (SELECT PERCENTILE_CONT(0.99) 
    WITHIN GROUP (ORDER BY shares) FROM posts_engagement) 
    THEN shares ELSE 0 END) * 100.0 / SUM(shares) AS pct_shares_from_top1
FROM posts_engagement
GROUP BY period;</code></pre>

    <table>
      <tr>
        <th>Metric</th>
        <th>Prev Month</th>
        <th>This Month</th>
        <th>Change</th>
        <th>Signal</th>
      </tr>
      <tr>
        <td>Share rate (≥1 share)</td>
        <td>7.2%</td>
        <td>7.5%</td>
        <td>+0.3pp</td>
        <td>Basically flat — broad quality didn't change</td>
      </tr>
      <tr>
        <td>Mean shares (all posts)</td>
        <td>1.8</td>
        <td>2.9</td>
        <td>+61%</td>
        <td>The headline number — misleading</td>
      </tr>
      <tr>
        <td>Mean shares (shared posts)</td>
        <td>25</td>
        <td>39</td>
        <td>+56%</td>
        <td>Intensity up among shared posts</td>
      </tr>
      <tr>
        <td>P99 shares</td>
        <td>1,200</td>
        <td>4,800</td>
        <td>+300%</td>
        <td>⚠️ A few mega-viral posts</td>
      </tr>
      <tr>
        <td>% of shares from top 1%</td>
        <td>42%</td>
        <td>68%</td>
        <td>+26pp</td>
        <td>⚠️ Extreme concentration</td>
      </tr>
    </table>

    <p><strong>Key interview insight:</strong> "Content quality didn't broadly improve. The share rate is flat at 7.5% — the same proportion of posts are resonating. The '61% increase' in mean shares is driven almost entirely by a handful of mega-viral posts (the top 1% now drives 68% of all shares vs. 42% before). This is noise from the power-law tail, not a real content quality improvement. I'd report the share rate as the stable metric and flag the viral outliers as one-time events."</p>

    <hr>

    <h5>Case F: "Video completion rate on Reels shows a bimodal pattern. Is this a reporting bug?"</h5>

    <p><strong>Expected distribution:</strong> Video completion rate (% of video watched per view) is <strong>bimodal</strong> — NOT normal, NOT log-normal. There's a spike near 0% (users who scroll past immediately) and another spike near 100% (users who watch to completion or loop).</p>

    <p><strong>Why bimodal:</strong></p>
    <ul>
      <li>Short-form video is a <strong>binary decision</strong>: within 1-2 seconds, the user either scrolls past (0-5% watched) or commits to watching most/all of it (70-100% watched).</li>
      <li>The middle range (20-60%) is relatively sparse — few users watch exactly half a video then leave.</li>
      <li>This is NOT a bug — it reflects genuine binary user behavior.</li>
    </ul>

    <p><strong>Practical implications:</strong></p>
    <table>
      <tr>
        <th>Approach</th>
        <th>Why It Fails / Works</th>
      </tr>
      <tr>
        <td>❌ Report mean completion rate</td>
        <td>A mean of 45% implies a "typical" viewer watches about half — but almost no one does. It averages two completely different behaviors.</td>
      </tr>
      <tr>
        <td>✅ Report <strong>hook rate</strong> (% who watch ≥3 sec)</td>
        <td>Measures how many users get past the initial scroll decision.</td>
      </tr>
      <tr>
        <td>✅ Report <strong>full-view rate</strong> (% who watch ≥90%)</td>
        <td>Measures engaged viewers. This is what the recommendation algo should optimize for.</td>
      </tr>
      <tr>
        <td>✅ Segment by viewer cohort</td>
        <td>New users have lower hook rates; returning followers have higher full-view rates.</td>
      </tr>
    </table>

    <pre><code>-- Bimodal analysis: separate the two populations
SELECT
  period,
  COUNT(*) AS total_views,
  -- Hook rate: first decision point
  AVG(CASE WHEN pct_watched >= 0.05 THEN 1.0 ELSE 0.0 END) AS hook_rate,
  -- Full view rate: engagement signal
  AVG(CASE WHEN pct_watched >= 0.90 THEN 1.0 ELSE 0.0 END) AS full_view_rate,
  -- Mean is misleading for bimodal data, but report for reference
  AVG(pct_watched) AS mean_completion,
  -- Loop rate: users who rewatch
  AVG(CASE WHEN loops > 1 THEN 1.0 ELSE 0.0 END) AS loop_rate
FROM video_views
GROUP BY period;</code></pre>

    <p><strong>Key interview insight:</strong> "This is expected bimodal behavior, not a bug. Short-form video completion rate has two modes — quick-scroll (~0%) and full-watch (~100%). The mean is meaningless here. I'd always report hook rate (≥3s watched) and full-view rate (≥90%) separately. Any A/B test measuring 'average completion rate' on this data needs to be restructured around these two distinct metrics."</p>

    <hr>

    <h5>Case G: "Our notification open rate dropped from 12% to 9%. What do we look at?"</h5>

    <p><strong>Expected distribution:</strong> Notification open rate follows a <strong>Beta distribution</strong> bounded between 0% and 100%. At the aggregate level it's a single proportion, but across notification types and user segments, rates form a Beta-distributed cloud with wide variance.</p>

    <p><strong>The decomposition approach:</strong></p>
    <pre><code>-- Decompose by notification type and urgency
SELECT
  notification_type,
  period,
  COUNT(*) AS notifs_sent,
  AVG(CASE WHEN opened THEN 1.0 ELSE 0.0 END) AS open_rate,
  -- Volume shift: are we sending more low-quality notifs?
  COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY period) AS pct_of_volume
FROM notifications
WHERE sent_date BETWEEN '2026-02-01' AND '2026-03-15'
GROUP BY notification_type, period
ORDER BY notification_type, period;</code></pre>

    <table>
      <tr>
        <th>Notification Type</th>
        <th>Open Rate (Feb)</th>
        <th>Volume % (Feb)</th>
        <th>Open Rate (Mar)</th>
        <th>Volume % (Mar)</th>
      </tr>
      <tr>
        <td>Direct message</td>
        <td>42%</td>
        <td>15%</td>
        <td>41%</td>
        <td>12%</td>
      </tr>
      <tr>
        <td>Friend request</td>
        <td>35%</td>
        <td>10%</td>
        <td>34%</td>
        <td>8%</td>
      </tr>
      <tr>
        <td>Post like</td>
        <td>8%</td>
        <td>30%</td>
        <td>8%</td>
        <td>22%</td>
      </tr>
      <tr>
        <td>Suggested content</td>
        <td>3%</td>
        <td>20%</td>
        <td>3%</td>
        <td>38% ⚠️</td>
      </tr>
      <tr>
        <td>Engagement reminder</td>
        <td>5%</td>
        <td>25%</td>
        <td>5%</td>
        <td>20%</td>
      </tr>
      <tr>
        <td><strong>Blended</strong></td>
        <td><strong>12%</strong></td>
        <td>100%</td>
        <td><strong>9%</strong></td>
        <td>100%</td>
      </tr>
    </table>

    <p><strong>Key interview insight:</strong> "This is Simpson's paradox. None of the individual notification types had a meaningful open rate change — they're all within ±1pp. The blended rate dropped because the <strong>volume mix shifted</strong>: suggested content notifications (3% open rate) went from 20% to 38% of volume, diluting the overall rate. The fix isn't improving open rates — it's reducing the volume of low-value notifications. I'd recommend a notification relevance model that gates sending based on predicted open probability."</p>

    <hr>

    <h4>🎯 Interview Pattern: How to Answer "A Metric Changed" Questions</h4>
    <p>Every social media metric question follows the same analytical structure:</p>
    <ol>
      <li><strong>State the expected distribution.</strong> "This metric typically follows a [distribution] because [reason]."</li>
      <li><strong>Challenge the summary statistic.</strong> "The mean/median/rate can be misleading because [distribution property]. I'd look at [better statistic]."</li>
      <li><strong>Decompose the change.</strong> Use one of:
        <ul>
          <li><strong>Body vs. tail:</strong> Did the median shift, or just the extremes? (likes, shares, revenue)</li>
          <li><strong>Incidence vs. intensity:</strong> Did the rate of occurrence change, or the magnitude given occurrence? (comments, shares, purchases)</li>
          <li><strong>Mix shift:</strong> Did the composition of the population change? (notification types, user segments, content formats)</li>
        </ul>
      </li>
      <li><strong>Identify root cause.</strong> Map the decomposition to potential causes (algo change, UI change, content mix, seasonality, measurement change).</li>
      <li><strong>Recommend action</strong> with trade-offs acknowledged.</li>
    </ol>

    </details>
  </div>

  <div class="card">
    <h3>⚠️ Common Analytical Execution Mistakes</h3>
    <table>
      <tr>
        <th>Mistake</th>
        <th>Why It Hurts</th>
        <th>Fix</th>
      </tr>
      <tr>
        <td>Diving into data without asking questions</td>
        <td>You may solve the wrong problem</td>
        <td>Always ask 3-5 clarifying questions first</td>
      </tr>
      <tr>
        <td>Only one hypothesis</td>
        <td>Shows narrow thinking</td>
        <td>Generate 3-5 hypotheses, then prioritize</td>
      </tr>
      <tr>
        <td>Complex analysis, no insight</td>
        <td>Impressive SQL ≠ business value</td>
        <td>End every query with "so what?"</td>
      </tr>
      <tr>
        <td>No recommendation</td>
        <td>Analysis without action is useless</td>
        <td>Always propose next steps</td>
      </tr>
      <tr>
        <td>Ignoring trade-offs</td>
        <td>Real decisions have costs</td>
        <td>Acknowledge what you'd give up</td>
      </tr>
    </table>
  </div>

  <div class="card">
    <h3>✅ Self-Assessment Checklist</h3>
    <p>Before your interview, confirm you can:</p>
    <ul>
      <li>☐ Ask 5+ clarifying questions before analyzing</li>
      <li>☐ Generate multiple hypotheses and prioritize them</li>
      <li>☐ Write SQL to segment and diagnose issues</li>
      <li>☐ Summarize findings in one "so what" sentence</li>
      <li>☐ Recommend actions with trade-offs acknowledged</li>
      <li>☐ Discuss a case study for 15+ minutes without notes</li>
    </ul>
  </div>

</div>

<div class="navigation-buttons">
  <a href="{{ '/interview-preparation/technical-skills/' | relative_url }}">Previous: Technical Skills</a>
  <a href="{{ '/interview-preparation/analytical-reasoning/' | relative_url }}">Next: Analytical Reasoning</a>
</div>

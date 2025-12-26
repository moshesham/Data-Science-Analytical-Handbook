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

---
layout: default
title: "Product Analytics Agent Framework"
permalink: /interview-preparation/product-analytics-agent-framework/
difficulty: "Intermediate"
estimated_time: "40 mins"
tags: [Product Analytics, Frameworks, HEART, AARRR, AI Orchestration, Meta, Interview]
track: "Interview Preparation"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/interview-preparation/' | relative_url }}">Interview Preparation</a> <span>&gt;</span>
  <span>Product Analytics Agent Framework</span>
</div>

<div class="header">
  <h1>Product Analytics Agent Framework</h1>
  <p>How to structure a complete, structured analytical response to any product question — from ambiguous prompt to actionable recommendation.</p>
</div>

<div class="section">

  <div class="card">
    <h3>The Problem with Single-Pass Answers</h3>
    <p>Product analytics interview questions are intentionally vague: "Instagram engagement dropped 10% — investigate." A common failure mode is jumping to conclusions: "It's probably a bug" or listing metrics without structure. Interviewers are evaluating <em>how</em> you think, not just what you know.</p>
    <p>The solution is to treat your answer as an <strong>orchestrated workflow</strong>: break the problem into specialist sub-tasks, execute each with discipline, then synthesize into a recommendation. This mirrors how senior data scientists actually work.</p>
  </div>

  <div class="card">
    <h3>The Four-Agent Mental Model</h3>
    <p>Think of your analytical response as four specialist "agents" operating in sequence. In a real AI system (or the MCP server's <code>run_product_analytics_framework</code> tool), these run in parallel — in your interview answer, you execute them sequentially out loud.</p>

    <table>
      <tr>
        <th>Agent</th>
        <th>Question it answers</th>
        <th>Output</th>
      </tr>
      <tr>
        <td><strong>1. Orchestrator</strong></td>
        <td>What type of problem is this? What framework applies?</td>
        <td>Framework selection (HEART vs AARRR), scope definition</td>
      </tr>
      <tr>
        <td><strong>2. Metric Definer</strong></td>
        <td>What metrics matter? What do we protect?</td>
        <td>Primary metric, counter-metrics, segments to analyze</td>
      </tr>
      <tr>
        <td><strong>3. Experiment Designer</strong></td>
        <td>If we test a fix, how? What are the risks?</td>
        <td>Randomization unit, duration, network-effect risks, guardrails</td>
      </tr>
      <tr>
        <td><strong>4. Synthesis Agent</strong></td>
        <td>What do we recommend and how do we communicate it?</td>
        <td>Investigation order, root cause hypotheses, decision criteria</td>
      </tr>
    </table>
  </div>

</div>

<div class="section">
  <h2>Framework Selection: HEART vs AARRR vs North Star</h2>

  <div class="card">
    <h3>When to Use HEART</h3>
    <p><strong>HEART</strong> (Happiness, Engagement, Adoption, Retention, Task Success) was developed by Google UX Research. It is best for evaluating <em>existing feature quality</em> and <em>user experience improvements</em>.</p>
    <ul>
      <li>Use when: diagnosing engagement drops, evaluating a redesign, improving retention</li>
      <li>Strength: covers both quantitative metrics (retention, engagement) and qualitative signals (happiness, task success)</li>
      <li>Meta context: core to product sense interviews — "How would you measure the success of Stories?"</li>
    </ul>
    <table>
      <tr><th>Dimension</th><th>What it measures</th><th>Example signals</th></tr>
      <tr><td>Happiness</td><td>User satisfaction and sentiment</td><td>NPS, CSAT, app store rating</td></tr>
      <tr><td>Engagement</td><td>Frequency and depth of use</td><td>DAU, sessions/day, actions/session</td></tr>
      <tr><td>Adoption</td><td>New users reaching core value</td><td>Feature adoption rate, time-to-first-use</td></tr>
      <tr><td>Retention</td><td>Users returning over time</td><td>D7/D30 retention, churn rate, stickiness (DAU/MAU)</td></tr>
      <tr><td>Task Success</td><td>Users completing intended goals</td><td>Completion rate, error rate, funnel conversion</td></tr>
    </table>
  </div>

  <div class="card">
    <h3>When to Use AARRR</h3>
    <p><strong>AARRR</strong> (Acquisition, Activation, Retention, Referral, Revenue) is the growth framework. Use it for evaluating <em>growth levers</em>, <em>new market expansion</em>, or <em>monetization decisions</em>.</p>
    <ul>
      <li>Use when: evaluating a new market launch, improving onboarding, increasing virality, monetization analysis</li>
      <li>Strength: maps the full user lifecycle from discovery to revenue</li>
      <li>Meta context: common in "How would you grow WhatsApp in India?" type questions</li>
    </ul>
    <table>
      <tr><th>Stage</th><th>Key Question</th><th>Core Metrics</th></tr>
      <tr><td>Acquisition</td><td>How do users find us?</td><td>Installs, signups, CPA by channel</td></tr>
      <tr><td>Activation</td><td>Do users experience core value?</td><td>Onboarding completion rate, time-to-aha-moment</td></tr>
      <tr><td>Retention</td><td>Do users come back?</td><td>D7/D30 retention, churn rate, resurrection rate</td></tr>
      <tr><td>Referral</td><td>Do users bring others?</td><td>Viral coefficient (K-factor), invite acceptance rate</td></tr>
      <tr><td>Revenue</td><td>Do we monetize effectively?</td><td>ARPU, LTV, conversion to paid, ARPDAU</td></tr>
    </table>
  </div>

  <div class="card">
    <h3>North Star Metric</h3>
    <p>Every product has one metric that best captures its core value delivery. For complex interviews, anchor your entire answer to the relevant North Star — then explain how your proposed actions affect it.</p>
    <table>
      <tr><th>Product</th><th>North Star</th><th>Why</th></tr>
      <tr><td>Facebook Feed</td><td>DAU/MAU (stickiness)</td><td>Captures daily habit formation at scale</td></tr>
      <tr><td>Instagram Reels</td><td>Watch-through rate × share rate</td><td>Both consumption quality and viral distribution</td></tr>
      <tr><td>WhatsApp</td><td>Messages sent per DAU</td><td>Depth of engagement, not just presence</td></tr>
      <tr><td>Marketplace</td><td>Successful transactions per MAU</td><td>End-to-end value delivery (listing → sale)</td></tr>
    </table>
  </div>

</div>

<div class="section">
  <h2>Worked Example: End-to-End Answer</h2>

  <div class="card">
    <h3>Prompt: "Instagram Stories engagement is down 10% week-over-week. Investigate."</h3>

    <h4>Agent 1 — Orchestrator: Frame the problem</h4>
    <blockquote>
      <p>"Before diving in, I want to clarify a few things: Is this a rate drop (engagement per story view) or an absolute drop? Is it global or region/platform specific? And what's the measurement window? I'll assume engagement rate = reactions + replies per story impression, global, last 7 days vs. prior 7 days."</p>
      <p>"This is a diagnostics problem. I'll use the HEART framework with a focus on the Engagement and Task Success dimensions."</p>
    </blockquote>

    <h4>Agent 2 — Metric Definer: Define what to measure</h4>
    <blockquote>
      <ul>
        <li><strong>Primary metric:</strong> Story engagement rate = (reactions + replies) / story impressions</li>
        <li><strong>Counter-metrics (guardrails):</strong> Story creation rate (did creators stop posting?), story view rate (did reach change?), spam rate (quality signal)</li>
        <li><strong>Segments to break down:</strong> Platform (iOS/Android/Web), country, user cohort (new vs. established), content type (text vs. photo vs. video)</li>
        <li><strong>Leading indicators to check:</strong> Story creation rate (if creators dropped, impressions follow), notification delivery rate (push notifications drive story views)</li>
      </ul>
    </blockquote>

    <h4>Agent 3 — Experiment Designer: Plan a test if we identify a fix</h4>
    <blockquote>
      <p>"If our investigation identifies a fixable cause — say, the reaction tray is harder to reach in a new UI — we'd A/B test the fix. Key considerations:"</p>
      <ul>
        <li><strong>Randomization unit:</strong> User-level (not story-level), since story consumption is tied to individual user behavior patterns</li>
        <li><strong>Network effects:</strong> Stories are social — if I see fewer stories (treatment), my network activity also changes. Use cluster randomization by social graph partition to minimize spillover</li>
        <li><strong>Duration:</strong> Minimum 2 weeks to capture the full weekly usage cycle and control for novelty effects</li>
        <li><strong>Decision criteria:</strong> Ship if engagement rate improves ≥ 2% (MDE) with p &lt; 0.05, no regression in story creation rate or spam rate</li>
      </ul>
    </blockquote>

    <h4>Agent 4 — Synthesis: Order of investigation and recommendation</h4>
    <blockquote>
      <ol>
        <li><strong>Check data pipeline first:</strong> Is the drop in the data or the product? Verify event ingestion lag and logging completeness</li>
        <li><strong>Pinpoint timing:</strong> Plot daily engagement rate over last 30 days. If the drop is a step-change on a specific date → look for releases or infra changes</li>
        <li><strong>Segment isolation:</strong> Run segment breakdown (platform × country). If 100% of the drop comes from Android users in Europe → likely a release bug</li>
        <li><strong>Funnel diagnosis:</strong> Did story views drop (reach problem) or did reactions per view drop (interaction problem)? These have different fixes</li>
        <li><strong>Root cause hypotheses (ordered by likelihood):</strong>
          <ul>
            <li>Product release changed the reaction UI → test on that release date</li>
            <li>Algorithm change reduced story distribution → check organic reach rate</li>
            <li>Seasonal behavior change → compare to same week prior year</li>
            <li>Competitor launch pulling engagement elsewhere → cross-app usage data</li>
          </ul>
        </li>
        <li><strong>Communication:</strong> "We observed a 10% drop in story engagement rate starting [date], concentrated in [segment]. Our primary hypothesis is [cause] because [evidence]. We recommend [action] and will monitor story creation rate as a guardrail."</li>
      </ol>
    </blockquote>
  </div>

</div>

<div class="section">
  <h2>AI Agent Orchestration in the MCP Server</h2>

  <div class="card">
    <h3>How This Maps to the <code>run_product_analytics_framework</code> Tool</h3>
    <p>The MCP server implements this four-agent pattern as a single orchestrated tool. When you call <code>run_product_analytics_framework</code>, it fans out to three specialist sub-components (metric definition, experiment design, diagnostic SQL) and then synthesizes the outputs.</p>

    <pre><code>-- Example MCP tool call (via Claude or VS Code):
{
  "name": "run_product_analytics_framework",
  "arguments": {
    "question": "Instagram Stories engagement is down 10% week-over-week",
    "product_area": "engagement",
    "framework": "HEART",
    "include_sql": true
  }
}</code></pre>

    <p>The tool returns:</p>
    <ul>
      <li><strong>Metric framework</strong> — HEART dimensions relevant to engagement, with primary signals and guardrails</li>
      <li><strong>Experiment design</strong> — Randomization unit, network-effect risks, decision criteria</li>
      <li><strong>Diagnostic SQL templates</strong> — Time-series, segment breakdown, funnel, cohort comparison queries</li>
      <li><strong>Synthesis</strong> — Ordered investigation steps and communication template</li>
    </ul>

    <h4>Additional Specialist Tools</h4>
    <table>
      <tr><th>Tool</th><th>When to Use</th></tr>
      <tr><td><code>define_product_metrics</code></td><td>Only need metric definition (e.g., preparing for a metrics-focused interview round)</td></tr>
      <tr><td><code>design_product_experiment</code></td><td>Only need experiment design (e.g., evaluating a specific A/B test plan)</td></tr>
      <tr><td><code>generate_diagnostic_sql</code></td><td>Only need SQL templates (e.g., practicing diagnostic queries)</td></tr>
      <tr><td><code>design_ab_experiment</code></td><td>Statistical experiment design with sample size calculation (from A/B testing tools)</td></tr>
    </table>
  </div>

  <div class="card">
    <h3>Why Orchestrator Pattern (Not Pipeline)</h3>
    <p>Metric definition, experiment design, and SQL generation are <strong>independent tasks</strong> — they don't depend on each other's outputs. The orchestrator pattern runs them in parallel and passes all results to the synthesis step, which has a dependency on all three. This is faster and more modular than a linear pipeline where each step must wait for the previous one.</p>

    <pre><code>User Question
      │
      ▼
 Orchestrator Agent   ← classifies problem, selects framework
      │ fans out (parallel)
 ┌────┴────────────────────────┐
 ▼              ▼              ▼
Metric       Experiment    SQL Query
Definer      Designer      Generator
 └────┬────────────────────────┘
      │ aggregates
      ▼
 Synthesis Agent   ← ordered investigation + communication plan</code></pre>
  </div>

</div>

<div class="section">
  <h2>Framework Quick Reference</h2>

  <div class="card">
    <h3>Which Framework for Which Question?</h3>
    <table>
      <tr><th>Question Type</th><th>Framework</th><th>Key Dimensions to Emphasize</th></tr>
      <tr><td>"Metric X dropped — investigate"</td><td>HEART</td><td>Engagement, Task Success (funnel), then Happiness</td></tr>
      <tr><td>"Measure success of feature Y"</td><td>HEART</td><td>Adoption, Engagement, Retention (post-feature)</td></tr>
      <tr><td>"Grow product Z in new market"</td><td>AARRR</td><td>Acquisition, Activation, Referral</td></tr>
      <tr><td>"Should we add monetization?"</td><td>AARRR + guardrails</td><td>Revenue vs. Retention trade-off</td></tr>
      <tr><td>"Define the North Star for X"</td><td>North Star</td><td>Value delivery, frequency, breadth of impact</td></tr>
      <tr><td>"Design an A/B test for Y"</td><td>Experiment Design</td><td>Randomization, network effects, duration, MDE</td></tr>
    </table>
  </div>

  <div class="card">
    <h3>Network Effect Risks — Cheat Sheet</h3>
    <table>
      <tr><th>Risk</th><th>What It Is</th><th>Mitigation</th></tr>
      <tr><td>Interference / Spillover</td><td>Treatment users interact with control via social graph</td><td>Cluster randomization by social graph partition or geography</td></tr>
      <tr><td>Novelty Effect</td><td>Engagement spike from excitement, not real lift</td><td>Run 2–4 weeks; analyze engagement by days-in-experiment</td></tr>
      <tr><td>Primacy Effect</td><td>Users resist change initially, then adapt</td><td>Segment by days-in-experiment; look for behavior stabilization</td></tr>
      <tr><td>Sample Ratio Mismatch</td><td>Groups aren't the expected size → logging bug or selection bias</td><td>Chi-square test on group sizes within 24h of launch</td></tr>
      <tr><td>Multiple Testing</td><td>Many metrics → inflated false positive rate</td><td>Pre-register primary metric; Bonferroni correction for secondary metrics</td></tr>
    </table>
  </div>

</div>

<div class="navigation-buttons">
  <a href="{{ '/interview-preparation/analytical-reasoning/' | relative_url }}">Previous: Analytical Reasoning</a>
  <a href="{{ '/interview-preparation/behavioral-interview/' | relative_url }}">Next: Behavioral Interview</a>
</div>

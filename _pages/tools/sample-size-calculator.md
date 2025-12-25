---
layout: default
title: "A/B Test Sample Size Calculator"
permalink: /tools/sample-size-calculator/
difficulty: "Intermediate"
estimated_time: "10 mins"
tags: [A/B Testing, Statistics, Tools]
track: "Interview Prep"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <span>Sample Size Calculator</span>
</div>

<div class="header">
  <h1>A/B Test Sample Size Calculator</h1>
  <p>Calculate the required sample size for your A/B tests to achieve statistical significance.</p>
</div>

<div class="section">
  
  <div class="card">
    <h3>About This Tool</h3>
    <p>When designing an A/B test, one of the most critical decisions is determining how many users you need in each variant to detect a meaningful difference. This calculator helps you estimate the required sample size based on your baseline conversion rate, minimum detectable effect, and desired statistical power.</p>
  </div>

  <div class="card">
    <h3>Calculator</h3>
    <form id="sampleSizeForm" style="max-width: 600px;">
      <div style="margin-bottom: 20px;">
        <label for="baselineRate" style="display: block; margin-bottom: 5px; font-weight: bold;">
          Baseline Conversion Rate (%)
        </label>
        <input type="number" id="baselineRate" step="0.1" min="0" max="100" value="5" 
               style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
        <small style="color: #666;">Current conversion rate of your control group</small>
      </div>

      <div style="margin-bottom: 20px;">
        <label for="minEffect" style="display: block; margin-bottom: 5px; font-weight: bold;">
          Minimum Detectable Effect (%)
        </label>
        <input type="number" id="minEffect" step="0.1" min="0" max="100" value="10" 
               style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
        <small style="color: #666;">Relative change you want to detect (e.g., 10% means detecting 5% → 5.5%)</small>
      </div>

      <div style="margin-bottom: 20px;">
        <label for="significance" style="display: block; margin-bottom: 5px; font-weight: bold;">
          Significance Level (α)
        </label>
        <select id="significance" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
          <option value="0.01">0.01 (99% confidence)</option>
          <option value="0.05" selected>0.05 (95% confidence)</option>
          <option value="0.10">0.10 (90% confidence)</option>
        </select>
        <small style="color: #666;">Probability of false positive (Type I error)</small>
      </div>

      <div style="margin-bottom: 20px;">
        <label for="power" style="display: block; margin-bottom: 5px; font-weight: bold;">
          Statistical Power (1-β)
        </label>
        <select id="power" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
          <option value="0.70">0.70 (70% power)</option>
          <option value="0.80" selected>0.80 (80% power)</option>
          <option value="0.90">0.90 (90% power)</option>
          <option value="0.95">0.95 (95% power)</option>
        </select>
        <small style="color: #666;">Probability of detecting a real effect (1 - Type II error)</small>
      </div>

      <button type="button" onclick="calculateSampleSize()" 
              style="width: 100%; padding: 12px; background-color: #0366d6; color: white; border: none; border-radius: 4px; font-size: 16px; cursor: pointer;">
        Calculate Sample Size
      </button>
    </form>

    <div id="results" style="margin-top: 30px; padding: 20px; background-color: #f6f8fa; border-radius: 4px; display: none;">
      <h4 style="margin-top: 0;">Results</h4>
      <div id="resultsContent"></div>
    </div>
  </div>

  <div class="card">
    <h3>Understanding the Parameters</h3>
    <ul>
      <li><strong>Baseline Conversion Rate:</strong> The current conversion rate of your control group (e.g., 5% of users complete a purchase)</li>
      <li><strong>Minimum Detectable Effect (MDE):</strong> The smallest relative change you want to be able to detect. For example, if your baseline is 5% and MDE is 10%, you want to detect a change to 5.5%</li>
      <li><strong>Significance Level (α):</strong> The probability of incorrectly concluding there's a difference when there isn't one (false positive). Common value: 0.05</li>
      <li><strong>Statistical Power (1-β):</strong> The probability of correctly detecting a real difference. Common value: 0.80 (80% power)</li>
    </ul>
  </div>

  <div class="card">
    <h3>Key Insights</h3>
    <ul>
      <li>Higher baseline conversion rates require <strong>smaller sample sizes</strong></li>
      <li>Detecting smaller effects requires <strong>larger sample sizes</strong></li>
      <li>Higher power or lower significance levels require <strong>larger sample sizes</strong></li>
      <li>Plan for longer test durations or higher traffic if your calculated sample size is large</li>
    </ul>
  </div>

</div>

<script>
function calculateSampleSize() {
  // Get input values
  const baselineRate = parseFloat(document.getElementById('baselineRate').value) / 100;
  const minEffect = parseFloat(document.getElementById('minEffect').value) / 100;
  const alpha = parseFloat(document.getElementById('significance').value);
  const power = parseFloat(document.getElementById('power').value);
  
  // Validate inputs
  if (isNaN(baselineRate) || baselineRate <= 0 || baselineRate >= 1) {
    alert('Please enter a valid baseline conversion rate between 0 and 100');
    return;
  }
  if (isNaN(minEffect) || minEffect <= 0) {
    alert('Please enter a valid minimum detectable effect greater than 0');
    return;
  }
  
  // Calculate the treatment conversion rate
  const treatmentRate = baselineRate * (1 + minEffect);
  
  if (treatmentRate >= 1) {
    alert('The combination of baseline rate and effect size exceeds 100%. Please adjust your inputs.');
    return;
  }
  
  // Calculate pooled probability
  const p = (baselineRate + treatmentRate) / 2;
  
  // Get z-scores (approximations for common values)
  const zAlpha = getZScore(alpha / 2); // Two-tailed test
  const zBeta = getZScore(1 - power);
  
  // Sample size formula for proportions (per group)
  const numerator = Math.pow(zAlpha + zBeta, 2) * 2 * p * (1 - p);
  const denominator = Math.pow(treatmentRate - baselineRate, 2);
  const sampleSizePerGroup = Math.ceil(numerator / denominator);
  const totalSampleSize = sampleSizePerGroup * 2;
  
  // Calculate expected test duration (assuming 1000 visitors per day as example)
  const visitorsPerDay = 1000;
  const daysNeeded = Math.ceil(totalSampleSize / visitorsPerDay);
  
  // Display results
  const resultsDiv = document.getElementById('results');
  const resultsContent = document.getElementById('resultsContent');
  
  resultsContent.innerHTML = `
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
      <div>
        <div style="font-size: 14px; color: #666; margin-bottom: 5px;">Sample Size per Group</div>
        <div style="font-size: 32px; font-weight: bold; color: #0366d6;">${sampleSizePerGroup.toLocaleString()}</div>
      </div>
      <div>
        <div style="font-size: 14px; color: #666; margin-bottom: 5px;">Total Sample Size</div>
        <div style="font-size: 32px; font-weight: bold; color: #0366d6;">${totalSampleSize.toLocaleString()}</div>
      </div>
    </div>
    
    <div style="padding: 15px; background-color: white; border-radius: 4px; border-left: 4px solid #28a745;">
      <p style="margin: 0 0 10px 0;"><strong>What this means:</strong></p>
      <ul style="margin: 0; padding-left: 20px;">
        <li>You need <strong>${sampleSizePerGroup.toLocaleString()} users</strong> in each variant (control and treatment)</li>
        <li>Total of <strong>${totalSampleSize.toLocaleString()} users</strong> in your experiment</li>
        <li>With ${(baselineRate * 100).toFixed(1)}% baseline, you can detect a change to <strong>${(treatmentRate * 100).toFixed(2)}%</strong></li>
        <li>At 1,000 visitors/day (50/50 split), this would take approximately <strong>${daysNeeded} days</strong></li>
      </ul>
    </div>
    
    <div style="margin-top: 15px; padding: 12px; background-color: #fff3cd; border-radius: 4px; border-left: 4px solid #ffc107;">
      <p style="margin: 0; font-size: 14px;"><strong>⚠️ Note:</strong> This is a simplified calculation. Actual tests should account for multiple comparisons, segmentation, and guardrail metrics.</p>
    </div>
  `;
  
  resultsDiv.style.display = 'block';
  resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function getZScore(probability) {
  // Approximations for common z-scores
  const zTable = {
    0.005: 2.576,  // 99% confidence (two-tailed)
    0.025: 1.960,  // 95% confidence (two-tailed)
    0.05: 1.645,   // 90% confidence (two-tailed)
    0.10: 1.282,
    0.15: 1.036,
    0.20: 0.842,
    0.25: 0.674,
    0.30: 0.524
  };
  
  // Find closest match
  const probabilities = Object.keys(zTable).map(Number);
  const closest = probabilities.reduce((prev, curr) => 
    Math.abs(curr - probability) < Math.abs(prev - probability) ? curr : prev
  );
  
  return zTable[closest];
}
</script>

<div class="navigation-buttons">
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Back to Statistics & Probability</a>
  <a href="{{ '/simulations/distributions/' | relative_url }}">Next: Distribution Visualizations</a>
</div>

---
layout: default
title: "Interactive Distribution Visualizations"
permalink: /simulations/distributions/
difficulty: "Intermediate"
estimated_time: "15 mins"
tags: [Statistics, Probability, Distributions, Visualization]
track: "Foundational Knowledge"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Statistics & Probability</a> <span>&gt;</span>
  <span>Distribution Visualizations</span>
</div>

<div class="header">
  <h1>Interactive Distribution Visualizations</h1>
  <p>Explore and understand key probability distributions through interactive visualizations.</p>
</div>

<div class="section">
  
  <div class="card">
    <h3>About This Tool</h3>
    <p>Understanding probability distributions is fundamental to data science and statistics. This interactive tool lets you visualize and manipulate different distributions to build intuition about their properties and use cases.</p>
  </div>

  <!-- Normal Distribution -->
  <div class="card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2px; border-radius: 8px;">
    <div style="background-color: white; padding: 25px; border-radius: 6px;">
      <h3 style="margin-top: 0; color: #667eea;">📊 Normal (Gaussian) Distribution</h3>
      <p style="color: #666;">The bell curve - fundamental to statistics. Characterized by mean (μ) and standard deviation (σ).</p>
      
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
        <div>
          <label for="normalMean" style="display: block; margin-bottom: 5px; font-weight: bold;">Mean (μ)</label>
          <input type="range" id="normalMean" min="-5" max="5" step="0.5" value="0" 
                 style="width: 100%;" oninput="updateNormalDistribution()">
          <div style="text-align: center; color: #666; margin-top: 5px;">
            <span id="normalMeanValue">0</span>
          </div>
        </div>
        <div>
          <label for="normalStd" style="display: block; margin-bottom: 5px; font-weight: bold;">Standard Deviation (σ)</label>
          <input type="range" id="normalStd" min="0.5" max="3" step="0.1" value="1" 
                 style="width: 100%;" oninput="updateNormalDistribution()">
          <div style="text-align: center; color: #666; margin-top: 5px;">
            <span id="normalStdValue">1</span>
          </div>
        </div>
      </div>
      
      <canvas id="normalChart" height="80"></canvas>
      
      <div style="margin-top: 15px; padding: 15px; background-color: #f8f9fa; border-radius: 4px; border-left: 4px solid #667eea;">
        <p style="margin: 0; font-size: 14px;"><strong>Key Properties:</strong></p>
        <ul style="margin: 10px 0 0 0; font-size: 14px;">
          <li>~68% of data within 1σ of mean</li>
          <li>~95% of data within 2σ of mean</li>
          <li>~99.7% of data within 3σ of mean (Empirical Rule)</li>
          <li><strong>Use Cases:</strong> Heights, test scores, measurement errors, CLT applications</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Binomial Distribution -->
  <div class="card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 2px; border-radius: 8px;">
    <div style="background-color: white; padding: 25px; border-radius: 6px;">
      <h3 style="margin-top: 0; color: #f5576c;">🎲 Binomial Distribution</h3>
      <p style="color: #666;">Models the number of successes in n independent trials with probability p.</p>
      
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
        <div>
          <label for="binomialN" style="display: block; margin-bottom: 5px; font-weight: bold;">Number of Trials (n)</label>
          <input type="range" id="binomialN" min="5" max="50" step="1" value="20" 
                 style="width: 100%;" oninput="updateBinomialDistribution()">
          <div style="text-align: center; color: #666; margin-top: 5px;">
            <span id="binomialNValue">20</span>
          </div>
        </div>
        <div>
          <label for="binomialP" style="display: block; margin-bottom: 5px; font-weight: bold;">Success Probability (p)</label>
          <input type="range" id="binomialP" min="0" max="1" step="0.05" value="0.5" 
                 style="width: 100%;" oninput="updateBinomialDistribution()">
          <div style="text-align: center; color: #666; margin-top: 5px;">
            <span id="binomialPValue">0.5</span>
          </div>
        </div>
      </div>
      
      <canvas id="binomialChart" height="80"></canvas>
      
      <div style="margin-top: 15px; padding: 15px; background-color: #f8f9fa; border-radius: 4px; border-left: 4px solid #f5576c;">
        <p style="margin: 0; font-size: 14px;"><strong>Key Properties:</strong></p>
        <ul style="margin: 10px 0 0 0; font-size: 14px;">
          <li>Mean = n × p = <span id="binomialMean">10</span></li>
          <li>Variance = n × p × (1-p) = <span id="binomialVar">5</span></li>
          <li><strong>Use Cases:</strong> Conversion rates, click-through rates, A/B test outcomes, quality control</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Poisson Distribution -->
  <div class="card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 2px; border-radius: 8px;">
    <div style="background-color: white; padding: 25px; border-radius: 6px;">
      <h3 style="margin-top: 0; color: #00a8e8;">⏱️ Poisson Distribution</h3>
      <p style="color: #666;">Models the number of events in a fixed interval of time or space.</p>
      
      <div style="max-width: 400px; margin-bottom: 20px;">
        <label for="poissonLambda" style="display: block; margin-bottom: 5px; font-weight: bold;">Rate Parameter (λ)</label>
        <input type="range" id="poissonLambda" min="0.5" max="15" step="0.5" value="5" 
               style="width: 100%;" oninput="updatePoissonDistribution()">
        <div style="text-align: center; color: #666; margin-top: 5px;">
          <span id="poissonLambdaValue">5</span> events per interval
        </div>
      </div>
      
      <canvas id="poissonChart" height="80"></canvas>
      
      <div style="margin-top: 15px; padding: 15px; background-color: #f8f9fa; border-radius: 4px; border-left: 4px solid #00a8e8;">
        <p style="margin: 0; font-size: 14px;"><strong>Key Properties:</strong></p>
        <ul style="margin: 10px 0 0 0; font-size: 14px;">
          <li>Mean = Variance = λ</li>
          <li>Events occur independently</li>
          <li>Average rate is constant</li>
          <li><strong>Use Cases:</strong> Page views per hour, customer arrivals, system failures, email volume</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Exponential Distribution -->
  <div class="card" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 2px; border-radius: 8px;">
    <div style="background-color: white; padding: 25px; border-radius: 6px;">
      <h3 style="margin-top: 0; color: #ff6b6b;">⏳ Exponential Distribution</h3>
      <p style="color: #666;">Models the time between events in a Poisson process.</p>
      
      <div style="max-width: 400px; margin-bottom: 20px;">
        <label for="exponentialLambda" style="display: block; margin-bottom: 5px; font-weight: bold;">Rate Parameter (λ)</label>
        <input type="range" id="exponentialLambda" min="0.1" max="3" step="0.1" value="1" 
               style="width: 100%;" oninput="updateExponentialDistribution()">
        <div style="text-align: center; color: #666; margin-top: 5px;">
          <span id="exponentialLambdaValue">1</span> events per unit time
        </div>
      </div>
      
      <canvas id="exponentialChart" height="80"></canvas>
      
      <div style="margin-top: 15px; padding: 15px; background-color: #f8f9fa; border-radius: 4px; border-left: 4px solid #ff6b6b;">
        <p style="margin: 0; font-size: 14px;"><strong>Key Properties:</strong></p>
        <ul style="margin: 10px 0 0 0; font-size: 14px;">
          <li>Mean = 1/λ = <span id="exponentialMean">1.00</span></li>
          <li>Memoryless property</li>
          <li>Always right-skewed</li>
          <li><strong>Use Cases:</strong> Time until next customer, server response times, system lifetimes, wait times</li>
        </ul>
      </div>
    </div>
  </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
<script>
// Utility functions
function normalPDF(x, mean, std) {
  const variance = std * std;
  const exponent = -Math.pow(x - mean, 2) / (2 * variance);
  return (1 / Math.sqrt(2 * Math.PI * variance)) * Math.exp(exponent);
}

function binomialPMF(k, n, p) {
  function factorial(num) {
    if (num <= 1) return 1;
    let result = 1;
    for (let i = 2; i <= num; i++) result *= i;
    return result;
  }
  
  function combination(n, k) {
    return factorial(n) / (factorial(k) * factorial(n - k));
  }
  
  return combination(n, k) * Math.pow(p, k) * Math.pow(1 - p, n - k);
}

function poissonPMF(k, lambda) {
  function factorial(num) {
    if (num <= 1) return 1;
    let result = 1;
    for (let i = 2; i <= num; i++) result *= i;
    return result;
  }
  
  return (Math.pow(lambda, k) * Math.exp(-lambda)) / factorial(k);
}

function exponentialPDF(x, lambda) {
  if (x < 0) return 0;
  return lambda * Math.exp(-lambda * x);
}

// Chart configurations
const chartOptions = {
  responsive: true,
  maintainAspectRatio: true,
  plugins: {
    legend: { display: false },
    tooltip: {
      callbacks: {
        label: function(context) {
          return 'Probability: ' + context.parsed.y.toFixed(4);
        }
      }
    }
  },
  scales: {
    y: {
      beginAtZero: true,
      title: { display: true, text: 'Probability Density' }
    },
    x: {
      title: { display: true, text: 'Value' }
    }
  }
};

// Normal Distribution
let normalChart;
function updateNormalDistribution() {
  const mean = parseFloat(document.getElementById('normalMean').value);
  const std = parseFloat(document.getElementById('normalStd').value);
  
  document.getElementById('normalMeanValue').textContent = mean.toFixed(1);
  document.getElementById('normalStdValue').textContent = std.toFixed(1);
  
  const xValues = [];
  const yValues = [];
  
  for (let x = mean - 4 * std; x <= mean + 4 * std; x += (8 * std) / 100) {
    xValues.push(x.toFixed(2));
    yValues.push(normalPDF(x, mean, std));
  }
  
  if (normalChart) normalChart.destroy();
  
  const ctx = document.getElementById('normalChart').getContext('2d');
  normalChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: xValues,
      datasets: [{
        label: 'Normal Distribution',
        data: yValues,
        borderColor: '#667eea',
        backgroundColor: 'rgba(102, 126, 234, 0.1)',
        fill: true,
        tension: 0.4,
        pointRadius: 0
      }]
    },
    options: chartOptions
  });
}

// Binomial Distribution
let binomialChart;
function updateBinomialDistribution() {
  const n = parseInt(document.getElementById('binomialN').value);
  const p = parseFloat(document.getElementById('binomialP').value);
  
  document.getElementById('binomialNValue').textContent = n;
  document.getElementById('binomialPValue').textContent = p.toFixed(2);
  
  const mean = n * p;
  const variance = n * p * (1 - p);
  document.getElementById('binomialMean').textContent = mean.toFixed(2);
  document.getElementById('binomialVar').textContent = variance.toFixed(2);
  
  const xValues = [];
  const yValues = [];
  
  for (let k = 0; k <= n; k++) {
    xValues.push(k.toString());
    yValues.push(binomialPMF(k, n, p));
  }
  
  if (binomialChart) binomialChart.destroy();
  
  const ctx = document.getElementById('binomialChart').getContext('2d');
  binomialChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: xValues,
      datasets: [{
        label: 'Binomial Distribution',
        data: yValues,
        backgroundColor: 'rgba(245, 87, 108, 0.7)',
        borderColor: '#f5576c',
        borderWidth: 1
      }]
    },
    options: chartOptions
  });
}

// Poisson Distribution
let poissonChart;
function updatePoissonDistribution() {
  const lambda = parseFloat(document.getElementById('poissonLambda').value);
  
  document.getElementById('poissonLambdaValue').textContent = lambda.toFixed(1);
  
  const xValues = [];
  const yValues = [];
  
  const maxK = Math.max(20, lambda * 3);
  for (let k = 0; k <= maxK; k++) {
    xValues.push(k.toString());
    yValues.push(poissonPMF(k, lambda));
  }
  
  if (poissonChart) poissonChart.destroy();
  
  const ctx = document.getElementById('poissonChart').getContext('2d');
  poissonChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: xValues,
      datasets: [{
        label: 'Poisson Distribution',
        data: yValues,
        backgroundColor: 'rgba(0, 168, 232, 0.7)',
        borderColor: '#00a8e8',
        borderWidth: 1
      }]
    },
    options: chartOptions
  });
}

// Exponential Distribution
let exponentialChart;
function updateExponentialDistribution() {
  const lambda = parseFloat(document.getElementById('exponentialLambda').value);
  
  document.getElementById('exponentialLambdaValue').textContent = lambda.toFixed(1);
  document.getElementById('exponentialMean').textContent = (1 / lambda).toFixed(2);
  
  const xValues = [];
  const yValues = [];
  
  const maxX = 5 / lambda;
  for (let x = 0; x <= maxX; x += maxX / 100) {
    xValues.push(x.toFixed(2));
    yValues.push(exponentialPDF(x, lambda));
  }
  
  if (exponentialChart) exponentialChart.destroy();
  
  const ctx = document.getElementById('exponentialChart').getContext('2d');
  exponentialChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: xValues,
      datasets: [{
        label: 'Exponential Distribution',
        data: yValues,
        borderColor: '#ff6b6b',
        backgroundColor: 'rgba(255, 107, 107, 0.1)',
        fill: true,
        tension: 0.4,
        pointRadius: 0
      }]
    },
    options: chartOptions
  });
}

// Initialize all charts on page load
document.addEventListener('DOMContentLoaded', function() {
  updateNormalDistribution();
  updateBinomialDistribution();
  updatePoissonDistribution();
  updateExponentialDistribution();
});
</script>

<div class="navigation-buttons">
  <a href="{{ '/foundational_knowledge/1/' | relative_url }}">Back to Statistics & Probability</a>
  <a href="{{ '/tools/sample-size-calculator/' | relative_url }}">Next: Sample Size Calculator</a>
</div>

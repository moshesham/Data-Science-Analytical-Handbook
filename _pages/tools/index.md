---
layout: default
title: "Interactive Tools & Simulations"
permalink: /tools/
difficulty: "All Levels"
estimated_time: "Variable"
tags: [Tools, Interactive, Learning]
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <span>Interactive Tools</span>
</div>

<div class="header">
  <h1>Interactive Tools & Simulations</h1>
  <p>Hands-on tools to help you learn and practice data science concepts.</p>
</div>

<div class="section">
  
  <div class="card">
    <h3>About These Tools</h3>
    <p>Learning by doing is the best way to master data science concepts. These interactive tools and simulations allow you to experiment with parameters, visualize concepts, and build intuition without writing any code.</p>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 30px;">
    
    <a href="{{ '/tools/sample-size-calculator/' | relative_url }}" style="text-decoration: none; color: inherit;">
      <div class="card" style="height: 100%; transition: transform 0.2s, box-shadow 0.2s; cursor: pointer; border: 2px solid #e1e4e8;">
        <div style="font-size: 48px; text-align: center; margin-bottom: 15px;">🧮</div>
        <h3 style="color: #0366d6; margin-top: 0;">Sample Size Calculator</h3>
        <p style="color: #666; margin-bottom: 15px;">Calculate the required sample size for your A/B tests based on baseline conversion rate, minimum detectable effect, and desired statistical power.</p>
        <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 15px;">
          <span style="background-color: #e1f5fe; color: #01579b; padding: 4px 8px; border-radius: 3px; font-size: 12px;">A/B Testing</span>
          <span style="background-color: #f3e5f5; color: #4a148c; padding: 4px 8px; border-radius: 3px; font-size: 12px;">Statistics</span>
          <span style="background-color: #e8f5e9; color: #1b5e20; padding: 4px 8px; border-radius: 3px; font-size: 12px;">Experimentation</span>
        </div>
      </div>
    </a>

    <a href="{{ '/simulations/distributions/' | relative_url }}" style="text-decoration: none; color: inherit;">
      <div class="card" style="height: 100%; transition: transform 0.2s, box-shadow 0.2s; cursor: pointer; border: 2px solid #e1e4e8;">
        <div style="font-size: 48px; text-align: center; margin-bottom: 15px;">📊</div>
        <h3 style="color: #0366d6; margin-top: 0;">Distribution Visualizations</h3>
        <p style="color: #666; margin-bottom: 15px;">Explore and manipulate Normal, Binomial, Poisson, and Exponential distributions with interactive sliders and real-time visualizations.</p>
        <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 15px;">
          <span style="background-color: #fff3e0; color: #e65100; padding: 4px 8px; border-radius: 3px; font-size: 12px;">Probability</span>
          <span style="background-color: #f3e5f5; color: #4a148c; padding: 4px 8px; border-radius: 3px; font-size: 12px;">Statistics</span>
          <span style="background-color: #fce4ec; color: #880e4f; padding: 4px 8px; border-radius: 3px; font-size: 12px;">Visualization</span>
        </div>
      </div>
    </a>

  </div>

  <div class="card" style="margin-top: 30px; background-color: #f6f8fa; border-left: 4px solid #0366d6;">
    <h3>🎯 Learning Tips</h3>
    <ul>
      <li><strong>Experiment freely:</strong> Adjust sliders and parameters to see how distributions and calculations change</li>
      <li><strong>Connect to concepts:</strong> Refer back to the theory pages to understand the math behind what you're seeing</li>
      <li><strong>Use in interviews:</strong> These tools help you estimate sample sizes and validate assumptions during case studies</li>
      <li><strong>Build intuition:</strong> Understanding how parameters affect outcomes is key to practical data science</li>
    </ul>
  </div>

  <div class="card" style="margin-top: 20px; background-color: #fff3cd; border-left: 4px solid #ffc107;">
    <h3>💡 Coming Soon</h3>
    <p>We're working on additional interactive tools including:</p>
    <ul style="margin-bottom: 0;">
      <li>Hypothesis Testing Simulator</li>
      <li>Confidence Interval Calculator</li>
      <li>SQL Query Playground</li>
      <li>Monte Carlo Simulation Tool</li>
    </ul>
  </div>

</div>

<style>
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}
</style>

<div class="navigation-buttons">
  <a href="{{ '/tracks/' | relative_url }}">Previous: Learning Tracks</a>
  <a href="{{ '/meta-specificity/' | relative_url }}">Next: Meta Specificity</a>
</div>

---
layout: default
title: "Role-Level Learning Path"
permalink: /learning-path/
difficulty: "Beginner"
estimated_time: "5 mins"
tags: [Learning Path, Career Level, Role Level, Personalized, Planning]
track: "Reference"
---

<div class="breadcrumb">
  <a href="{{ '/' | relative_url }}">Home</a> <span>&gt;</span>
  <span>Role-Level Learning Path</span>
</div>

<div class="header">
  <h1>Role-Level Learning Path</h1>
  <p>Select your target role level to get a customized study plan, curated exercises, and level-appropriate examples.</p>
</div>

<div class="section">

  <div class="card" id="level-selector-card">
    <h3><i class="fas fa-crosshairs"></i> What level are you targeting?</h3>
    <p>Your selection is saved in the browser and shown across the site so every recommendation stays relevant.</p>

    <div class="level-picker" id="level-picker">
      {% for level in site.data.job_levels %}
      <button
        class="level-pick-btn"
        data-level="{{ level.id }}"
        style="--level-color: {{ level.badge_color }};"
        aria-pressed="false">
        <span class="level-pick-icon"><i class="{{ level.icon }}"></i></span>
        <span class="level-pick-label">{{ level.short_label }}</span>
        <span class="level-pick-title">{{ level.label | split: " — " | last }}</span>
      </button>
      {% endfor %}
    </div>
  </div>

  <!-- No level selected state -->
  <div id="no-level-msg" class="card" style="display:none;">
    <p><i class="fas fa-arrow-up"></i> Select a level above to see your personalized plan.</p>
  </div>

  <!-- Level plans — one per level, shown/hidden by JS -->
  {% for level in site.data.job_levels %}
  <div class="level-plan" id="plan-{{ level.id }}" style="display:none;" data-level="{{ level.id }}">

    <!-- Level overview banner -->
    <div class="level-banner" style="border-left: 4px solid {{ level.badge_color }};">
      <div class="level-banner-header">
        <span class="level-badge-lg" style="background: {{ level.badge_color }};">
          <i class="{{ level.icon }}"></i> {{ level.short_label }}
        </span>
        <div>
          <h2>{{ level.label }}</h2>
          <p class="level-duration"><i class="fas fa-clock"></i> Suggested timeline: <strong>{{ level.duration }}</strong></p>
        </div>
      </div>
      <p class="level-description">{{ level.description }}</p>
      <p class="level-audience"><strong>Who this is for:</strong> {{ level.target_audience }}</p>
    </div>

    <!-- Interview rounds -->
    <div class="card">
      <h3><i class="fas fa-clipboard-list"></i> What to Expect in the Interview Loop</h3>
      <ol>
        {% for round in level.typical_rounds %}
        <li>{{ round }}</li>
        {% endfor %}
      </ol>
    </div>

    <!-- Key skills grid -->
    <div class="card">
      <h3><i class="fas fa-tools"></i> Key Skills to Master</h3>
      <div class="skills-grid-lp">

        {% if level.key_skills.sql %}
        <div class="skill-area-card">
          <h4><i class="fas fa-database"></i> {{ level.key_skills.sql.label }}</h4>
          {% if level.key_skills.sql.challenge_bar %}
          <p class="challenge-bar">Challenge bar: <strong>{{ level.key_skills.sql.challenge_bar }}</strong></p>
          {% endif %}
          <ul>
            {% for topic in level.key_skills.sql.topics %}
            <li>{{ topic }}</li>
            {% endfor %}
          </ul>
        </div>
        {% endif %}

        {% if level.key_skills.python %}
        <div class="skill-area-card">
          <h4><i class="fab fa-python"></i> {{ level.key_skills.python.label }}</h4>
          <ul>
            {% for topic in level.key_skills.python.topics %}
            <li>{{ topic }}</li>
            {% endfor %}
          </ul>
        </div>
        {% endif %}

        {% if level.key_skills.statistics %}
        <div class="skill-area-card">
          <h4><i class="fas fa-chart-bell-curve"></i> {{ level.key_skills.statistics.label }}</h4>
          <ul>
            {% for topic in level.key_skills.statistics.topics %}
            <li>{{ topic }}</li>
            {% endfor %}
          </ul>
        </div>
        {% endif %}

        {% if level.key_skills.product_sense %}
        <div class="skill-area-card">
          <h4><i class="fas fa-lightbulb"></i> {{ level.key_skills.product_sense.label }}</h4>
          <ul>
            {% for topic in level.key_skills.product_sense.topics %}
            <li>{{ topic }}</li>
            {% endfor %}
          </ul>
        </div>
        {% endif %}

        {% if level.key_skills.data_modeling %}
        <div class="skill-area-card">
          <h4><i class="fas fa-project-diagram"></i> {{ level.key_skills.data_modeling.label }}</h4>
          <ul>
            {% for topic in level.key_skills.data_modeling.topics %}
            <li>{{ topic }}</li>
            {% endfor %}
          </ul>
        </div>
        {% endif %}

        {% if level.key_skills.distributed_systems %}
        <div class="skill-area-card">
          <h4><i class="fas fa-network-wired"></i> {{ level.key_skills.distributed_systems.label }}</h4>
          <ul>
            {% for topic in level.key_skills.distributed_systems.topics %}
            <li>{{ topic }}</li>
            {% endfor %}
          </ul>
        </div>
        {% endif %}

      </div>
    </div>

    <!-- Phase-by-phase plan -->
    <div class="card">
      <h3><i class="fas fa-map-signs"></i> Your Phased Study Plan</h3>
      <div class="phase-timeline">
        {% for phase in level.learning_plan %}
        <div class="phase-block">
          <div class="phase-header" style="border-left: 3px solid {{ level.badge_color }};">
            <div class="phase-title-row">
              <h4>{{ phase.phase }}</h4>
              {% if phase.daily_time %}
              <span class="phase-time"><i class="fas fa-stopwatch"></i> {{ phase.daily_time }}</span>
              {% endif %}
            </div>
            <p class="phase-focus"><strong>Focus:</strong> {{ phase.focus }}</p>
          </div>
          <ul class="phase-exercises">
            {% for exercise in phase.exercises %}
            <li><i class="fas fa-check-circle" style="color: {{ level.badge_color }};"></i> {{ exercise }}</li>
            {% endfor %}
          </ul>
        </div>
        {% endfor %}
      </div>
    </div>

    <!-- Curated pages -->
    <div class="card">
      <h3><i class="fas fa-book-open"></i> Curated Handbook Pages for {{ level.short_label }}</h3>
      <div class="curated-pages-grid">
        {% for page in level.pages %}
        <a href="{{ page.url | relative_url }}" class="curated-page-link" style="border-top: 3px solid {{ level.badge_color }};">
          <i class="fas fa-arrow-right" style="color: {{ level.badge_color }};"></i>
          {{ page.label }}
        </a>
        {% endfor %}
      </div>
    </div>

  </div>
  {% endfor %}

</div>

<style>
/* ---- Level Picker ---- */
.level-picker {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.level-pick-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
  padding: 1rem 1.5rem;
  border: 2px solid var(--color-bg-tertiary, #e5e7eb);
  border-radius: 12px;
  background: var(--color-bg-secondary, #f9fafb);
  cursor: pointer;
  transition: all 0.2s ease;
  min-width: 120px;
  font-family: inherit;
}

.level-pick-btn:hover {
  border-color: var(--level-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.level-pick-btn[aria-pressed="true"],
.level-pick-btn.active {
  border-color: var(--level-color);
  background: color-mix(in srgb, var(--level-color) 10%, white);
  box-shadow: 0 4px 12px rgba(0,0,0,0.12);
}

.level-pick-icon {
  font-size: 1.5rem;
  color: var(--level-color);
}

.level-pick-label {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--level-color);
}

.level-pick-title {
  font-size: 0.75rem;
  color: var(--color-text-secondary, #6b7280);
  text-align: center;
}

/* ---- Level Banner ---- */
.level-banner {
  padding: 1.5rem;
  background: var(--color-bg-secondary, #f9fafb);
  border-radius: 12px;
  margin-bottom: 1.5rem;
}

.level-banner-header {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 1rem;
}

.level-badge-lg {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  color: white;
  font-weight: 700;
  font-size: 1rem;
  white-space: nowrap;
  flex-shrink: 0;
}

.level-duration {
  font-size: 0.9rem;
  color: var(--color-text-tertiary, #6b7280);
  margin-top: 0.25rem;
}

.level-description {
  margin-bottom: 0.5rem;
}

.level-audience {
  font-size: 0.9rem;
  color: var(--color-text-tertiary, #6b7280);
  font-style: italic;
}

/* ---- Skills Grid ---- */
.skills-grid-lp {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1rem;
  margin-top: 0.75rem;
}

.skill-area-card {
  padding: 1rem;
  background: var(--color-bg-secondary, #f9fafb);
  border-radius: 10px;
  border: 1px solid var(--color-bg-tertiary, #e5e7eb);
}

.skill-area-card h4 {
  font-size: 0.95rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--color-text-primary, #111827);
}

.skill-area-card ul {
  padding-left: 1.2rem;
  font-size: 0.875rem;
  color: var(--color-text-secondary, #374151);
}

.skill-area-card li {
  margin-bottom: 0.2rem;
}

.challenge-bar {
  font-size: 0.8rem;
  margin-bottom: 0.5rem;
  color: var(--color-text-tertiary, #6b7280);
}

/* ---- Phase Timeline ---- */
.phase-timeline {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  margin-top: 0.75rem;
}

.phase-block {
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid var(--color-bg-tertiary, #e5e7eb);
}

.phase-header {
  padding: 0.75rem 1rem;
  background: var(--color-bg-secondary, #f9fafb);
}

.phase-title-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1rem;
  flex-wrap: wrap;
}

.phase-title-row h4 {
  margin: 0;
  font-size: 1rem;
}

.phase-time {
  font-size: 0.8rem;
  color: var(--color-text-tertiary, #6b7280);
  white-space: nowrap;
}

.phase-focus {
  font-size: 0.875rem;
  margin-top: 0.25rem;
  color: var(--color-text-secondary, #374151);
}

.phase-exercises {
  list-style: none;
  padding: 0.75rem 1rem;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.phase-exercises li {
  font-size: 0.9rem;
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
}

.phase-exercises li i {
  margin-top: 0.15rem;
  flex-shrink: 0;
}

/* ---- Curated Pages Grid ---- */
.curated-pages-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 0.75rem;
  margin-top: 0.75rem;
}

.curated-page-link {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: var(--color-bg-secondary, #f9fafb);
  border-radius: 8px;
  text-decoration: none;
  font-size: 0.875rem;
  color: var(--color-text-primary, #111827);
  border: 1px solid var(--color-bg-tertiary, #e5e7eb);
  transition: all 0.15s ease;
}

.curated-page-link:hover {
  background: var(--color-bg-tertiary, #f1f5f9);
  text-decoration: underline;
}

/* Dark mode */
[data-theme="dark"] .level-pick-btn {
  background: var(--color-bg-tertiary, #1f2937);
  border-color: var(--color-bg-tertiary, #374151);
}

[data-theme="dark"] .level-pick-btn[aria-pressed="true"],
[data-theme="dark"] .level-pick-btn.active {
  background: color-mix(in srgb, var(--level-color) 20%, #1f2937);
}

[data-theme="dark"] .level-banner,
[data-theme="dark"] .skill-area-card,
[data-theme="dark"] .phase-header,
[data-theme="dark"] .curated-page-link {
  background: var(--color-bg-tertiary, #1f2937);
  border-color: var(--color-bg-tertiary, #374151);
}
</style>

<script>
(function () {
  const STORAGE_KEY = 'target_job_level';

  function applyLevel(levelId) {
    // Update buttons
    document.querySelectorAll('.level-pick-btn').forEach(function (btn) {
      const active = btn.dataset.level === levelId;
      btn.setAttribute('aria-pressed', active ? 'true' : 'false');
      btn.classList.toggle('active', active);
    });

    // Show/hide plans
    document.querySelectorAll('.level-plan').forEach(function (plan) {
      plan.style.display = plan.dataset.level === levelId ? 'block' : 'none';
    });

    // Hide no-level message
    const msg = document.getElementById('no-level-msg');
    if (msg) msg.style.display = levelId ? 'none' : 'block';

    // Persist
    if (levelId) {
      localStorage.setItem(STORAGE_KEY, levelId);
    }

    // Update global indicator in header (if present)
    const headerBadge = document.getElementById('header-level-badge');
    if (headerBadge) {
      headerBadge.textContent = levelId ? levelId.toUpperCase() : '—';
    }
    const headerSelect = document.getElementById('header-level-select');
    if (headerSelect) {
      headerSelect.value = levelId || '';
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    // Wire picker buttons
    document.querySelectorAll('.level-pick-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        applyLevel(this.dataset.level);
      });
    });

    // Restore saved level
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
      applyLevel(saved);
    } else {
      document.getElementById('no-level-msg').style.display = 'block';
    }
  });
})();
</script>

<div class="navigation-buttons">
  <a href="{{ '/tracks/' | relative_url }}">← Learning Tracks</a>
  <a href="{{ '/skills/' | relative_url }}">Skills Matrix →</a>
</div>

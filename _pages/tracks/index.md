---
layout: page
title: "Learning Tracks"
permalink: /tracks/
nav_order: 1
parent: "Learning Paths"
difficulty: "Beginner"
estimated_time: "10 mins"
tags: [Learning Paths, Tracks, Planning]
track: "Reference"
---

# Learning Tracks

Choose your path to mastery. Each track is designed for specific goals and experience levels, guiding you through curated content to achieve your objectives.

<div class="tracks-grid">
  {% for track in site.data.tracks %}
  <div class="track-card">
    <div class="track-header">
      <div class="track-icon">
        <i class="{{ track.icon }}"></i>
      </div>
      <div class="track-meta">
        <span class="track-duration">{{ track.duration }}</span>
        <span class="track-difficulty {{ track.difficulty | downcase }}">{{ track.difficulty }}</span>
      </div>
    </div>

    <h3>{{ track.name }}</h3>
    <p class="track-description">{{ track.description }}</p>

    <div class="track-audience">
      <strong>Perfect for:</strong> {{ track.target_audience }}
    </div>

    <div class="track-content">
      <h4>Content Overview ({{ track.pages | size }} modules)</h4>
      <ul class="track-modules">
        {% for page_url in track.pages %}
          {% assign page = site.pages | where: "url", page_url | first %}
          {% if page %}
          <li>
            <a href="{{ page.url | relative_url }}">
              {{ page.title }}
              {% if page.difficulty %}
              <span class="module-difficulty {{ page.difficulty | downcase }}">{{ page.difficulty }}</span>
              {% endif %}
              {% if page.estimated_time %}
              <span class="module-time">{{ page.estimated_time }}</span>
              {% endif %}
            </a>
          </li>
          {% endif %}
        {% endfor %}
      </ul>
    </div>

    <div class="track-actions">
      <a href="#track-{{ forloop.index }}" class="btn btn-primary track-start-btn">
        <i class="fas fa-play"></i> Start Track
      </a>
      <button class="btn btn-secondary track-progress-btn" data-track="{{ track.name | slugify }}">
        <i class="fas fa-chart-line"></i> Track Progress
      </button>
    </div>
  </div>
  {% endfor %}
</div>

<div class="tracks-info">
  <div class="info-card">
    <h3><i class="fas fa-question-circle"></i> How Learning Tracks Work</h3>
    <ul>
      <li><strong>Structured Learning:</strong> Follow a curated sequence of content designed for your goals</li>
      <li><strong>Progress Tracking:</strong> Mark modules as complete and track your advancement</li>
      <li><strong>Flexible Pace:</strong> Learn at your own speed with self-paced tracks</li>
      <li><strong>Skill Building:</strong> Each track builds specific competencies for your career</li>
    </ul>
  </div>

  <div class="info-card">
    <h3><i class="fas fa-lightbulb"></i> Tips for Success</h3>
    <ul>
      <li>Complete modules in order for the best learning experience</li>
      <li>Take notes and practice examples as you go</li>
      <li>Don't rush - understanding is more important than speed</li>
      <li>Review completed modules periodically to reinforce learning</li>
    </ul>
  </div>
</div>

<script>
// Simple progress tracking using localStorage
document.addEventListener('DOMContentLoaded', function() {
  const progressButtons = document.querySelectorAll('.track-progress-btn');
  const SITE_BASEURL = "{{ site.baseurl }}";

  function normalizeSitePath(pathname) {
    if (!pathname) return pathname;
    if (SITE_BASEURL && SITE_BASEURL !== '/' && pathname.startsWith(SITE_BASEURL)) {
      const stripped = pathname.slice(SITE_BASEURL.length);
      return stripped.startsWith('/') ? stripped : `/${stripped}`;
    }
    return pathname;
  }

  progressButtons.forEach(button => {
    const trackId = button.getAttribute('data-track');
    const completedModules = (JSON.parse(localStorage.getItem(`track_${trackId}_progress`) || '[]') || []).map(normalizeSitePath);

    // Update button text with progress
    const trackCard = button.closest('.track-card');
    const totalModules = trackCard.querySelectorAll('.track-modules li').length;
    const completedCount = completedModules.length;

    if (completedCount > 0) {
      button.innerHTML = `<i class="fas fa-chart-line"></i> ${completedCount}/${totalModules} Complete`;
      button.classList.add('has-progress');
    }

    button.addEventListener('click', function() {
      showProgressModal(trackId, trackCard);
    });
  });

  function showProgressModal(trackId, trackCard) {
    const modules = trackCard.querySelectorAll('.track-modules li a');
    const completedModules = (JSON.parse(localStorage.getItem(`track_${trackId}_progress`) || '[]') || []).map(normalizeSitePath);

    let modalContent = '<div class="progress-modal">';
    modalContent += '<h3>Track Progress</h3>';
    modalContent += '<div class="progress-modules">';

    modules.forEach((moduleLink, index) => {
      const moduleUrl = normalizeSitePath(moduleLink.getAttribute('href'));
      const isCompleted = completedModules.includes(moduleUrl);
      const checkboxId = `module_${index}`;

      modalContent += `
        <label class="progress-item ${isCompleted ? 'completed' : ''}" for="${checkboxId}">
          <input type="checkbox" id="${checkboxId}" ${isCompleted ? 'checked' : ''} data-url="${moduleUrl}">
          <span class="checkmark"></span>
          ${moduleLink.innerHTML}
        </label>
      `;
    });

    modalContent += '</div>';
    modalContent += '<button class="btn btn-primary" onclick="closeProgressModal()">Close</button>';
    modalContent += '</div>';

    // Create modal overlay
    const modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = modalContent;
    document.body.appendChild(modal);

    // Add event listeners to checkboxes
    modal.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
      checkbox.addEventListener('change', function() {
        const moduleUrl = normalizeSitePath(this.getAttribute('data-url'));
        let completedModules = JSON.parse(localStorage.getItem(`track_${trackId}_progress`) || '[]');

        if (this.checked) {
          if (!completedModules.includes(moduleUrl)) {
            completedModules.push(moduleUrl);
          }
          this.closest('.progress-item').classList.add('completed');
        } else {
          completedModules = completedModules.filter(url => url !== moduleUrl);
          this.closest('.progress-item').classList.remove('completed');
        }

        localStorage.setItem(`track_${trackId}_progress`, JSON.stringify(completedModules));

        // Update progress button
        const progressBtn = trackCard.querySelector('.track-progress-btn');
        const totalModules = modules.length;
        const completedCount = completedModules.length;

        if (completedCount > 0) {
          progressBtn.innerHTML = `<i class="fas fa-chart-line"></i> ${completedCount}/${totalModules} Complete`;
          progressBtn.classList.add('has-progress');
        } else {
          progressBtn.innerHTML = `<i class="fas fa-chart-line"></i> Track Progress`;
          progressBtn.classList.remove('has-progress');
        }
      });
    });
  }
});

// Global function for closing modal
function closeProgressModal() {
  const modal = document.querySelector('.modal-overlay');
  if (modal) {
    modal.remove();
  }
}
</script>
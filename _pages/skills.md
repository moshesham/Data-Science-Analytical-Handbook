---
layout: page
title: "Skills Matrix"
permalink: /skills/
nav_order: 2
parent: "Learning Paths"
difficulty: "Beginner"
estimated_time: "10 mins"
tags: [Skills, Navigation, Reference]
track: "Reference"
---

# Skills Matrix

Explore content organized by specific skills and topics. Click on any skill to see all related materials, from beginner introductions to advanced techniques.

{% assign all_tags = "" %}
{% for page in site.pages %}
  {% if page.tags %}
    {% for tag in page.tags %}
      {% assign all_tags = all_tags | append: tag | append: "," %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% assign unique_tags = all_tags | split: "," | uniq | sort %}
{% assign filtered_tags = unique_tags | where_exp: "tag", "tag != ''" %}

<div class="skills-overview">
  <div class="skills-stats">
    <div class="stat-card">
      <div class="stat-number">{{ filtered_tags | size }}</div>
      <div class="stat-label">Total Skills Tagged</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">{{ site.pages | size }}</div>
      <div class="stat-label">Content Modules</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">3</div>
      <div class="stat-label">Difficulty Levels</div>
    </div>
  </div>
</div>

<div class="skills-cloud">
  <h3>Skills Cloud</h3>
  <div class="tags-container">
    {% for tag in unique_tags %}
      {% if tag != "" %}
        {% assign tag_pages = site.pages | where_exp: "page", "page.tags contains tag" %}
        {% assign tag_count = tag_pages | size %}
        <a href="#skill-{{ tag | slugify }}" class="skill-tag" data-count="{{ tag_count }}">
          {{ tag }}
          <span class="tag-count">{{ tag_count }}</span>
        </a>
      {% endif %}
    {% endfor %}
  </div>
</div>

<div class="skills-content">
  {% for tag in unique_tags %}
    {% if tag != "" %}
      {% assign tag_pages = site.pages | where_exp: "page", "page.tags contains tag" %}
      {% assign beginner_pages = tag_pages | where: "difficulty", "Beginner" %}
      {% assign intermediate_pages = tag_pages | where: "difficulty", "Intermediate" %}
      {% assign advanced_pages = tag_pages | where: "difficulty", "Advanced" %}

      <div id="skill-{{ tag | slugify }}" class="skill-section">
        <h3>
          <i class="fas fa-tag"></i>
          {{ tag }}
          <span class="skill-count">({{ tag_pages | size }} modules)</span>
        </h3>

        <div class="skill-difficulty-tabs">
          {% if beginner_pages.size > 0 %}
          <button class="tab-btn active" data-difficulty="beginner">
            Beginner ({{ beginner_pages | size }})
          </button>
          {% endif %}
          {% if intermediate_pages.size > 0 %}
          <button class="tab-btn" data-difficulty="intermediate">
            Intermediate ({{ intermediate_pages | size }})
          </button>
          {% endif %}
          {% if advanced_pages.size > 0 %}
          <button class="tab-btn" data-difficulty="advanced">
            Advanced ({{ advanced_pages | size }})
          </button>
          {% endif %}
        </div>

        <div class="skill-content-tabs">
          {% if beginner_pages.size > 0 %}
          <div class="tab-content active" data-difficulty="beginner">
            <div class="skill-modules">
              {% for page in beginner_pages %}
              <div class="skill-module-card">
                <div class="module-header">
                  <h4><a href="{{ page.url | relative_url }}">{{ page.title }}</a></h4>
                  <span class="module-time">{{ page.estimated_time | default: "15 mins" }}</span>
                </div>
                <p>{{ page.excerpt | strip_html | truncate: 120 }}</p>
                <div class="module-meta">
                  {% if page.track %}
                  <span class="module-track">{{ page.track }}</span>
                  {% endif %}
                  <button class="mark-complete-btn" data-url="{{ page.url }}">
                    <i class="fas fa-check"></i> Mark Complete
                  </button>
                </div>
              </div>
              {% endfor %}
            </div>
          </div>
          {% endif %}

          {% if intermediate_pages.size > 0 %}
          <div class="tab-content" data-difficulty="intermediate">
            <div class="skill-modules">
              {% for page in intermediate_pages %}
              <div class="skill-module-card">
                <div class="module-header">
                  <h4><a href="{{ page.url | relative_url }}">{{ page.title }}</a></h4>
                  <span class="module-time">{{ page.estimated_time | default: "30 mins" }}</span>
                </div>
                <p>{{ page.excerpt | strip_html | truncate: 120 }}</p>
                <div class="module-meta">
                  {% if page.track %}
                  <span class="module-track">{{ page.track }}</span>
                  {% endif %}
                  <button class="mark-complete-btn" data-url="{{ page.url }}">
                    <i class="fas fa-check"></i> Mark Complete
                  </button>
                </div>
              </div>
              {% endfor %}
            </div>
          </div>
          {% endif %}

          {% if advanced_pages.size > 0 %}
          <div class="tab-content" data-difficulty="advanced">
            <div class="skill-modules">
              {% for page in advanced_pages %}
              <div class="skill-module-card">
                <div class="module-header">
                  <h4><a href="{{ page.url | relative_url }}">{{ page.title }}</a></h4>
                  <span class="module-time">{{ page.estimated_time | default: "45 mins" }}</span>
                </div>
                <p>{{ page.excerpt | strip_html | truncate: 120 }}</p>
                <div class="module-meta">
                  {% if page.track %}
                  <span class="module-track">{{ page.track }}</span>
                  {% endif %}
                  <button class="mark-complete-btn" data-url="{{ page.url }}">
                    <i class="fas fa-check"></i> Mark Complete
                  </button>
                </div>
              </div>
              {% endfor %}
            </div>
          </div>
          {% endif %}
        </div>
      </div>
    {% endif %}
  {% endfor %}
</div>

<script>
// Tab switching functionality
document.addEventListener('DOMContentLoaded', function() {
  const tabButtons = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabButtons.forEach(button => {
    button.addEventListener('click', function() {
      const difficulty = this.getAttribute('data-difficulty');
      const skillSection = this.closest('.skill-section');

      // Remove active class from all tabs in this section
      skillSection.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      skillSection.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));

      // Add active class to clicked tab and corresponding content
      this.classList.add('active');
      skillSection.querySelector(`.tab-content[data-difficulty="${difficulty}"]`).classList.add('active');
    });
  });

  // Mark complete functionality
  const completeButtons = document.querySelectorAll('.mark-complete-btn');

  completeButtons.forEach(button => {
    const pageUrl = button.getAttribute('data-url');
    const completedPages = JSON.parse(localStorage.getItem('completed_pages') || '[]');

    if (completedPages.includes(pageUrl)) {
      button.classList.add('completed');
      button.innerHTML = '<i class="fas fa-check-circle"></i> Completed';
    }

    button.addEventListener('click', function() {
      const completedPages = JSON.parse(localStorage.getItem('completed_pages') || '[]');

      if (completedPages.includes(pageUrl)) {
        // Unmark as complete
        const index = completedPages.indexOf(pageUrl);
        completedPages.splice(index, 1);
        this.classList.remove('completed');
        this.innerHTML = '<i class="fas fa-check"></i> Mark Complete';
      } else {
        // Mark as complete
        completedPages.push(pageUrl);
        this.classList.add('completed');
        this.innerHTML = '<i class="fas fa-check-circle"></i> Completed';
      }

      localStorage.setItem('completed_pages', JSON.stringify(completedPages));
    });
  });

  // Smooth scroll to skill sections when clicking tags
  const skillTags = document.querySelectorAll('.skill-tag');

  skillTags.forEach(tag => {
    tag.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);

      if (targetElement) {
        targetElement.scrollIntoView({ behavior: 'smooth' });

        // Highlight the target section briefly
        targetElement.classList.add('highlight');
        setTimeout(() => {
          targetElement.classList.remove('highlight');
        }, 2000);
      }
    });
  });
});
</script>
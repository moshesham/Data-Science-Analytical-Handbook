# Integration Examples for Omniscient Architect

This document provides examples of integrating the Omniscient Architect tool into various workflows.

## Table of Contents

1. [GitHub Actions CI/CD](#github-actions-cicd)
2. [Pre-commit Hook](#pre-commit-hook)
3. [Python Script Integration](#python-script-integration)
4. [Automated Reporting](#automated-reporting)
5. [VS Code Task](#vs-code-task)

---

## GitHub Actions CI/CD

Create `.github/workflows/code-review.yml`:

```yaml
name: Automated Code Review

on:
  pull_request:
    branches: [ main, develop ]
  push:
    branches: [ main ]

jobs:
  code-review:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Run Omniscient Architect
      run: |
        python omniscient_architect.py . \
          --objective "Build production-ready application" \
          --output code-review-report.md
    
    - name: Upload Review Report
      uses: actions/upload-artifact@v3
      with:
        name: code-review-report
        path: code-review-report.md
    
    - name: Comment PR with Report Summary
      if: github.event_name == 'pull_request'
      uses: actions/github-script@v6
      with:
        script: |
          const fs = require('fs');
          const report = fs.readFileSync('code-review-report.md', 'utf8');
          const summary = report.split('\n').slice(0, 30).join('\n');
          
          github.rest.issues.createComment({
            issue_number: context.issue.number,
            owner: context.repo.owner,
            repo: context.repo.repo,
            body: '## 🧠 Automated Code Review\n\n' + summary + '\n\n*See artifacts for full report*'
          });
```

---

## Pre-commit Hook

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Pre-commit hook to run Omniscient Architect

echo "🧠 Running Omniscient Architect analysis..."

# Run the analyzer
python omniscient_architect.py . \
  --objective "Maintain code quality standards" \
  --output /tmp/pre-commit-review.md

# Extract alignment score
SCORE=$(grep "Goal Alignment Score:" /tmp/pre-commit-review.md | grep -oE '[0-9]+')

echo "Alignment Score: $SCORE%"

# Fail if score is below threshold
if [ "$SCORE" -lt 60 ]; then
  echo "❌ Code quality below threshold (60%). Review report at /tmp/pre-commit-review.md"
  echo ""
  echo "Critical issues found. Please address them before committing."
  cat /tmp/pre-commit-review.md | grep -A 10 "Critical Review"
  exit 1
fi

echo "✅ Code quality check passed!"
exit 0
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

---

## Python Script Integration

Use the tool programmatically in your Python scripts:

```python
#!/usr/bin/env python3
"""
Example: Use Omniscient Architect in your Python automation
"""

import subprocess
import json
import re
from pathlib import Path

def analyze_codebase(repo_path: str, objective: str = "") -> dict:
    """
    Run Omniscient Architect and parse results
    
    Args:
        repo_path: Path to repository
        objective: Project objective
    
    Returns:
        dict with analysis results
    """
    # Run the analyzer
    cmd = [
        'python', 'omniscient_architect.py',
        repo_path,
        '--output', '/tmp/analysis.md'
    ]
    
    if objective:
        cmd.extend(['--objective', objective])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Read the output
    with open('/tmp/analysis.md', 'r') as f:
        report = f.read()
    
    # Parse key metrics
    score_match = re.search(r'Goal Alignment Score: (\d+)%', report)
    score = int(score_match.group(1)) if score_match else 0
    
    strengths = len(re.findall(r'\*\*Strength:\*\*', report))
    weaknesses = len(re.findall(r'\*\*Issue:\*\*', report))
    
    return {
        'score': score,
        'strengths_count': strengths,
        'weaknesses_count': weaknesses,
        'report_path': '/tmp/analysis.md'
    }

def main():
    # Analyze multiple projects
    projects = [
        ('project-a', 'Build REST API'),
        ('project-b', 'Create data pipeline'),
        ('project-c', 'Develop ML model'),
    ]
    
    results = []
    for project_path, objective in projects:
        print(f"Analyzing {project_path}...")
        analysis = analyze_codebase(project_path, objective)
        results.append({
            'project': project_path,
            'score': analysis['score'],
            'strengths': analysis['strengths_count'],
            'weaknesses': analysis['weaknesses_count']
        })
    
    # Generate comparison report
    print("\n" + "=" * 60)
    print("COMPARATIVE ANALYSIS")
    print("=" * 60)
    
    for result in sorted(results, key=lambda x: x['score'], reverse=True):
        print(f"{result['project']:15} | Score: {result['score']:3}% | "
              f"Strengths: {result['strengths']} | Weaknesses: {result['weaknesses']}")

if __name__ == '__main__':
    main()
```

---

## Automated Reporting

Generate weekly code quality reports:

```python
#!/usr/bin/env python3
"""
Weekly Code Quality Report Generator
"""

import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def generate_weekly_report():
    """Generate and email weekly code review report"""
    
    # Run analysis
    subprocess.run([
        'python', 'omniscient_architect.py',
        '.',
        '--objective', 'Maintain production-ready codebase',
        '--output', 'weekly-report.md'
    ])
    
    # Read report
    with open('weekly-report.md', 'r') as f:
        report_content = f.read()
    
    # Create email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'Weekly Code Review - {datetime.now().strftime("%Y-%m-%d")}'
    msg['From'] = 'codereviewer@yourcompany.com'
    msg['To'] = 'team@yourcompany.com'
    
    # Email body
    html = f"""
    <html>
      <body>
        <h2>📊 Weekly Code Quality Report</h2>
        <p>Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <pre>{report_content}</pre>
      </body>
    </html>
    """
    
    msg.attach(MIMEText(html, 'html'))
    
    # Send email (configure your SMTP server)
    # smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # smtp.starttls()
    # smtp.login('your-email@gmail.com', 'your-password')
    # smtp.send_message(msg)
    # smtp.quit()
    
    print("Weekly report generated!")

if __name__ == '__main__':
    generate_weekly_report()
```

---

## VS Code Task

Create `.vscode/tasks.json`:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Code Review - Quick Analysis",
            "type": "shell",
            "command": "python",
            "args": [
                "omniscient_architect.py",
                ".",
                "--objective",
                "Quick quality check"
            ],
            "group": "test",
            "presentation": {
                "reveal": "always",
                "panel": "new"
            }
        },
        {
            "label": "Code Review - Full Report",
            "type": "shell",
            "command": "python",
            "args": [
                "omniscient_architect.py",
                ".",
                "--objective",
                "Comprehensive analysis for ${input:projectObjective}",
                "--output",
                "code-review-${input:reportDate}.md"
            ],
            "group": "test",
            "presentation": {
                "reveal": "always",
                "panel": "new"
            }
        },
        {
            "label": "Code Review - Pre-Release",
            "type": "shell",
            "command": "python",
            "args": [
                "omniscient_architect.py",
                ".",
                "--objective",
                "Prepare for production release",
                "--output",
                "pre-release-review.md"
            ],
            "group": "test",
            "presentation": {
                "reveal": "always",
                "panel": "new"
            },
            "problemMatcher": []
        }
    ],
    "inputs": [
        {
            "id": "projectObjective",
            "type": "promptString",
            "description": "What is your project's main objective?",
            "default": "Build production-ready application"
        },
        {
            "id": "reportDate",
            "type": "promptString",
            "description": "Report date (YYYYMMDD)",
            "default": "${date:yyyyMMdd}"
        }
    ]
}
```

Access via: `Terminal > Run Task > Code Review - [option]`

---

## Advanced: Score Tracking

Track alignment scores over time:

```python
#!/usr/bin/env python3
"""
Track code quality scores over time
"""

import subprocess
import re
import json
from datetime import datetime
from pathlib import Path

HISTORY_FILE = 'quality-history.json'

def get_current_score():
    """Get current alignment score"""
    subprocess.run([
        'python', 'omniscient_architect.py',
        '.',
        '--output', '/tmp/score-check.md'
    ])
    
    with open('/tmp/score-check.md', 'r') as f:
        content = f.read()
    
    match = re.search(r'Goal Alignment Score: (\d+)%', content)
    return int(match.group(1)) if match else 0

def update_history(score):
    """Update score history"""
    history = []
    
    if Path(HISTORY_FILE).exists():
        with open(HISTORY_FILE, 'r') as f:
            history = json.load(f)
    
    history.append({
        'date': datetime.now().isoformat(),
        'score': score
    })
    
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def print_trend():
    """Print score trend"""
    if not Path(HISTORY_FILE).exists():
        print("No history available")
        return
    
    with open(HISTORY_FILE, 'r') as f:
        history = json.load(f)
    
    print("\n📈 Code Quality Trend:")
    print("-" * 50)
    
    for entry in history[-10:]:  # Last 10 entries
        date = datetime.fromisoformat(entry['date']).strftime('%Y-%m-%d')
        score = entry['score']
        bar = '█' * (score // 5)
        print(f"{date}: {score:3}% {bar}")

def main():
    score = get_current_score()
    update_history(score)
    print_trend()
    
    print(f"\n✅ Current Score: {score}%")

if __name__ == '__main__':
    main()
```

---

## Best Practices

### Continuous Integration
- Run on every PR
- Set minimum score thresholds
- Track trends over time

### Development Workflow
- Use pre-commit hooks for quick checks
- Generate reports before releases
- Include in code review process

### Team Collaboration
- Share reports in team meetings
- Set team quality goals
- Track improvement metrics

---

## Troubleshooting

### Issue: Script not found
**Solution:** Use absolute path or add to PATH
```bash
export PATH=$PATH:/path/to/omniscient_architect
```

### Issue: Permissions denied
**Solution:** Make script executable
```bash
chmod +x omniscient_architect.py
```

### Issue: Python version mismatch
**Solution:** Specify Python version
```bash
python3.9 omniscient_architect.py .
```

---

For more examples, see the main documentation: `OMNISCIENT_ARCHITECT_README.md`

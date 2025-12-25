# Contributing to Data Science Analytical Handbook

Thank you for your interest in contributing to the Data Science Analytical Handbook! This guide will help you get started.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Project Structure](#project-structure)
- [Style Guidelines](#style-guidelines)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## How Can I Contribute?

### Reporting Issues

- Check existing issues to avoid duplicates
- Use a clear and descriptive title
- Provide as much detail as possible

### Suggesting Enhancements

- Open an issue describing the enhancement
- Explain why this enhancement would be useful
- Include any relevant examples or resources

### Contributing Content

- Fix typos or improve clarity
- Add new practice problems or examples
- Update outdated information
- Improve documentation

## Project Structure

```
Data-Science-Analytical-Handbook/
├── _pages/                    # Jekyll pages for GitHub Pages site
│   ├── foundational_knowledge/  # Statistics, SQL, Python content
│   └── interview_preparation/   # Interview guides
├── supplementary/             # Additional study materials
│   ├── sql-example-problems.md
│   ├── statistics-probability-example-questions.md
│   └── ...
├── Best-Practices/            # Data engineering best practices
│   └── Deep_Dive/
├── Analytical-HandsOn-Projects/  # Hands-on projects
├── Simulations/               # Interactive notebooks
├── assets/                    # CSS and images
└── streamlit_app/             # Streamlit application
```

## Style Guidelines

### File Naming

- Use lowercase for markdown files: `my-document.md`
- Use underscores for multi-word names: `data_acquisition.md`
- Use `.md` extension (not `.MD`)

### Markdown Formatting

- Use headers hierarchically (# > ## > ###)
- Add a blank line before and after headers
- Use code fences with language specifiers:

  ```python
  # Example Python code
  import pandas as pd
  ```

- Use tables for structured information
- Include links to external resources where helpful

### Code Examples

- Ensure code is correct and tested
- Add comments to explain complex logic
- Follow language-specific style guides (PEP 8 for Python)

## Submitting Changes

1. **Fork the repository**
2. **Create a branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**
4. **Test locally** (run Jekyll if making website changes)
5. **Commit**: Use clear, descriptive commit messages
6. **Push**: `git push origin feature/your-feature-name`
7. **Open a Pull Request**: Describe your changes clearly

### Commit Message Format

```
type: brief description

Longer explanation if needed.
```

Types: `fix`, `feat`, `docs`, `style`, `refactor`, `test`

## Local Development

### Jekyll (for GitHub Pages)

```bash
# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve
```

### Python Notebooks

```bash
# Install requirements
pip install -r requirements-notebooks.txt

# Run Jupyter
jupyter notebook
```

## Questions?

Open an issue or reach out to the maintainers. We're happy to help!

---

Thank you for contributing! 🎉

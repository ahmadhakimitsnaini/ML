# Troubleshooting Guide

This guide helps you solve common problems when working with the Machine Learning for Beginners curriculum. If you don't find a solution here, please check our [Discord Discussions](https://aka.ms/foundry/discord) or [open an issue](https://github.com/microsoft/ML-For-Beginners/issues)


## Table of Contents

- [Installation Issues](#installation-issues)
- [Jupyter Notebook Issues](#jupyter-notebook-issues)
- [Python Package Issues](#python-package-issues)
- [R Environment Issues](#r-environment-issues)
- [Quiz Application Issues](#quiz-application-issues)
- [Data and File Path Issues](#data-and-file-path-issues)
- [Common Error Messages](#common-error-messages)
- [Performance Issues](#performance-issues)
- [Environment and Configuration](#environment-and-configuration)

---

## Installation Issues

### Python Installation

**Problem**: `python: command not found`

**Solution**:
1. Install Python 3.8 or higher from [python.org](https://www.python.org/downloads/)
2. Verify installation: `python --version` or `python3 --version`
3. On macOS/Linux, you may need to use `python3` instead of `python`

**Problem**: Multiple Python versions causing conflicts

**Solution**:
```bash
# Use virtual environments to isolate projects
python -m venv ml-env

# Activate virtual environment
# On Windows:
ml-env\Scripts\activate
# On macOS/Linux:
source ml-env/bin/activate
```

### Jupyter Installation

**Problem**: `jupyter: command not found`

**Solution**:
```bash
# Install Jupyter
pip install jupyter

# Or with pip3
pip3 install jupyter

# Verify installation
jupyter --version
```
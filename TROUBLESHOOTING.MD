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

**Problem**: Jupyter won't launch in browser

**Solution**:
```bash
# Try specifying the browser
jupyter notebook --browser=chrome

# Or copy the URL with token from terminal and paste in browser manually
# Look for: http://localhost:8888/?token=...
```

### R Installation

**Problem**: R packages won't install

**Solution**:
```r
# Ensure you have the latest R version
# Install packages with dependencies
install.packages(c("tidyverse", "tidymodels", "caret"), dependencies = TRUE)

# If compilation fails, try installing binary versions
install.packages("package-name", type = "binary")
```

**Problem**: IRkernel not available in Jupyter

**Solution**:
```r
# In R console
install.packages('IRkernel')
IRkernel::installspec(user = TRUE)
```

---

## Jupyter Notebook Issues

### Kernel Issues

**Problem**: Kernel keeps dying or restarting

**Solution**:
1. Restart the kernel: `Kernel → Restart`
2. Clear output and restart: `Kernel → Restart & Clear Output`
3. Check for memory issues (see [Performance Issues](#performance-issues))
4. Try running cells individually to identify problematic code

**Problem**: Wrong Python kernel selected

**Solution**:
1. Check current kernel: `Kernel → Change Kernel`
2. Select the correct Python version
3. If kernel is missing, create it:
```bash
python -m ipykernel install --user --name=ml-env
```


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

**Problem**: Kernel won't start

**Solution**:
```bash
# Reinstall ipykernel
pip uninstall ipykernel
pip install ipykernel

# Register the kernel again
python -m ipykernel install --user
```

### Notebook Cell Issues

**Problem**: Cells are running but not showing output

**Solution**:
1. Check if cell is still running (look for `[*]` indicator)
2. Restart kernel and run all cells: `Kernel → Restart & Run All`
3. Check browser console for JavaScript errors (F12)

**Problem**: Can't run cells - no response when clicking "Run"

**Solution**:
1. Check if Jupyter server is still running in terminal
2. Refresh the browser page
3. Close and reopen the notebook
4. Restart Jupyter server

---

## Python Package Issues

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'sklearn'`

**Solution**:
```bash
pip install scikit-learn

# Common ML packages for this course
pip install scikit-learn pandas numpy matplotlib seaborn
```

**Problem**: `ImportError: cannot import name 'X' from 'sklearn'`

**Solution**:
```bash
# Update scikit-learn to latest version
pip install --upgrade scikit-learn

# Check version
python -c "import sklearn; print(sklearn.__version__)"
```

### Version Conflicts

**Problem**: Package version incompatibility errors

**Solution**:
```bash
# Create a new virtual environment
python -m venv fresh-env
source fresh-env/bin/activate  # or fresh-env\Scripts\activate on Windows

# Install packages fresh
pip install jupyter scikit-learn pandas numpy matplotlib seaborn

# If specific version needed
pip install scikit-learn==1.3.0
```

**Problem**: `pip install` fails with permission errors

**Solution**:
```bash
# Install for current user only
pip install --user package-name

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install package-name
```

### Data Loading Issues

**Problem**: `FileNotFoundError` when loading CSV files

**Solution**:
```python
import os
# Check current working directory
print(os.getcwd())

# Use relative paths from notebook location
df = pd.read_csv('../../data/filename.csv')

# Or use absolute paths
df = pd.read_csv('/full/path/to/data/filename.csv')
```

---


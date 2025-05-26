# Data Science Dev Container for VS Code (GCP + Spark)

![Version](https://img.shields.io/badge/Version-1.5-blue)
![Updated](https://img.shields.io/badge/Updated-May%202025-green)
![Python](https://img.shields.io/badge/Python-3.11-yellow)
![Spark](https://img.shields.io/badge/Spark-3.5.3-orange)

A comprehensive VS Code development container for data science and analytics projects utilizing Apache Spark and Google BigQuery. This environment provides a consistent, reproducible workspace with all the necessary dependencies pre-configured.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Prerequisites](#system-prerequisites)
- [Getting Started](#getting-started)
  - [Setting up the Dev Container](#setting-up-the-dev-container)
  - [Verifying Your Setup](#verifying-your-setup)
  - [GCP Authentication](#gcp-authentication)
  - [GitLab Integration](#gitlab-integration)
- [Included Libraries](#included-libraries)
- [Interactive Notebooks](#interactive-notebooks)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

## 🔍 Overview

This VS Code Dev Container provides a pre-configured environment for developing PySpark applications that interact with Google BigQuery. It eliminates the "works on my machine" problem by ensuring all developers use identical environments with consistent versions of Python, Spark, and related libraries.

The container is optimized for data engineering and data science workflows that require:
- Processing large datasets with Apache Spark
- Querying and analyzing data in Google BigQuery
- Developing reproducible, production-ready code

## ✨ Features

- **Apache Spark 3.5.3** pre-installed and configured
- **Python 3.11** with essential data science libraries
- **Google Cloud SDK** for BigQuery authentication and access
- **VS Code integration** with recommended extensions for Python and Spark development
- **Interactive Jupyter Notebooks** for exploring data and documenting workflows
- **Isolated development** environment with all dependencies pre-configured
- **Spark UI** access via port forwarding (port 4040)
- **Non-root user** configuration for better security
- **Seamless file sharing** with host machine

## 🖥️ System Prerequisites

Before using this Dev Container, ensure you have:

- **Docker Desktop** (Windows/Mac) or Docker Engine (Linux)
- **Visual Studio Code** with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed
- **Git** for version control
- **Google Cloud Platform** account with BigQuery access
- At least **8GB RAM** allocated to Docker
- At least **10GB** of free disk space

## 🚀 Getting Started

### Setting up the Dev Container

1. **Clone the repository**:
   ```bash
   git clone https://your-repo-url/pyspark-dev-container.git
   cd pyspark-dev-container
   ```

2. **Open in VS Code**:
   ```bash
   code .
   ```

3. **Start the Dev Container**:
   - When prompted, select "Reopen in Container"
   - Or press `F1`, type "Remote-Containers: Reopen in Container"
   - The first build may take several minutes as it downloads and configures all dependencies

4. **Verify installation**:
   ```bash
   python -c "import pyspark; print(f'PySpark {pyspark.__version__} is installed')"
   ```

### Verifying Your Setup

This repository includes two interactive notebooks that help you verify your environment is correctly configured:

1. **Basic BigQuery Authentication** (`base_test_bq.ipynb`):
   - Verifies your GCP authentication is working
   - Lists available BigQuery datasets in your project
   - Runs a simple query to confirm connection

2. **Spark-BigQuery Integration** (`base_test_bq_spark.ipynb`):
   - Tests PySpark connectivity with BigQuery
   - Demonstrates reading from public datasets
   - Shows how to execute queries through Spark
   - Includes proper configuration for the BigQuery connector

Simply open either notebook and run the cells to verify your setup is working correctly.

### GCP Authentication

To authenticate with Google BigQuery:

1. **Run the authentication command**:
   ```bash
   gcloud auth login
   ```

2. **Set application default credentials**:
   ```bash
   gcloud auth application-default login
   ```

3. **Set your project**:
   ```bash
   gcloud config set project YOUR_PROJECT_ID
   ```

4. **Verify authentication**:
   Open and run the `base_test_bq.ipynb` notebook to verify your authentication is working correctly. The notebook will display your authenticated account, project, and available BigQuery datasets.

### GitLab Integration

To configure GitLab access:

1. **Generate SSH key pair** (if needed):
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```

2. **Copy the public key**:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

3. **Add the key to GitLab**:
   - Go to GitLab > User Settings > SSH Keys
   - Paste your public key and save

4. **Test GitLab connection**:
   ```bash
   ssh -T git@gitlab.com
   ```

## 📚 Included Libraries

The environment comes with these Python packages pre-installed:

| Library | Description |
|---------|-------------|
| **pyspark** | Python API for Apache Spark distributed computing framework |
| **google-cloud-bigquery** | Google Cloud client library for BigQuery integration |
| **google-cloud-storage** | Google Cloud client library for Cloud Storage access |
| **pandas** | Data manipulation and analysis library with DataFrame support |
| **numpy** | Fundamental package for scientific computing and numerical operations |
| **matplotlib** | Comprehensive library for creating static, animated, and interactive visualizations |
| **seaborn** | Statistical data visualization based on matplotlib with enhanced aesthetics |
| **pyarrow** | Apache Arrow implementation for efficient in-memory columnar data format |
| **delta-spark** | Delta Lake integration for Spark providing ACID transactions on data lakes |
| **jupyter** | Interactive computing environment for creating notebook documents |
| **jupyterlab** | Next-generation web-based user interface for Project Jupyter |
| **scikit-learn** | Machine learning library featuring various classification, regression algorithms |
| **pytest** | Testing framework for writing simple and scalable test cases |
| **black** | Uncompromising Python code formatter for consistent code style |
| **flake8** | Tool for style guide enforcement and linting |
| **isort** | Utility to sort imports alphabetically and automatically separate them |
| **pylint** | Static code analysis tool for finding bugs and quality problems |

Additional packages can be installed using `pip`:

```bash
pip install package-name
```

## 🔬 Interactive Notebooks

This environment includes two Jupyter notebooks to help you get started:

### `base_test_bq.ipynb`: BigQuery Authentication Test

This notebook helps you verify that your Google Cloud Platform BigQuery authentication is working correctly. It:

- Displays your current authentication information (user and project)
- Lists all available BigQuery datasets in your project
- Executes a simple test query to confirm connection

**Perfect for**: Initial setup verification, troubleshooting authentication issues

### `base_test_bq_spark.ipynb`: PySpark-BigQuery Integration

This more advanced notebook demonstrates the integration between Apache Spark and Google BigQuery. It:

- Creates a SparkSession with the BigQuery connector properly configured
- Tests reading from a public Shakespeare dataset (no authentication required)
- Attempts to read from datasets in your authenticated project
- Shows how to execute queries through Spark with proper materialization settings

**Perfect for**: Data engineers setting up PySpark workflows with BigQuery, understanding connector configuration

Both notebooks include:
- Clear documentation explaining each step
- Customizable variables at the top for easy modification
- Troubleshooting tips for common issues
- Ready-to-use code snippets you can incorporate into your projects

To run these notebooks:
1. Open the notebook in VS Code using the Jupyter extension
2. Modify the configuration variables at the top as needed
3. Execute each cell sequentially using Shift+Enter or the Run button

## ❓ Troubleshooting

### Common Issues

#### BigQuery Authentication Errors

If you encounter authentication issues in the notebooks:

1. **Check your authentication status**:
   ```bash
   gcloud auth list
   gcloud config list
   ```

2. **Refresh your credentials**:
   ```bash 
   gcloud auth login
   gcloud auth application-default login
   ```

3. **Set your project explicitly** in the notebook:
   ```python
   from google.cloud import bigquery
   client = bigquery.Client(project="your-project-id")
   ```

#### Spark-BigQuery Connection Issues

If the `base_test_bq_spark.ipynb` notebook fails with materialization errors:

```python
# Use materializationDataset instead of dataset
query_result = (
    spark.read.format("bigquery")
    .option("viewsEnabled", "true")
    .option("query", "SELECT 'Success!' as message, CURRENT_TIMESTAMP() as timestamp")
    .option("materializationDataset", dataset_id)  # Use this instead of dataset
    .load()
)
```

#### Container Resource Issues

If the container is sluggish or crashes:
- Increase Docker memory allocation (recommend: 4GB minimum)
- Increase Docker CPU allocation (recommend: 2 CPUs minimum)

## 👤 Credits

- **Author**: Greg McLaughlin
- **Version**: 1.5
- **Date**: May 26, 2025

---

**Happy coding!** 🎉
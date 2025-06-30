# Data Science Dev Container for VS Code (GCP + Spark)

![Version](https://img.shields.io/badge/Version-1.6-blue)
![Updated](https://img.shields.io/badge/Updated-June%202025-green)
![Python](https://img.shields.io/badge/Python-3.11-yellow)
![Spark](https://img.shields.io/badge/Spark-3.5.3-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A comprehensive VS Code development container for data science and analytics projects utilizing Apache Spark and Google BigQuery. This environment is distributed as a pre-built Docker image to ensure a fast, consistent, and reproducible workspace for all team members, even those behind corporate firewalls.

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [System Prerequisites](#-system-prerequisites)
- [Getting Started](#-getting-started)
- [Verifying Your Setup](#-verifying-your-setup)
- [Authentication](#-authentication)
  - [Google Cloud Platform (GCP)](#google-cloud-platform-gcp)
  - [GitLab / GitHub](#gitlab--github)
- [Included Libraries](#-included-libraries)
- [Troubleshooting](#-troubleshooting)
- [For Maintainers](#-for-maintainers)
- [Credits](#-credits)

## 🔍 Overview

This VS Code Dev Container provides a pre-configured environment for developing PySpark applications that interact with Google BigQuery. It eliminates the "works on my machine" problem by ensuring all developers pull an identical, pre-built environment from Docker Hub with consistent versions of Python, Spark, and related libraries.

The container is optimized for data engineering and data science workflows that require:
- Processing large datasets with Apache Spark
- Querying and analyzing data in Google BigQuery
- Developing reproducible, production-ready code

## ✨ Features

- **Pre-built Image:** Pulls directly from Docker Hub for a fast, firewall-friendly setup.
- **Apache Spark 3.5.3:** Pre-installed and configured to start automatically.
- **Google Cloud SDK:** Ready for BigQuery authentication and access.
- **VS Code Integration:** Comes with recommended extensions for Python and GCP development.
- **Isolated Environment:** All dependencies are self-contained.
- **Spark UI Access:** Key ports (4040, 8080) are forwarded for easy access.
- **Secure by Default:** Runs with a non-root `vscode` user.

## 🖥️ System Prerequisites

Before using this Dev Container, ensure you have:

- **Docker Desktop** (Windows/Mac) or Docker Engine (Linux)
- **Visual Studio Code** with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed
- **Git** for version control
- A **Google Cloud Platform** account with BigQuery access
- At least **8GB RAM** allocated to Docker

## 🚀 Getting Started

This setup uses a pre-built image, so you do not need to build the container locally.

1.  **Clone this Repository:**
    ```bash
    git clone https://github.com/geemac-cdn/data_science_dev.git
        cd pyspark-dev-container
    ```

2.  **Open in VS Code:**
    ```bash
    code .
    ```

3.  **Start the Dev Container:**
    - VS Code will detect the `.devcontainer/devcontainer.json` file and show a notification in the bottom-right corner.
    - Click **"Reopen in Container"**.

VS Code will now pull the `mclg/data-science-container:1.6` image from Docker Hub and start the container. This will be much faster than a local build.

## ✅ Verifying Your Setup

Once the container is running, open a new terminal in VS Code (`Terminal` > `New Terminal`) and run these commands to verify the environment:

1.  **Check the User:**
    ```bash
    whoami
    # Expected output: vscode
    ```

2.  **Check Python and PySpark:**
    ```bash
    python -c "import pyspark; print(f'PySpark Version: {pyspark.__version__}')"
    # Expected output: PySpark Version: 3.5.3
    ```

3.  **Check Google Cloud SDK:**
    ```bash
    gcloud --version
    # Expected output: Google Cloud SDK version information
    ```

4.  **Check Spark Services:**
    ```bash
    jps
    # Expected output: A list of Java processes including 'Master' and 'Worker'
    ```

## 🔐 Authentication

### Google Cloud Platform (GCP)

From the terminal inside your VS Code dev container, run the following commands to authenticate with GCP:

1.  **Log in to your account:**
    ```bash
    gcloud auth application-default login
    ```
    This will provide a URL to open in your browser to complete the login flow.

2.  **Set your project:**
    ```bash
    gcloud config set project YOUR_PROJECT_ID
    ```

### GitLab / GitHub

To configure SSH access for Git:

1.  **Generate an SSH key** inside the container (if you don't have one):
    ```bash
    ssh-keygen -t ed25519 -C "your.email@example.com"
    ```

2.  **Copy the public key** to your clipboard:
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```

3.  **Add the key** to your GitLab or GitHub account under `Settings > SSH and GPG keys`.

## 📚 Included Libraries

The environment comes with these key Python packages pre-installed. See `package_list.txt` for the full list.

| Library                 | Description                                                 |
| ----------------------- | ----------------------------------------------------------- |
| **pyspark**             | Python API for Apache Spark distributed computing           |
| **google-cloud-bigquery** | Google Cloud client library for BigQuery integration        |
| **pandas**              | Data manipulation and analysis library                      |
| **numpy**               | Fundamental package for scientific computing                |
| **matplotlib**          | Comprehensive library for creating visualizations           |
| **scikit-learn**        | Machine learning library with various algorithms            |
| **delta-spark**         | Delta Lake integration for Spark (ACID transactions)        |
| **pytest**              | Testing framework for writing simple and scalable tests     |
| **black**               | Uncompromising Python code formatter                        |
| **flake8**              | Tool for style guide enforcement and linting                |

## ❓ Troubleshooting

-   **Error pulling image:** If Docker fails to pull `mclg/data-science-container:1.6`, check your internet connection and ensure you are logged into Docker Hub (`docker login`). If you are behind a corporate firewall, ensure `hub.docker.com` is allowed.
-   **`jps` command shows no Spark processes:** The `postStartCommand` may have failed. You can try running it manually in the terminal: `bash -c '$SPARK_HOME/sbin/start-master.sh && $SPARK_HOME/sbin/start-worker.sh spark://localhost:7077'`.
-   **Permission Denied in `/workspace`:** This can happen if the `workspaceMount` is not configured correctly. Ensure your `devcontainer.json` includes the `workspaceMount` and `remoteUser: 'vscode'` properties.

## 🔧 For Maintainers

This repository contains the source files to build and publish new versions of the dev container image. The end-user `devcontainer.json` points to a pre-built image on Docker Hub, but maintainers will use the `Dockerfile` to create it.


## 👤 Credits

-   **Author**: Greg McLaughlin
-   **Version**: 1.6
-   **Date**: June 30, 2025

---

**Happy coding!** 🎉

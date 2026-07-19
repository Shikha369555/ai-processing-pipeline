# ⚙️ AI Data Preprocessing Pipeline

An interactive, production-ready Python and Streamlit web application designed to accelerate data engineering and preparation phases for machine learning pipelines. This tool automates raw dataset profiling, flags data integrity issues, and applies real-time transformations to ensure downstream model readiness.

## 🚀 Features

* **Instant Data Ingestion:** Simple drag-and-drop uploading for raw CSV datasets.
* **Automated Data Validation:** Real-time metrics dashboard tracking total missing records and duplicate entries immediately upon upload.
* **Configurable Transformation Pipeline:** Dynamic UI checkboxes allowing users to select and trigger custom cleaning workflows:
  * Drop null/missing values instantly.
  * Eliminate duplicate rows.
  * Standardize and normalize text strings (automatic lowercasing and whitespace stripping).
* **Instant Export:** Download the fully processed, production-ready dataset as a clean CSV with a single click.

## 🛠️ Tech Stack

* **Frontend Framework:** Streamlit (Python-based interactive dashboard)
* **Data Engineering:** Pandas (High-performance data manipulation)
* **Language:** Python 3

## 📁 Repository Structure

```text
ai_preprocessing_pipeline/
├── app.py              # Main Streamlit application file
└── requirements.txt    # Standard Python dependencies

# MoonLight-Energy-Solar-Challenge-Week1

## Introduction

This repository contains the Week 1 challenge for the 10 Academy training program.

As an **Analytics Engineer** at MoonLight Energy Solutions, your role is to analyze environmental measurement data to provide actionable insights for strategic solar investments in **Benin**, **Sierra Leone**, and **Togo**.

This challenge assesses your practical skills in:

- Python Programming
- Git & GitHub workflows
- Exploratory Data Analysis (EDA)
- CI/CD concepts
- Streamlit dashboard creation (to come)

---

## 🚀 Deliverables

- ✅ Data profiling and cleaning for Benin, Sierra Leone, and Togo
- ✅ Outlier detection and handling using Z-score
- ✅ Exploratory Data Analysis (EDA) on irradiance and sensor data
- ✅ Cross-country comparison of solar potential
- ✅ Statistical testing using ANOVA
- ✅ Interactive dashboard built using Streamlit

## Setup Instructions

Follow these steps to set up your local development environment.

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Create and activate a virtual environment

For **Windows**:

```bash
python -m venv .venv
.venv\Scripts\activate
```

For **macOS/Linux**:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install project dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

To run the interactive dashboard:

```bash
streamlit run app.py

##This will launch the dashboard in your browser at http://localhost:8501. ##



## 📁 Project Structure

```

├── .github/ # GitHub Actions workflows
│ └── workflows/
├── .venv/ # Python virtual environment (excluded in .gitignore)
├── data/ # Raw solar datasets
│ ├── benin-malanville.csv
│ ├── sierraleone-bumbuna.csv
│ └── togo-dapaong_qc.csv
│ ├── benin_clean.csv
│ ├── sierraleone_clean.csv
│ └── togo_clean.csv
├── notebooks/ # Jupyter notebooks for EDA and comparison
│ ├── benin_eda.ipynb
│ ├── sierraleone_eda.ipynb
│ ├── togo_eda.ipynb
│ └── compare_countries.ipynb
├── scripts/ # Utility or analysis scripts
│ └── README.md
├── app.py # Streamlit dashboard app
├── .gitignore # Files/folders to ignore in Git
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 📬 License

This repository is part of the **10 Academy Training Program** and is provided for educational and assessment purposes only.

```

```

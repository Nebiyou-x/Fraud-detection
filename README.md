# 🕵️‍♂️ Fraud Detection System

## 📌 Project Overview

This project focuses on building **robust fraud detection pipelines** using two real-world datasets:

1. **E-commerce transaction data**
2. **Credit card transaction data**

Fraud detection is a highly imbalanced classification problem where fraudulent cases are rare but costly. The project emphasizes:

* Careful data preprocessing
* Meaningful feature engineering
* Correct handling of class imbalance
* Reproducibility and testing
* Model explainability

---

## 📂 Datasets

### 1. `Fraud_Data.csv`

E-commerce transactions with user, device, time, and network information.

**Key Columns**

* `user_id` – Unique user identifier
* `signup_time`, `purchase_time` – Timestamps
* `purchase_value` – Transaction amount
* `device_id` – Device identifier
* `source` – Acquisition channel (SEO, Ads, etc.)
* `browser` – Browser type
* `sex`, `age` – User demographics
* `ip_address` – Transaction IP
* `class` – Target (1 = Fraud, 0 = Legitimate)

**Challenge:** Highly imbalanced target variable.

---

### 2. `IpAddress_to_Country.csv`

Maps IP address ranges to countries.

**Columns**

* `lower_bound_ip_address`
* `upper_bound_ip_address`
* `country`

Used to enrich fraud data with **geolocation features**.

---

### 3. `creditcard.csv`

An anonymized credit card transaction dataset.

**Columns**

* `Time` – Seconds since first transaction
* `V1`–`V28` – PCA-transformed features
* `Amount` – Transaction amount
* `Class` – Target (1 = Fraud, 0 = Legitimate)

**Challenge:** Extreme class imbalance (~0.2% fraud).

---

## 🗂 Project Structure

```
fraud-detection/
│
├── data/                    # Ignored by git
│   ├── raw/                 # Original datasets
│   └── processed/           # Cleaned & feature-engineered data
│
├── notebooks/
│   ├── eda-fraud-data.ipynb
│   ├── eda-creditcard.ipynb
│   ├── feature-engineering.ipynb
│   ├── modeling.ipynb
│   ├── shap-explainability.ipynb
│   └── README.md
│
├── src/                     # Reusable source code
│   ├── __init__.py
│   └── preprocessing.py
│
├── tests/                   # Unit tests
│   ├── __init__.py
│   └── test_preprocessing.py
│
├── models/                  # Saved models (ignored by git)
│
├── scripts/                 # Utility scripts
│
├── .github/workflows/
│   └── unittests.yml        # GitHub Actions CI
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Nebiyou-x/fraud-detection.git
cd fraud-detection
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔍 Task 1: Data Analysis & Preprocessing

### ✔ Data Cleaning

* Removed duplicates
* Handled missing values (median for numerical, mode/“Unknown” for categorical)
* Converted timestamps to `datetime`
* Ensured correct data types

---

### ✔ Exploratory Data Analysis (EDA)

* Univariate and bivariate analysis
* Fraud vs non-fraud comparisons
* Temporal fraud patterns
* Class distribution visualization

📓 Implemented in:

* `eda-fraud-data.ipynb`
* `eda-creditcard.ipynb`

---

### ✔ Geolocation Integration

* Converted IP addresses to integers
* Used **range-based merge** to map IPs to countries
* Analyzed fraud rates by country

📌 This step significantly improves fraud signal strength.

---

### ✔ Feature Engineering (Fraud_Data.csv)

* **Time-based features**

  * `hour_of_day`
  * `day_of_week`
  * `is_weekend`
* **Behavioral features**

  * `time_since_signup`
  * Transaction frequency per user
  * Time since last transaction
* **Geographical features**

  * Country of transaction

---

### ✔ Data Transformation

* **StandardScaler** for numerical features
* **One-Hot Encoding** for categorical features
* Ensured transformations are reproducible

---

## ⚖️ Handling Class Imbalance

Fraud detection suffers from **severe class imbalance**.

### Strategy Used

* **Train/Test split first** (to avoid data leakage)
* **SMOTE** applied only to training data
* Test data kept untouched and imbalanced

### Justification

* SMOTE preserves majority class information
* Improves recall for minority (fraud) class
* Suitable for highly imbalanced datasets

📊 Class distributions before and after resampling are documented in notebooks.

---

## 🤖 Modeling (Overview)

* Baseline models: Logistic Regression
* Advanced models: Random Forest, XGBoost
* Metrics used:

  * Precision
  * Recall
  * F1-score
  * ROC-AUC

📓 Implemented in `modeling.ipynb`

---

## 🔍 Model Explainability

* SHAP used for global and local explanations
* Identifies most influential fraud features
* Improves model transparency and trust

📓 Implemented in `shap-explainability.ipynb`

---

## 🧪 Testing & CI

* Unit tests written using **pytest**
* Core preprocessing logic tested
* GitHub Actions automatically runs tests on:

  * Push
  * Pull requests

📁 Config: `.github/workflows/unittests.yml`

---

## 📦 Dependencies

Key libraries:

* pandas, numpy
* scikit-learn
* imbalanced-learn
* xgboost
* shap
* matplotlib, seaborn
* pytest

See `requirements.txt` for full list.

---

## 🚀 Key Takeaways

* Fraud detection requires **domain-specific feature engineering**
* Class imbalance must be handled carefully to avoid misleading results
* Geolocation and behavioral features significantly improve detection
* Explainability is essential for real-world fraud systems

---



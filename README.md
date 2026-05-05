# Customer Intelligence System 🚀

## 📌 Overview

This project is an end-to-end **Customer Intelligence System** that analyzes customer behavior and provides actionable business insights. It combines **machine learning + business logic** to identify customer segments, predict churn risk, and recommend actions.

The goal is to help businesses:

* Understand different types of customers
* Identify customers at risk of leaving
* Take proactive decisions (discounts, upsell, engagement)

---

## 🎯 Features

* Customer Segmentation using clustering (KMeans)
* Churn Prediction using machine learning (Random Forest)
* Business Recommendation Engine
* Interactive UI using Streamlit
* Real-time predictions based on user input

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Pickle (model persistence)

---

## 📊 Approach

### 1. Data Preprocessing

* Removed null values
* Filtered invalid transactions
* Created `TotalPrice` feature

### 2. Feature Engineering (RFM)

* **Recency** → Days since last purchase
* **Frequency** → Number of transactions
* **Monetary** → Total spend

### 3. Customer Segmentation

* Applied **KMeans clustering**
* Grouped customers into 4 segments

### 4. Churn Prediction

* Created churn label based on inactivity
* Trained **Random Forest Classifier**

### 5. Business Logic

* Combined segment + churn to recommend actions:

  * High churn → Offer discount
  * High value → Upsell
  * Others → Engagement strategies

---

## ⚙️ Project Structure

```
customer_intelligence/
│── data/
│── models/
│── src/
│    ├── train.py
│    ├── predict.py
│── ui.py
│── requirements.txt
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Train models

```
python src/train.py
```

### 3. Run Streamlit app

```
streamlit run ui.py
```

---

## 🖥️ Usage

* Enter:

  * Recency
  * Frequency
  * Monetary value

* Get:

  * Customer Segment
  * Churn Risk
  * Recommended Action

---

## 💡 Example Output

```
Segment: 2  
Churn Risk: 1  
Action: Offer discount
```

---

## 🚀 Deployment

The project is deployed using **Streamlit Cloud** for easy access and demonstration.

---

## 📈 Business Impact

* Helps identify high-value customers
* Reduces churn through early detection
* Improves marketing and retention strategies

---

## 🔮 Future Improvements

* Use real churn labels instead of rule-based
* Add XGBoost for better performance
* Integrate FastAPI backend
* Improve UI/UX with advanced visualization

---

## 👩‍💻 Author

Shrushti Kurve
(Data Science & AI Enthusiast)

---

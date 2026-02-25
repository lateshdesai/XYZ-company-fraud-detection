# 🚀 XYZ Company Fraud Detection System

An end-to-end Machine Learning based Fraud Detection System built using:

- Python
- Scikit-learn (RandomForest)
- FastAPI
- Streamlit
- Anaconda Environment
- Fully deployed from Local Disk D:

---

## 📌 Project Overview

This project detects fraudulent financial transactions using historical transaction data.

The system works by:

1. Training a Machine Learning model
2. Saving the trained model
3. Allowing users to enter a `transaction_id`
4. Automatically fetching transaction data
5. Predicting whether the transaction is Fraud (Yes/No)
6. Displaying fraud probability

---

## 🗂 Project Structure

```
XYZ-company-fraud-detection
│
├── data
│   └── Fraud detection Dataset.csv
│
├── models
│   └── fraud_model.pkl
│
├── src
│   ├── train.py
│   └── predict.py
│
├── api
│   └── main.py
│
├── app_streamlit.py
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Environment (Stored in D Drive)

```
conda create --prefix D:\XYZ-company-fraud-detection\env python=3.10
conda activate D:\XYZ-company-fraud-detection\env
```

### 2️⃣ Install Dependencies

```
pip install pandas numpy scikit-learn joblib fastapi uvicorn streamlit
```

---

## 🏋️ Train the Model

```
python src\train.py
```

Model will be saved in:

```
models/fraud_model.pkl
```

---

## 🌐 Run FastAPI Backend

```
uvicorn api.main:app --reload
```

Open:
```
http://127.0.0.1:8000/docs
```

---

## 🖥 Run Streamlit App

```
streamlit run app_streamlit.py
```

Open:
```
http://localhost:8501/
```

---

## 🎯 How It Works

User enters:

```
transaction_id
```

System:

- Fetches row from dataset
- Drops unused columns
- Sends to trained model
- Returns:
  - Fraud Prediction (Yes/No)
  - Fraud Probability

---

## 📊 Model Used

- RandomForestClassifier
- OneHotEncoding for categorical variables
- Train/Test Split with Stratification

---

## 💡 Features

✔ Transaction ID based prediction  
✔ No manual feature entry  
✔ Clean Yes/No output  
✔ Fraud probability score  
✔ Fully local D Drive deployment  
✔ API + Web Interface  

---

## 🔮 Future Improvements

- Real-time database integration
- Model monitoring dashboard
- CI/CD pipeline
- Cloud deployment (AWS/Azure/GCP)
- Model versioning

---

## 👨‍💻 Author

GitHub: https://github.com/lateshdesai

---

⭐ If you found this project useful, consider giving it a star!
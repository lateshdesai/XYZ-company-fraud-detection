import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv(r"D:\XYZ-company-fraud-detection\data\Fraud detection Dataset.csv")

# Define X and y
X = df.drop(["is_fraud", "transaction_id", "user_id", "transaction_time"], axis=1)
y = df["is_fraud"]

categorical_features = ["transaction_type", "location", "device_type"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ],
    remainder="passthrough"
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=200, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model.fit(X_train, y_train)

joblib.dump(model, r"D:\XYZ-company-fraud-detection\models\fraud_model.pkl")

print("Model trained and saved in D: successfully")
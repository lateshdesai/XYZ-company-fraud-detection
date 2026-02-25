import joblib
import pandas as pd

# Load trained model
model = joblib.load(r"D:\XYZ-company-fraud-detection\models\fraud_model.pkl")

# Load full dataset
dataset = pd.read_csv(r"D:\XYZ-company-fraud-detection\data\Fraud detection Dataset.csv")

def predict_fraud_by_transaction_id(transaction_id):

    # Find the transaction row
    row = dataset[dataset["transaction_id"] == transaction_id]

    if row.empty:
        return {"error": "transaction_id not found"}

    # Drop columns exactly like during training
    input_data = row.drop(
        ["is_fraud", "transaction_id", "user_id", "transaction_time"],
        axis=1
    )

    # Predict
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return {
        "transaction_id": transaction_id,
        "is_fraud_prediction": int(prediction),
        "fraud_probability": float(probability)
    }
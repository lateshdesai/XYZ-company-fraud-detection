from fastapi import FastAPI
from src.predict import predict_fraud

app = FastAPI()

@app.get("/")
def home():
    return {"message": "XYZ Fraud Detection Running from D Drive"}

@app.post("/predict")
def predict(data: dict):
    return predict_fraud(data)
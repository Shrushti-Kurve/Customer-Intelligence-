from fastapi import FastAPI
from src.predict import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Customer Intelligence API running"}

@app.post("/predict")
def make_prediction(data: dict):
    result = predict(data)
    return result
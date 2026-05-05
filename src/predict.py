import pickle
import pandas as pd
from functools import lru_cache

@lru_cache(maxsize=1)
def load_models():
    """Load models once and cache them"""
    model = pickle.load(open("models/churn.pkl", "rb"))
    kmeans = pickle.load(open("models/segment.pkl", "rb"))
    scaler = pickle.load(open("models/scaler.pkl", "rb"))
    return model, kmeans, scaler

model, kmeans, scaler = load_models()

def get_action(segment, churn):
    if churn == 1:
        return "Give discount / retention offer"
    elif segment == 0:
        return "Upsell premium products"
    elif segment == 1:
        return "Send engagement emails"
    else:
        return "Maintain relationship"

def predict(data):
    recency = data["recency"]
    frequency = data["frequency"]
    monetary = data["monetary"]

    # Create DataFrame with proper feature names to match training data
    X = pd.DataFrame(
        [[recency, frequency, monetary]],
        columns=["Recency", "Frequency", "Monetary"]
    )

    scaled = scaler.transform(X)

    segment = int(kmeans.predict(scaled)[0])
    churn = int(model.predict(X)[0])

    action = get_action(segment, churn)

    return {
        "segment": segment,
        "churn_risk": churn,
        "action": action
    }
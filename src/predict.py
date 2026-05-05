import pickle

model = pickle.load(open("models/churn.pkl", "rb"))
kmeans = pickle.load(open("models/segment.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

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

    X = [[recency, frequency, monetary]]

    scaled = scaler.transform(X)

    segment = int(kmeans.predict(scaled)[0])
    churn = int(model.predict(X)[0])

    action = get_action(segment, churn)

    return {
        "segment": segment,
        "churn_risk": churn,
        "action": action
    }
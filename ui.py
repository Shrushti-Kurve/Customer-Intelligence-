import streamlit as st
import pickle
import os

st.set_page_config(
    page_title="Customer Intelligence Pro",
    page_icon="🚀",
    layout="wide"
)

st.title("🎯 Customer Intelligence Pro")
st.write("Predict customer segment and churn risk using AI models")

def get_action(segment, churn):
    if churn == 1:
        return "Give discount / retention offer"
    if segment == 0:
        return "Upsell premium products"
    if segment == 1:
        return "Send engagement emails"
    return "Maintain relationship"

st.subheader("📊 Enter Customer Metrics")
col1, col2, col3 = st.columns(3)

with col1:
    recency = st.number_input("Recency (days)", min_value=0, max_value=500, value=45)
with col2:
    frequency = st.number_input("Frequency (purchases)", min_value=0, max_value=300, value=10)
with col3:
    monetary = st.number_input("Monetary Value ($)", min_value=0.0, max_value=100000.0, value=500.0, step=10.0)

if st.button("⚡ Predict"):
    try:
        model = pickle.load(open("models/churn.pkl", "rb"))
        kmeans = pickle.load(open("models/segment.pkl", "rb"))
        scaler = pickle.load(open("models/scaler.pkl", "rb"))

        X = [[recency, frequency, monetary]]
        scaled = scaler.transform(X)
        segment = int(kmeans.predict(scaled)[0])
        churn = int(model.predict(X)[0])
        action = get_action(segment, churn)

        st.success("✅ Prediction successful!")
        
        r1, r2, r3 = st.columns(3)
        r1.metric("Customer Segment", f"Tier {segment}")
        r2.metric("Churn Risk", "HIGH 🔴" if churn == 1 else "LOW 🟢")
        r3.metric("Strategy", action)

    except FileNotFoundError:
        st.error("Model files not found – ensure models/churn.pkl, models/segment.pkl, models/scaler.pkl exist")
    except Exception as e:
        st.error(f"Error: {str(e)}")
            st.error(f"❌ Error: {str(e)}")
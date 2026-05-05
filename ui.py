import streamlit as st
import pickle
import os
import sys
import pandas as pd

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from predict import predict

st.set_page_config(
    page_title="Customer Intelligence Pro",
    page_icon="🚀",
    layout="wide"
)

# Animated CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

* { font-family: 'Poppins', sans-serif; }

.stApp { 
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    color: #ffffff;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
}

@keyframes glow {
    0%, 100% { box-shadow: 0 0 10px rgba(102, 126, 234, 0.4); }
    50% { box-shadow: 0 0 25px rgba(102, 126, 234, 0.8); }
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.85; }
}

.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 50px 30px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
    animation: float 3s ease-in-out infinite;
    margin-bottom: 40px;
    border: 2px solid rgba(255,255,255,0.1);
}

.header h1 {
    color: white !important;
    font-size: 48px !important;
    font-weight: 800 !important;
    margin: 0 !important;
    text-shadow: 0 4px 15px rgba(0,0,0,0.3);
}

.header p {
    color: rgba(255,255,255,0.9) !important;
    font-size: 16px !important;
    margin: 10px 0 0 0 !important;
}

.input-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
    padding: 35px;
    border-radius: 18px;
    border: 2px solid rgba(102, 126, 234, 0.3);
    margin: 20px 0;
    backdrop-filter: blur(10px);
    animation: glow 3s ease-in-out infinite;
}

.metric-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(102, 126, 234, 0.08) 100%);
    padding: 25px;
    border-radius: 16px;
    border: 2px solid rgba(102, 126, 234, 0.3);
    text-align: center;
    box-shadow: 0 8px 30px rgba(102, 126, 234, 0.2);
    animation: pulse 2s ease-in-out infinite;
    color: white;
    margin: 10px 0;
}

.metric-gold {
    background: linear-gradient(135deg, rgba(255, 215, 0, 0.2) 0%, rgba(255, 165, 0, 0.2) 100%);
    border: 2px solid rgba(255, 215, 0, 0.5);
}

.metric-silver {
    background: linear-gradient(135deg, rgba(192, 192, 192, 0.2) 0%, rgba(128, 128, 128, 0.2) 100%);
    border: 2px solid rgba(192, 192, 192, 0.5);
}

.metric-bronze {
    background: linear-gradient(135deg, rgba(205, 127, 50, 0.2) 0%, rgba(139, 69, 19, 0.2) 100%);
    border: 2px solid rgba(205, 127, 50, 0.5);
}

.metric-standard {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
    border: 2px solid rgba(102, 126, 234, 0.5);
}

.metric-high {
    background: linear-gradient(135deg, rgba(255, 107, 107, 0.2) 0%, rgba(238, 90, 111, 0.2) 100%);
    border: 2px solid rgba(255, 107, 107, 0.5);
}

.metric-low {
    background: linear-gradient(135deg, rgba(81, 207, 102, 0.2) 0%, rgba(55, 178, 77, 0.2) 100%);
    border: 2px solid rgba(81, 207, 102, 0.5);
}

.action-card {
    background: linear-gradient(135deg, rgba(240, 147, 251, 0.15) 0%, rgba(245, 87, 108, 0.15) 100%);
    padding: 30px;
    border-radius: 18px;
    border: 2px solid rgba(240, 147, 251, 0.4);
    text-align: center;
    color: #f093fb;
    font-size: 18px !important;
    font-weight: 700 !important;
    box-shadow: 0 8px 30px rgba(240, 147, 251, 0.2);
    animation: float 2.5s ease-in-out infinite;
    margin: 20px 0;
}

h2, h3 {
    color: white !important;
    text-shadow: 0 2px 8px rgba(0,0,0,0.3);
}

.stNumberInput > label {
    color: #ffffff !important;
    font-weight: 600 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    font-weight: 700 !important;
    padding: 15px 40px !important;
    border-radius: 12px !important;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6) !important;
}

.stSuccess, .stError, .stInfo {
    border-radius: 12px !important;
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}

hr {
    border: 1px solid rgba(102, 126, 234, 0.2) !important;
    margin: 30px 0 !important;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <h1>🚀 CUSTOMER INTELLIGENCE PRO</h1>
    <p>AI-Powered Customer Analytics & Predictive Insights</p>
</div>
""", unsafe_allow_html=True)

def get_action(segment, churn):
    if churn == 1:
        return "🎁 Offer exclusive discount & retention deal"
    if segment == 0:
        return "⭐ Upsell premium products"
    if segment == 1:
        return "💌 Send personalized engagement emails"
    return "📊 Maintain steady relationship"

# Input Section
st.markdown('<div class="input-card">', unsafe_allow_html=True)
st.markdown("### 📊 Enter Customer Metrics")

col1, col2, col3 = st.columns(3)
with col1:
    recency = st.number_input("📅 Recency (days)", min_value=0, max_value=500, value=45, step=1)
with col2:
    frequency = st.number_input("🔄 Frequency (purchases)", min_value=0, max_value=300, value=10, step=1)
with col3:
    monetary = st.number_input("💰 Monetary Value ($)", min_value=0.0, max_value=100000.0, value=500.0, step=10.0)

st.markdown('</div>', unsafe_allow_html=True)

# Predict Button
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_btn = st.button("⚡ PREDICT", use_container_width=True)

if predict_btn:
    try:
        # Use the predict function from src/predict.py (with proper DataFrame feature names)
        result = predict({
            "recency": recency,
            "frequency": frequency,
            "monetary": monetary
        })
        segment = result["segment"]
        churn = result["churn_risk"]
        action = result["action"]

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("## 📈 PREDICTION RESULTS")
        
        # Results Row
        res1, res2, res3 = st.columns(3, gap="medium")
        
        segment_class = {0: "metric-gold", 1: "metric-silver", 2: "metric-bronze", 3: "metric-standard"}.get(segment, "metric-standard")
        segment_name = {0: "🏆 GOLD TIER", 1: "💎 SILVER TIER", 2: "🥉 BRONZE TIER", 3: "⭐ STANDARD TIER"}.get(segment, "UNKNOWN")
        
        with res1:
            st.markdown(f'<div class="metric-card {segment_class}"><h3 style="margin:0; font-size:14px; color:#ffd700;">SEGMENT</h3><p style="margin:10px 0 0 0; font-size:24px; font-weight:800;">{segment_name}</p></div>', unsafe_allow_html=True)
        
        churn_class = "metric-high" if churn == 1 else "metric-low"
        churn_text = "🔴 HIGH RISK" if churn == 1 else "🟢 LOW RISK"
        churn_color = "#ff6b6b" if churn == 1 else "#51cf66"
        
        with res2:
            st.markdown(f'<div class="metric-card {churn_class}"><h3 style="margin:0; font-size:14px; color:{churn_color};">CHURN RISK</h3><p style="margin:10px 0 0 0; font-size:24px; font-weight:800;">{churn_text}</p></div>', unsafe_allow_html=True)
        
        with res3:
            confidence = 95 if churn == 0 else 85
            st.markdown(f'<div class="metric-card" style="background: linear-gradient(135deg, rgba(78, 205, 196, 0.2) 0%, rgba(68, 160, 141, 0.2) 100%); border: 2px solid rgba(78, 205, 196, 0.5);"><h3 style="margin:0; font-size:14px; color:#4ecdc4;">CONFIDENCE</h3><p style="margin:10px 0 0 0; font-size:24px; font-weight:800;">{confidence}%</p></div>', unsafe_allow_html=True)
        
        # Action Card
        st.markdown(f'<div class="action-card">✨ Recommended Action<br><strong style="font-size: 16px; color: #f5576c;">{action}</strong></div>', unsafe_allow_html=True)
        
        # Summary
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("## 📋 INPUT SUMMARY")
        
        sum1, sum2, sum3 = st.columns(3, gap="medium")
        with sum1:
            st.markdown(f'<div class="metric-card"><h4 style="margin:0; font-size:13px; color:#51cf66;">📅 RECENCY</h4><p style="margin:10px 0 0 0; font-size:22px; font-weight:800;">{recency} days</p></div>', unsafe_allow_html=True)
        with sum2:
            st.markdown(f'<div class="metric-card"><h4 style="margin:0; font-size:13px; color:#667eea;">🔄 FREQUENCY</h4><p style="margin:10px 0 0 0; font-size:22px; font-weight:800;">{frequency} buys</p></div>', unsafe_allow_html=True)
        with sum3:
            st.markdown(f'<div class="metric-card"><h4 style="margin:0; font-size:13px; color:#f5576c;">💰 MONETARY</h4><p style="margin:10px 0 0 0; font-size:22px; font-weight:800;">${monetary:.2f}</p></div>', unsafe_allow_html=True)
        
        st.success("✅ Analysis Complete!")

    except FileNotFoundError:
        st.error("❌ Model files not found – ensure models/churn.pkl, models/segment.pkl, models/scaler.pkl exist")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
import streamlit as st
import requests
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="Customer Intelligence Pro",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced CSS with animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&family=Space+Mono:wght@400;700&display=swap');

    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }
    
    /* Animated Background */
    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 5px rgba(102, 126, 234, 0.4), 0 0 20px rgba(102, 126, 234, 0.2); }
        50% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.8), 0 0 40px rgba(102, 126, 234, 0.4); }
    }
    
    /* Header with Animation */
    .header-container {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient-shift 15s ease infinite;
        padding: 50px 40px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 40px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        border: 2px solid rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .header-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 20% 50%, rgba(255,255,255,0.1) 0%, transparent 50%);
        pointer-events: none;
    }
    
    .header-container h1 {
        color: white !important;
        font-size: 56px !important;
        font-weight: 800 !important;
        margin: 0 !important;
        text-shadow: 0 4px 20px rgba(0,0,0,0.3);
        letter-spacing: -1px;
    }
    
    .header-container p {
        color: rgba(255,255,255,0.95) !important;
        font-size: 18px !important;
        margin-top: 15px !important;
        font-weight: 300;
        letter-spacing: 0.5px;
    }
    
    /* Input Section */
    .input-section {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        padding: 40px;
        border-radius: 20px;
        border: 2px solid rgba(102, 126, 234, 0.3);
        margin-bottom: 30px;
        backdrop-filter: blur(10px);
        animation: glow 3s ease-in-out infinite;
    }
    
    .input-section h3 {
        color: #ffffff !important;
        font-size: 28px !important;
        font-weight: 700 !important;
        margin-bottom: 25px !important;
    }
    
    /* Input Fields */
    .stNumberInput input {
        background: rgba(255,255,255,0.05) !important;
        color: white !important;
        border: 2px solid rgba(102, 126, 234, 0.5) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput input:focus {
        background: rgba(255,255,255,0.1) !important;
        border: 2px solid #667eea !important;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.5) !important;
    }
    
    .stNumberInput label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        padding: 18px 50px !important;
        border: none !important;
        border-radius: 12px !important;
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.6) !important;
    }
    
    .stButton button:active {
        transform: translateY(-1px) !important;
    }
    
    /* Result Cards */
    .result-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(102, 126, 234, 0.05) 100%);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid rgba(102, 126, 234, 0.3);
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        backdrop-filter: blur(10px);
        animation: float 3s ease-in-out infinite;
    }
    
    /* Metric Cards with Styles */
    .metric-card-gold {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        animation: glow 2s ease-in-out infinite;
    }
    
    .metric-card-silver {
        background: linear-gradient(135deg, #C0C0C0 0%, #808080 100%);
        animation: glow 2s ease-in-out infinite;
    }
    
    .metric-card-bronze {
        background: linear-gradient(135deg, #CD7F32 0%, #8B4513 100%);
        animation: glow 2s ease-in-out infinite;
    }
    
    .metric-card-standard {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        animation: glow 2s ease-in-out infinite;
    }
    
    .metric-card-risk-high {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
        animation: pulse 1.5s ease-in-out infinite;
    }
    
    .metric-card-risk-low {
        background: linear-gradient(135deg, #51cf66 0%, #37b24d 100%);
        animation: pulse 2s ease-in-out infinite;
    }
    
    .metric-card {
        padding: 30px;
        border-radius: 18px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        border: 2px solid rgba(255,255,255,0.1);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: scale(1.05);
    }
    
    .metric-card h4 {
        margin: 0 !important;
        color: white !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .metric-card p {
        color: rgba(255,255,255,0.95) !important;
        font-size: 32px !important;
        font-weight: 800 !important;
        margin: 15px 0 0 0 !important;
        font-family: 'Space Mono', monospace;
    }
    
    .metric-card .subtitle {
        font-size: 12px !important;
        color: rgba(255,255,255,0.7) !important;
        margin-top: 8px !important;
    }
    
    /* Action Card */
    .action-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 15px 50px rgba(245, 87, 108, 0.4);
        border: 2px solid rgba(255,255,255,0.2);
        animation: float 2s ease-in-out infinite;
        margin: 30px 0;
    }
    
    .action-card .action-text {
        font-size: 18px;
        font-weight: 600;
        opacity: 0.9;
        margin-bottom: 15px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .action-card .action-value {
        font-size: 26px;
        font-weight: 800;
        margin-top: 15px;
        text-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    
    /* Titles */
    h1, h2 {
        color: #ffffff !important;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2) !important;
    }
    
    h2 {
        font-size: 36px !important;
        font-weight: 800 !important;
        margin-bottom: 30px !important;
        letter-spacing: -0.5px;
    }
    
    h3 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    
    /* Status Messages */
    .stSuccess, .stError, .stWarning, .stInfo {
        border-radius: 12px !important;
    }
    
    .stSuccess {
        background: rgba(81, 207, 102, 0.2) !important;
        color: #51cf66 !important;
    }
    
    .stError {
        background: rgba(255, 107, 107, 0.2) !important;
        color: #ff6b6b !important;
    }
    
    /* Spinner text */
    .stSpinner {
        color: #667eea !important;
    }
    
    /* Separator */
    hr {
        border: 1px solid rgba(102, 126, 234, 0.2) !important;
        margin: 40px 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Hidden sidebar
st.markdown("""
<style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Animated Header
st.markdown("""
<div class="header-container">
    <h1>🚀 CUSTOMER INTELLIGENCE PRO</h1>
    <p>Advanced ML-Powered Customer Analytics Platform</p>
</div>
""", unsafe_allow_html=True)

# Input Section with Animation
st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.markdown("### 📊 Enter Customer Metrics")

col_a, col_b, col_c = st.columns(3)

with col_a:
    recency = st.number_input(
        "📅 Recency",
        min_value=0,
        max_value=500,
        value=45,
        step=1,
        help="Days since last purchase"
    )

with col_b:
    frequency = st.number_input(
        "🔄 Frequency",
        min_value=0,
        max_value=300,
        value=10,
        step=1,
        help="Total number of purchases"
    )

with col_c:
    monetary = st.number_input(
        "💰 Monetary",
        min_value=0.0,
        max_value=100000.0,
        value=500.0,
        step=10.0,
        help="Total spending amount"
    )

st.markdown('</div>', unsafe_allow_html=True)

# Prediction Button
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_button = st.button(
        "⚡ ANALYZE NOW",
        key="predict_btn",
        use_container_width=True
    )

# Results Section
if predict_button:
    with st.spinner("🔍 Processing data with AI..."):
        payload = {
            "recency": recency,
            "frequency": frequency,
            "monetary": monetary
        }

        try:
            response = requests.post("http://127.0.0.1:8000/predict", json=payload, timeout=5)

            if response.status_code == 200:
                data = response.json()
                
                st.markdown("<hr>", unsafe_allow_html=True)
                st.markdown("<h2 style='text-align: center; margin-bottom: 40px;'>📈 ANALYSIS RESULTS</h2>", unsafe_allow_html=True)
                
                # Result Cards
                res_col1, res_col2, res_col3 = st.columns(3, gap="large")
                
                segment = data["segment"]
                segment_map = {
                    0: ("🏆 GOLD TIER", "metric-card-gold"),
                    1: ("💎 SILVER TIER", "metric-card-silver"),
                    2: ("🥉 BRONZE TIER", "metric-card-bronze"),
                    3: ("⭐ STANDARD TIER", "metric-card-standard")
                }
                
                segment_name, segment_class = segment_map.get(segment, ("UNKNOWN", "metric-card-standard"))
                
                with res_col1:
                    st.markdown(f"""
                    <div class="metric-card {segment_class}">
                        <h4>👥 CUSTOMER SEGMENT</h4>
                        <p>{segment_name}</p>
                        <div class="subtitle">Tier Level: {segment}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                churn_risk = data["churn_risk"]
                churn_text = "🔴 HIGH RISK" if churn_risk == 1 else "🟢 LOW RISK"
                churn_class = "metric-card-risk-high" if churn_risk == 1 else "metric-card-risk-low"
                
                with res_col2:
                    st.markdown(f"""
                    <div class="metric-card {churn_class}">
                        <h4>⚠️ CHURN RISK</h4>
                        <p>{churn_text}</p>
                        <div class="subtitle">Risk Level: {churn_risk * 100:.0f}%</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with res_col3:
                    probability = (churn_risk * 100)
                    confidence = 100 - probability
                    st.markdown(f"""
                    <div class="metric-card" style="background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);">
                        <h4>📊 CONFIDENCE</h4>
                        <p>{confidence:.0f}%</p>
                        <div class="subtitle">Prediction Accuracy</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Recommended Action
                action = data["action"]
                st.markdown(f"""
                <div class="action-card">
                    <div class="action-text">✨ Recommended Strategy</div>
                    <div class="action-value">{action}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Input Summary
                st.markdown("<hr>", unsafe_allow_html=True)
                st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>📋 INPUT SUMMARY</h2>", unsafe_allow_html=True)
                
                summary_col1, summary_col2, summary_col3 = st.columns(3, gap="large")
                
                with summary_col1:
                    st.markdown(f"""
                    <div class="result-card">
                        <h4 style="color: #51cf66;">📅 RECENCY</h4>
                        <p style="font-size: 28px; margin: 10px 0 0 0;">{recency}</p>
                        <p style="font-size: 12px; color: rgba(255,255,255,0.6); margin: 5px 0 0 0;">Days Since Purchase</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with summary_col2:
                    st.markdown(f"""
                    <div class="result-card">
                        <h4 style="color: #667eea;">🔄 FREQUENCY</h4>
                        <p style="font-size: 28px; margin: 10px 0 0 0;">{frequency}</p>
                        <p style="font-size: 12px; color: rgba(255,255,255,0.6); margin: 5px 0 0 0;">Total Transactions</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with summary_col3:
                    st.markdown(f"""
                    <div class="result-card">
                        <h4 style="color: #f5576c;">💰 MONETARY VALUE</h4>
                        <p style="font-size: 28px; margin: 10px 0 0 0;">${monetary:.2f}</p>
                        <p style="font-size: 12px; color: rgba(255,255,255,0.6); margin: 5px 0 0 0;">Total Spending</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.success("✅ Analysis completed successfully!", icon="✅")
                
            else:
                st.error(f"❌ API Error: {response.status_code}")
                st.info("Ensure FastAPI backend is running: `uvicorn app:app --reload --port 8000`")
        
        except requests.exceptions.ConnectionError:
            st.error("❌ Cannot connect to API backend")
            st.warning("Start the backend: `uvicorn app:app --reload --port 8000`")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
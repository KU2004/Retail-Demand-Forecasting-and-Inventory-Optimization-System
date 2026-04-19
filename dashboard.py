import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Retail AI System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

/* Background */
body {
    background-color: #0E1117;
    color: white;
}

/* Title */
.main-title {
    font-size: 45px;
    font-weight: bold;
    color: #00C6FF;
    margin-bottom: 10px;
}

/* Cards */
.card {
    background: linear-gradient(135deg, #232526, #414345);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align: center;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.05);
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg, #00C6FF, #0072FF);
    color: white;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown('<div class="main-title">🚀 Retail Forecasting & Inventory System</div>', unsafe_allow_html=True)

st.write("### 👋 Welcome to your AI-powered Retail Analytics Platform")

st.write("""
This system helps in:
- 📈 Sales Forecasting  
- 📦 Inventory Optimization  
- ⚠️ Reorder Alerts  
- 📊 Business Insights  
""")

# =========================
# NAVIGATION CARDS
# =========================
st.subheader("📊 Navigate to Modules")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.markdown('<div class="card">📊 Overview Dashboard</div>', unsafe_allow_html=True)
    if st.button("Go to Overview"):
        st.switch_page("pages/overview.py")

with col2:
    st.markdown('<div class="card">📈 Forecasting Analysis</div>', unsafe_allow_html=True)
    if st.button("Go to Forecasting"):
        st.switch_page("pages/forecasting.py")

with col3:
    st.markdown('<div class="card">📦 Inventory Optimization</div>', unsafe_allow_html=True)
    if st.button("Go to Inventory"):
        st.switch_page("pages/inventory.py")

with col4:
    st.markdown('<div class="card">📊 Business Insights</div>', unsafe_allow_html=True)
    if st.button("Go to Insights"):
        st.switch_page("pages/insights.py")

# =========================
# SIDEBAR INFO
# =========================
st.sidebar.title("📌 Navigation")

st.sidebar.info("""
Use the sidebar or buttons to explore:
- Overview  
- Forecasting  
- Inventory  
- Insights  
""")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Built with ❤️ | Retail AI System")
import streamlit as st
import pandas as pd

# =========================
# PAGE TITLE
# =========================
st.title("📦 Inventory Optimization")

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("outputs/forecast.csv")

# =========================
# FILTERS
# =========================
col1, col2 = st.columns(2)

with col1:
    product = st.selectbox("Select Product", df['product'].unique())

with col2:
    venue = st.selectbox("Select Store", df['venue'].unique())

# Filter data
filtered = df[(df['product'] == product) & (df['venue'] == venue)]

# =========================
# INVENTORY TABLE
# =========================
st.subheader("📊 Inventory Table")

st.dataframe(
    filtered[['date', 'sales', 'forecast', 'reorder_point', 'order_qty']],
    width="stretch"
)

# =========================
# ALERT SYSTEM (FIXED)
# =========================
st.subheader("🚨 Reorder Alerts")

# Only rows where reorder needed
alerts = filtered[filtered['order_qty'] > 0]

# 👉 Take only recent alerts (last 7 days)
recent_alerts = alerts.tail(7)

if len(alerts) > 0:
    st.error(f"⚠️ {len(recent_alerts)} recent reorder alerts (last 7 days)")
    
    st.dataframe(
        recent_alerts[['date', 'order_qty']],
        width="stretch"
    )
else:
    st.success("✅ Inventory is stable")

# =========================
# KPI SUMMARY (BONUS)
# =========================
st.subheader("📌 Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Reorder Qty", int(filtered['order_qty'].sum()))
col2.metric("Max Reorder Qty", int(filtered['order_qty'].max()))
col3.metric("Avg Reorder Qty", int(filtered['order_qty'].mean()))

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Smart Inventory System 🚀")
import streamlit as st
import pandas as pd

st.title("📊 Business Insights")

df = pd.read_csv("outputs/forecast.csv")

# Top products
st.subheader("Top Selling Products")
top_products = df.groupby("product")["sales"].sum().sort_values(ascending=False)
st.bar_chart(top_products)

# Store comparison
st.subheader("Store Performance")
store_sales = df.groupby("venue")["sales"].sum()
st.bar_chart(store_sales)

# Demand pattern
st.subheader("Monthly Demand")
monthly = df.groupby(df['date'].str[:7])['sales'].sum()
st.line_chart(monthly)
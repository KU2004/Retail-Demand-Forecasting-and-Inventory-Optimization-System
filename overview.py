import streamlit as st
import pandas as pd

st.title("📊 Overview Dashboard")

df = pd.read_csv("outputs/forecast.csv")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", int(df["sales"].sum()))
col2.metric("Avg Forecast", int(df["forecast"].mean()))
col3.metric("Total Reorder Qty", int(df["order_qty"].sum()))

# Charts
st.subheader("Sales Trend")
st.line_chart(df.groupby("date")["sales"].sum())

st.subheader("Forecast Trend")
st.line_chart(df.groupby("date")["forecast"].sum())
import streamlit as st
import pandas as pd

st.title("📈 Forecasting Analysis")

df = pd.read_csv("outputs/forecast.csv")

product = st.selectbox("Select Product", df['product'].unique())
venue = st.selectbox("Select Store", df['venue'].unique())

filtered = df[(df['product']==product) & (df['venue']==venue)]

st.subheader("Sales vs Forecast")
st.line_chart(filtered[['sales','forecast']])

st.subheader("Forecast Table")
st.dataframe(filtered[['date','sales','forecast']])
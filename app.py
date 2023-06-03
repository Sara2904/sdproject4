import pandas as pd
import numpy as np
import csv
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

figl = px.histogram(df, x='price', nbins=50)

fig2 = px.histogram(df, x='odometer', nbins=30)

fig3 = px.scatter(df, x='odometer', y='price')

fig4 = px.scatter(df, x='model_year', y='price')

st.header("Car Advertisement Dataset Analysis")

st.subheader("Histogram: Price Distribution")
st.plotly_chart(figl)

st.subheader("Histogram: Odometer Distribution")
st.plotly_chart(fig2)

st.subheader("Scatter Plot: Price vs. Odometer")
st.plotly_chart(fig3)

st.subheader("Scatter Plot: Price vs. Model Year")
st.plotly_chart(fig4)

show_data = st.checkbox("Show Raw Data")
if show_data:
    st.subheader("Raw Data")
    st.write(df)

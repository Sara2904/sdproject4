#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import csv
import plotly.express as px
import streamlit as st


df = pd.read_csv('vehicles_us.csv')

figl = px.histogram(df, x='price', nbins=50)
figl.show()

fig2 = px.histogram(df, x='odometer', nbins=30)
fig2.show()

fig3 = px.scatter(df, x='odometer', y='price')
fig3.show()

fig4 = px.scatter(df, x='model_year', y='price')
fig4.show()

st.header("Car Advertisement Dataset Analysis")

st.subheader("Histogram: Price Distribution")
fig_histogram = px.histogram(df, x='price')
st.plotly_chart(fig_histogram)

st.subheader("Scatter Plot: Price vs. Odometer")
fig_scatter = px.scatter(df, x='odometer', y='price', color='condition')
st.plotly_chart(fig_scatter)

show_data = st.checkbox("Show Raw Data")
if show_data:
    st.write(df)





#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import csv
import plotly.express as px
import streamlit as st


# In[16]:


df = pd.read_csv('/Users/sarar/sdproject4/vehicles_us.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


figl = px.histogram(df, x='price', nbins=50)
figl.show()


# In[8]:


fig2 = px.histogram(df, x='odometer', nbins=30)
fig2.show()


# In[9]:


fig3 = px.scatter(df, x='odometer', y='price')
fig3.show()


# In[14]:


fig4 = px.scatter(df, x='model_year', y='price')
fig4.show()


# In[13]:


st.header("Car Advertisement Dataset Analysis")

# Histogram
st.subheader("Histogram: Price Distribution")
fig_histogram = px.histogram(df, x='price')
st.plotly_chart(fig_histogram)

# Scatter Plot 
st.subheader("Scatter Plot: Price vs. Odometer")
fig_scatter = px.scatter(df, x='odometer', y='price', color='condition')
st.plotly_chart(fig_scatter)

# Checkbox
show_data = st.checkbox("Show Raw Data")
if show_data:
    st.write(df)


# In[ ]:





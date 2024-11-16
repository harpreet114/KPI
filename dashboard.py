# Install Streamlit if not already installed: pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set up the dashboard title
st.title("KPI Dashboard")

# Example data
data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sales': [20000, 24000, 22000, 27000, 30000, 28000],
    'Profit': [5000, 6000, 5500, 7000, 8000, 7500],
    'Customer Acquisitions': [100, 120, 110, 130, 150, 140]
})

# Sidebar for filters
st.sidebar.header("Filter Options")
selected_month = st.sidebar.selectbox("Select Month", data['Month'])

# Display KPIs
selected_data = data[data['Month'] == selected_month]
if not selected_data.empty:
    sales = selected_data['Sales'].values[0]
    profit = selected_data['Profit'].values[0]
    customers = selected_data['Customer Acquisitions'].values[0]

    st.metric(label="Sales", value=f"${sales:,}")
    st.metric(label="Profit", value=f"${profit:,}")
    st.metric(label="Customer Acquisitions", value=customers)

# Add a line chart for trends
st.subheader("Sales and Profit Trends")
st.line_chart(data[['Sales', 'Profit']])

# Add a bar chart for customer acquisition
st.subheader("Customer Acquisitions")
st.bar_chart(data['Customer Acquisitions'])

# Data table
st.subheader("Raw Data")
st.dataframe(data)

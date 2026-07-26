import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page layout to wide
st.set_page_config(page_title="HR Analytics", layout="wide")

# Custom CSS for the Blinkit Yellow aesthetic
st.markdown("""
    
    """, unsafe_allow_html=True)

st.title("⚡ HR Analytics Dashboard")

# Load Data
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Create Top KPI Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", len(df))
col2.metric("Attrition Rate", f"{round((df['Attrition'] == 'Yes').mean() * 100, 1)}%")
col3.metric("Avg Monthly Income", f"${round(df['MonthlyIncome'].mean())}")

# Add a Plotly Chart
fig = px.histogram(df, x="Department", color="Attrition", 
                   color_discrete_sequence=["#000000", "#FCEC52"])
st.plotly_chart(fig, use_container_width=True)
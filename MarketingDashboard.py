import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Visa Inc. color palette (simplified)
VISA_BLUE = "#1A1F71"
VISA_GOLD = "#FFB600"
VISA_WHITE = "#FFFFFF"
VISA_LIGHT_GREY = "#F5F5F5"
VISA_DARK_GREY = "#333333"
VISA_GREEN = "#00A651"

st.set_page_config(page_title="Bank Campaign Platform", layout="wide", page_icon="💳")

# Dummy data for campaigns/experiments
today = datetime.today()
dummy_campaigns = [
    {
        "Name": "Summer Cashback Blast",
        "Start Date": today - timedelta(days=30),
        "End Date": today + timedelta(days=30),
        "Status": "Active",
        "Progress": 55,
        "Conversions": 1200,
        "Spend ($)": 25000,
        "CTR (%)": 2.1,
        "Data Pipeline": "Healthy"
    },
    {
        "Name": "SafePay Awareness",
        "Start Date": today - timedelta(days=60),
        "End Date": today - timedelta(days=5),
        "Status": "Completed",
        "Progress": 100,
        "Conversions": 3100,
        "Spend ($)": 40000,
        "CTR (%)": 3.7,
        "Data Pipeline": "Completed"
    },
    {
        "Name": "Digital Card Push",
        "Start Date": today - timedelta(days=7),
        "End Date": today + timedelta(days=14),
        "Status": "Active",
        "Progress": 35,
        "Conversions": 480,
        "Spend ($)": 7000,
        "CTR (%)": 1.6,
        "Data Pipeline": "Healthy"
    },
    {
        "Name": "Refer-A-Friend",
        "Start Date": today - timedelta(days=15),
        "End Date": today + timedelta(days=45),
        "Status": "Active",
        "Progress": 22,
        "Conversions": 220,
        "Spend ($)": 3000,
        "CTR (%)": 1.1,
        "Data Pipeline": "Warning"
    },
    {
        "Name": "Winter Rewards Wrap-up",
        "Start Date": today - timedelta(days=120),
        "End Date": today - timedelta(days=20),
        "Status": "Completed",
        "Progress": 100,
        "Conversions": 4100,
        "Spend ($)": 60000,
        "CTR (%)": 4.4,
        "Data Pipeline": "Completed"
    },
]

df = pd.DataFrame(dummy_campaigns)

# Sidebar Quick Actions
st.sidebar.markdown(f"<h2 style='color:{VISA_BLUE}'>Quick Actions</h2>", unsafe_allow_html=True)
st.sidebar.button("➕ Create New Experiment")
st.sidebar.button("📄 Documentation")
st.sidebar.button("💬 Support")
st.sidebar.markdown("---")
st.sidebar.markdown(f"<h4 style='color:{VISA_GOLD}'>Active Experiments: {len(df[df['Status']=='Active'])}</h4>", unsafe_allow_html=True)

# Main Dashboard Title
st.markdown(f"<h1 style='color:{VISA_BLUE}'>Bank Campaign Experiments Dashboard</h1>", unsafe_allow_html=True)
st.write("Monitor, analyze, and manage your campaigns efficiently.")

# Overview of Active Experiments
st.markdown(f"<h3 style='color:{VISA_GOLD}'>Overview of Experiments</h3>", unsafe_allow_html=True)

for idx, row in df.iterrows():
    col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 2])
    with col1:
        st.markdown(f"<b>{row['Name']}</b>", unsafe_allow_html=True)
        st.caption(f"Start: {row['Start Date'].strftime('%Y-%m-%d')}")
        st.caption(f"End: {row['End Date'].strftime('%Y-%m-%d')}")
    with col2:
        status_color = VISA_GREEN if row['Status'] == "Active" else VISA_DARK_GREY
        st.markdown(f"<span style='color:{status_color}'>{row['Status']}</span>", unsafe_allow_html=True)
        st.progress(row['Progress'] / 100)
    with col3:
        st.metric("Conversions", row["Conversions"])
        st.metric("CTR (%)", row["CTR (%)"])
    with col4:
        st.metric("Spend ($)", row["Spend ($)"])
    with col5:
        pipeline_color = VISA_GREEN if row['Data Pipeline'] in ["Healthy", "Completed"] else VISA_GOLD
        st.markdown(f"<span style='color:{pipeline_color}'>{row['Data Pipeline']}</span>", unsafe_allow_html=True)
    st.markdown("---")

# Key Metrics Summary
st.markdown(f"<h3 style='color:{VISA_BLUE}'>Key Metrics Summary</h3>", unsafe_allow_html=True)
metrics = {
    "Total Conversions": df["Conversions"].sum(),
    "Total Spend ($)": df["Spend ($)"].sum(),
    "Avg. CTR (%)": round(df["CTR (%)"].mean(),2)
}
col1, col2, col3 = st.columns(3)
col1.metric("Total Conversions", metrics["Total Conversions"])
col2.metric("Total Spend ($)", f"${metrics['Total Spend ($)']:,}")
col3.metric("Avg. CTR (%)", metrics["Avg. CTR (%)"])

# Data Pipelines Section
st.markdown(f"<h3 style='color:{VISA_GOLD}'>Data Pipelines Overview</h3>", unsafe_allow_html=True)
pipeline_status = df["Data Pipeline"].value_counts().to_dict()
st.write(pipeline_status)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:#888'>© 2025 Bank Campaign Platform • Powered by Visa Colors</p>",
    unsafe_allow_html=True
)

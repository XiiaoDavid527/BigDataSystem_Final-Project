import pandas as pd
import streamlit as st

# Read data
df = pd.read_csv("jobs.csv")

# Title
st.title("Student Part-Time Job Dashboard")

# Show all jobs
st.subheader("All Job Listings")
st.dataframe(df)

# Average wage
st.subheader("Average Wage")
st.metric("Average Hourly Wage", round(df["wage"].mean(), 2))

# Highest paying jobs
st.subheader("Highest Paying Jobs")
st.dataframe(df.sort_values("wage", ascending=False))

# Wage by category
st.subheader("Average Wage by Category")
avg_wage = df.groupby("category")["wage"].mean()
st.bar_chart(avg_wage)

category = st.selectbox(
    "Choose Category",
    df["category"].unique()
)

filtered = df[df["category"] == category]

st.dataframe(filtered)

# Average Wage
st.metric(
    "Average Wage",
    round(filtered["wage"].mean(), 2)
)

top_job = filtered.loc[filtered["wage"].idxmax()]

# Highest Pay
st.metric(
    "Highest Wage",
    f"{top_job['wage']} NTD/hr"
)
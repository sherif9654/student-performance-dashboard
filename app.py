import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Dashboard", layout="wide")
st.title("Student Performance Analytics Dashboard")

def load_data():
    return pd.read_csv("student_data.csv")

df = load_data()

st.sidebar.header("Filter Data")
status_filter = st.sidebar.multiselect("Select Status:", options=df["Status"].unique(), default=df["Status"].unique())
filtered_df = df[df["Status"].isin(status_filter)]

col1, col2 = st.columns(2)
with col1:
    st.subheader("Data Preview")
    st.dataframe(filtered_df)
with col2:
    st.subheader("Statistics Summary")
    st.write(filtered_df.describe())

st.divider()

col3, col4 = st.columns(2)
with col3:
    st.subheader("Pass vs Fail Distribution")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=filtered_df, x="Status", ax=ax1)
    st.pyplot(fig1)
with col4:
    st.subheader("Feature Correlation")
    fig2, ax2 = plt.subplots()
    numeric_df = filtered_df.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax2)
    st.pyplot(fig2)

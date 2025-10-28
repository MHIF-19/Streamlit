import streamlit as st
import pandas as pd

st.title("PSL Dashboard")

file= st.file_uploader("Upload your data in CSV type",type=['csv'])
if file:
    df=pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)
    
if file:
    st.subheader("Data Summary")
    st.write(df.describe())

if file:
    batter=df.batter.unique()
    selected_batter=st.selectbox("Filter By Batter",batter)
    filtered_data=df[df.batter==selected_batter]
    st.dataframe(filtered_data)
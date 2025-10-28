import streamlit as st
import datetime as dt

current_date=dt.date.today()

st.title("Age Calculator App")
dob=st.date_input("Enter your Date of Birth",max_value=current_date,min_value=dt.date(1900,1,1))

if dob:
    age=current_date.year-dob.year

st.write(f"You are {age} years old")
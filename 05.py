import streamlit as st
import requests

st.title("Live Currency Converter")
amount=st.number_input("Enter the amount in PKR",min_value=1)

target_currency=st.selectbox("Convert to",["USD","AUD","AED","CAD","INR","EUR","JPY","CNY"])

if st.button("Convert"):
    url="https://v6.exchangerate-api.com/v6/af819e980fb76c40fd60e238/latest/PKR"
    responses =requests.get(url)


    if responses.status_code==200:
        data=responses.json()
        rate= data["conversion_rates"][target_currency]
        converted =rate*amount
        st.success(f"{amount} PKR = {converted}{target_currency}")

    else:
        st.error("Failed to fetch conversion rate")
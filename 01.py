import streamlit as st
st.title("Hello World")
st.subheader("Made with Streamlit")
st.text("Welcome to my First Streamlit App")
st.write("Choose your favourite color")
fav_color="Blue"

color=st.selectbox("Your favourite color",["Pink","Orange","Green","Blue","Red"])

st.write(f"You choose {color}, Excellent Choice")
if color==fav_color:
    st.success(f"Your color has been picked!, which is {color}")
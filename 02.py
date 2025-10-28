import streamlit as st


st.title("Coffee Maker App")

if st.button("Make Coffee"):
    st.success("Your coffee is being made")

sugar= st.checkbox("Add Sugar")

if sugar:
    sugar_level=st.slider("Sugar Level (Spoon)",0,5,2)
    st.write(f"Sugar added to your coffee, sugar level is {sugar_level}")

coffee_type= st.radio("Pick your type of coffee",["Normal","Capichhino","Sugary","Non sugary","Karachi-style"])

st.write(f"Selected type {coffee_type}")

flavour=st.selectbox("Pick your flovour",["Black Coffee","With Milk"])

st.write(f"Selected flavour is {flavour}")

cups=st.number_input("How many cups?",min_value=1,max_value=10,step=1)

st.write(f"Selected number of cups are {cups}")

coffee_name=st.text_input("Enter the name on coffee")

if coffee_name:
    st.write(f"Welcome {coffee_name}! your coffee is on the way")

dob=st.date_input("Enter your date of birth")
if dob:
    st.write(f"Your date of birth is {dob}")
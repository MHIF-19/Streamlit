import streamlit as st

st.write("City Interest Poll")

col1, col2=st.columns(2)

with col1:
    st.header("Karachi")
    st.image("https://media.istockphoto.com/id/1127500841/photo/beautiful-view-of-bahadurabad-chorangi-karachi-pakistan.jpg?s=612x612&w=0&k=20&c=HzRA0Vbqa1zTSL88RNnUgebJZaZwDb6tZfmkXWwu89M=",width=200)
    vote1= st.button("Vote for Karachi")

with col2:
    st.header("Lahore")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJAZOpEd54rQA7-VlPDVG6braVDPmlv-S2-A&s",width=200)
    vote2= st.button("Vote for Lahore")

if vote1:
    st.success("Thanks for voting Karachi")
elif vote2:
    st.success("Thanks for voting Lahore")



name=st.sidebar.text_input("Enter your name")
city= st.sidebar.selectbox("Choose your favourite city", ["Karachi","Lahore"])

st.sidebar.write(f"Welcome {name}, I also love {city}")

with st.expander("Show Nicknames of Cities of Pakistan"):
    st.write("""
    1.City Of Lights
             
    2.City of sufi saints
             
    3.City of Lahore
             
    4.City of Pathans
""")
    
st.markdown('# Welcome to City Selector')
st.markdown('> Blockquote')

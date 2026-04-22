import streamlit as st

st.title("Youness First App")
name = st.text_input("Who is talking?")

if name:
    if name == "Youness":
        st.write("You are in love with Ikram!")
    if name == "Anas":
        st.write(f"you are in love with (7choma nktb smitha)")
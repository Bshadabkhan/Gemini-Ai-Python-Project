import streamlit as st

st.title("streamlit application")
a=None
a= st.input("enter your name")
if a == None: 
  st.write(a)
            

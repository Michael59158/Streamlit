import streamlit as st

if st.button("Home"):
    st.switch_page("projet.py")
if st.button("Conversation avec l'assistant"):
    st.switch_page("chatbot.py")
if st.button("Historique de conversation"):
    st.switch_page("histobot.py")

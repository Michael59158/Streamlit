import streamlit as st
import requests
import pandas as pd 

st.title("FAQ Streamlit Michael")

base_url = st.sidebar.text_input("Insert API URL")

option = st.sidebar.selectbox(
    "Choississez vote modele ?",
    ("gpt-4", "gpt-3", "davinci"),
)

if "messages' not in st.session_state:
    st.session_state.messages = []

if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
         st.markdown(prompt)
  
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Using "with" notation
    url = f"{base_url}insert_data"
    data = {"message": prompt}

    response_api = requests.post(url,params=data)

    if response_api.status_code == 200:
       response = f"{response_api.text}"
    else:
      response = f'Echo : "Error calling API:", {response_api.status_code}'


    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

import streamlit as st
import requests

st.title("FAQ Streamlit Michael")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
         st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    base_url = st.sidebar.text_input("Insert API URL")
    # Using "with" notation
    url = "https://378d-34-31-223-192.ngrok-free.app/insert_data"
    data = {"message": prompt}
 
    response_api = requests.post(url,params=data)

    if response_api.status_code == 200:
       response = f"Echo: {response_api.text}"
    else:
      response = f'Echo : "Error calling API:", {response_api.status_code}'

    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

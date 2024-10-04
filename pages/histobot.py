import streamlit as st
import requests
import pandas as pd 

st.title('historique de conversation')

with st.form('exec'):
    base_url = st.text_input('Insert API URL')
    submit = st.form_submit_button('Submit')
    
if submit:    
    url = f"{base_url}select_data"
    select_url = f"{base_url}select_data"
    response_api_select = requests.get(select_url)
    df = pd.DataFrame(response_api_select.json())
    st.data_editor(df)
    

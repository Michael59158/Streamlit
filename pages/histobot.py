import streamlit as st
import requests
import pandas as pd 

st.title('historique de conversation')

url = f"{base_url}select_data"
select_url = f"{base_url}select_data"
response_api_select = requests.get(select_url)
df = pd.DataFrame(response_api_select.json())
st.data_editor(df)

import streamlit as st
import pandas as pd

st.title('My Dashboard MWI')

df = pd.read_csv('data.csv')

st.write(df)

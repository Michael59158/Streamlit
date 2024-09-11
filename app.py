import streamlit as st
import pandas as pd

st.title('My Dashboard MWI')

# lecture du fichier et affectation dans un dataframe
df = pd.read_csv('data.csv')

# Envoi sur la sortie streamlit. 

if st.checkbox('afficher le jeu de données'):
  st.write(df)

#liste déroulante
st.selectbox('Selectionnez une profession :',[1,2,3,4])

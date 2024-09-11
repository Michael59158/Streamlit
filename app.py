import streamlit as st
import pandas as pd

st.title('My Dashboard MWI')

# lecture du fichier et affectation dans un dataframe
df = pd.read_csv('data.csv')

pro = df.Profession.unique()

#liste déroulante
#st.selectbox('Selectionnez une profession :',[1,2,3,4])
#liste déroulante sur la colonne Profession 
user_selectbox_pro = st.selectbox('Selectionnez une profession :',pro)

# barre de sélection de min à max, avec position par défaut sur value et déplacement d'un pas de 1
user_slider_age = st.slider('Selectionner un age : ', min_value=18, max_value=99,value=30,step=1)


# Envoi sur la sortie streamlit. 
if st.checkbox('afficher le jeu de données'):
  st.write(df[(df.Profession == user_selectbox_pro)(df.Age == user_slider_age)])

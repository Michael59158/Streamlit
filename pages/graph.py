import streamlit as st
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("Choose a file",file='csv')
if uploaded_file is not None:
    # To read file as bytes:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

    cols = dataframe.columns
    user_select_cols = st.selectbox('Selectionnez les colonnes', cols)
    #affichage de la colonne sélectionnée
    st.write(dataframe[user_select_cols])

    # graphique
    cols_selected_value = dataframe[user_select_cols]
    fig, ax = plt.subplots()
    ax.hist(cols_selected_value, bins=20)

    st.pyplot(fig)

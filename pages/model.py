import streamlit as st 

# barre de sélection de min à max, avec position par défaut sur value et déplacement d'un pas de 1
user_slider_longitude = st.slider('longitude : ', min_value=-180, max_value=180,value=0,step=1)
user_slider_latitude = st.slider('longitude : ', min_value=-180, max_value=180,value=0,step=1)


with st.form("my_form"):
  st.write("My Form")
  name = st.text.input("Your name ?")

  #every 
  submitted = st.form_submit_button("Submit")
  if submitted:
        st.write(f'Hi {name}')

import streamlit as st 




with st.form("my_form"):
  st.write("My Form")
  name = st.text_input("Your name ?")

  # barre de sélection de min à max, avec position par défaut sur value et déplacement d'un pas de 1
  user_slider_longitude = st.slider('longitude : ', min_value=-180, max_value=180,value=0,step=1)
  user_slider_latitude = st.slider('latitude : ', min_value=-180, max_value=180,value=0,step=1)

  user_slider_housing_median_age = st.slider('Median_Age : ', min_value=20, max_value=300,value=50,step=10)
  user_slider_total_rooms = st.slider('total rooms : ', min_value=50, max_value=500,value=50,step=10)
  user_slider_total_bedrooms = st.slider('total_bedrooms : ', min_value=80, max_value=180,value=100,step=5)
  user_slider_population = st.slider('population : ', min_value=2000, max_value=800000,value=50000,step=1000)
  user_slider_households = st.slider('households : ', min_value=20, max_value=300,value=50,step=10)
  user_slider_median_income = st.slider('median_income : ', min_value=2000, max_value=800000,value=50000,step=1000)


 
  #every 
  submitted = st.form_submit_button("Submit")
  if submitted:
        st.write(f'Hi {name}')

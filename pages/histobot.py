left, right = st.columns(2)
if left.button("Historique de conversation", use_container_width=True):
    url = f"{base_url}select_data"
    select_url = f"{base_url}select_data"
    response_api_select = requests.get(select_url)
    df = pd.DataFrame(response_api_select.json())
    st.data_editor(df)

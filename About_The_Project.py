import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Bienvenidos 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    En este proyecto se ha utilizado streamlit para crear una aplicación web que permite visualizar datos de Google Trends.
    ### ¿Qué es Streamlit?
    Streamlit es un framework para crear aplicaciones web de forma sencilla con Python. Puedes crear aplicaciones web interactivas con tan solo unas pocas líneas de código.
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### ¿Qué es Google Trends?
    Google Trends es una herramienta de Google que muestra cómo cambian las tendencias de búsqueda en Google con el tiempo. Puedes utilizar Google Trends para analizar la popularidad de ciertos términos de búsqueda en Google.
"""
)
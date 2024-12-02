#Pagina de Login

#Importações
import streamlit as st
import time

#Configurações principais
st.set_page_config(
    page_title = "Frangoeste - Controle de Descartes",
    page_icon = ":chicken:",
    layout = "centered",
)

#Definindo uma variavel para ficar com o formulário
login_form = st.form("index_form")


#Formulário de Login
with st.sidebar:
    titulo = st.title("Frangoeste - Controle de descartes")
    botao_login = login_form.form_submit_button(
        label = "Entrar",
        type = "secondary"
        )

#add_selectbox = st.sidebar.selectbox(
#    "How would you like to be contacted?",
#    ("Email", "Home phone", "Mobile phone")
#)

# Using "with" notation
#with st.sidebar:
#    add_radio = st.radio(
#        "Choose a shipping method",
#        ("Standard (5-15 days)", "Express (2-5 days)")
#    )
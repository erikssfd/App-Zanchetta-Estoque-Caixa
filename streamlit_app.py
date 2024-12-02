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
    login_form.title("Frangoeste - Controle de descartes")
    login_form.form_submit_button(
        label = "Entrar",
        type = "secondary"
        )
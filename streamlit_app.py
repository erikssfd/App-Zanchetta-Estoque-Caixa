#Pagina de Login

#Importações
import streamlit as st
import time

#Configurações principais
st.set_page_config(
    page_title = "Frangoeste - Controle de Descartes",
    page_icon = ":chicken:",
    layout = "wide",
)

#Definindo uma variavel para ficar com o formulário
login_form = st.form("index_form")


#Formulário de Login
with st.sidebar("menu_lateral"):
    with login_form:
        login_form.st.write("Frangoeste - Controle de descartes")

        login_form.st.text_input(
            label = "Nome de Usuário:",
            type = "default",
            placeholder = "Usuário"
            )
        login_form.st.text_input(
            label = "Senha:",
            type = "password",
            placeholder = "Senha"
            )
        login_form.st.submit_button(
            label = "Entrar",
            type = "primary",
            help = "Pressione para logar!"
            )
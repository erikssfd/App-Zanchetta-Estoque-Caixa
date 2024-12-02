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
    with login_form:
        st.title("Frangoeste - Controle de descartes")
    
        st.text_input(
            label = "Nome de Usuário:",
            type = "default",
            placeholder = "Usuário"
            )
        
        st.text_input(
            label = "Senha:",
            type = "password",
            placeholder = "Senha"
            )
        
        st.form_submit_button(
            label = "Entrar",
            type = "primary",
            help = "Pressione para logar!"
            )
#Pagina de Login

#Importações
import streamlit as st
import time

#Formulário de Login
with st.form("login_form"):
    st.write("Login")
    st.divider()
    
    st.text_input("Nome de usuario:")
    st.text_input("Senha")
    st.divider()
    
    st.form_submit_button(
        label = "Entrar",
        help = "Precisa de ajuda?",
        on_click = None,
        type = "primary"
    )
#Pagina de Login

#Importações
import streamlit as st
import time

#Configurações principais
st.set_page_config(
    page_title = "Frangoeste - Contorle de Descartes",
    page_icon = ":chicken:",
    layout = "wide",
)

#Formulário de Login
with st.form("login_form"):
    #imagem de logotipo
    #img_logo = "imagens/logotipo.png"
    #st.image(image = img_logo, caption = "Frangoeste")
    
    st.subheader("Controle de descartes")
    st.divider()
    
    st.text_input("Nome de usuario:")
    st.text_input("Senha")
    st.divider()
    
    st.form_submit_button(
        label = "Entrar",
        on_click = None,
        type = "primary"
    )
#Pagina de Login

#Configurações principais
st.set_page_config(
    page_title = "Frangoeste - Contorle de Descartes",
    page_icon = "",
    layout = "wide",
)


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

pagina1 = st.page(str = "home", path = "paginas/home.py")
pagina2 = st.page(str = "configuração", path = "paginas/configuracoes.py")
pagina3 = st.page(str = "relatorios", path = "paginas/relatorios.py")
#Pagina de Login

#Importações
import streamlit as st
import time

#Importando arquivo CSS
with open("estilo.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    
#Configurações principais
st.set_page_config(
    page_title = "Frangoeste - Controle de Descartes",
    page_icon = ":chicken:",
    layout = "centered",
)

#Definindo uma variavel para ficar com o formulário
login_form = st.form("index_form")
col1, col2 = st.columns([1, 4], gap = "large")


#Formulário de Login
with col1:
    titulo = st.title("Frangoeste - Controle de descartes")
    botao_login = login_form.form_submit_button(
        label = "Entrar",
        type = "secondary"
        )
with col2:
    texto_col2 = st.title("Seja bem-vindo")
    subtitulo_col2 = st.subheader("Controle de produção e descartes")
    #imagem_fundo = st.image()

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
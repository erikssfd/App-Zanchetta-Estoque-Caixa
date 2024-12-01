#Importando Bibliotecas
import streamlit as st
import time

#Definindo variáveis e menu lateral

#Titulo e logotipo lateral
st.title("Frangoeste - Controle de descartes")

#Menu lateral
with st.sidebar:
    st.header("Seja Bem-Vindo")
    st.divider()
    
    st.text("Papelão")
    
    forn_op = st.selectbox(
        "Forncedores",
        ("WestRock", "Sopasta", "Klabin"),
        index = None,
        placeholder = "Selecione um fornecedor:"
    )
    st.write("Voce selecionou o fornecedor: ", forn_op)
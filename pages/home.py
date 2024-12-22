#Importações
import streamlit as st
import time

# Configurações Principais da Página

# Estilo da página
st.markdown(
    """
    <style>
    
        /*Monitores e PC's*/
        
        /*Tablets*/
        @media (max-width: 1024px) {
        
        }
        
        /*Smartphones Grandes e Médios*/
        @media (max-width: 767px) {
            
        }
        
        /*Smartphones Pequenos*/
        @media (max-width: 479px) {
            
        }
        
    </style>
    """,
    unsafe_allow_html=True,
)

#Inicio Tela home

def home():

    # Iniciando um tela de orientações do usuário

    st.markdown("*Gostaria de utilizar algum recurso? * " + st.session_state.nome_user)

home()
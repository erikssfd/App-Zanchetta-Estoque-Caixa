import streamlit as st
import streamlit_app
import pandas as pd
import matplotlib.pyplot as plt

def home():
    # Nome do usuário e um breve texto do que ele irá encontrar
    st.markdown("Seja bem vindo - " + st.session_state.usuario_nome)
   # st.markdown("Seja bem vindo, abaixo está um resumo dos controles!")

    # Divisória
    st.divider()

    st.markdown("Por favor selecione as abas para ver um resumo!")

    # Criando as abas dos setores
    cortes, inteiros, paletizacao, expedicao = st.tabs(["Cortes", "Inteiros", "Paletização", "Expedição"])

    # Editando aba 1
    with cortes:
        st.header("Secundária Cortes")
        st.divider()

        # Criando um dataframe de exemplo
        df = {
            "Setor" : "Secundária Cortes",
            "Qtd_descartes" : 50,
            "Dt_descartes" : 2024-10-20,
            "Liderança" : "Leonardo Amorim",
            "motivo_descartes" : "exemplo1"       
        }



home()
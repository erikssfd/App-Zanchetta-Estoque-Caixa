import streamlit as st
import streamlit_app
import pandas as pd 

def home():
    # Nome do usuário e um breve texto do que ele irá encontrar
    st.markdown(st.session_state.usuario_nome + ", por favor selecione as abas para ver um resumo")

    # Divisória
    st.divider()

    # Criando as abas dos setores
    cortes, inteiros, paletizacao, expedicao = st.tabs(["Cortes", "Inteiros", "Paletização", "Expedição"])

    # Editando aba 1
    with cortes:
        st.header("Secundária Cortes")

        # Criando colunas
        resumo1, resumo2 = st.columns([0.5, 0.5])

        # Coluna 1
        with resumo1:

            # Criando um dataframe de exemplo
            data1 = {
            "Setor": "Cortes",
            "Qtd_Descarte": [10, 5, 7, 12],
            "Data_Descarte": ["2024-12-20", "2024-12-21", "2024-12-22", "2024-12-23"],
            "Motivo_Descarte": ["Dano físico", "Erro de processo", "Falha de empacotamento", "Produto vencido"]
            }
            
            df = pd.DataFrame(data1)
            df
        # Coluna 2
        with resumo2:
            st.markdown(" **Quantidade de caixas X Motivos** ")

            st.line_chart(
                data1, x = "Qtd_Descarte",
                y = "Motivo_Descarte",
                x_label= "Quantidade de Caixas",
                y_label= "Motivos de Descartes",
                color = [0.3, 0.6, 0.8, 1.0]
                )

    with inteiros:
        st.header("Secundária Inteiros")

        # Criando um dataframe de exemplo
        data2 = {
              "Setor": "Inteiros",
              "Qtd_Descarte": [10, 5, 7, 12],
              "Data_Descarte": ["2024-12-20", "2024-12-21", "2024-12-22", "2024-12-23"],
              "Motivo_Descarte": ["Dano físico", "Erro de processo", "Falha de empacotamento", "Produto vencido"]
              }
        df = pd.DataFrame(data2)
        df

    with paletizacao:
        st.header("Paletização")

        # Criando um dataframe de exemplo
        data3 = {
        "Setor": "Paletização",
        "Qtd_Descarte": [10, 5, 7, 12],
        "Data_Descarte": ["2024-12-20", "2024-12-21", "2024-12-22", "2024-12-23"],
        "Motivo_Descarte": ["Dano físico", "Erro de processo", "Falha de empacotamento", "Produto vencido"]
        }

        df = pd.DataFrame(data3)
        df

    with expedicao:
        st.header("Expedição")
        # Criando um dataframe de exemplo
        data4 = {
                "Setor": "Expedição",
                "Qtd_Descarte": [10, 5, 7, 12],
                "Data_Descarte": ["2024-12-20", "2024-12-21", "2024-12-22", "2024-12-23"],
                "Motivo_Descarte": ["Dano físico", "Erro de processo", "Falha de empacotamento", "Produto vencido"]
                }

        df = pd.DataFrame(data4)
        df
home()
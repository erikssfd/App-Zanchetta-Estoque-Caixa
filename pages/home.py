import streamlit as st
import streamlit_app

def home():
    st.markdown(" *No posso te ajudar hoje?* " + st.session_state.usuario_nome)

    st.markdown(
        "Possuo algumas opções bem interessantes que possa lhe interessar."
    )

home()
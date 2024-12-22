import streamlit as st

def home():
    st.markdown("*No posso te ajudar hoje? *" + st.session_state.username)

    st.markdown(
        "Possuo algumas opções bem interessantes que possa lhe interessar."
    )
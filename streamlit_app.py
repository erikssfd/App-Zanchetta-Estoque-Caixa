#Importações
import streamlit as st
# Configurações Principais da Página
st.set_page_config("Frangoeste - Controle de descartes", page_icon = ":chicken:", layout = "wide")

#Estilo da página
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            display: none !important;
        }
    
        .stFormSubmitButton > button{
            transition: 0.5s;
        }
        
        .stFormSubmitButton > button:hover {
            background-color: blue !important;
            transition: 0.6s;
        }
        
        .stForm {
            border: none !important;
            transition: 0.8s;
        }
        
        
        /*Tablets*/
        @media (max-width: 1024px){
            section[data-testid="stSidebar"] {
                display: none !important;
            }
        }
        
        /*Smartphones Grandes e Médios*/
        @media (max-width: 767px) {
            
            section[data-testid="stSidebar"] {
                display: none !important;
            }
        }
        
        /*Smartphones Pequenos*/
        @media (max-width: 479px) {
            
            section[data-testid="stSidebar"] {
                display: none !important;
            }
        }
        
    </style>
    """,
    unsafe_allow_html=True,
)

def login():
    # Definindo uma variavel para ficar com o formulário
    login_form = st.form("index_form")
    
    # Botão recuperar acesso
    btn_recuperar = st.link_button

    # Imagem e Textos
    logotipo = "images/logotipo.png"

    # Formulário de Login
    with login_form:
        
        st.image(logotipo, width = 350)
        nome_usuario = st.text_input("Nome de usuario:", key = "user_name")
        senha_usuario = st.text_input("Senha:", type = "password", key = "user_pass")
        
        botao_login = login_form.form_submit_button(
            label = "Entrar",
            type = "primary",
            )
        
        st.divider()
        
        # Link para recuperar acesso
        btn_recuperar("Recuperar Acesso", "pages/recuperacao.py")
        
        # Configurações (BACKEND)
        if botao_login:
            
            if nome_usuario == "" or senha_usuario == "":
                st.warning("Por favor verifique se existem campos em branco! :warning:")
            
            if "user_name" not in st.session_state:
                st.session_state.user_name = nome_usuario

            if nome_usuario == "ubiratansilva" and senha_usuario == "ok" or nome_usuario == "admin" and senha_usuario == "admin":
                st.switch_page("pages/home.py")
                
            else:
                st.error("Senha e usuarios invalidos! :red_circle:")

# Estanciando a Página de login
login()
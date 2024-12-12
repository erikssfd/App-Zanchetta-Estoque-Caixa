#Importações
import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
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
    
    # Paginas laterais
    sections = st.sidebar.toggle("Sections", value=False, key="opsections")
    
    nav = get_nav_from_toml(
       "../pages.toml" if sections else "../sect_pages.toml"
    )
    
    # Estanciando as paginas
    paginas = st.navigation(nav)
    
    add_page_title(paginas)
    
    paginas.run()
    
home()

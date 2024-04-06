import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title='Navbar',
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    selected = option_menu(
        menu_title="Dashboard",
        options=["Home","About","Contact"],
        icons=["house","book","envelope"],
        menu_icon="cast",
        default_index=0,
    )
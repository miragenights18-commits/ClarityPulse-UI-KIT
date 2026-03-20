import streamlit as st

def initialize_state():
    if "screen" not in st.session_state:
        st.session_state.screen = "onboarding"

    if "user_profile" not in st.session_state:
        st.session_state.user_profile = {
            "name": "",
            "age": ""
        }
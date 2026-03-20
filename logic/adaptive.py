import streamlit as st

def get_ui_config():
    profile = st.session_state.user_profile

    if int(profile["age"]) > 60:
        return {
            "font_size": "24px",
            "button_size": "large"
        }
    else:
        return {
            "font_size": "16px",
            "button_size": "normal"
        }


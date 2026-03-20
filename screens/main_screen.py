
import streamlit as st
from logic.adaptive import get_ui_config

def show_main():
    config = get_ui_config()
    

    st.markdown(f"""
        <style>
        .big-text {{
            font-size: {config['font_size']};
        }}
        </style>
    """, unsafe_allow_html=True)

    name = st.session_state.user_profile["name"]

    st.markdown(f"<p class='big-text'>Hello {name} 👋</p>", unsafe_allow_html=True)

    st.write("This is your adaptive UI")

    if st.button("Back"):
        st.session_state.screen = "onboarding"

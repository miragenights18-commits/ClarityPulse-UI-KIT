import streamlit as st


from utils.state_init import initialize_state
from screens.onboarding import show_onboarding
from screens.main_screen import show_main

initialize_state()

if st.session_state.screen == "onboarding":
    show_onboarding()

elif st.session_state.screen == "main":
    show_main()
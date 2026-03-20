import streamlit as st



def show_onboarding():
    #code for the onboarding page

    st.title("Welcome to ClarityPulse")

    name = st.text_input("enter your name")

    age = st.number_input("Enter the age",min_value= 0,max_value= 150)

    if st.button("continue"):
        st.session_state.user_profile['name'] = name
        st.session_state.user_profile['age'] = age

        st.session_state.screen = 'main'

    



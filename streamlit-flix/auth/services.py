import streamlit as st

from api.services import Auth


def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password
    )

    if response.get('error'):
        st.error(f'Falha ao realizar login: {response.get("error")}')

    else:
        st.session_state.token = response.get("access")

        st.rerun()


def logout():
    st.session_state.clear()

    st.rerun()

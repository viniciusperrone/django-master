import pandas as pd

import streamlit as st
from st_aggrid import AgGrid
from genres.services import GenreService


def show_genres():
    genre_services = GenreService()
    genres = genre_services.get_genres()

    if genres:
        st.write('Lista de Gêneros')

        genres_df = pd.json_normalize(genres)

        AgGrid(
            data=genres_df,
            reload_data=True,
            key='genres_grid'
        )

    else:
        st.warning('Nenhum gênero encontrado.')

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome de Gênero')

    if st.button('Cadastrar'):
        st.success(f'Gênero {name} cadastrado com sucesso!')

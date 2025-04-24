import pandas as pd

import streamlit as st
from st_aggrid import AgGrid


movies = [
    {
        'id': 1,
        'name': 'Titanic'
    },
    {
        'id': 2,
        'name': 'Os Mercenários'
    },
    {
        'id': 3,
        'name': 'De volta para o futuro'
    }
]

def show_movies():
    st.write('Lista de Filmes')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid'
    )

    st.title('Cadastrar novo Filme')
    name = st.text_input('Nome de Filme')

    if st.button('Cadastrar'):
        st.success(f'Filme {name} cadastrado com sucesso!')

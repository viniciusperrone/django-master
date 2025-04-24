import pandas as pd

import streamlit as st
from st_aggrid import AgGrid


reviews = [
    {
        'id': 1,
        'stars': 5
    },
    {
        'id': 2,
        'stars': 4
    },
    {
        'id': 3,
        'stars': 3
    }
]

def show_reviews():
    st.write('Lista de Avaliações')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='movies_grid'
    )

    st.title('Cadastrar nova Avaliação')
    name = st.text_input('Nome de Avaliação')

    if st.button('Cadastrar'):
        st.success(f'Availiação "{name}" cadastrado com sucesso!')

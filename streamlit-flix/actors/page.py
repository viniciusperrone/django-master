import pandas as pd
from datetime import datetime as dt

import streamlit as st
from st_aggrid import AgGrid

from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores/Atrizes')

        actors_df = pd.json_normalize(actors)

        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid'
        )

    else:
        st.warning('Nenhum Ator/Atriz encontrado.')

    st.title('Cadastrar novo(a) Ator/Atriz')
    name = st.text_input('Nome do(a) Ator/Atriz')
    birthday = st.date_input(
        label='Data de Nascimento',
        value=dt.today(),
        min_value=dt(1600, 1, 1).date(),
        max_value=dt.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ['BRAZIL', 'USA']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown
    )

    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality
        )

        if new_actor:
            st.rerun()

        else:
            st.error('Erro ao cadastrar o(a) Ator/Atriz. Verifique os campos')

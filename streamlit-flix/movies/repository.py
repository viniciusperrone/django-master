import requests

import streamlit as st

from login.service import logout


class MovieRepository:

    def __init__(self) -> None:
        self.__base_url = 'http://localhost:8000/api/v1'
        self.__movies_url = f'{self.__base_url}/movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(
            url=self.__movies_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()

            return None

        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_movie(self, movie):
        response = requests.post(
            url=self.__movies_url,
            headers=self.__headers,
            data=movie
        )

        if response.status_code == 201 or response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()

            return None

        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def get_movies_stats(self):
        response = requests.get(
            url=f'{self.__movies_url}stats/',
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()

            return None

        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

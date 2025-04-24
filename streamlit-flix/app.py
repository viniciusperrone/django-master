import streamlit as st

from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews

def main():
    st.title('Flix App')

    menu_option = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Início', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações']
    )

    if menu_option == 'Início':
        st.write('Início ')

    if menu_option == 'Gêneros':
        show_genres()

    if menu_option == 'Atores/Atrizes':
        show_actors()

    if menu_option == 'Filmes':
        show_movies()

    if menu_option == 'Avaliações':
        show_reviews()


if __name__ == '__main__':
    main()

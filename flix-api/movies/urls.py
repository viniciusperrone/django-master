from django.urls import path
from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
]
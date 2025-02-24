from django.urls import path
from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroyView, MovieStatsView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
    path('movies/stats/', MovieStatsView.as_view(), name='movie-stats'),
]
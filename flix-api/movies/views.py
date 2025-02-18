from rest_framework import generics

from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie
    serializer_class = MovieSerializer

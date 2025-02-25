from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.db.models import Count, Avg

from movies.models import Movie
from movies.serializers import MovieSerializer, MovieListDetailSerializer, MovieStatsSerializer
from reviews.models import Review

from utils.permissions import GlobalDefaultPermission

class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MovieSerializer
        else:
            return MovieListDetailSerializer

class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()


    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0
        }

        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    
from django.contrib import admin
from django.urls import path

from genres.views import create_and_list_genre_view, genre_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', create_and_list_genre_view, name='genre-create-list'),
    path('genres/<int:pk>/', genre_detail_view, name='genre-detail-list')
]

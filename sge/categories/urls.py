from django.urls import path
from categories.views import (
    CategoryListView, CategoryCreateView,
    CategoryDetailView, CategoryUpdateView,
    CategoryDeleteView, CategoryCreateListAPIView,
    CategoryRetrieveUpdateDestroyAPIView
)

from utils.api import BASIC_API_URL


urlpatterns = [
    path('categories/list', CategoryListView.as_view(), name='category_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/detail/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path(f'{BASIC_API_URL}/categories/', CategoryCreateListAPIView.as_view(), name='category-create-list-api-view'),
    path(f'{BASIC_API_URL}/categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail-api-view'),
]

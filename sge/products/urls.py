from django.urls import path
from products.views import (
    ProductListView, ProductCreateView,
    ProductDetailView, ProductUpdateView,
    ProductDeleteView, ProductCreateListAPIView,
    ProductRetrieveUpdateDestroyAPIView
)

from utils.api import BASIC_API_URL


urlpatterns = [
    path('products/list', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name="product_create"),
    path('products/<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path(f'{BASIC_API_URL}/products/', ProductCreateListAPIView.as_view(), name='product-create-list-api-view'),
    path(f'{BASIC_API_URL}/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail-api-view'),
]

from django.urls import path
from suppliers.views import (
    SupplierListView, SupplierCreateView,
    SupplierDetailView, SupplierUpdateView,
    SupplierDeleteView, SupplierCreateListAPIView,
    SupplierRetrieveUpdateDestroyAPIView
)

from utils.api import BASIC_API_URL


urlpatterns = [
    path('suppliers/list', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/detail/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),

    path(f'{BASIC_API_URL}/suppliers/', SupplierCreateListAPIView.as_view(), name='supplier-create-list-api-view'),
    path(f'{BASIC_API_URL}/suppliers/<int:pk>/', SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier-detail-api-view')
]

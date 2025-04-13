from django.urls import path
from brands.views import BrandListView, BrandCreateView


urlpatterns = [
    path('brands/list', BrandListView.as_view(), name='brand_list'),
    path('brand/create/', BrandCreateView.as_view(), name="brand_create")
]

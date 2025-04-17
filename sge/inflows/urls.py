from django.urls import path
from inflows.views import (
    InflowListView, InflowCreateView,
    InflowDetailView, InflowCreateListAPIView,
    InflowRetrieveAPIView
)

from utils.api import BASIC_API_URL


urlpatterns = [
    path('inflows/list', InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', InflowCreateView.as_view(), name="inflow_create"),
    path('inflows/<int:pk>/detail/', InflowDetailView.as_view(), name='inflow_detail'),

    path(f'{BASIC_API_URL}/inflows/', InflowCreateListAPIView.as_view(), name='inflow-create-list-api-view'),
    path(f'{BASIC_API_URL}/inflows/<int:pk>/', InflowRetrieveAPIView.as_view(), name='inflow-detail-api-view')
]

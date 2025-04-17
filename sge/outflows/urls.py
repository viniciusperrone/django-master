from django.urls import path
from outflows.views import (
    OutflowListView, OutflowCreateView,
    OutflowDetailView, OutflowCreateListAPIView,
    OutflowRetrieveAPIView
)

from utils.api import BASIC_API_URL


urlpatterns = [
    path('outflows/list', OutflowListView.as_view(), name='outflow_list'),
    path('outflows/create/', OutflowCreateView.as_view(), name="outflow_create"),
    path('outflows/<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),

    path(f'{BASIC_API_URL}/outflows/', OutflowCreateListAPIView.as_view(), name='outflow-create-list-api-view'),
    path(f'{BASIC_API_URL}/outflows/<int:pk>/', OutflowRetrieveAPIView.as_view(), name='outflow-detail-api-view')
]

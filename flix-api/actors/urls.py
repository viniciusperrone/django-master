from django.urls import path
from actors.views import ActorListCreateView, ActorRetrieveUpdateDestroyView

urlpatterns = [
    path('actors/', ActorListCreateView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail'),
]
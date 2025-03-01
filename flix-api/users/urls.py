from django.urls import path
from users.views import UserRetrieveAPIView, UserCreateAPIView


urlpatterns = [
    path('me/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('user/', UserCreateAPIView.as_view(), name='user-create'),
]

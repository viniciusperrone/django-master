from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from utils.api import BASIC_API_URL


urlpatterns = [
    path(f'{BASIC_API_URL}/authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{BASIC_API_URL}/authentication/token/refresh', TokenRefreshView.as_view(), name='token_refresh_view'),
    path(f'{BASIC_API_URL}/authentication/token/verify', TokenVerifyView.as_view(), name='token_verify'),
]

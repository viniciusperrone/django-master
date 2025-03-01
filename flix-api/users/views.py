from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserSerializer, UserCreateSerializer
from utils.permissions import GlobalDefaultPermission


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "is_staff", "permissions"]

    def get_permissions(self, obj):
        return obj.user_permissions.values_list("codename", flat=True)
    
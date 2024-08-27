from rest_framework.serializers import ModelSerializer
from library_users.models import CustomUserModel

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = "__all__"
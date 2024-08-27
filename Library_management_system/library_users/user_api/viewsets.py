from library_users.models import CustomUserModel
from .serializers import CustomUserSerializer
from rest_framework.generics import  CreateAPIView

class CreateUser(CreateAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer


from .user_api.viewsets import CreateUser
from django.urls import path

urlpatterns = [
    path('register/', CreateUser.as_view())
]

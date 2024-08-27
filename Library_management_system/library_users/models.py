from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UsersManager
# Create your models here.
class CustomUserModel(AbstractUser):
    USER_TYPE_CHOICES= [
        (1,"Admin"),
        (2,"Author"),
        (3, "User")
    ]
        
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    username =None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'address']

    objects = UsersManager()

from django.db import models
from library_users.models import CustomUserModel

# Create your models here.

class Book(models.Model):
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE,related_name='book_author')
    book_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()


 
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from books.models import Book
from library_users.models import CustomUserModel
# Create your models here.
class Reviews(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='user_review')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review')
    rating = models.IntegerField(validators=[MaxValueValidator,MinValueValidator], null=True, blank=True)
    comments = models.CharField(max_length=200, null= True, blank= True)


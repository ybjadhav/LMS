from django.db import models
from library_users.models import CustomUserModel
from books.models import Book
# Create your models here.
class BorrowBooks(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE,related_name='user_details')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    book_return_date = models.DateField(null=True,blank=True)
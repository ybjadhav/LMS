from django.contrib import admin
from .models import BorrowBooks
# Register your models here.

class BorrowBookAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'borrowed_date', 'book_return_date']

admin.site.register(BorrowBooks, BorrowBookAdmin)

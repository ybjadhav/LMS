from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['author', 'book_name', 'description', 'quantity', 'quantity']

admin.site.register(Book, BookAdmin)


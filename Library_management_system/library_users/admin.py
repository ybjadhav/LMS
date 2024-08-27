from django.contrib import admin
from .models import CustomUserModel
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone', 'address']

admin.site.register(CustomUserModel, CustomUserAdmin)

class AuthorUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'author_name', 'book_name', 'phone', 'address']
    

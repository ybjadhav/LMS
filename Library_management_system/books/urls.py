from django.urls import path
from books_api.viewsets import CreateBook, UpdateBook, DetailBook, DeleteBook, ListOfBooks

urlpatterns = [
    path('all/', ListOfBooks.as_view() ),
    path('one/<int:id>/', DetailBook.as_view()),
    path('add/', CreateBook.as_view()),
    path('update/<int:id>/', UpdateBook.as_view())
]
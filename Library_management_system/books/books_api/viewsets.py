from .serializers import BookSerializer
from books.models import Book
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class ListOfBooks(ListAPIView):
    queryset = Book
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class CreateBook(CreateAPIView):
    queryset = Book
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

class UpdateBook(RetrieveUpdateAPIView):
    queryset = Book
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

class DetailBook(RetrieveAPIView):
    queryset = Book
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

class DeleteBook(DestroyAPIView):
    queryset = Book
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

from rest_framework.serializers import ModelSerializer
from borrow_books.models import BorrowBooks

class BorrowSerializer(ModelSerializer):
    class Meta:
        model = BorrowBooks
        fields = '__all__'
from rest_framework.serializers import ModelSerializer
from book_reviews.models import Reviews

class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
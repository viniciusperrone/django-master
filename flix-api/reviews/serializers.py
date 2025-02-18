from rest_framework import serializers

from reviews.models import Movie

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
from rest_framework import serializers
from .models import RatingOptions
from .models import Movie
from .models import MovieOrder

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False, default=None)
    rating = serializers.ChoiceField(choices=RatingOptions.choices, default="G")
    synopsis = serializers.CharField(required=False, default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj: Movie):
        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127, read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2, required=True)
    buyed_by = serializers.EmailField(max_length=127, read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
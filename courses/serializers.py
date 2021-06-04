from rest_framework import serializers
from django.db.models import Avg

from .models import Course, Rating


class RatingSerializer(serializers.ModelSerializer): 
    class Meta:
        extra_kwargs = {
            'email' : {'write_only': True}
        }
        model = Rating
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rate',
            'created',
            'is_active'
        )
    
    def validate_rate(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('A avaliação precisa ser uma nota entre 1.0 e 5.0')


class CourseSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    rate_mean = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'created',
            'is_active',
            'rate_mean',
            'ratings'
        )

    def get_rate_mean(self, obj):
        mean = obj.ratings.aggregate(Avg('rate')).get('rate__avg')

        if mean is None:
            return 0
        return round(mean * 2) / 2
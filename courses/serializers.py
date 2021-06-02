from rest_framework import serializers
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


class CourseSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'created',
            'is_active',
            'ratings'
        )

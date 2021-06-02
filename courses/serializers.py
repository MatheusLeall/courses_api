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
    
    def validate_rate(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('A avaliação precisa ser uma nota entre 1.0 e 5.0')


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

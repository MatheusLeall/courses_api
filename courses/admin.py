from django.contrib import admin
from .models import Course, Rating


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'url', 
        'created', 
        'updated', 
        'is_active'
    )


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'course', 
        'name', 
        'email', 
        'rate',
        'created',
        'updated',
        'is_active'
    )

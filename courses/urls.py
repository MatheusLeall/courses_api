from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    CourseAPIView, 
    RatingAPIView, 
    CourseDetailAPIView,
    RatingDetailAPIView,
    CourseViewSet,
    RatingViewSet
)

router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course_details'),
    path('courses/<int:course_pk>/ratings/', RatingAPIView.as_view(), name='course_ratings'),
    path('courses/<int:course_pk>/ratings/<int:rating_pk>', RatingDetailAPIView.as_view(), name='course_rating_details'),
    path('ratings/', RatingAPIView.as_view(), name='ratings'),
    path('ratings/<int:rating_pk>/', RatingDetailAPIView.as_view(), name='rating_details'),
]
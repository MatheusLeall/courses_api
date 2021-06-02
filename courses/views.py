from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializer
from .permissions import IsAdminUser

"""
API versão 1
"""

class CourseAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RatingAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()


class RatingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_object(self):
        if self.kwargs.get('course_pk'):
            return generics.get_object_or_404(self.get_queryset(), 
                                              course_id=self.kwargs.get('course_pk'),
                                              pk=self.kwargs.get('rating_pk')
                                             )
        return generics.get_object_or_404(self.get_queryset(), pk=self.kwargs.get('rating_pk'))


"""
API versão 2
"""

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminUser)

    @action(detail=True, methods=['get'])
    def ratings(self, request, pk=None):
        self.pagination_class.page_size = 1
        ratings = Rating.objects.filter(course_id=pk)
        page = self.paginate_queryset(ratings)
        
        if page is not None:
            serializer = RatingSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminUser)
from rest_framework import generics, permissions
from .models import Course,Topic, Lesson
from .serializers import( 
    CourseSerializer,
    LessonSerializer, 
    TopicSerializer)

class CourseAPI(generics.ListAPIView):
    serializer_class=CourseSerializer
    queryset= Course.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]

class LessonAPI(generics.ListAPIView):
    serializer_class=LessonSerializer
    queryset= Lesson.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]


class TopicAPI(generics.ListAPIView):
    serializer_class=TopicSerializer
    queryset= Topic.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]



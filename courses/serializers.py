from rest_framework import serializers
from .models import Course, Lesson, Topic


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields='__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields='__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields='__all__'
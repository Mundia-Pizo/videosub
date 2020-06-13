from django.urls import path
from .api import CourseAPI,LessonAPI,TopicAPI

urlpatterns=[
    path('', CourseAPI.as_view(), name="courses"),
    path('lessons/', LessonAPI.as_view(), name="lessons"),
    path('topics/', TopicAPI.as_view(), name="topics"),
]




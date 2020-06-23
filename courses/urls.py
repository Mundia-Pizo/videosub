from django.urls import path
from .api import CourseAPI,LessonAPI,TopicAPI, CourseDetailAPIView

urlpatterns=[
    path('', CourseAPI.as_view(), name="courses"),
    path('<slug:slug>/lessons', LessonAPI.as_view(), name="lessons"),
    path('<int:pk>/', CourseDetailAPIView.as_view(), name="course-detail"),
    path('topics/', TopicAPI.as_view(), name="topics"),
    
]




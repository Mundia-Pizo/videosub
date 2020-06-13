from django.contrib import admin
from .models import Topic,Course,Lesson


admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Topic)

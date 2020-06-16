from django.db import models
from django.shortcuts import reverse

class Course(models.Model):
    title        = models.CharField(max_length=200)
    descritption = models.TextField()
    image        = models.ImageField(upload_to="course-images")

    def __str__(self):
        return self.title

    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse('lesson', kwargs={
    #         "slug":self.slug
    #     })

class Lesson(models.Model):
    course      = models.ForeignKey(Course, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(upload_to="lesson-images")

    def __str__(self):
        return self.title

    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse('lesson', kwargs={
    #         "course_slug":self.course.slug,
    #         "slug":self.slug
    #     })

class Topic(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title  = models.CharField(max_length=200)
    detail = models.TextField()
    video  = models.FileField(upload_to="topic-files")

    def __str__(self):
        return self.title

    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse('lesson', kwargs={
    #         "course_slug":self.course.slug,
    #         "lesson_slug":self.lesson.slug,
    #         "topic_slug":self.slug
    #     })



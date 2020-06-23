from django.db import models
from django.shortcuts import reverse

class Course(models.Model):
    title        = models.CharField(max_length=200)
    descritption = models.TextField()
    image        = models.ImageField(upload_to="course-images")
    slug         = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('lessons', kwargs={
            "slug":self.slug
        })
    @property
    def lesson(self):
        return self.lesson_set().order_by('-date')

class Lesson(models.Model):
    course      = models.ForeignKey(Course, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(upload_to="lesson-images")
    slug        = models.SlugField(null=True, blank=True)
    date        = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('lessons', kwargs={
            "course_slug":self.course.slug,
            "slug":self.slug
        })
    @property
    def topic(self):
        return self.topic_set.objects.all()
        
class Topic(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title  = models.CharField(max_length=200)
    detail = models.TextField()
    video  = models.FileField(upload_to="topic-files")
    slug   = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('lessons', kwargs={
            "course_slug":self.course.slug,
            "lesson_slug":self.lesson.slug,
            "topic_slug":self.slug
        })



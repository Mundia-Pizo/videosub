from django.db import models

class Course(models.Model):
    title        = models.CharField(max_length=200)
    descritption = models.TextField()
    image        = models.ImageField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course      = models.ForeignKey(Course, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField()
    # slug        = models.SlugField()

    def __str__(self):
        return self.title

class Topic(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title  = models.CharField(max_length=200)
    detail = models.TextField()
    video  = models.FileField()

    def __str__(self):
        return self.title



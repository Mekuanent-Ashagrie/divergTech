from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.category_name

class Teacher(models.Model):
    teache_name = models.CharField(max_length=200)
    teacher_photo = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.teache_name

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_overview = models.CharField(max_length=2000)
    course_certificate_available = models.BooleanField()
    course_image = models.ImageField(upload_to='media/')
    course_rating = models.IntegerField()
    course_duration = models.FloatField() #hours it will take to complete this course 
    course_lectures = models.IntegerField()
    course_fee = models.FloatField()
    course_skill_level = models.CharField(max_length=100)
    course_language = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    def getTechImage():
        return Teacher.objects.filter(teacher__pk=1)

class Curriculum(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    

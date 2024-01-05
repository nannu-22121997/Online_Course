from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import connections
import datetime


import datetime

class Student(AbstractUser):
    gender=models.CharField(max_length=6)
    qualification=models.CharField(max_length=15)
    date_of_birth=models.DateField(default=datetime.date.today)
    photo=models.ImageField(upload_to='photos/')
    class Meta:
        db_table='learning_Student'
        
class Course(models.Model):
    Courseid=models.IntegerField()
    coursename=models.CharField(max_length=40)
    description=models.CharField(max_length=250)
    duration=models.IntegerField()
    price=models.IntegerField()
    class Meta:
        db_table='learning_Course'

class Marks(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    studentname = models.CharField(max_length=20)
    c = models.IntegerField()
    python = models.IntegerField()
    java = models.IntegerField()
    react = models.IntegerField()
    django = models.IntegerField()
    total = models.IntegerField(null=True, blank=True)  
    passed = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = "learning_mark"




from django.db import models


# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(max_length=50)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

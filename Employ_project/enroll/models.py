from django.db import models

# Create your models here.

class Student(models.Model):

    Student_name= models.CharField(max_length=50)
    date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(unique=True , null=False)
    city = models.CharField(max_length=30)
    marks = models.IntegerField()
    pass_data = models.DateField()
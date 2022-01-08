from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50,blank=False)
    age=models.IntegerField(blank=True)
    email=models.EmailField(blank=False)
    url=models.URLField(blank=False)
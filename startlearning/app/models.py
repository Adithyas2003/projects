from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Courses(models.Model):
    
    name=models.TextField()
    dis=models.TextField()
    img=models.FileField()



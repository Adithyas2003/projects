from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class courses(models.Model):
    name=models.TextField()
    dis=models.TextField()
    img=models.FileField()



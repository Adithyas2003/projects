from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class File(models.Model):
    name=models.CharField(max_length=255)
    file=models.FileField
    dis=models.TextField


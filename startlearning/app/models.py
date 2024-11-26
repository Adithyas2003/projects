from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Courses(models.Model):
    
    name=models.TextField()
    dis=models.TextField()
    img=models.FileField()

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


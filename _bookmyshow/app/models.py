from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    votes = models.IntegerField()
    language = models.CharField(max_length=50)
    format = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    certificate = models.CharField(max_length=10)
    release_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()  # URL for the movie poster

    def __str__(self):
        return self.name

class CastMember(models.Model):
    movie = models.ForeignKey(Movie, related_name="cast", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)  # Actor's role in the movie
    image_url = models.URLField()  # URL for actor's image

    def __str__(self):
        return self.name


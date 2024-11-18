from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Movie, CastMember  # Assuming you have these models in your app.

# Create your views here.
def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)  # Fetch the movie from the database.
        cast_members = CastMember.objects.filter(movie=movie)  # Fetch cast members related to the movie.

        context = {
            'movie': movie,
            'cast': cast_members,
        }

        return render(request, 'movie_detail.html', context)

    except Movie.DoesNotExist:
        return render(request, 'index.html')  # A 404 page if movie is not found


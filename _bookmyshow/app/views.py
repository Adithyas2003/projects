from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Movie, CastMember  # Assuming you have these models in your app.

# Create your views here.
def index(req):
    return render(req,'index.html')
   
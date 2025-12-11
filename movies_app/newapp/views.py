from django.shortcuts import render
from .models import Movie

# Create your views here.
def movie_view(request):
    movie_objects = Movie.objects.all()
    
    return render(request,"newapp/movies_view.html", {"movies":movie_objects})
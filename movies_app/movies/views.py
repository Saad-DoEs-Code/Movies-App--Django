from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class ActionMovieViewSet(viewsets.ModelViewSet):
    
    queryset = Movie.objects.filter(category="Action")
    serializer_class = MovieSerializer
    
class ComedyMovieViewSet(viewsets.ModelViewSet):
    
    queryset = Movie.objects.filter(category="Comedy")
    serializer_class = MovieSerializer
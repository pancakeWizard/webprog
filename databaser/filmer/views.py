from django.shortcuts import render
from .models import *
# Create your views here.

def filmerHome(request):
    film_infos = Movie.objects.all()

    return render(request, 'filmer.html', {'film_infos':film_infos})

def directorFilmer(request, directorID):
    director_info = Director.objects.get(id=directorID)
    movies = Movie.objects.filter(director=director_info)
    context = {
        'director_info':director_info,
        'movies': movies
    }
    return render(request, 'director.html', context)
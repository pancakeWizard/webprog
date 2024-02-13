from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def filmerHome(request):
    if request.method == "POST":
        genre = request.POST.get("genre")
        year = request.POST.get("year")
        sortByYear = request.POST.get("sortera")
        filmName = request.POST.get("film")
        if filmName:
            film_infos = Movie.objects.filter(title__icontains=filmName)
        else:
            film_infos = Movie.objects.all()
        if year:
            film_infos = film_infos.filter(year=year)
        if genre != "Alla":
            film_infos = film_infos.filter(genre=genre)      
        if sortByYear:
            film_infos = film_infos.order_by("year")
    else:
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

def addFilm(request):
    directors = Director.objects.all()
    if request.method == "POST":
        title = request.POST.get("name")
        try:
            director = Director.objects.get(name=request.POST.get("director"))
        except:
            error = "något gick fel"
            return render(request, "addfilm.html", {"directors":directors, "error":error})
        year = request.POST.get("year")
        length = request.POST.get("length")
        genre = request.POST.get("genre")

        try:
            Movie.objects.create(title=title, director=director, year=year, length=length, genre=genre)
        except:
            error = "något gick fel"
            return render(request, "addfilm.html", {"directors":directors, "error":error})
        return redirect("filmerHome")
    else:
        return render(request, "addfilm.html", {"directors":directors})
    
def addDirector(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        desc = request.POST.get("description")
        try:
            Director.objects.create(name=name, age=age, description=desc)
        except: render(request, "adddirector.html", {"error":"något gick fel."})
    return render(request, "adddirector.html")
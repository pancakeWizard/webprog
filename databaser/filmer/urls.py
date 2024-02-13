from . import views

from django.urls import path, include

urlpatterns = [
    path('', views.filmerHome, name="filmerHome"),
    path('director/<int:directorID>', views.directorFilmer, name="directorFilmer"),
    path('add', views.addFilm, name="addFilm"),
    path('director', views.addDirector, name="addDirector")
]
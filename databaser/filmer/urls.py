from . import views

from django.urls import path, include

urlpatterns = [
    path('', views.filmerHome, name="filmerHome"),
    path('director/<int:directorID>', views.directorFilmer, name="directorFilmer")
]
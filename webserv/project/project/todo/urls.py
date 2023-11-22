"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.toDo, name='toDo'),
    path('task/status_finish', views.changeStatus, name='changeStatus'),
    path('add', views.toDoAdd, name='toDoAdd'),
    path('add/category', views.categoryAdd, name='categoryAdd'),
    path('add/category/', views.categoryApplier, name='categoryApplier'),
    path('add/', views.toDoAddApplier, name='toDoAddApplier'),
    path('task/<int:taskID>', views.changeTask, name='changeTask'),
    path('task/applyChange', views.changeTaskApply, name='changeTaskApply'),
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name="books"),
    path('<str:bookName>.<int:bookId>', views.bookRes, name="bookRes"),
    path('<str:bookName>.<int:bookId>/', views.bookCreateRes, name="bookCreateRes"),
    path('authors/', views.authors, name="authors"),
    path('filtred/', views.filterBooks, name="filterBooks"),
]
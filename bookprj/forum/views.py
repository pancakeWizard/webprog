from django.shortcuts import render
from . models import *

# Create your views here.
def books(request):
    books = Book.objects.all()
    data = {
        "navBookBtn": True,
        "books": books
    }
    return render(request, 'books.html', data)
from django.shortcuts import render

# Create your views here.

def block(request):
    return render(request, "block.html")

def layout(request):
    return render(request, "layout.html")
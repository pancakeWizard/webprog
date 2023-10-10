from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def testfunc(request):
    return HttpResponse("Another apps hilow world.")
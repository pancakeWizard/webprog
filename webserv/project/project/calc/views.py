from django.shortcuts import render
from django.shortcuts import redirect, reverse 
# Create your views here.

def calchome(request):
    return render(request, "calc.html")

def calc(request, number):
    result = []
    for i in range(10):
        a = number * (i+1)
        result.append(a)
    return render(request, "calc.html", {"results": result, "number":number})

def calcform(request):
    if request.method == "POST":
        try:
            number = int(request.POST.get("number"))
        except:
            return redirect('calchome')
    return redirect('calc',number)
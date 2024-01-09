from django.shortcuts import render
from django.shortcuts import redirect 
# Create your views here.

def calchome(request):
    return render(request, "calc.html")

def calc(request, number):
    """
    Funktionen som skapar själva multiplikationstabellen
    och skickar alla resultat vidare till htmlen.
    Funktionen tar emot en argument som ska vara int.
    """
    result = []
    for i in range(10):
        a = number * (i+1)
        result.append(a)
    return render(request, "calc.html", {"results": result, "number":number})

def calcform(request):
    """
    Funktioner används för att multiplicera ett tal
    som användare skriver i en form. 
    """
    if request.method == "POST":
        try:
            number = int(request.POST.get("number"))
        except:
            return redirect('calchome')
    return redirect('calc',number)
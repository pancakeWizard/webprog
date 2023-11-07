from django.shortcuts import render

# Create your views here.

def block(request):
    return render(request, "block.html")

def layout(request):
    return render(request, "layout.html")

def task(request):
    tasks = ["Diska", "Tvätta", "Dammsuga", "Spela", "Suga"]
    if request.method == "POST":
        input = request.POST.get("input")
        tasks.append(input)
    return render(request, "tasklists.html", {'tasks':tasks})
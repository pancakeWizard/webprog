from django.shortcuts import render
from .models import Celebrity

# Create your views here.
def renderCelebrity(request):
    c1 = Celebrity(name="Celebrity 1", age=20)
    c2 = Celebrity(name="Celebrity 2", age=22)
    c1.save()
    c2.save()

    celebrities = Celebrity.objects.all()
    return render(request, 'index.html', {"celebrities":celebrities})
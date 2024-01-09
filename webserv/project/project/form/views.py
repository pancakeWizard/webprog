from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse 
from django.contrib.auth import authenticate, logout, login

# Create your views here.
notConfirmed = "Du skickat in olika lösenord. Försök igen."
cannotCreateUser = "Namnet du väljer redan används."
wrongUserData = "Felaktigt användarnamn eller lösenord."
def signin(request):
    return render(request, 'signin.html')

def signin_getdata(request):
    """
    Funktionen bearbetar form från signin.
    Den tar user input och med hjälp av inbyggda
    metoder försöker skapa ett konto.
    Om lösenord inte bekräftas så ska användare inte skapas
    utan bara kunna försöka igen. Respektive fel visas.
    Om användare lyckas med att skapa ett konto då ska den 
    redirecta till logga in.
    """
    if request.method == "POST":
        password = request.POST.get("password")
        passwordConfirm = request.POST.get("passwordConfirm")
        if password == passwordConfirm:
            name  = request.POST.get("nickname")
            email = request.POST.get("email")
            try:
                user = User.objects.create_user(name, email, password)
            except:
                return render(request, 'signin.html', {"error":cannotCreateUser})
            else:
                return redirect('user_login')
        else:
            return render(request, 'signin.html', {"error":notConfirmed})
    return redirect('signin')

def user_login(request):
    return render(request, 'login.html')

def auth(request):
    """
    Funktionen bearbetar form från user_login.
    Med hjälp av inbyggda django-funktioner
    auktoriseras användare om användarnamn och
    lösenord stämmer. Annars får man försöka igen.
    Respektive fel visas.
    Om man lyckas med inloggning så ska funktionen redirecta
    till profile.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user )
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': wrongUserData})
    else:
        return redirect('user_login')
    
def profile(request):
    """
    Funktionen visar användarens profil genom att
    ta information från databas och skicka till HTMLen.
    Om användare är inte inloggat så ska hen redirectas till
    logga in.
    """
    user = request.user
    if user.is_authenticated:
        username_send = user.username
        email_send = user.email
        firstName_send = user.first_name
        lastName_send = user.last_name
        joined_send = user.date_joined
        return render(request, 'profile.html', {'username': username_send, 'email': email_send, 'name':firstName_send, 'lastname':lastName_send, 'joined':joined_send})
    else:
        return redirect('login')

def profileChange(request):
    """
    Denna funktion visar en form där man kan ändra
    sin information. Som placeholders används det 
    värde som redan finns i databas.
    Om användare är inte inloggat så ska funktionen
    redirecta till logga in.
    """
    user = request.user
    if user.is_authenticated:
        username_send = user.username
        email_send = user.email
        firstName_send = user.first_name
        lastName_send = user.last_name
        return render(request, 'profileChange.html', {'username':username_send, 'name': firstName_send, 'lastname':lastName_send, 'email': email_send})
    else:
        redirect('user_login')

def profileChangeForm(request):
    """
    Funktionen bearbetar form från profileChange.
    Funktionen tar user input och uppdaterar 
    info i databas. Därefter redirectas användare till
    sin profil.
    Om man är inte inloggat så ska man redirectas till inloggning.
    """
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            first_name = request.POST.get('firstName')
            last_name = request.POST.get('lastName')
            email = request.POST.get('email')
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            return redirect('profile')
        else:
            return redirect('profileChange')
    else:
        return redirect('user_login')

def user_logout(request):
    """
    Funktionen använder inbyggda django-funktioner
    för att logga ut användare. 
    Om användare är inte inloggat så ska hen redirektas till logga in.
    """
    user = request.user
    if user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('login')
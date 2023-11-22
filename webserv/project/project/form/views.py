from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse 
from django.contrib.auth import authenticate, logout, login

# Create your views here.
notConfirmed = "Du skickat in olika lösenord. Försök igen."
cannotCreateUser = "Namnet du väljer redan används."
wrongUserData = "Felaktigt användarnamn eller lösenord."
def signin(request, error=None):
    if not error:
        return render(request, 'signin.html')
    else:
        if error == 1:
            return render(request, 'signin.html', {"error":cannotCreateUser})
        if error == 2:
            return render(request, 'signin.html', {"error":notConfirmed})

def signin_getdata(request):
    if request.method == "POST":
        password        = request.POST.get("password")
        passwordConfirm = request.POST.get("passwordConfirm")
        if password == passwordConfirm:
            name  = request.POST.get("nickname")
            email = request.POST.get("email")
            try:
                user = User.objects.create_user(name, email, password)
            except:
                return render(request, 'signin.html', {"error":cannotCreateUser})
            else:
                return redirect('/user/login')

        else:
            return render(request, 'signin.html', {"error":notConfirmed})

def user_login(request, error=None):
    if not error:
        return render(request, 'login.html')
    else:
        return render(request, 'login.html', {"error":wrongUserData})

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': wrongUserData})
    else:
        return render(request, 'login.html')
    
def profile(request):
    user = request.user
    if user.is_authenticated:
        username_send = user.username
        email_send = user.email
        firstName_send = user.first_name
        lastName_send = user.last_name
        joined_send = user.date_joined
        return render(request, 'profile.html', {'username': username_send, 'email': email_send, 'name':firstName_send, 'lastname':lastName_send, 'joined':joined_send})
    else:
        return render(request, 'login.html', {'error': 'Logga in för att kunna se denna sidan.'})

def profileChange(request):
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
    user = request.user
    if user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('login')
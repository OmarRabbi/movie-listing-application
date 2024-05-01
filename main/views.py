from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not (first_name and email and username and password):
            messages.error(request, 'All fields are required.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'A user with that username already exists.')
            return redirect('register')

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name)
        messages.success(
            request, 'Registration successful. You can now log in.')
        return redirect('login')

    return render(request, 'register.html', {
        'page': 'register',
    })
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    context = {
        'page': 'login',
    }
    return render(request, 'login.html', context)
def logout_view(request):
    return redirect('login')



def home(request):
    context = {
        'page': 'home'
    }
    return render(request, 'home.html', context)


def movie_details(request):
    context = {
        'page': 'movie-details'
    }
    return render(request, 'movieDetails.html', context)

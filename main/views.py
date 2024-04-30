from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
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
            messages.error(
                request, 'A user with that username already exists.')
            return redirect('register')

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name)
        messages.success(
            request, 'Registration successful. You can now log in.')
        return redirect('home')

    return render(request, 'register.html', {
        'page': 'register',
    })


# def login_page(request):
#     context = {
#         'page': 'login',
#     }
#     return render(request, 'login.html', context)


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

from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('movie-details/', movie_details, name='movie_details')
]
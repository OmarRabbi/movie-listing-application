from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('movie-details/', movie_details, name='movie_details')
]
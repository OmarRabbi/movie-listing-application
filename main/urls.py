from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
     path('logout/',logout_view, name='logout'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('movie-details/', movie_details, name='movie_details')
]
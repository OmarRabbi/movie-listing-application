from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENRE_CHOICES=(
    ('A','ACTION'),
    ('CO','COMEDY'),
    ('CR','CRIME'),
    ('D','DRAMA'),
    ('F','FANTASY'),
    ('H','HORROR'),
    ('M','MYSTERY'),
    ('O', 'OTHER'),
    ('R','ROMACTIC'),
    ('SF','SCI-FI'),
    ('T','THRILLER'),
    ('W','WAR'),
    ('WE','WESTERN'),
)
CATEGORY_CHOICES =(
    ('TR', 'TOP RATED'),
    ('MW', 'MOST WATCHED'),
    ('RA', 'RECENTLY ADDED')
)
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    director = models.CharField(max_length=200)
    cast = models.CharField(max_length=700)
    genre = models.CharField(choices=GENRE_CHOICES,max_length=3)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    poster = models.URLField(max_length=1000, default=None, null=True)

    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.movie.title}"
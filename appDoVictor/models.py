from django.db import models


class Filmes(models.Model):
  title = models.CharField(max_length=50)
  director = models.CharField(max_length=70)
  genre = models.CharField(max_length=20)
  release_date = models.DateField()

class FavouriteMovies(models.Model):
  OPTIONS=[
    ('Never','N'),
    ('Sometimes','S'),
    ('Always','A')
  ]
  REVIEWRTOMATOES=[
    ('Rotten','R'),
    ('Fresh','F'),
    ('Very fresh','V')
  ]
  title = models.CharField(max_length=50)
  how_often = models.CharField(max_length=50,choices=OPTIONS)
  review=models.CharField(max_length=50,choices=REVIEWRTOMATOES)
  priority = models.IntegerField()
# Create your models here.

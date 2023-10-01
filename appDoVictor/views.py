from django.shortcuts import render, redirect
from .models import Filmes, FavouriteMovies
# Create your views here.
def mPagina(request):
  movie=Filmes.objects.all()
  fMovie=FavouriteMovies.objects.all()
  return render(request, "mPagina.html", context={'movies':movie,     
  'fMovies':fMovie })


def create_movie(request):
  if request.method == 'POST':
    Filmes.objects.create(
      title=request.POST['title'],
      director=request.POST['director'],
      genre=request.POST['genre'],
      release_date=request.POST['release_date'],
    )
    return redirect('mPagina')
  return render(request, 'forms.html',context={'action':'Adicionar'})
    
def create_favourite_movie(request):
  if request.method == 'POST':
    FavouriteMovies.objects.create(
      #OPTIONS=request.POST[OPTIONS],
      #REVIEWRTOMATOES=REQUEST.POST[REVIEWRTOMATOES],
      title=request.POST['title'],
      how_often=request.POST['how_often'],
      review=request.POST['review'],
      priority=request.POST['priority'],
    )
    return redirect('mPagina')
  options_review = FavouriteMovies.review.field.choices
  options_how_often = FavouriteMovies.how_often.field.choices
  return render(request, 'formsFMovies.html',context={'action':'Adicionar', 'options_review': options_review, 'options_how_often': options_how_often })
# Create your views here.

def update_movie(request, id):
  movie=Filmes.objects.get(id=id)
  if request.method == 'POST':
    movie.title=request.POST['title']
    movie.director=request.POST['director']
    movie.genre=request.POST['genre']
    movie.release_date=request.POST['release_date']
    movie.save()
    return redirect('mPagina')
  return render(request, 'forms.html', context={'action':'Atualizar','movies':movie})

def update_favourite_movie(request,id):
  fMovie=FavouriteMovies.objects.get(id=id)
  if request.method == 'POST':
      #OPTIONS=request.POST[OPTIONS],
      #REVIEWRTOMATOES=REQUEST.POST[REVIEWRTOMATOES],
    fMovie.title=request.POST['title']
    fMovie.how_often=request.POST['how_often']
    fMovie.review=request.POST['review']
    fMovie.priority=request.POST['priority']
    fMovie.save()
    return redirect('mPagina')
  options_review = FavouriteMovies.review.field.choices
  options_how_often = FavouriteMovies.how_often.field.choices
  return render(request, 'formsFMovies.html', context={'action':'Atualizar','fMovies':fMovie,'options_review': options_review, 'options_how_often': options_how_often })

def delete_movie(request,id):
  movie=Filmes.objects.get(id=id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      movie.delete()
    return redirect('mPagina')
  return render(request, 'are_you_sure.html', context=    
  {'movie':movie})

def delete_favourite_movie(request,id):
  fMovie=FavouriteMovies.objects.get(id=id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      fMovie.delete()
    return redirect('mPagina')
  return render(request, 'are_you_sure.html', context=    
  {'movie':fMovie})
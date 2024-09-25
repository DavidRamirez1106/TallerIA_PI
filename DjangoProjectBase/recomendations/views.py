from django.shortcuts import render
from movie.models import Movie
from .management.commands.movie_recomendations import Command
# Create your views here.

def recomendations(request):
    req = request.GET.get('searchMovie') # GET se usa para solicitar recursos de un servidor
    if req:
        movie=Command.handle(req, Command.handle)
        movies = Movie.objects.filter(title__icontains=movie)
    else:
        movies= None

    return render(request, 'recomendations.html', {'movies':movies, 'req': req}) 
    
from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    movies_list = Movie.objects.filter(status="on")
    pages = Page.objects.all()
    return render(request, 'pages/index.html', {
        'pages': pages,
        'movie_list': movies_list
    })


def movies(request):
    movies_on = Movie.objects.filter(status="on")
    movies_com = Movie.objects.filter(status="com")
    pages = Page.objects.all()

    return render(request, 'pages/movies.html', {
        'pages': pages,
        'movies_on': movies_on,
        'movies_com': movies_com
    })


def movie_information(request, slug):
    try:
        selected_film = Movie.objects.get(name=slug)
        return render(request, 'pages/movie_information.html', {
            'lolo': selected_film.name
        })
    except Exception as exc:
        return render(request, 'pages/movie_information.html', {
            'vampire_found': False
        })

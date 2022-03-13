from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'pages/index.html', {
        'movie-list': movies
    })


# def vampire_profile(request, vampire_slug):
#     try:
#         selected_vampire = Vampire.objects.get(slug=vampire_slug)
#         return render(request, 'vampire.html', {
#             'vampire_found': True,
#             'vampire_name': selected_vampire.name,
#             'vampire_title': selected_vampire.title
#         })
#     except Exception as exc:
#         return render(request, 'vampire.html', {
#             'vampire_found': False
#         })

from django.urls import path
from .models import Page
from . import views
from .models import Page

urlpatterns = [
    path(Page.objects.get(name='Home').url, views.index, name="Home"),
    # our-domain.com/Home, views.index is the template
    path(Page.objects.get(name='Movies').url, views.movies, name='Movies'),
    path(Page.objects.get(name='Movies').url + '/<slug:slug>/', views.movie_information, name='Movie information')
]

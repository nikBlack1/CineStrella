from django.urls import path
from .models import Page
from . import views


urlpatterns = [
    path('cinema/', views.index, name="Home"),  # our-domain.com/Home, views.index is the template
    # path('castle/<slug:vampire_slug>', views.vampire_profile, name='vampire-profile')
]

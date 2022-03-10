from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index, name='Home'),  # our-domain.com/Home, views.index is the template
    # path('castle/<slug:vampire_slug>', views.vampire_profile, name='vampire-profile')
]

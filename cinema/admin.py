from django.contrib import admin
from django.apps import apps
from .models import *

# Register your models here.


models = apps.get_models()


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_rating', 'duration', 'status')
    list_filter = ('age_rating', 'status')
    prepopulated_fields = {'slug': ('name',)}


class EventAdmin(admin.ModelAdmin):
    list_display = ('film', 'week_day', 'time_slot', 'hall')
    list_filter = ('week_day', 'time_slot', 'hall')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Event, EventAdmin)

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

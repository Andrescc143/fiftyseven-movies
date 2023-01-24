from django.contrib import admin
from apps.movies.models import Movie, MoviePlaylist

# Register your models here.
admin.site.register(MoviePlaylist)
admin.site.register(Movie)

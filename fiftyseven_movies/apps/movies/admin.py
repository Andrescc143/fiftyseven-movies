from django.contrib import admin
from apps.movies.models import Movie, Language, Gener, MoviePlaylist

# Register your models here.
admin.site.register(MoviePlaylist)
admin.site.register(Movie)
admin.site.register(Language)
admin.site.register(Gener)

from django.contrib import admin
from django.urls import path, include

from apps.movies.views import get_movies_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-v1/', include('apps.users.urls')),
    path('api-v1/usuario/', include('apps.users.api.urls')),
    path('api-v1/movie/', include('apps.movies.api.routers')),
    path('get-movies/', get_movies_view, name='get_movies_view'),
]

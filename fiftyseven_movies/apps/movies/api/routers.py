from rest_framework.routers import DefaultRouter

from apps.movies.api.api import PMoviePlaylistViewSet


router = DefaultRouter()

router.register(r'playlist', PMoviePlaylistViewSet, basename='playlist')

urlpatterns = router.urls
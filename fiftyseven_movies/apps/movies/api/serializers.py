from apps.movies.models import MoviePlaylist, Movie

from rest_framework import serializers      


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
        

class PMoviePlaylistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MoviePlaylist
        exclude = ('created_date',)
        

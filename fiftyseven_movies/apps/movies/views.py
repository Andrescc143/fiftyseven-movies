from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.movies.src.movies import movies
from apps.movies.models import Movie
from apps.movies.api.serializers import MovieSerializer


# Create your views here.

@api_view(['GET'])
def get_movies_view(request):
    if request.method == 'GET':
        
        for movie in movies:    
            movie_serializer = MovieSerializer(data=movie)
            

            if movie_serializer.is_valid():
                movie_serializer.save()        
                
        return Response({'message': 'Movie created correctly'}, status=status.HTTP_201_CREATED)
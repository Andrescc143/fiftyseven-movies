from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.movies.api.serializers import PMoviePlaylistSerializer
from apps.movies.models import MoviePlaylist


class PMoviePlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PMoviePlaylistSerializer
    permission_classes = (IsAuthenticated, )
    
    
    def get_queryset(self, pk=None):
        if not pk:
            return self.serializer_class.Meta.model.objects.filter(public=True)
        return  self.serializer_class.Meta.model.objects.filter(owner=pk, public=False) 
    
    
    def retrieve(self, request, *args, **kwargs):
        
        playlists = self.get_queryset(pk)
        
        if not playlists:        
            serializer = self.serializer_class(playlists, many=True)
            
            return Response({'message': 'Private data retrieved correctly.',
                            'data': serializer.data}, status=status.HTTP_200_OK)
            
        return Response({'error': 'No private movie playlists were found associated to this user.'},
                         status=status.HTTP_404_NOT_FOUND)

        
    
    

class PrivateMoviePlaylistViewSet(viewsets.ViewSet):
    serializer_class = PMoviePlaylistSerializer
    #permission_classes = (IsAuthenticated, )
    
    queryset = serializer_class.Meta.model.objects.filter(public=False)
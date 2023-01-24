from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.movies.api.serializers import PMoviePlaylistSerializer
from apps.movies.models import MoviePlaylist

from apps.users.api.serializers import UserSerializer


class PMoviePlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PMoviePlaylistSerializer
    permission_classes = (IsAuthenticated, )
    
    
    def get_queryset(self, pk=None):
        if not pk:
            return self.serializer_class.Meta.model.objects.filter(public=True)
        
        return self.serializer_class.Meta.model.objects.filter(owner=pk, public=False)
        
    
    
    def retrieve(self, request, *args, **kwargs):
        
        playlists = self.get_queryset(kwargs['pk'])
        
        if playlists:        
            serializer = self.serializer_class(playlists, many=True)
        
            if int(kwargs['pk']) == self.request.user.id:
                
                return Response({'message': 'Private data retrieved correctly.',
                                'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'You do not have access to others private playlists',
                                'data': serializer.data}, status=status.HTTP_401_UNAUTHORIZED)
            
        return Response({'error': 'No private movie playlists were found associated to this user.'},
                         status=status.HTTP_404_NOT_FOUND)
        
    
    def update(self, request, *args, **kwargs):
        
        playlist = self.serializer_class.Meta.model.objects.filter(id=kwargs['pk']).first()
        print(playlist)
        if playlist:        
            playlist_serializer = self.serializer_class(playlist, data=request.data)
            
            if playlist_serializer.is_valid():
        
                if playlist.owner.id == self.request.user.id:
                    playlist_serializer.save()
                    
                    return Response({'message': 'Playlist data updated correctly.',
                                    'data': playlist_serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'You do not have access to others private playlists',
                                    'data': playlist_serializer.data}, status=status.HTTP_401_UNAUTHORIZED)
                
            return Response({'error': playlist_serializer.errors},
                         status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'error': 'No any playlist was found with the id provided.'},
                         status=status.HTTP_404_NOT_FOUND)

        
    
    

class PrivateMoviePlaylistViewSet(viewsets.ViewSet):
    serializer_class = PMoviePlaylistSerializer
    #permission_classes = (IsAuthenticated, )
    
    queryset = serializer_class.Meta.model.objects.filter(public=False)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.api.serializers import UserSerializer


@api_view(['GET', 'DELETE'])
def user_detail_api_view(request, pk):
    user = User.objects.filter(id=pk).first()    

    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)

            return Response(user_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            user.delete()

            return Response({'message': 'User deleted correctly'}, status=status.HTTP_200_OK)

    return Response({'message':'User not found'},  status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated, )
    
    queryset = serializer_class.Meta.model.objects.all().values('id', 'email', 'password')
    
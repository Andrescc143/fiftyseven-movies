from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

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


@api_view(['GET', 'POST'])
def user_api_view(request):
    #to plot the total list of users
    if request.method == 'GET':
        users = User.objects.all().values('id', 'email', 'password')
        users_serialized = UserSerializer(users, many=True)

        return Response(users_serialized.data, status=status.HTTP_200_OK)
    

    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'User created correctly', 'data': user_serializer.data}, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
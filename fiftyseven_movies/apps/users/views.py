from django.contrib.auth import authenticate

from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.api.serializers import UserSerializer, CustomTokenObtainPairView
from apps.users.api.api import User


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairView
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        
        user_serializer = UserSerializer(data=request.data)
        
        #Getting the errors in case of unsuccesful validation
        if not user_serializer.is_valid():
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(
            email = email,
            password = password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            
            if login_serializer.is_valid():
                return Response({
                    'message': 'Session initiated correctly',
                    'token': login_serializer.validated_data['access'],
                    'refresh-token': login_serializer.validated_data['refresh'],
                    'user': user_serializer.data
                }, status=status.HTTP_200_OK)
            
        return Response({
                    'error': 'No user was found with the credentials provided'
                }, status=status.HTTP_400_BAD_REQUEST)
            


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', ''))
        
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({
                'message': 'session closed correctly'
            }, status=status.HTTP_200_OK)
            
        return Response({
                    'error': 'No user was found.'
                }, status=status.HTTP_400_BAD_REQUEST)
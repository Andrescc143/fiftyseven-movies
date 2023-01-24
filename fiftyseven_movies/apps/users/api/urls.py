from django.urls import path, include
from apps.users.api.api import user_detail_api_view#, user_api_v
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('<int:pk>/', user_detail_api_view, name='user_detail_api_view'),
    path('', include('apps.users.api.routers')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('', user_api_view, name='user_api') 
]

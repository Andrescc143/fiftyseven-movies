from django.urls import path
from apps.users.api.api import user_detail_api_view, user_api_view


urlpatterns = [
    path('<int:pk>/', user_detail_api_view, name='user_detail_api_view'),
    path('', user_api_view, name='user_api') 
]

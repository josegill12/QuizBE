# users/urls.py
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserList, UserDetail

urlpatterns = [
  path('', include('djoser.urls')),
  path('', include('djoser.urls.authtoken')),
  path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
  path('users/users', UserList.as_view(), name='user-list'),
  path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
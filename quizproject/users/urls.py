# users/urls.py
from django.urls import path, include
from .views import UserList, UserDetail

urlpatterns = [
    # Including Djoser URLs for auth-related operations
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),

    # Endpoint for listing and creating users
    # This might be redundant with Djoser's user creation endpoint
    path('users/', UserList.as_view(), name='user-list'),

    # Endpoint for retrieving, updating, and deleting a user
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
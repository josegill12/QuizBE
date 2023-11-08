from .models import User  # Import your custom user model
from rest_framework import authentication
from rest_framework import exceptions

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return None
        try:
            # Make sure you're using the correct user model and token field
            user = User.objects.get(auth_token=token)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return (user, None)
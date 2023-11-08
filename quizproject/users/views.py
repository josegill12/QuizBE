from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from requests import Response
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import generics

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
   if created:
       Token.objects.create(user=instance)

class UserDetail(RetrieveUpdateDestroyAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer

   async def retrieve(self, request, *args, **kwargs):
       instance = await self.get_object()
       serializer = UserSerializer(instance)
       return Response(serializer.data)

   async def update(self, request, *args, **kwargs):
       instance = await self.get_object()
       serializer = UserSerializer(instance, data=request.data)
       if serializer.is_valid():
           await serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=400)



class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class UserProfileviewset(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    async def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            await serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

# class User
    

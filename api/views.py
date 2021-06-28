from .serializers import UsersSerializer
from rest_framework import generics
from django.contrib.auth.models import User
 

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
   

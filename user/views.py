from django.shortcuts import render
from rest_framework import generics

from user.models import Profile
from user.serializers import RegistrationUserSerializer, UserSerializer


# Create your views here.
# class RegistrationView(generics.CreateAPIView):
#     serializer_class = RegistrationUserSerializer
#

class ListUser(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
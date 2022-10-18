from django.shortcuts import render
from rest_framework import viewsets

from user.models import Profile
from user.serializers import RegistrationUserSerializer


# Create your views here.
class RegistrationView():
    template_name = 'user/create_update_user.html'
    serializer_class = RegistrationUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
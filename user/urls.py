from django.urls import path
from rest_framework import routers

from .views import ListUser

# router = routers.DefaultRouter()
# router.register('users', ListUser)
urlpatterns = [
    path('userlist/', ListUser.as_view(), name='list')
]
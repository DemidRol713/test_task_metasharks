from django.urls import path, include
from rest_framework import routers

from .api import OrderViewSet, ListColorApiView, ListBrandAutoApiView

router = routers.DefaultRouter()
router.register('order', OrderViewSet),

urlpatterns = [
    path('list_orders/colors/', ListColorApiView.as_view()),
    path('list_orders/brands/', ListBrandAutoApiView.as_view()),
    path(r'', include(router.urls))
]
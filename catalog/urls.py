from django.urls import path, include
from rest_framework import routers

from catalog.api import ColorViewSet, BrandAutoViewSet, ModelAutoViewSet

router = routers.DefaultRouter()

router.register('color', ColorViewSet)
router.register('model_auto', ModelAutoViewSet)
router.register('brand_auto', BrandAutoViewSet)


urlpatterns = [
    path(r'', include(router.urls))
]
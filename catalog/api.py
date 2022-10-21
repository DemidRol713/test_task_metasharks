from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import viewsets

from catalog.models import Color, BrandAuto, ModelAuto
from catalog.serializers import ColorSerializer, BrandAutoSerializer, ModelAutoSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        color_serializer = self.serializer_class(data=request.data)
        if color_serializer.is_valid():
            color_serializer.save()
            return Response(data=color_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=color_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        color = get_object_or_404(Color.objects.all(), pk=int(kwargs['pk']))
        color_serializer = self.serializer_class(color, data=request.data)
        if color_serializer.is_valid():
            color_serializer.save()
            return Response(data=color_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=color_serializer.data, status=status.HTTP_400_BAD_REQUEST)


class BrandAutoViewSet(viewsets.ModelViewSet):
    queryset = BrandAuto.objects.all()
    serializer_class = BrandAutoSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        brand_auto_serializer = self.serializer_class(data=request.data)
        if brand_auto_serializer.is_valid():
            brand_auto_serializer.save()
            return Response(data=brand_auto_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=brand_auto_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        brand_auto = get_object_or_404(BrandAuto.objects.all(), pk=int(kwargs['pk']))
        brand_auto_serializer = self.serializer_class(brand_auto, data=request.data)
        if brand_auto_serializer.is_valid():
            brand_auto_serializer.save()
            return Response(data=brand_auto_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=brand_auto_serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ModelAutoViewSet(viewsets.ModelViewSet):
    queryset = ModelAuto.objects.all()
    serializer_class = ModelAutoSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        model_auto_serializer = self.serializer_class(data=request.data)
        if model_auto_serializer.is_valid():
            model_auto_serializer.save()
            return Response(data=model_auto_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=model_auto_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        model_auto = get_object_or_404(BrandAuto.objects.all(), pk=int(kwargs['pk']))
        model_auto_serializer = self.serializer_class(model_auto, data=request.data)
        if model_auto_serializer.is_valid():
            model_auto_serializer.save()
            return Response(data=model_auto_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=model_auto_serializer.data, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status, generics
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import viewsets

from catalog.models import Color, BrandAuto
from .models import Order
from .serializers import OrderSerializer, ListOrdersWithColorSerializer, ListOrdersWithBrandAutoSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['amount', 'model__brand__name']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        order = get_object_or_404(Order.objects.all(), pk=int(kwargs['pk']))
        order_serializer = self.serializer_class(order, data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(data=order_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=order_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        order_serializer = self.serializer_class(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(data=order_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=order_serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ListColorApiView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ListOrdersWithColorSerializer
    pagination_class = StandardResultsSetPagination


class ListBrandAutoApiView(generics.ListAPIView):
    queryset = BrandAuto.objects.all()
    serializer_class = ListOrdersWithBrandAutoSerializer
    pagination_class = StandardResultsSetPagination

from django.db.models import QuerySet
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order
# from rest_framework.viewsets import

from .serializers import OrderSerializer, CreateOrderSerializer


class CreateOrderView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):

        order_serializer = self.serializer_class(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(data=order_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=order_serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ListOrderView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
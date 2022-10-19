from django.utils import timezone
from rest_framework import serializers

from catalog.models import ModelAuto, Color
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.Serializer):
    model = serializers.SlugRelatedField(
        slug_field='name',
        required=True,
        queryset=ModelAuto.objects,
    )
    color = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Color.objects,
        required=True
    )
    amount = serializers.IntegerField(required=True)
    date_created = serializers.DateField(
        format='%Y-%m-%d',
        default=timezone.now().strftime('%Y-%m-%d'),
        input_formats=['%Y-%m-%d',]
    )

    def create(self, validated_data):
        validated_data['brand'] = validated_data['model'].brand
        return Order.objects.create(**validated_data)
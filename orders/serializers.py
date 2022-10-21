from django.utils import timezone
from rest_framework import serializers

from catalog.models import ModelAuto, Color
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    model = serializers.SlugRelatedField(
        slug_field='name',
        queryset=ModelAuto.objects,
        required=True
    )
    brand = serializers.SlugRelatedField(
        slug_field='name',
        source='model.brand',
        read_only=True
    )

    amount = serializers.IntegerField(required=True)
    color = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Color.objects,
        required=True
    )

    date_created = serializers.DateField(
        format='%Y-%m-%d',
        initial=timezone.now().strftime('%Y-%m-%d'),
        default=timezone.now().strftime('%Y-%m-%d'),
        input_formats=['%Y-%m-%d', ]
    )

    class Meta:
        model = Order
        fields = ('brand', 'model', 'color', 'amount', 'date_created',)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.color = validated_data.get('color', instance.color)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        return instance


class CreateOrderSerializer(serializers.Serializer):
    model = serializers.SlugRelatedField(
        slug_field='name',
        required=True,
        queryset=ModelAuto.objects
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
        input_formats=['%Y-%m-%d', ]
    )

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.color = validated_data.get('color', instance.color)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        return instance


class ListOrdersWithColorSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    amount_order = serializers.IntegerField(default=0, read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['amount_order'] = Order().get_amount_of_orders_with_color(color_id=representation['id'])

        return representation


class ListOrdersWithBrandAutoSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    amount_order = serializers.IntegerField(default=0, read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['amount_order'] = Order().get_amount_of_orders_with_brand_auto(brand_id=representation['id'])

        return representation




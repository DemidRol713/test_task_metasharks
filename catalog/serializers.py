from rest_framework import serializers

from catalog.models import ModelAuto, Color, BrandAuto


class ColorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)

    class Meta:
        model = Color
        fields = '__all__'

    def create(self, validated_data):
        return Color.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance


class ListOrdersWithColorSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(read_only=True)
    amount_order = serializers.IntegerField(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['amount_order'] = instance.get_amount_of_orders_with_color(representation['id'])

        return representation



class ModelAutoSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        slug_field='name',
        queryset=BrandAuto.objects,
        required=True
    )
    name = serializers.CharField(max_length=30, required=True)

    class Meta:
        model = ModelAuto
        fields = '__all__'

    def create(self, validated_data):
        return ModelAuto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.brand = validated_data.get('brand', instance.brand)
        return instance


class BrandAutoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=30)

    class Meta:
        model = BrandAuto
        fields = '__all__'

    def create(self, validated_data):
        return BrandAuto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance



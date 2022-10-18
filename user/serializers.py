from rest_framework import serializers

from user.models import Profile


class RegistrationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
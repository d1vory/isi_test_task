from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16, write_only=True)
    password_repeat = serializers.CharField(max_length=16, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'password_repeat')

    def validate_password(self, value):
        try:
            password_validation.validate_password(value)
        except DjangoValidationError as e:
            raise ValidationError(e.messages) from e
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password_repeat = attrs.pop('password_repeat', None)
        if password != password_repeat:
            raise ValidationError('passwords are not matching')
        return attrs


    def create(self, validated_data):
        instance = User.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        return instance
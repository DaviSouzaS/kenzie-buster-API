from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField(max_length=150, validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")])

    email = serializers.EmailField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")])

    password = serializers.CharField(max_length=127, write_only=True)

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(default=False, allow_null=True)
    is_superuser = serializers.BooleanField(default=False, allow_null=True, read_only=True)

    def create(self, validated_data):
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(instance.password)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, write_only=True)
    password = serializers.CharField(max_length=127, write_only=True)

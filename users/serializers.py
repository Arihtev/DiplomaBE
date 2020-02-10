from django.contrib.auth import authenticate
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler

from .models import User


class UserSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False)

    class Meta:
        model = User
        fields = '__all__'
        # ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'user_type', 'gender', 'photo',
        #  'cars_owned')


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'birth_date', 'phone')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class OwnerSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'gender', 'photo', 'phone', 'birth_date')

    def get_image_url(self, obj):
        return "http://127.0.0.1:8000/media/" + str(obj.photo)


class FavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('favourite_cars', )

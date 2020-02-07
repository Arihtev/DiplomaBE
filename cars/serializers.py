from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from users.serializers import OwnerSerializer
from users.models import User
from .models import Car, Picture, ExtraCategory, Extra


class PicSerializer(serializers.ModelSerializer):
    picture = Base64ImageField(required=False)

    class Meta:
        model = Picture
        fields = ('picture',)


class GetPicSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Picture
        fields = ('picture',)

    def get_image_url(self, obj):
        return "http://127.0.0.1:8000/media/" + str(obj.picture)


class ExtraCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraCategory
        fields = ('id', 'name')


class ExtraSerializer(serializers.ModelSerializer):
    # category_id = ExtraCategorySerializer(many=False)

    class Meta:
        model = Extra
        fields = ('id', 'category_id', 'name')


class CarListSerializer(serializers.ModelSerializer):
    # extras = ExtraSerializer(many=True)
    pictures = GetPicSerializer(many=True)
    owner = OwnerSerializer(many=False)

    class Meta:
        model = Car
        fields = ('id', 'owner', 'year', 'make', 'model', 'transmission', 'engine_type', 'category', 'region', 'city',
                  'address', 'pictures', 'seats', 'consumption', 'horsepower', 'included_km', 'price_per_extra_km',
                  'price', 'weekly_discount', 'monthly_discount')


class CarDetailsSerializer(serializers.ModelSerializer):
    extras = ExtraSerializer(many=True)
    pictures = GetPicSerializer(many=True)
    owner = OwnerSerializer(many=False)

    class Meta:
        model = Car
        fields = '__all__'


class CarCreateSerializer(serializers.ModelSerializer):
    pictures = PicSerializer(many=True)

    class Meta:
        model = Car
        fields = ('year', 'make', 'model', 'transmission', 'engine_type', 'category', 'region', 'city', 'address',
                  'zip_code', 'description', 'pictures', 'seats', 'consumption', 'horsepower', 'extras', 'pets',
                  'smoking', 'included_km', 'price_per_extra_km', 'price', 'weekly_discount',
                  'monthly_discount')
        read_only_fields = ('owner',)

    def create(self, validated_data):
        owner = self.context['request'].user
        extras_data = validated_data.pop('extras')
        pictures_data = validated_data.pop('pictures')
        car = Car.objects.create(owner=owner, **validated_data)
        owner.cars_owned.add(car)
        for picture_data in pictures_data:
            instance = Picture.objects.create(**picture_data)
            car.pictures.add(instance)
        for extra_data in extras_data:
            car.extras.add(extra_data)
        return car

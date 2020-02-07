from rest_framework import serializers

from cars.serializers import CarListSerializer
from users.serializers import OwnerSerializer
from .models import Reservation, Review


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'


class UserReservationsSerializer(serializers.ModelSerializer):
    car_id = CarListSerializer(many=False)
    renter_id = OwnerSerializer(many=False)

    class Meta:
        model = Reservation
        fields = '__all__'


class CarReservationsSerializer(serializers.ModelSerializer):
    renter_id = OwnerSerializer(many=False)

    class Meta:
        model = Reservation
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

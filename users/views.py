import datetime

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, exceptions, status
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.views import ObtainJSONWebToken, jwt_response_payload_handler
from rest_framework_jwt.settings import api_settings

from cars.models import Car
from cars.serializers import CarListSerializer
from .permissions import IsAdmin, IsUser
from .serializers import UserSerializer, CreateUserSerializer, FavouriteSerializer
from .models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdmin]


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    # permission_classes = [IsAdmin]


class CheckUsername(APIView):

    def post(self, request):
        username = request.data.get('username')
        return Response(username in [user.username for user in User.objects.all()])


class CheckEmail(APIView):

    def post(self, request):
        username = request.data.get('email')
        return Response(username in [user.email for user in User.objects.all()])


class OwnUserRUD(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    # permission_classes = [IsUser]

    def patch(self, request, *args, **kwargs):
        user = User.objects.get(id=1)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data="wrong parameters")


class AddFavourite(APIView):
    serializer_class = FavouriteSerializer

    def post(self, request):
        user = get_object_or_404(User, id=request.user.id)
        car = get_object_or_404(Car, id=request.data.get('id'))
        if user.favourite_cars.filter(id=car.id).exists():
            user.favourite_cars.remove(car)
            # raise ValueError("Exists")
            return Response("Премахнат от любими!", status=status.HTTP_200_OK)

        user.favourite_cars.add(car)
        return Response("Добавен в любими!", status=status.HTTP_200_OK)
# self.request.user.favourite_cars.all()


class Favourites(APIView):

    def get(self, request):
        cars = request.user.favourite_cars.all()
        cars_data = CarListSerializer(cars, many=True).data
        for car in cars_data:
            car_entity = Car.objects.get(pk=car['id'])
            reviews = car_entity.review_set.all()
            car['rating'] = self.get_rating(reviews)
            car['times_rented'] = reviews.count()

        return Response(cars_data, status=status.HTTP_200_OK)

    def get_rating(self, reviews):
        if not reviews:
            return 0
        rates = []
        for review in reviews:
            rates.append(review.rate)
        return round(sum(rates) / len(rates), 1)

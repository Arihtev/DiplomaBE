import datetime
import sys
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from reservations.models import Reservation
from users.models import User
from users.permissions import IsAdmin, IsUser
from users.serializers import UserSerializer, OwnerSerializer
from .models import Car, Picture, ExtraCategory, Extra
from .serializers import CarListSerializer, PicSerializer, ExtraCategorySerializer, ExtraSerializer, \
    CarCreateSerializer, CarDetailsSerializer
from reservations.serializers import ReservationSerializer, ReviewSerializer


class CarListView(APIView):
    # queryset = Car.objects.filter(id=15)
    # serializer_class = CarListSerializer

    def get(self, request):
        # user = self.request.start_date
        cars = []
        if request.query_params:
            start = datetime.datetime.strptime(self.request.query_params['start_date'], "%Y-%m-%d").date()
            end = datetime.datetime.strptime(self.request.query_params['end_date'], "%Y-%m-%d").date()
            # start_date = datetime.datetime.strptime(start, "%Y-%m-%d").date()
            for car in Car.objects.all():
                all_reservations = car.reservation_set.all().order_by('start_date')
                if self.check_dates(start, end, all_reservations):
                    # raise ValueError(car.id)
                    cars.append(car)
        else:
            cars = Car.objects.all()
            # return cars
            # TO DO: filter by availability, maybe add method to Car class
        cars_data = CarListSerializer(cars, many=True).data
        for car in cars_data:
            # raise ValueError(car)
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
        return round(sum(rates)/len(rates), 1)

    def check_dates(self, start, end, all_reservations):
        if not all_reservations:
            return True
        if end < all_reservations.first().start_date or start > all_reservations.last().end_date:
            return True
        else:
            for index, reservation in enumerate(all_reservations):
                end2 = reservation.end_date
                try:
                    next_reservation = all_reservations[index + 1]
                except IndexError:
                    next_reservation = 'null'
                if next_reservation and end2 < start and end < next_reservation.start_date:
                    return True
            return False


class CarDetailsView(APIView):
    # queryset = Car.objects.all()
    # serializer_class = CarSerializer
    # lookup_field = 'pk'
    # # permission_classes = [IsUser]

    def get(self, request, pk):
        car = get_object_or_404(Car, id=pk)
        reservations_set = car.reservation_set.all()
        reviews_set = car.review_set.all()
        reservations = ReservationSerializer(reservations_set, many=True).data
        reviews = ReviewSerializer(reviews_set, many=True).data
        car_data = CarDetailsSerializer(car, many=False).data
        for review in reviews:
            reservation = Reservation.objects.get(pk=review['reservation'])
            review['reservation'] = ReservationSerializer(reservation, many=False).data
            renter_id = User.objects.get(pk=review['reservation']['renter_id'])
            review['reservation']['renter_id'] = OwnerSerializer(renter_id, many=False).data
        # picturess = GetPicSerializer(car.pictures, many=True).data
        # raise exceptions.ValidationError(picturess)
        car_data['reservations'] = reservations
        car_data['reviews'] = reviews
        car_data['rating'] = self.get_rating(reviews_set)
        car_data['times_rented'] = reviews_set.count()

        return Response(car_data, status=status.HTTP_200_OK)

    def get_rating(self, reviews):
        if not reviews:
            return 0
        rates = []
        for review in reviews:
            rates.append(review.rate)
        return round(sum(rates)/len(rates), 1)


class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer
    permission_classes = [IsUser]

    # def perform_create(self, serializer):
    #     # owner = User.objects.filter(id=self.request.user.id).first()
    #     owner = self.request.user
    #     # serializer.save(owner=owner)
    #     raise Exception(owner)


class CarUpdateView(APIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer
    lookup_field = 'pk'

    # permission_classes = [IsUser]

    def patch(self, request, *args, **kwargs):
        # raise ValueError(self.kwargs.get('pk'))
        pk = self.kwargs.get('pk')
        car = Car.objects.get(id=pk)
        serializer = CarCreateSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data="wrong parameters")


class PictureCreateView(generics.CreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PicSerializer


class ExtraCategoryLC(generics.ListCreateAPIView):
    queryset = ExtraCategory.objects.all()
    serializer_class = ExtraCategorySerializer


class ExtraLC(generics.ListCreateAPIView):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer
    permission_classes = [IsUser]

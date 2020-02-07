from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status, exceptions
from rest_framework.views import APIView

from .models import Reservation
from .serializers import ReservationSerializer, UserReservationsSerializer, CarReservationsSerializer, ReviewSerializer
from rest_framework.response import Response
from datetime import date, datetime


class ReservationsLCView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        start = serializer.validated_data['start_date']
        end = serializer.validated_data['end_date']
        car = serializer.validated_data['car_id']
        all_reservations = car.reservation_set.all().order_by('start_date')
        if self.check_dates(start, end, all_reservations):
            serializer.save()
        else:
            raise exceptions.ValidationError("This date has been booked already!")

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


class UserReservationsView(APIView):
    # serializer_class = UserReservationsSerializer

    def get(self, request):
        # raise ValueError(self.request.user.id)
        reservations = Reservation.objects.filter(renter_id=self.request.user.id).order_by('start_date')
        serializer = UserReservationsSerializer(reservations, many=True)
        for res in serializer.data:
            res['present'] = self.present(res['end_date'], res['status'])
        return Response(serializer.data)

    def present(self, end, status):
        return datetime.strptime(end, '%Y-%m-%d').date() >= date.today() and status == 'paid'


class CarReservationsView(APIView):

    def get(self, request, pk):
        reservations = Reservation.objects.filter(car_id=pk).order_by('-start_date')
        serializer = CarReservationsSerializer(reservations, many=True)
        for res in serializer.data:
            res['present'] = self.present(res['end_date'], res['status'])
        return Response(serializer.data)

    def present(self, end, status):
        return datetime.strptime(end, '%Y-%m-%d').date() >= date.today() and status == 'paid'


class ReservationCancelView(APIView):

    def patch(self, request, pk):
        reservation = Reservation.objects.filter(id=pk).first()
        serializer = CarReservationsSerializer(reservation, data=request.data, many=False, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateReview(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        reservation = serializer.validated_data['reservation']
        reservation.reviewed = True
        reservation.save()
        serializer.save()
        # raise ValueError(serializer.data)

from django.db import models
import datetime


class Reservation(models.Model):
    car_id = models.ForeignKey('cars.Car', on_delete=models.CASCADE)
    renter_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date)
    end_date = models.DateField(default=datetime.date)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    days_reserved = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=20, default='paid')
    reviewed = models.BooleanField(default=False)


class Review(models.Model):
    car_id = models.ForeignKey('cars.Car', on_delete=models.CASCADE)
    reservation = models.ForeignKey('reservations.Reservation', on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, default='')
    rate = models.PositiveSmallIntegerField()
    date = models.DateTimeField(default=datetime.datetime)

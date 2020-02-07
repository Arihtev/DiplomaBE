from django.db import models
# from users.models import User
from reservations.models import Reservation


class ExtraCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Extra(models.Model):
    category_id = models.ForeignKey(ExtraCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Picture(models.Model):
    # car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d', max_length=255, null=True, blank=True)


class Car(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.PROTECT)
    year = models.PositiveSmallIntegerField()
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200, default="")
    transmission = models.CharField(max_length=50, default="")
    engine_type = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=50, default="")

    price = models.DecimalField(max_digits=6, decimal_places=2)
    weekly_discount = models.PositiveSmallIntegerField()
    monthly_discount = models.PositiveSmallIntegerField()
    included_km = models.PositiveSmallIntegerField()
    price_per_extra_km = models.DecimalField(max_digits=5, decimal_places=2)

    region = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    zip_code = models.PositiveSmallIntegerField()

    description = models.CharField(max_length=550, null=True, blank=True)
    pictures = models.ManyToManyField(Picture, blank=True)
    # picture = models.ImageField(upload_to='photos/%Y/%m/%d', max_length=255, null=True, blank=True)
    seats = models.PositiveSmallIntegerField()
    consumption = models.DecimalField(max_digits=5, decimal_places=1)
    horsepower = models.PositiveSmallIntegerField()

    extras = models.ManyToManyField(Extra, blank=True)
    pets = models.BooleanField(null=True, blank=True)
    smoking = models.BooleanField(null=True, blank=True)
    # min_rent = models.CharField(max_length=10, null=True, blank=True)
    # max_rent = models.CharField(max_length=10, null=True, blank=True)

    # reservations = models.ForeignKey(Reservation, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.make} - {self.model}'

    # def reservations(self):
    #     # pass
    #     # return Reservation.objects.filter(id=self.id)
    #     return reservations_set

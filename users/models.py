from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
# Create your models here.
from cars.models import Car
from .enums import GenderTypesEnum


class User(AbstractUser):
    GENDER_TYPES = (
        (GenderTypesEnum.MALE.value, GenderTypesEnum.MALE.value),
        (GenderTypesEnum.FEMALE.value, GenderTypesEnum.FEMALE.value),
        (GenderTypesEnum.OTHER.value, GenderTypesEnum.OTHER.value),
    )

    username = models.CharField(max_length=200, blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    user_type = models.CharField(max_length=30, default="user")
    gender = models.CharField(choices=GENDER_TYPES, max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', default='default.jpg', blank=True, null=True)
    cars_owned = models.ManyToManyField(Car, related_name="owned", blank=True)
    favourite_cars = models.ManyToManyField(Car, related_name="favourite", blank=True)
    birth_date = models.DateField(blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)

    @property
    def is_admin(self):
        return self.user_type == "admin"

    def is_user(self):
        return self.user_type == "user"

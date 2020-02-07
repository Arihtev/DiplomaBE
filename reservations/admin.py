from django.contrib import admin

# Register your models here.
from .models import Reservation, Review

admin.site.register(Reservation)
admin.site.register(Review)

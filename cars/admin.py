from django.contrib import admin

# Register your models here.
from .models import Car, Picture, ExtraCategory, Extra

admin.site.register(Car)
admin.site.register(Picture)
admin.site.register(Extra)
admin.site.register(ExtraCategory)

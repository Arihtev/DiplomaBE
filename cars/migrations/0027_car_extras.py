# Generated by Django 2.2.4 on 2019-08-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0026_remove_car_extras'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='extras',
            field=models.ManyToManyField(blank=True, to='cars.Extra'),
        ),
    ]

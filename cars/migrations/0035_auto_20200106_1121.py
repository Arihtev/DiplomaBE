# Generated by Django 2.2.4 on 2020-01-06 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
        ('cars', '0034_car_reservations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='reservations',
        ),
        migrations.AddField(
            model_name='car',
            name='reservations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.Reservation'),
        ),
    ]
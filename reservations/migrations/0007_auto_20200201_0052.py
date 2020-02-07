# Generated by Django 2.2.4 on 2020-01-31 22:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0046_auto_20200127_2303'),
        ('reservations', '0006_auto_20200129_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='', max_length=500)),
                ('rate', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.Reservation')),
            ],
        ),
    ]

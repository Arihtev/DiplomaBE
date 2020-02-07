# Generated by Django 2.2.4 on 2020-01-11 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='start_datetime',
        ),
        migrations.AddField(
            model_name='reservation',
            name='end_date',
            field=models.DateField(default=datetime.date(2020, 1, 11)),
        ),
        migrations.AddField(
            model_name='reservation',
            name='start_date',
            field=models.DateField(default=datetime.date(2020, 1, 11)),
        ),
    ]

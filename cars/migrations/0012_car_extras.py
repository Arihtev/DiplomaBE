# Generated by Django 2.2.4 on 2019-08-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_carextra'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='extras',
            field=models.ManyToManyField(to='cars.Extra'),
        ),
    ]

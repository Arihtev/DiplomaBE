# Generated by Django 2.2.4 on 2019-10-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0031_car_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.CharField(default=50, max_length=10),
            preserve_default=False,
        ),
    ]
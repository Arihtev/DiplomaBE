# Generated by Django 2.2.4 on 2019-08-20 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0017_auto_20190820_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='address',
        ),
        migrations.RemoveField(
            model_name='car',
            name='category',
        ),
        migrations.RemoveField(
            model_name='car',
            name='city',
        ),
        migrations.RemoveField(
            model_name='car',
            name='engine_type',
        ),
        migrations.RemoveField(
            model_name='car',
            name='model',
        ),
        migrations.RemoveField(
            model_name='car',
            name='region',
        ),
        migrations.RemoveField(
            model_name='car',
            name='transmission',
        ),
        migrations.RemoveField(
            model_name='car',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='car_id',
        ),
        migrations.AddField(
            model_name='car',
            name='pictures',
            field=models.ManyToManyField(blank=True, to='cars.Picture'),
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_auto_20190820_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='pictures',
            field=models.ManyToManyField(blank=True, to='cars.Picture'),
        ),
    ]

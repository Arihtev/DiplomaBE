# Generated by Django 2.2.4 on 2020-01-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20200119_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.TextField(default='paid'),
        ),
    ]
# Generated by Django 2.2.4 on 2020-01-28 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20200127_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='days_reserved',
            field=models.PositiveSmallIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=9),
            preserve_default=False,
        ),
    ]

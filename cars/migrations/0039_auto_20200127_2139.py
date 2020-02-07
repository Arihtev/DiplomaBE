# Generated by Django 2.2.4 on 2020-01-27 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0038_auto_20200127_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='horsepower',
        ),
        migrations.AlterField(
            model_name='car',
            name='consumption',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='included_km',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='monthly_discount',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='car',
            name='price_per_extra_km',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='seats',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='weekly_discount',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='zip_code',
            field=models.PositiveSmallIntegerField(),
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_safety'),
    ]

    operations = [
        migrations.AddField(
            model_name='safety',
            name='abs',
            field=models.BooleanField(default=False, verbose_name='Антиблокираща система'),
        ),
        migrations.AddField(
            model_name='safety',
            name='airbags',
            field=models.BooleanField(default=False, verbose_name='Въздушни възглавници'),
        ),
        migrations.AddField(
            model_name='safety',
            name='asc',
            field=models.BooleanField(default=False, verbose_name='Автоматичен контрол на стабилността'),
        ),
        migrations.AddField(
            model_name='safety',
            name='break_assistance',
            field=models.BooleanField(default=False, verbose_name='Система за подпомагане на спирането'),
        ),
        migrations.AddField(
            model_name='safety',
            name='traction_control',
            field=models.BooleanField(default=False, verbose_name='Система за защита от пробуксуване'),
        ),
        migrations.AlterField(
            model_name='safety',
            name='isofix',
            field=models.BooleanField(default=False, verbose_name='ISOFIX'),
        ),
        migrations.AlterField(
            model_name='safety',
            name='parktronic',
            field=models.BooleanField(default=False, verbose_name='Парктроник'),
        ),
    ]
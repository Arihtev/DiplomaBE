# Generated by Django 2.2.4 on 2019-08-13 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_pictures'),
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
            name='description',
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
            name='pictures',
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
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, max_length=255, null=True, upload_to='photos/%Y/%m/%d')),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car')),
            ],
        ),
    ]
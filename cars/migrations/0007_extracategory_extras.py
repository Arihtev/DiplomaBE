# Generated by Django 2.2.4 on 2019-08-19 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20190819_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.ExtraCategory')),
            ],
        ),
    ]

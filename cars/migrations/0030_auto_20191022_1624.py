# Generated by Django 2.2.4 on 2019-10-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0029_auto_20191022_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='horsepower',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='seats',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
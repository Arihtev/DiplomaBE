# Generated by Django 2.2.4 on 2019-08-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20190813_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='new',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

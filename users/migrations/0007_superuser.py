# Generated by Django 2.2.4 on 2020-02-01 22:01
import datetime

from django.db import migrations, models

from users.models import User


def input_data(apps, schema_editor):
    superuser = User.objects.create_superuser(username="arihtev", password="arihtev", first_name="arihtev", last_name="arihtev",
              email="arihtev@mail.com", user_type="admin", birth_date=datetime.date(1996, 5, 4), phone="0899777888")


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200202_0001'),
    ]

    operations = [
        migrations.RunPython(input_data)
    ]
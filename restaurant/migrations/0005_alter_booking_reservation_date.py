# Generated by Django 4.1.4 on 2024-02-18 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0004_alter_booking_reservation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="reservation_date",
            field=models.DateField(default=datetime.date(2024, 2, 18)),
        ),
    ]

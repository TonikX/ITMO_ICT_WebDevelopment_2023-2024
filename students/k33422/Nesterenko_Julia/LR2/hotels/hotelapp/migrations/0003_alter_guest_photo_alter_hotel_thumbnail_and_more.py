# Generated by Django 4.2.5 on 2023-10-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotelapp", "0002_alter_booking_date_until_alter_guest_country_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guest",
            name="photo",
            field=models.ImageField(blank=True, default="user.svg", upload_to=""),
        ),
        migrations.AlterField(
            model_name="hotel",
            name="thumbnail",
            field=models.ImageField(upload_to=""),
        ),
        migrations.AlterField(
            model_name="room",
            name="thumbnail",
            field=models.ImageField(upload_to=""),
        ),
    ]

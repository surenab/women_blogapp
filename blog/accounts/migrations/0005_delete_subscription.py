# Generated by Django 4.2.4 on 2023-09-17 18:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_subscription"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Subscription",
        ),
    ]

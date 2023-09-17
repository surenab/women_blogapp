# Generated by Django 4.2.4 on 2023-09-17 21:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_subscription"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.URLField()),
                ("icon_name", models.CharField(blank=True, max_length=100, null=True)),
                ("link_name", models.CharField(max_length=100)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

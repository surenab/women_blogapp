# Generated by Django 4.2.4 on 2023-09-24 18:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="teammember",
            name="social_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="BlogImage",
        ),
    ]

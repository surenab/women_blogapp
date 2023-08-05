# Generated by Django 4.2.2 on 2023-08-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="blog_type",
            field=models.CharField(
                choices=[
                    ("1", "Sport"),
                    ("2", "Travel"),
                    ("3", "Handmade"),
                    ("4", "Funny Animals"),
                    ("5", "Nature"),
                ],
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="Media"
            ),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-02 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutTeam",
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
                ("our_team", models.TextField(max_length=1000)),
                (
                    "team_image",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to="Media"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Blog",
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
                (
                    "blog_category",
                    models.CharField(
                        choices=[
                            ("1", "Travel"),
                            ("2", "Sport"),
                            ("3", "Nature"),
                            ("4", "Animals"),
                            ("5", "Food"),
                            ("6", "DIY and Crafts"),
                            ("7", "Science and Technology"),
                            ("8", "Fashion"),
                            ("9", "Medicine"),
                            ("10", "Psycology"),
                            ("11", "Art"),
                        ],
                        default="1",
                        max_length=2,
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("created_on", models.DateField(auto_now_add=True)),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to="Media"
                    ),
                ),
                (
                    "image1",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to="Media"
                    ),
                ),
                (
                    "image2",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to="Media"
                    ),
                ),
                ("view_count", models.PositiveIntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("full_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=150)),
                ("message", models.TextField(max_length=1000)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="TeamMember",
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
                ("full_name", models.CharField(max_length=50)),
                ("job_position", models.CharField(max_length=50)),
                ("about_member", models.TextField(max_length=1000)),
                (
                    "member_image",
                    models.ImageField(
                        blank=True, default=None, null=True, upload_to="Media"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BlogComment",
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
                ("text", models.TextField(max_length=400)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.blog"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

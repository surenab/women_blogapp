# Generated by Django 4.2.2 on 2023-08-05 20:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_remove_blog_blog_type_blog_blog_category_blog_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="image",
        ),
    ]
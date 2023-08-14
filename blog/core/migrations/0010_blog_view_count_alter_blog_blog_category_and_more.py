# Generated by Django 4.2 on 2023-08-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_blog_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_category',
            field=models.CharField(choices=[('1', 'Travel'), ('2', 'Sport'), ('3', 'Nature'), ('4', 'Animals'), ('5', 'Food'), ('6', 'DIY and Crafts'), ('7', 'Science and Technology'), ('8', 'Fashion'), ('9', 'Medicine'), ('10', 'Psycology'), ('11', 'Art')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
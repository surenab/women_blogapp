# Generated by Django 4.2.2 on 2023-08-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_type', models.CharField(choices=[('1', 'Travel'), ('2', 'Sport'), ('3', 'Natural'), ('4', 'Funny animals'), ('5', 'nature')], default='1', max_length=1)),
                ('title', models.CharField(max_length=50)),
                ('create_data', models.DateField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='Media')),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]

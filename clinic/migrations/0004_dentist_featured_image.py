# Generated by Django 4.2.13 on 2024-06-07 21:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_rename_title_service_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentist',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
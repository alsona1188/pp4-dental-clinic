# Generated by Django 4.2.13 on 2024-06-18 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_contactformrequest_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactformrequest',
            name='user',
        ),
        migrations.AddField(
            model_name='contactformrequest',
            name='name',
            field=models.CharField(default='Enter your name', max_length=200),
        ),
    ]
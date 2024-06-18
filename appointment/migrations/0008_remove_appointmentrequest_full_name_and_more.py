# Generated by Django 4.2.13 on 2024-06-14 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0007_alter_appointmentrequest_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentrequest',
            name='full_name',
        ),
        migrations.AddField(
            model_name='appointmentrequest',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
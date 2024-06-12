# Generated by Django 4.2.13 on 2024-06-09 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0003_alter_appointmentrequest_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentrequest',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 4.2.6 on 2023-10-23 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0004_alter_clientmessages_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentresponses',
            name='agent_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
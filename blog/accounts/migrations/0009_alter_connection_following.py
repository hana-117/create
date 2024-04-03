# Generated by Django 3.2.4 on 2023-12-01 06:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_connection_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]

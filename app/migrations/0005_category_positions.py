# Generated by Django 5.1.4 on 2025-02-17 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_eventbooking_extra_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='positions',
            field=models.IntegerField(default=0),
        ),
    ]

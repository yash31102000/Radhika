# Generated by Django 5.1.4 on 2025-03-20 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventbooking', '0003_alter_eventbooking_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventbooking',
            name='mobile_no',
            field=models.CharField(max_length=17),
        ),
    ]

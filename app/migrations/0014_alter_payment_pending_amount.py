# Generated by Django 5.1.4 on 2025-02-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_payment_pending_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pending_amount',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]

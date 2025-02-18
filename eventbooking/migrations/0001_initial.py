# Generated by Django 5.1.4 on 2025-02-18 04:33

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_items', models.JSONField(default=dict)),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Mobile number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('reference', models.CharField(max_length=50)),
                ('event_date', models.DateField()),
                ('event_time', models.CharField(max_length=100)),
                ('event_address', models.TextField()),
                ('advance_amount', models.CharField(blank=True, max_length=150, null=True)),
                ('advance_payment_mode', models.CharField(blank=True, choices=[('CASH', 'CASH'), ('CHEQUE', 'CHEQUE'), ('BANK_TRANSFER', 'BANK TRANSFER'), ('ONLINE', 'ONLINE'), ('OTHER', 'OTHER')], max_length=20, null=True)),
                ('per_dish_amount', models.CharField(max_length=150)),
                ('estimated_persons', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirm', 'Confirm'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('done', 'Done')], default='pending', max_length=20)),
                ('extra_service_amount', models.CharField(blank=True, max_length=250, null=True)),
                ('extra_service', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-event_date', '-event_time'],
            },
        ),
        migrations.CreateModel(
            name='StokeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]

# Generated by Django 5.1.4 on 2025-01-31 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_payment_billed_to_payment_unique_billed_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(choices=[('PARTIAL', 'Partial'), ('UNPAID', 'Unpaid'), ('PAID', 'Paid')], default='UNPAID', max_length=10),
        ),
    ]

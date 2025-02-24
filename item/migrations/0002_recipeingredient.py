# Generated by Django 5.1.4 on 2025-02-18 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.JSONField(default=dict)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='item.item')),
            ],
        ),
    ]

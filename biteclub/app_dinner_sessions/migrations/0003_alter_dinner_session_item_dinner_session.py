# Generated by Django 5.1.3 on 2024-11-11 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_dinner_sessions', '0002_alter_dinner_session_restaurants_dinner_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinner_session_item',
            name='dinner_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_dinner_sessions.dinner_session'),
        ),
    ]
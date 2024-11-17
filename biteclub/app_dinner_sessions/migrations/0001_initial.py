# Generated by Django 5.1.3 on 2024-11-11 07:48

import app_dinner_sessions.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_common', '0001_initial'),
        ('app_restaurants', '0002_restaurant_address'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner_Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_expires', models.DateTimeField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dinner_Session_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('user_comments', models.CharField(blank=True, max_length=200)),
                ('dinner_session', models.IntegerField(verbose_name=app_dinner_sessions.models.Dinner_Session)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_common.address')),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_restaurants.menu_item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dinner_Session_Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinner_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_restaurants.menu_item')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_restaurants.restaurant')),
            ],
        ),
    ]

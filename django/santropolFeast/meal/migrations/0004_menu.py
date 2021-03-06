# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0003_meal_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('date', models.DateField(verbose_name='date')),
                ('ingredients', models.ManyToManyField(related_name='related_menus', to='meal.Ingredient')),
            ],
            options={
                'verbose_name_plural': 'menus',
            },
        ),
    ]

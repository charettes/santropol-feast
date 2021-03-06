# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-13 21:41
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0014_auto_20160512_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name_plural': 'Notes'},
        ),
        migrations.RemoveField(
            model_name='note',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='note',
            name='priority',
            field=models.CharField(choices=[('normal', 'Normal'), ('urgent', 'Urgent')], default='normal', max_length=15),
        ),
        migrations.AlterField(
            model_name='note',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notes', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='note',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='Is read'),
        ),
        migrations.AlterField(
            model_name='note',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notes', to='member.Member', verbose_name='Member'),
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='referencing',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 13), verbose_name='referral_date'),
        ),
    ]

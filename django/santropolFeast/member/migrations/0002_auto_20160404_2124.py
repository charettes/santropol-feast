# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-04 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('D', 'pending'), ('A', 'active'), ('S', 'paused'), ('N', 'stopnocontact'), ('C', 'stopcontact'), ('I', 'deceased')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='address',
            name='floor',
            field=models.IntegerField(verbose_name='floor'),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.PositiveIntegerField(verbose_name='street_number'),
        ),
        migrations.AlterField(
            model_name='client',
            name='billing_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Address', verbose_name='billing_Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('Home phone', 1), ('Cell phone', 2), ('Work phone', 3), ('Email', 4)], max_length=100, verbose_name='contact_type'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-30 21:04
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_group_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='lat',
            field=models.CharField(default=None, help_text='Please supply a latitude for this group', max_length=255),
        ),
        migrations.AddField(
            model_name='group',
            name='lon',
            field=models.CharField(default=None, help_text='Please supply a longitude for this group', max_length=255),
        ),
        migrations.AlterField(
            model_name='group',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]

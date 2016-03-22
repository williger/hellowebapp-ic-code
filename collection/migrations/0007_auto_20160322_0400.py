# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-22 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='thing',
            name='upgraded',
            field=models.BooleanField(default=False),
        ),
    ]

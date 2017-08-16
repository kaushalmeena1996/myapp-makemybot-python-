# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-15 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0011_auto_20170814_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='greet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bot',
            name='message',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='bot',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
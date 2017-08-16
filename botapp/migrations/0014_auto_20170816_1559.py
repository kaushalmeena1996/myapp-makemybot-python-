# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-16 10:29
from __future__ import unicode_literals

import botapp.helper.helper
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0013_auto_20170816_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='avtaar',
            field=models.FileField(default='D:\\Projects\\WEB\\myapp-makemybot\\media\\avtaar\x08ot_default.png', upload_to=botapp.helper.helper.generate_filename),
        ),
        migrations.AlterField(
            model_name='bot',
            name='brain',
            field=models.FileField(default='D:\\Projects\\WEB\\myapp-makemybot\\media\\avtaar\x08ot_default.rive', upload_to=botapp.helper.helper.generate_filename),
        ),
        migrations.AlterField(
            model_name='bot',
            name='message',
            field=models.CharField(blank=True, default='hello', max_length=32),
        ),
    ]
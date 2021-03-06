# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 11:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('biog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 11, 11, 40, 55, 638572, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 11, 11, 41, 2, 981100, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-09 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='text',
            field=models.TextField(default=''),
        ),
    ]

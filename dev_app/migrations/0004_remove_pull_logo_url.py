# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-10-04 16:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dev_app', '0003_auto_20151004_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pull',
            name='logo_url',
        ),
    ]
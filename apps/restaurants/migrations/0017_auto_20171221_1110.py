# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 17:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0016_menuitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='menu',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]

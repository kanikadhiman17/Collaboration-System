# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 07:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0007_auto_20171129_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmembership',
            name='group_admin',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-11 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0009_remove_notification_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='level',
            field=models.CharField(choices=[('success', 'success'), ('info', 'info'), ('warning', 'warning'), ('error', 'error'), ('danger', 'danger')], default='danger', max_length=20),
        ),
    ]
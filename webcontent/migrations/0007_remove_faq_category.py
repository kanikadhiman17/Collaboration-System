# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-25 15:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcontent', '0006_faqcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='category',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20170920_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
    ]
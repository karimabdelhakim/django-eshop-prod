# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-10 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_auto_20161209_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-09 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_remove_cartproduct_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cart.Cart'),
        ),
    ]
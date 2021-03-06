# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-31 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20170731_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_root',
            field=models.BooleanField(default=False, verbose_name='是否是一级分类'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.Category', verbose_name='上级分类'),
        ),
    ]

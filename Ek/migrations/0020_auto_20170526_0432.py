# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 04:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ek', '0019_auto_20170526_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Ek.Pessoa'),
        ),
        migrations.AddField(
            model_name='item',
            name='capa',
            field=models.ImageField(blank=True, upload_to='Loja'),
        ),
    ]

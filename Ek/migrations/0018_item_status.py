# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ek', '0017_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('d', 'Rascunho'), ('p', 'Publicado'), ('o', 'Oculto'), ('r', 'Em Revis\xe3o')], default='d', max_length=1),
        ),
    ]

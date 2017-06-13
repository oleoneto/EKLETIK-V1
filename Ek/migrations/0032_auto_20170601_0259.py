# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ek', '0031_auto_20170601_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='item',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='sinopse',
        ),
        migrations.AddField(
            model_name='album',
            name='editorial',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='livro',
            name='editorial',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='livro',
            name='ficheiro',
            field=models.FileField(default=0, upload_to='Vendas'),
        ),
        migrations.AlterField(
            model_name='album',
            name='ficheiro',
            field=models.FileField(default=0, upload_to='Vendas'),
        ),
    ]

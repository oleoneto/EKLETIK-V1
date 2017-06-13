# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ek', '0003_auto_20170523_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('gestor', models.CharField(max_length=100)),
                ('cliente', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('dias', models.IntegerField(default=1)),
                ('destaque', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('d', 'Rascunho'), ('p', 'Publicado'), ('o', 'Oculto'), ('r', 'Em Revis\xe3o')], default='r', max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='artigo',
            name='status',
            field=models.CharField(choices=[('d', 'Rascunho'), ('p', 'Publicado'), ('o', 'Oculto'), ('r', 'Em Revis\xe3o')], default='d', max_length=1),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='Perfis'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='status',
            field=models.CharField(choices=[('d', 'Rascunho'), ('p', 'Publicado'), ('o', 'Oculto'), ('r', 'Em Revis\xe3o')], default='r', max_length=1),
        ),
    ]

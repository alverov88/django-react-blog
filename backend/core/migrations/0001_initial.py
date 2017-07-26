# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
                ('about', models.TextField(blank=True, default='', null=True)),
                ('description', models.TextField(blank=True, max_length=512)),
                ('keywords', models.TextField(blank=True, max_length=512)),
                ('description_social', models.TextField(blank=True, max_length=512)),
                ('image_social', models.ImageField(default='img/card.png', upload_to='img/')),
                ('analytics', models.CharField(max_length=64)),
            ],
        ),
    ]

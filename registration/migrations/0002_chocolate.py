# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 06:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Chocolate Name')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Chocolate Description')),
                ('manufacturer', models.CharField(blank=True, max_length=100, verbose_name='Chocolate Manufacturer')),
                ('price', models.IntegerField(blank=True, help_text='4 digits maximum', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)], verbose_name='Chocolate Price')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-21 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, null=True)),
                ('comment', models.TextField()),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
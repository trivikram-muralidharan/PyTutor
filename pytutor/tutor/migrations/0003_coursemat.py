# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-24 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_auto_20161224_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseMat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursecontent', models.CharField(max_length=1000)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('abstract', models.CharField(max_length=100)),
                ('emojiName', models.CharField(max_length=50)),
                ('mdFileName', models.CharField(max_length=50)),
                ('createTime', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'articles',
            },
        ),
    ]

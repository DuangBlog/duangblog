# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_articles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emojis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emojiName', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'emojis',
            },
        ),
        migrations.RemoveField(
            model_name='articles',
            name='emojiName',
        ),
        migrations.AddField(
            model_name='articles',
            name='emojiId',
            field=models.IntegerField(default=0),
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('topic', models.CharField(max_length=4)),
                ('user_comments', models.TextField(max_length=365)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralTopics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('electronic_project_topics', models.CharField(default=b'Ar', max_length=3, choices=[(b'Ar', b'Arduino'), (b'RPi', b'RaspberryPi'), (b'IG', b'Intel_Galileo')])),
            ],
        ),
    ]

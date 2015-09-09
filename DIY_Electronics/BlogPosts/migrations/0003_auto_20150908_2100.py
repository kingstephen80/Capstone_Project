# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPosts', '0002_auto_20150908_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generaltopics',
            name='electronic_project_topics',
        ),
        migrations.AddField(
            model_name='generaltopics',
            name='topic',
            field=models.CharField(default=datetime.datetime(2015, 9, 9, 4, 0, 35, 459000, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='topic',
            field=models.ForeignKey(to='BlogPosts.GeneralTopics'),
        ),
    ]

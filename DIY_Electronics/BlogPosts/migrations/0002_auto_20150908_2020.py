# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPosts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='text_main',
            field=models.TextField(max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='topic',
            field=models.CharField(max_length=90),
        ),
    ]

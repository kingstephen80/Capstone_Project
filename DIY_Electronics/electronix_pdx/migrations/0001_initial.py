# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTopics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='CreateNEW',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=90)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('posted_date', models.DateTimeField(null=True, blank=True)),
                ('main_text', models.TextField(max_length=5000, null=True, blank=True)),
                ('comments', models.TextField(max_length=366)),
                ('topic', models.ForeignKey(to='electronix_pdx.BlogTopics')),
            ],
        ),
    ]

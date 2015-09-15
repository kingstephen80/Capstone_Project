# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpostapp', '0003_auto_20150908_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateBlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text_main', models.TextField(max_length=5000, null=True, blank=True)),
                ('user_comments', models.TextField(max_length=365)),
                ('topic', models.ForeignKey(to='blogpostapp.GeneralTopics')),
            ],
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='topic',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]

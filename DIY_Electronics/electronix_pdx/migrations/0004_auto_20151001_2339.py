# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('electronix_pdx', '0003_remove_createnew_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=90)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('posted_date', models.DateTimeField(blank=True, null=True)),
                ('main_text', models.TextField(blank=True, max_length=5000, null=True)),
                ('comments', models.TextField(max_length=366)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(to='electronix_pdx.BlogTopics')),
            ],
        ),
        migrations.RemoveField(
            model_name='createnew',
            name='topic',
        ),
        migrations.DeleteModel(
            name='CreateNEW',
        ),
    ]

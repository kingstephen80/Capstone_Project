# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogpostapp', '0005_auto_20150914_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='createblogpost',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='createblogpost',
            name='post_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='createblogpost',
            name='author',
            field=models.ForeignKey(default=datetime.datetime(2015, 9, 15, 3, 22, 37, 458000, tzinfo=utc), to='blogpostapp.Author'),
            preserve_default=False,
        ),
    ]

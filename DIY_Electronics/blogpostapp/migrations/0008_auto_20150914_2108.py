# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpostapp', '0007_auto_20150914_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='createblogpost',
            name='author',
            field=models.ForeignKey(default=2, to='blogpostapp.Author'),
            preserve_default=False,
        ),
    ]

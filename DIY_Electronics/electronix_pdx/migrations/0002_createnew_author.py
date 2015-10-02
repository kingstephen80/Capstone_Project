# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('electronix_pdx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createnew',
            name='author',
            field=models.ForeignKey(default=datetime.datetime(2015, 9, 16, 2, 30, 16, 697000, tzinfo=utc), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

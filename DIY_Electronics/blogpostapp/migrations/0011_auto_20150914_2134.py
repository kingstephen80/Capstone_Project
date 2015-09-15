# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpostapp', '0010_auto_20150914_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createblogpost',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]

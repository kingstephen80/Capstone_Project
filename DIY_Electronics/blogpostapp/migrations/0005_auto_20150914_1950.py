# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpostapp', '0004_auto_20150911_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createblogpost',
            old_name='date',
            new_name='post_date',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ElectronixBlogPDX', '0002_createnew_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createnew',
            name='author',
        ),
    ]

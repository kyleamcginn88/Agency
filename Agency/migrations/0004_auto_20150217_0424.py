# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0003_friend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='frist_name',
            new_name='user_frist_name',
        ),
    ]

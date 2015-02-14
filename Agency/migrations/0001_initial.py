# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('age', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

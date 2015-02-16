# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=128)),
                ('last_name', models.CharField(default=b'', max_length=128)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=75)),
                ('zip', models.IntegerField()),
                ('phone', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0004_auto_20150217_0424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest3',
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
        migrations.RenameField(
            model_name='contest1',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='contest1',
            name='last_name',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]

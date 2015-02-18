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
                ('first_name', models.CharField(default=b'', max_length=128)),
                ('last_name', models.CharField(default=b'', max_length=128)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('zip', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_frist_name', models.CharField(default=b'', max_length=128)),
                ('age', models.IntegerField()),
                ('user_email', models.EmailField(max_length=75)),
                ('friend_name1', models.CharField(default=b'', max_length=128)),
                ('friend1_email', models.EmailField(max_length=75)),
                ('friend_name2', models.CharField(default=b'', max_length=128)),
                ('friend2_email', models.EmailField(max_length=75)),
                ('friend_name3', models.CharField(default=b'', max_length=128)),
                ('friend3_email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

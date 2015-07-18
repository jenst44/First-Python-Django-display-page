# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=200)),
                ('created_at', models.DateField()),
            ],
            options={
                'db_table': 'interests',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField(max_length=200)),
                ('last_name', models.TextField(max_length=200)),
                ('age', models.IntegerField()),
                ('created_at', models.DateField()),
                ('occupation', models.TextField(max_length=200)),
                ('interest', models.ForeignKey(to='interests.Interests')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]

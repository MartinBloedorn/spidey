# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GizmodoEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('post_id', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]

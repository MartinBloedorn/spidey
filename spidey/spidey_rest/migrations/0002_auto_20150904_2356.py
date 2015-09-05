# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spidey_rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gizmodoentry',
            name='description',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='gizmodoentry',
            name='keywords',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='gizmodoentry',
            name='post_date',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='gizmodoentry',
            name='url',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AlterField(
            model_name='gizmodoentry',
            name='text',
            field=models.TextField(default=b''),
        ),
    ]

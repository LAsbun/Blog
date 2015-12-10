# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151201_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(upload_to=b'./upload/2015/12/1', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]

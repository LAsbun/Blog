# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151201_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(upload_to=b'/static/upload/2015/12/6', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]

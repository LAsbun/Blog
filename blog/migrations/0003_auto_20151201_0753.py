# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(height_field=50, upload_to=b'./upload/2015/11/30', width_field=50, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]

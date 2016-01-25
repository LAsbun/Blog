# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20160116_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(upload_to=b'/uploads/2016/1', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160116_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(upload_to=b'/uploads/2016/1', null=True, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]

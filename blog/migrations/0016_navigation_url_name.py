# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160116_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigation',
            name='url_name',
            field=models.CharField(default='', max_length=20, verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe6\x9d\xa1\xe5\x9c\xb0\xe5\x9d\x80'),
            preserve_default=False,
        ),
    ]

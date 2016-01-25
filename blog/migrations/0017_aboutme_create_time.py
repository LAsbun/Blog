# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_navigation_url_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 2, 45, 7, 889847, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

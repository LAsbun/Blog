# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='conment_article',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe8\xaf\x84\xe6\x96\x87\xe7\xab\xa0', to='blog.Article'),
        ),
    ]

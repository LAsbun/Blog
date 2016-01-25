# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160115_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('self_tag', models.CharField(max_length=200, verbose_name=b'\xe8\x87\xaa\xe6\x88\x91\xe5\xae\x9a\xe4\xb9\x89\xe6\xa0\x87\xe7\xad\xbe')),
                ('something_to_say', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0\xe8\x87\xaa\xe5\xb7\xb1')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='conment_article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]

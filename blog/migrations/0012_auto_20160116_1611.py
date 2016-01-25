# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160116_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conten', models.TextField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('conment_name', models.CharField(max_length=50, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('conment_email', models.EmailField(max_length=254, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe4\xba\xba\xe9\x82\xae\xe7\xae\xb1')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('conment_article', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe8\xaf\x84\xe6\x96\x87\xe7\xab\xa0', to='blog.Article')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='self_tag',
            field=models.CharField(max_length=120, verbose_name=b'\xe8\x87\xaa\xe6\x88\x91\xe5\xae\x9a\xe4\xb9\x89\xe6\xa0\x87\xe7\xad\xbe'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='something_to_say',
            field=models.TextField(verbose_name=b'\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89'),
        ),
    ]

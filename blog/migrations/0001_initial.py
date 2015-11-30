# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('view_count', models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('prais_count', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe8\xb5\x9e\xe6\x95\xb0')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conten', models.TextField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('conment_name', models.CharField(max_length=50, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('conment_email', models.EmailField(max_length=254, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe4\xba\xba\xe9\x82\xae\xe7\xae\xb1')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('conment_article', models.ForeignKey(to='blog.Article')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe6\x9d\xa1\xe5\x90\x8d\xe7\xa7\xb0')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u5bfc\u822a',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('passwd', models.CharField(max_length=50, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('img', models.ImageField(upload_to=b'./upload/2015/11/30', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u7528\u6237',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to='blog.User'),
        ),
    ]

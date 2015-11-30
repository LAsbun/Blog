#coding: utf-8
from django.db import models
from time import gmtime

# Create your models here.

#导航条
class Navigation(models.Model):
    name = models.CharField(max_length=50,
                             verbose_name='导航条名称')
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name='创建时间')

    class Meta:
        ordering=['-create_time']
        verbose_name='导航'

    def __unicode__(self):
        return self.name

#用户
class User(models.Model):
    username = models.CharField(max_length=30,
                                verbose_name='用户名')
    passwd= models.CharField(max_length=50,
                             verbose_name='密码')
    upload_to = './upload/%s/%s/%s' %(gmtime()[:3])
    img = models.ImageField(upload_to=upload_to,
                            verbose_name='头像')
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name='创建时间')

    class Meta:
        ordering = ['-create_time']
        verbose_name='用户'

    def __unicode__(self):
        return self.username

#分类
class Category(models.Model):
    name = models.CharField(max_length=50,
                             verbose_name='分类名称')
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name='创建时间')

    class Meta:
        ordering=['-create_time']
        verbose_name='分类'

    def __unicode__(self):
        return self.name

#文章
class Article(models.Model):

    author = models.ForeignKey(User,
                               verbose_name='作者')

    title = models.CharField(max_length=100,
                             verbose_name='标题')
    content = models.TextField(verbose_name='文章内容')
    view_count = models.IntegerField(default=0,
                                     verbose_name='浏览量')
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name='创建时间')
    prais_count = models.IntegerField(default=0,
                                      verbose_name='点赞数')

    class Meta:
        ordering=['-create_time']
        verbose_name='文章'

    def __unicode__(self):
        return self.title

#评论
class Comment(models.Model):
    conment_article=models.ForeignKey(Article)
    conten = models.TextField(verbose_name='评论内容')
    conment_name = models.CharField(max_length=50,
                                    verbose_name='评论人姓名')
    conment_email=models.EmailField(verbose_name='评论人邮箱')
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name='创建时间')

    class Meta:
        ordering=['-create_time']
        verbose_name = '评论'

    def __uniccode__(self):
        return self.conment_name
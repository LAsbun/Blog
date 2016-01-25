#coding:utf8
from django.contrib import admin
from .models import Article, User, Category, AboutMe, Navigation, Comment
# Register your models here.

#user
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'create_time', 'img')

#文章内容
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_time')
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js'
        )

#分类
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time')

#AboutMe
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('self_tag', 'create_time')
    class Media:
       js = (
            '/static/js/kindeditor-4.1.10/kindeditor.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js'
        )

#导航条内容
class NavigationAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time')

#评论
class CommentAdmin(admin.ModelAdmin):
    list_display = ('conment_name', 'conment_article')

admin.site.register(Article, ArticleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Navigation, NavigationAdmin)
admin.site.register(Comment, CommentAdmin)
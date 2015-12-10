from django.contrib import admin
from .models import Article, User, Category, Comment, Navigation
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'create_time', 'img')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_time')
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js'
        )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('conment_name', 'conment_article')

class NavigationAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time')

admin.site.register(Article, ArticleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Navigation, NavigationAdmin)
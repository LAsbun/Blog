#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.template.context import RequestContext
from blog.models import *
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

nav_list = Navigation.objects.all()
category_list = Category.objects.all()


def index(request):
    try:
        nav_list = Navigation.objects.all()
        category_list = Category.objects.all()
        article_list = Article.objects.all()
        #分页
        paginator = Paginator(article_list,10) #每页分几个
        page = request.GET.get('page') #当翻到第2+页之后会有page=2.。？
        try:
            article_list = paginator.page(page)
        except PageNotAnInteger:
            article_list = paginator.page(1)
        except EmptyPage:
            article_list = paginator.page(paginator.num_pages)
        #print dir(article_list)
        context = {'article_list':article_list,
                   'nav_list':nav_list,
                   'category_list':category_list,
                   }
        #print nav_list
        #print article_list[0].id

        return render_to_response('index.html', context, context_instance=RequestContext(request))
    except Exception, e:
        return HttpResponse(e)

def get_article(request, id):
    try:
        article = Article.objects.get(id=id)
        context = {'article':article,
                   'nav_list':nav_list,
                   'category_list':category_list,}
        return render_to_response('page.html', context)
    except Exception, e:
        return HttpResponse(e)

def search(request, tag):
    try:
        article_list = Article.objects.filter(category__name=tag)
        print tag

        context = {'article_list':article_list,
                   'nav_list':nav_list,
                   'category_list':category_list,}
        return render_to_response('tag.html', context)
    except Exception, e:
        return HttpResponse(e)


def archieve(request):
    try:
        article_list = Article.objects.all()
        context = {'article_list':article_list,
                   'nav_list':nav_list,
                   'category_list':category_list,}
        return render_to_response('archieve.html', context)
    except Article.DoesNotExist, e:
        return  Http404()

def aboutme(request):
    try:
        myself = AboutMe.objects.all()[0]
        tag_list = myself.self_tag.split(',')
        content = myself.something_to_say
        context={'tag_list':tag_list,
                 'content':content,
                 'nav_list':nav_list,
                   'category_list':category_list,}
        return render_to_response('aboutme.html', context)
    except Exception, e:
        return HttpResponse(e)

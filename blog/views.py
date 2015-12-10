#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.template.context import RequestContext
from blog.models import *
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    try:
        nav_list = Navigation.objects.all()
        article_list = Article.objects.all()
        temp = article_list
        #分页
        paginator = Paginator(article_list,2) #每页分几个
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
                   }
        #print nav_list
        #print article_list[0].id

        return render_to_response('index.html', context, context_instance=RequestContext(request))
    except Exception, e:
        return HttpResponse(e)

def get_article(request, id):
    try:
        article = Article.objects.get(id=id)
        context = {'article':article}
        return render_to_response('page.html', context)
    except Exception, e:
        return HttpResponse(e)


def search(request):
    try:
        name = request._post.get('name', None)
        print name
        all_article = Article.objects.all()
        article_list=[]
        count = all_article.count()
        pattarn = re.compile(name)
        for i in range(count):
            print all_article[i].title
            if pattarn.search(all_article[i].title):
                article_list.append(all_article[i])


        print article_list
        context = {'article_list':article_list}
        return render_to_response('page.html', context, context_instance=RequestContext(request))
    except Exception, e:
        return HttpResponse(e)

def archieve(request):
    try:
        article_list = Article.objects.all()
        context = {'article_list':article_list}
        return render_to_response('archieve.html', context)
    except Article.DoesNotExist, e:
        return  Http404()
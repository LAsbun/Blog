from django.conf.urls import url
from .views import *


urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name='index'),
    url(r'^index', index, name='index'),
    url(r'^article/(?P<id>\d+)/?$', get_article, name='article'),
    url(r'^search/(?P<tag>\w+)/?$', search, name='search'),
    url(r'^archieve/?$', archieve, name='archieve'),
    url(r'^aboutme/?$', aboutme, name='aboutme'),
]

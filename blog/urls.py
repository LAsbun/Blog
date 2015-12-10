from django.conf.urls import include, url
from .views import *


urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name='index'),
    url(r'^article/(?P<id>\d+)/?$', get_article, name='article'),
    url(r'^search/$', search, name='search'),
    url(r'^archieve/?$', archieve, name='archieve'),
]

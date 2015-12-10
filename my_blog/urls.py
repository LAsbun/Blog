from django.conf.urls import include, url
from django.contrib import admin
import blog.urls
from django.conf import settings
from blog.upload import upload_image

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url('^markdown/', include( 'django_markdown.urls')),
    url(r'uploads/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$',
        upload_image,name='upload_image'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(blog.urls)),
]

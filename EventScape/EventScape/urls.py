from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EventScape.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^website/', include('website.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

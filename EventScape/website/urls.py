from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
)
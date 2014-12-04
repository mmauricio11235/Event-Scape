from django.conf.urls import patterns, url
from .views import RegisterUser, AddEvent

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', name="login"),
    url(r'^register/$', RegisterUser.as_view(), name="register"),
    url(r'^event/new$', AddEvent.as_view(), name="event-new"),
)
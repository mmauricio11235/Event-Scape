from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView

from .views import RegisterUser, AddEvent, EventSearch
from .models import Event

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', name="login"),
    url(r'^register/$', RegisterUser.as_view(), name="register"),
    url(r'^event/new$', AddEvent.as_view(), name="event-new"),
    url(r'^event/(?P<pk>\d+)/$', DetailView.as_view(model=Event,
                                                   template_name='event/detail.html'), name="event-detail"),
    url(r'^event/search$', EventSearch.as_view(), name="event-search"),
)
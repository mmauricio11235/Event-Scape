from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

from .views import RegisterUser, AddEvent, EventSearch
from .models import Event
urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name="logout"),
    url(r'^register/$', RegisterUser.as_view(), name="register"),
    url(r'^event/new$', AddEvent.as_view(), name="event-new"),
    url(r'^event/delete/(?P<pk>\d+)/$', DeleteView.as_view(model=Event,
                                                   template_name='event/delete_confirm.html',
                                                   success_url=reverse_lazy('event-search')), name="event-delete"),
    url(r'^event/(?P<pk>\d+)/$', DetailView.as_view(model=Event,
                                                   template_name='event/detail.html'), name="event-detail"),
    url(r'^event/search$', EventSearch.as_view(), name="event-search"),
)


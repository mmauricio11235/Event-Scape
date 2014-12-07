from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .views import RegisterUser, EventAdd, EventEdit, EventSearch, EventDelete, login_or_redirect
from .models import Event

# ##FOR TESTING ONLY###
from django.conf import settings
from django.conf.urls.static import static
# #####################


urlpatterns = patterns('',
                       url(r'^$', login_or_redirect, name="login"),
                       url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name="logout"),
                       url(r'^register/$', RegisterUser.as_view(), name="register"),
                       url(r'^event/new$', login_required(EventAdd.as_view()), name="event-new"),
                       url(r'^event/delete/(?P<pk>\d+)/$', EventDelete.as_view(), name="event-delete"),
                       url(r'^event/edit/(?P<pk>\d+)/$', EventEdit.as_view(), name="event-edit"),
                       url(r'^event/(?P<pk>\d+)/$', login_required(DetailView.as_view(model=Event,
                                                                                      template_name='event/detail.html')),
                           name="event-detail"),
                       url(r'^event/search$', login_required(EventSearch.as_view()), name="event-search"),
                       url(r'^user/profile/(?P<pk>\d+)/$', login_required(DetailView.as_view(model=User,
                                                                                             template_name='website/profile.html')),
                           name="user-profile"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # FOR TESTING ONLY


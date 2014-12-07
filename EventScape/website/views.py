from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, EventForm, SearchForm
from .models import Event

def login_or_redirect(request):
    if  request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return login(request)

class RegisterUser(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class EventAdd(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event/new.html'

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super(EventAdd, self).form_valid(form)


class EventEdit(UpdateView):
    form_class = EventForm
    template_name = 'event/new.html'

    def get_initial(self):
        tags = " ".join([t.name for t in self.object.tags.all()])
        return {'tags': tags}

    def get_queryset(self):
        return Event.objects.filter(host=self.request.user)


class EventDelete(DeleteView):
    template_name = 'event/delete_confirm.html'
    success_url = reverse_lazy('event-search')

    def get_queryset(self):
        return Event.objects.filter(host=self.request.user)


class EventSearch(ListView):
    model = Event
    template_name = 'event/search.html'

    def get_queryset(self):
        object_list = self.model.objects.all()


        initial = self.request.GET
        initial._mutable = True
        if not initial.get('keywords'):
            initial['keywords'] = " ".join([t.name for t in self.request.user.tags.all()])
        form = SearchForm(initial)
        if form.is_valid():
            kws = form.cleaned_data['keywords']
            if kws:
                kws = kws.split()
                queries = []
                for kw in kws:
                    queries.append(Q(name__contains=kw))
                    queries.append(Q(description__contains=kw))
                    queries.append(Q(tags__name__contains=kw))

                query = queries.pop()
                for q in queries:
                    query |= q

                object_list = object_list.filter(query)

            host = form.cleaned_data['host']
            if host:
                object_list = object_list.filter(host__contains=host)

            location = form.cleaned_data['location']
            if location:
                query = Q(address__contains=location) | Q(city__contains=location) | Q(state__contains=location)
                object_list = object_list.filter(query)

            after = form.cleaned_data['after']
            if after:
                object_list = object_list.filter(start__gte=after)

            before = form.cleaned_data['before']
            if before:
                object_list = object_list.filter(end__lte=before)

        return object_list


    def get_context_data(self, **kwargs):
        context = super(EventSearch, self).get_context_data(**kwargs)
        context['form'] = SearchForm(initial=self.request.GET)
        return context


@login_required
def event_attend(request):
    if request.method == 'GET':
        eid = request.GET['eid']
        try:
            e = Event.objects.get(pk=int(eid))
            e.attendees.add(request.user)
            return HttpResponse("true")
        except:
            return HttpResponse("error")
    else:
        return HttpResponse("false")


@login_required
def user_follow(request):
    if request.method == 'GET':
        uid = request.GET['uid']
        try:
            u = User.objects.get(pk=int(uid))
            u.userprofile.follows.add(request.user.userprofile)
            return HttpResponse("true")
        except:
            return HttpResponse("error")
    else:
        return HttpResponse("false")
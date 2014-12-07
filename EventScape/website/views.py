from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .forms import RegistrationForm, EventForm, SearchForm
from .models import Event

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
    model = Event
    form_class = EventForm
    template_name = 'event/new.html'

    def get_initial(self):
        tags = " ".join([t.name for t in self.object.tags.all()])
        return {'tags': tags}


class EventSearch(ListView):
    model = Event
    template_name = 'event/search.html'

    def get_queryset(self):
        object_list = self.model.objects.all()

        form = SearchForm(self.request.GET)
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

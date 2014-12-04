from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .forms import RegistrationForm, CreateEventForm
from .models import Event

class RegisterUser(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class AddEvent(CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'event/new.html'

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super(CreateView, self).form_valid(form)


class EventSearch(ListView):
    model = Event
    template_name = 'event/search.html'

    def get_queryset(self):
        try:
            search_q = self.kwargs['query']
        except:
            search_q = ''

        if search_q:
            kws = search_q.split()
            queries = []
            for kw in kws:
                queries.append(Q(name__contains=kw))
                queries.append(Q(tags__name__contains=kw))

            query = queries.pop()
            for q in queries:
                query |= q

            object_list = self.model.objects.filter(query)
            
        else:
            object_list = self.model.objects.all()

        return object_list

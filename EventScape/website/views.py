from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
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

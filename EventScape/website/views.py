from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

class RegisterUser(CreateView):
    model = User
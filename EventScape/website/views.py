from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.shortcuts import render

class RegisterUser(CreateView):
    model = User

def index(request):
	 return render(request, 'website/index.html')

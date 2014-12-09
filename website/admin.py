from django.contrib import admin
from .models import Event, Tag

admin.site.register(Tag)
admin.site.register(Event)

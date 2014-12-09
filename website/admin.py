from django.contrib import admin
from .models import Event, Tag, EventImage

admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(EventImage)

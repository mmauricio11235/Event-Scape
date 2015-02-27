import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventScape.settings')

import django
django.setup()
import datetime

from website.models import Event, User
from parse_events import getevents

def populate():

    events = getevents()
    for e in events:
        add_event(name = e.getTitle(), desc = e.getDescription())

    # Print out what we have added to the user.


def add_event(name, desc):
    e = Event(host = User.objects.all()[0],
              name = name,
        address = "POMONA COLLEGE",
        start =datetime.datetime.now(),
        description = desc,
        approved = 'A')
    print("GOT HERE")
    #e.save()
    return e

# Start execution here!
if __name__ == '__main__':
    print ("Starting Rango population script...")
    populate()
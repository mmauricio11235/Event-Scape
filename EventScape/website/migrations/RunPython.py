# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randrange
from datetime import date, timedelta
from django.db import models, migrations

def forwards_func(website, schema_editor):
	#Event = website.get_model()
	#db_alias = schema_editor.connection.alias

	Event.objects.using(db_alias).bulk_create([
		Namelist = ["A ", "Rager ", "to ", "End ", "All ", "Ragers ", "Throwdown ", "Game ", "Party ", "Free ", "Food ", 
			"Art ", "After ", "Hours ", "CMS ", "Pomona-Pitzer ", "Tournament ", "5C Hackathon "]
		addressList = ["3065 Jackson St", "Sixth St and College St", "Mauricio's Room", "Edmunds 229", "742 Amherst Ave", "Pomona Hall", "Museum of Natural History", "SFO", "Union Station", "Harvey Mudd College"]
		CityList = ["San Francisco", "Claremont", "Pomona", "London", "Altiris", "Los Angeles", "New York"]
		StateList = ["CA", "KY", "NY", "MO", "WA"]
		StartList = ["2014-12-06 05:19:59", "2014-12-10 15:00:00", "2014-12-25 00:00:00", "2015-01-01 00:00:00", "2013-04-19 14:30:00"]
		format = '%Y-%m-%d %H:%M:%S'
		TagList = ["Party", "Food", "Sports", "TV Show", "Movie", "Culture",
			"Holiday", "Rager", "CS", "Geology", "Dance", "Workshop"]

		for x in range(0, 99):
			RandName = randRange(len(Namelist))
			RandAddress = randrange(len(addressList))
			RandCity = randrange(len(CityList))
			RandState = randrange(len(StateList))
			RandStart = randrange(len(StartList));
			RandTags = sample(TagList, randint(1,5))

			Event(name=Namelist[RandName], address=addressList[RandAddress], 
				city=CityList[RandCity], state=StateList[RandState], 
				start=datetime.datetime.strptime(StartList[RandStart],format),
				end= start + timedelta(hours=3), description="Test Event",
				tags = RangTags)
	])


class Migration(migrations.Migration):

    dependencies = []

    operations = [
    	migrations.RunPython(forwards_func,),
    ]
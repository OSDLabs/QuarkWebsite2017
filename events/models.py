from django.db import models

# Create your models here.
from panel.models import Profile
from django.contrib.auth.models import User

EVENT_TYPES = (
	(u'T',u'Team'),
	(u'S',u'Single'),
	)

CATEGORY = (
    (u'Drama',u'Drama'),
    (u'Dance',u'Dance'),
    (u'Big 4',u'Big 4'),
    (u'Business',u'Business'),
    (u'Fine Arts',u'Fine Arts'),
    (u'Literary',u'Literary'),
    (u'Music',u'Music'),
    (u'Film and Photography',u'Film and Photography'),
    (u'Quiz',u'Quiz'),
    (u'Special',u'Special'),
    )

SPONS = (
    (u'Our Sponsors',u'Our Sponsors'),
    (u'Our Media Partners',u'Our Media Partners'),
    (u'Our Associations',u'Our Associations'),
    )
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, null=True)
    rules = models.FileField(upload_to = "adminuploads/events/rules/" , blank=True, null=True)
    img = models.ImageField(upload_to = "adminuploads/events/pics/" ,blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    types = models.CharField(max_length=1, choices=EVENT_TYPES)
    category = models.CharField(max_length=50, choices = CATEGORY, default='')

    def __str__(self):
        return self.eventName

class Indi_Event_Participants(models.Model):
	event = models.ForeignKey(Event, related_name = "event", on_delete = models.CASCADE)
	event_part = models.ForeignKey(User, related_name = "event_participating", on_delete = models.CASCADE)

class Rounds(models.Model):
    event = models.ForeignKey(Event, related_name = "rounds", on_delete = models.CASCADE)
    title = models. CharField(max_length = 50)
    day = models.DateField()
    location = models.CharField(max_length = 50)
    time = models.TimeField()

class Sponsor(models.Model):
    order = models.IntegerField()
    desc = models.CharField(max_length=200, blank = True, null=True)
    link = models.CharField(max_length=100)
    img = models.ImageField(upload_to = "adminuploads/sponsors/")
    types = models.CharField(max_length=100, choices=SPONS)

class FoodFest(models.Model):
    order = models.IntegerField()
    desc = models.CharField(max_length=200, blank = True, null=True)
    link = models.CharField(max_length=100)
    img = models.ImageField(upload_to = "adminuploads/sponsors/")
    # spons_type = models.CharField(max_length=100, choices=SPONS)

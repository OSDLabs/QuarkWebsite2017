from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
import registration


GENDER_CHOICES = (
	(u'M',u'Male'),
	(u'F',u'Female'),
	(u'N',u"Don't wish to reveal")
	)

YEAR_CHOICES = (
	(u'U1',u'Undergraduate 1st year'),
	(u'U2',u'Undergraduate 2nd year'),
	(u'U3',u'Undergraduate 3rd year'),
	(u'U4',u'Undergraduate 4th year'),
	(u'P1',u'Postgraduate 1st year'),
	(u'P2',u'Postgraduate 2nd year'),
	(u'SS',u'Schooling'),
	(u'PH',u'PhD.'),
	)


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 120)
	email = models.EmailField()
	mobile = models.CharField(max_length = 10)
	institute = models.CharField(max_length = 120)
	gender = models.CharField(max_length = 1, choices=GENDER_CHOICES)
	dob = models.DateField(auto_now_add = True, auto_now = False)
	year = models.CharField(max_length =2, choices = YEAR_CHOICES)
	updatedtime = models.DateTimeField(auto_now_add = False, auto_now = True)
	settime = models.DateTimeField(auto_now_add = True, auto_now = False)

	def __str__(self):
		return self.name

class Institute(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name


from django.db import models

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


class quick(models.Model):
	name = models.CharField(max_length = 120)
	email = models.EmailField()
	mobile = models.CharField(max_length = 10)
	institute = models.CharField(max_length = 120)
	gender = models.CharField(max_length = 1, choices=GENDER_CHOICES)
	year = models.CharField(max_length =2, choices = YEAR_CHOICES)
	panel_des = models.CharField(max_length = 100)
	panel_elixir = models.CharField(max_length = 100)
	panel_robo = models.CharField(max_length = 100)
	panel_prog = models.CharField(max_length = 100)
	panel_specials = models.CharField(max_length = 100)
	panel_init = models.CharField(max_length = 100)
	panel_elect = models.CharField(max_length = 100)
	panel_corporate = models.CharField(max_length = 100)
	workshop = models.CharField(max_length = 100)
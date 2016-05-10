from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	full_name = models.CharField(max_length = 120, blank = False)
	pic = models.FileField(upload_to = "uploads/")
	email = models.EmailField()
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	mobile = models.CharField(max_length = 10)
	institute = models.CharField(max_length = 120)
	gender = models.CharField(max_length = 1)
	dob = models.DateField()
	year = models.CharField()

	def __str__(self):
		return self.full_name


	
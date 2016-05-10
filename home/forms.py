from django import forms
from .models import Profile
from django.models.contrib.auth import User

class UpdateProfileForm(forms.ModelForm):
	
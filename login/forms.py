from django import forms
from django.contrib.auth.models import User
from login.models import UserProfileInfo	

class UserProfileInfoForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model=User
		fields=('username','password')
		def save(self, commit=True):
			user = super(UserProfileInfoForm, self).save(commit=False)
			if commit:
				user.save()
			return user
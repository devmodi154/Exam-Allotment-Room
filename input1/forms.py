from django import forms
from input1.models import Booking
# from input1.choices import *


class input1Form(forms.ModelForm):
	# room_no=forms.CharField(required=True)
	# division=forms.ChoiceField(choices=division_choices)

	class Meta():
		model=Booking
		fields=('division','room_no')
		# exclude=['room_no','block','faculty_assigned']

		# def __init__(self, *args, **kwargs):
			# super().__init__(*args, **kwargs)
			# self.fields['division']=forms.ChoiceField(choices=division_choices)
			# self.fields['division'].queryset = Booking.objects.none()

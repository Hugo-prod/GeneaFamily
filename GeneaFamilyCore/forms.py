from django.forms import ModelForm

from .models import Member


class MemberForm(ModelForm):
	""" Create or update member (A.K.A person's identity). """

	def clean_first_name(self):
		""" remove unnecessary spaces and convert all word in 'Title Case' """
		return " ".join(self.cleaned_data['first_name'].split()).title()

	def clean_family_name(self):
		""" remove unnecessary spaces and convert all word in 'Title Case' """
		return " ".join(self.cleaned_data['family_name'].split()).title()

	class Meta:
		model = Member
		fields = [	'first_name',
					'family_name',
					'gender']
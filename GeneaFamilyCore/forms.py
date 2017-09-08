from django.forms import ModelForm

from .models import Member, Locality
from .utils import clean_n_format


class MemberForm(ModelForm):
	""" Create or update member (A.K.A person's identity). """

	def clean(self):
		""" remove unnecessary spaces and convert all word in 'Title Case' """
		self.cleaned_data['first_name'] = \
			clean_n_format(self.cleaned_data['first_name'])

		self.cleaned_data['family_name'] = \
			clean_n_format(self.cleaned_data['family_name'])

	class Meta:
		model = Member
		fields = [	'first_name',
					'family_name',
					'gender']


class LocalityForm(ModelForm):
	""" Create or update locality. """

	def clean(self):
		""" remove unnecessary spaces and convert all word in 'Title Case' """
		self.cleaned_data['country'] = \
			clean_n_format(self.cleaned_data['country'])

		self.cleaned_data['city'] = \
			clean_n_format(self.cleaned_data['city'])

		self.cleaned_data['additional_address_information'] = \
			clean_n_format(self.cleaned_data['additional_address_information'])

	class Meta:
		model = Locality
		fields = [	'country',
					'city',
					'additional_address_information',
					'latitude',
					'longitude']
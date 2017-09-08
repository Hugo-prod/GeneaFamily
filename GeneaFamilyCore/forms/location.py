from django.forms import ModelForm

from GeneaFamilyCore.models import Locality
from GeneaFamilyCore.utils import clean_n_format


class LocalityForm(ModelForm):
	""" Create or update locality. """

	def clean(self):
		""" remove unnecessary spaces and convert all word in 'Title Case' """
		self.cleaned_data['country'] = clean_n_format(
			self.cleaned_data['country'],
			'T')

		self.cleaned_data['city'] = clean_n_format(
			self.cleaned_data['city'],
			'T')

		self.cleaned_data['additional_address_information'] = clean_n_format(
			self.cleaned_data['additional_address_information'],
			'T')

	class Meta:
		model = Locality
		fields = [	'country',
					'city',
					'additional_address_information',
					'latitude',
					'longitude']
from django.forms import ModelForm

from GeneaFamilyCore.models import EventType
from GeneaFamilyCore.utils import clean_n_format


class EventTypeForm(ModelForm):
	""" Create EventType. """

	def clean(self):
		""" remove unnecessary spaces and set capitalisation string """
		self.cleaned_data['name']=clean_n_format(self.cleaned_data['name'], 'C')

	class Meta:
		model = EventType
		fields = [	'name',
					'time_period_type',
					'description',]


class UpdateEventTypeForm(ModelForm):
	""" Update EventType. """

	def clean(self):
		""" remove unnecessary spaces and set capitalisation string """
		self.cleaned_data['name']=clean_n_format(self.cleaned_data['name'], 'C')

	class Meta:
		model = EventType
		fields = [	'name',
					'description',]
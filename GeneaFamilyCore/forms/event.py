from django.forms import ModelForm

from GeneaFamilyCore.models import Event


class EventDateForm(ModelForm):
	""" Create event (With unique date). """

	class Meta:
		model = Event
		fields = [	'title',
					'start_date',
					'start_date_is_approximately',
					'content',]


class EventPeriodForm(ModelForm):
	""" Create event (With period mode). """

	class Meta:
		model = Event
		fields = [	'title',
					'start_date',
					'start_date_is_approximately',
					'end_date',
					'end_date_is_approximately',
					'content',]
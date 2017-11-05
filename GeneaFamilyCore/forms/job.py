from django.forms import ModelForm

from GeneaFamilyCore.models import Job


class JobForm(ModelForm):
	""" Create Job. """

	class Meta:
		model = Job
		fields = [	'job_name',
					'date',
					'date_is_approximately',
					'locality_fk',]
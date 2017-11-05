from django.forms import ModelForm

from GeneaFamilyCore.models import Residence


class ResidenceForm(ModelForm):
	""" Create Residence. """

	class Meta:
		model = Residence
		fields = [	'date',
					'date_is_approximately',
					'locality_fk',]
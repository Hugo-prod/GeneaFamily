from django.forms import ModelForm

from GeneaFamilyCore.models import Baptism


class BaptismForm(ModelForm):
	""" Create Baptism. """

	class Meta:
		model = Baptism
		fields = [	'date',
					'time',
					'date_is_approximately',
					'godfather_fk',
					'godmother_fk',
					'locality_fk',]
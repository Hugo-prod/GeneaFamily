from django.forms import ModelForm

from GeneaFamilyCore.models import Family, Member


class FamilyForm(ModelForm):
	""" Create Family. """

	class Meta:
		model = Family
		fields = [	'father_fk',
					'mother_fk',]
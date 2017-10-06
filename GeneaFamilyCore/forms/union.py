from django.forms import ModelForm

from GeneaFamilyCore.models import Union, UnionWitness, UnionComparer


class UnionForm(ModelForm):
	""" Create Union. """

	class Meta:
		model = Union
		fields = [	'start_date',
					'start_date_is_approximately',
					'end_date',
					'end_date_is_approximately',
					'union_type',
					'locality_fk',]

class UnionWitnessForm(ModelForm):
	""" Create UnionForm. """

	class Meta:
		model = UnionWitness
		fields = [	'member_fk',
					'for_who',]

class UnionComparerForm(ModelForm):
	""" Create UnionComparer. """

	class Meta:
		model = UnionComparer
		fields = [	'member_fk',]
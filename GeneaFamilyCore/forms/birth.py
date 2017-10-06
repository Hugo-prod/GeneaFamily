from django.forms import ModelForm

from GeneaFamilyCore.models import Birth, BirthWitness, BirthComparer


class BirthForm(ModelForm):
	""" Create Birth. """

	class Meta:
		model = Birth
		fields = [	'birth_type',
					'date',
					'time',
					'date_is_approximately',
					'locality_fk',]


class BirthWitnessForm(ModelForm):
	""" Create BirthWitness. """

	class Meta:
		model = BirthWitness
		fields = ['member_fk']


class BirthComparerForm(ModelForm):
	""" Create BirthComparer. """

	class Meta:
		model = BirthComparer
		fields = ['member_fk']
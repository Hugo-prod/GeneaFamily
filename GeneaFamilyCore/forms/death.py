from django.forms import ModelForm

from GeneaFamilyCore.models import Death, DeathWitness, DeathComparer


class DeathForm(ModelForm):
	""" Create Death. """

	class Meta:
		model = Death
		fields =[	'date',
					'time',
					'date_is_approximately',
					'death_reason',
					'locality_fk',]


class DeathWitnessForm(ModelForm):
	""" Create DeathWitness. """

	class Meta:
		model = DeathWitness
		fields = ['member_fk']


class DeathComparerForm(ModelForm):
	""" Create DeathComparer. """

	class Meta:
		model = DeathComparer
		fields = ['member_fk']
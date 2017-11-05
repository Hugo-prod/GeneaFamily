from django.forms import ModelForm

from GeneaFamilyCore.models import Member
from GeneaFamilyCore.utils import clean_n_format


class MemberForm(ModelForm):
	""" Create or update member (A.K.A person's identity). """

	def clean(self):
		""" remove unnecessary spaces and convert all word in 'Title Case' """
		self.cleaned_data['first_name'] = \
			clean_n_format(self.cleaned_data['first_name'], 'T')

		self.cleaned_data['family_name'] = \
			clean_n_format(self.cleaned_data['family_name'], 'T')

	class Meta:
		model = Member
		fields = [	'first_name',
					'family_name',
					'pseudonyme',
					'gender']


class MemberInstructionForm(ModelForm):

	class Meta:
		model = Member
		fields = [	'read',
					'write',]
from django.forms import ModelForm

from GeneaFamilyCore.models import Military


class MilitarySignalmentForm(ModelForm):
	""" Create Military. """

	class Meta:
		model = Military
		fields =[	'head',
					'hair',
					'forehead',
					'eyes',
					'nose',
					'mouth',
					'chin',
					'size',
					'rectified_size',
					'additional_note',
					'special_brand',]


class MilitaryInstructionForm(ModelForm):
	""" Create Military. """

	class Meta:
		model = Military
		fields =[	'military_instruction',
					'general_instruction',]


class MilitaryClassForm(ModelForm):
	""" Create Military. """

	class Meta:
		model = Military
		fields =[	'recruitment_matricul_number',
					'mobilisation_class',]


class MilitaryRecruitmentForm(ModelForm):
	""" Create Military. """

	class Meta:
		model = Military
		fields =[	'recruitment_draw',
					'canton_recruitment',]


class MilitaryAdviceForm(ModelForm):
	""" Create Military. """

	class Meta:
		model = Military
		fields =[	'advice_decision',
					'advice_reason',]
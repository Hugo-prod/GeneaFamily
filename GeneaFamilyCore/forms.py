from django.forms import ModelForm

from .models import Member


class MemberForm(ModelForm):
	""" Create or update member (A.K.A person's identity). """

	class Meta:
		model = Member
		fields = [	'first_name',
					'family_name',
					'gender']
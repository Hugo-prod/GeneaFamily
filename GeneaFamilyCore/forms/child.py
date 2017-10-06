from django.forms import ModelForm

from GeneaFamilyCore.models import Child, Member


class ChildForm(ModelForm):
	""" Child form. """

	def __init__(self, *args, **kwargs):
		super(ChildForm, self).__init__(*args, **kwargs)
		# TODO: exclude all ancestror 
		member_to_exclude = [child.child_fk.pk for child in Child.objects.all()]
		member_to_exclude.append(kwargs['initial']['mother_pk'])
		member_to_exclude.append(kwargs['initial']['father_pk'])
		self.fields['child_fk'].queryset = Member.objects.exclude(
			id__in=member_to_exclude)

	class Meta:
		model = Child
		fields = ['child_fk',]

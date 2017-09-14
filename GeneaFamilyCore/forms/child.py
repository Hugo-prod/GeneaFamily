from django.forms import ModelForm

from GeneaFamilyCore.models import Child, Member


class ChildForm(ModelForm):
	""" Child form. """

	def __init__(self, *args, **kwargs):
		super(ChildForm, self).__init__(*args, **kwargs)
		# Todo: exclude all ancestror (father/father's father ...)
		self.fields['child_fk'].queryset = Member.objects.exclude(
			id__in=[child.child_fk.pk for child in Child.objects.all()])

	class Meta:
		model = Child
		fields = ['child_fk',]

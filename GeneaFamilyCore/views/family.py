from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView

from GeneaFamilyCore.models import Member, Family, Child


class FamilyDetail(DetailView):

	def get_context_data(self, **kwargs):
		context = super(FamilyDetail, self).get_context_data(**kwargs)
		return context


class CreateFamilyWithMember(CreateView):
	""" Create a family with a preselected member.
		Note: Be careful, if gender of member is 'Unknow',
			  this object will be considered as a woman (A.K.A: mother_fk).
	"""

	def get_initial(self):
		if Member.objects.filter(pk=self.kwargs['preselected_member_pk']).exists():
			member = Member.objects.get(pk=self.kwargs['preselected_member_pk'])
			if member.gender == 'M': return {'father_fk':member}
			else: return {'mother_fk':member}
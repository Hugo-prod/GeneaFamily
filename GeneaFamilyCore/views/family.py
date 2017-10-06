from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import DetailView

from GeneaFamilyCore.models import Family, Child


class FamilyDetail(DetailView):

	def get_context_data(self, **kwargs):
		context = super(FamilyDetail, self).get_context_data(**kwargs)
		return context

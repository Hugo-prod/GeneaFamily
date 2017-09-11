from django.shortcuts import render
from django.views.generic import DetailView

from GeneaFamilyCore.models import *


class MemberDetail(DetailView):
	def get_context_data(self, **kwargs):
		context = super(MemberDetail, self).get_context_data(**kwargs)
		context['all_events'] = Member.objects.get(
			pk=self.kwargs['pk']).get_events()
		context['all_event_types'] = EventType.objects.all()
		return context
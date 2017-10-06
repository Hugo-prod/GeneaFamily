from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, FormView

from GeneaFamilyCore.models import Military, Member


class CreateMilitary(FormView):

	def form_valid(self, form):
		military_obj = form.save()
		member_obj = Member.objects.get(pk=self.kwargs['member_pk'])
		member_obj.military_fk = military_obj
		member_obj.save()
		return super(CreateMilitary, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CreateMilitary, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(pk=self.kwargs['member_pk'])
		return context

	def get_success_url(self):
		return reverse('core:military_detail', args=[self.object.pk])
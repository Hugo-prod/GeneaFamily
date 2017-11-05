from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from GeneaFamilyCore.models import Residence, Member


class CreateResidence(CreateView):

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.member_fk = Member.objects.get(pk=self.kwargs['member_pk'])
		self.object.save()
		return super(CreateResidence, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CreateResidence, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(pk=self.kwargs['member_pk'])
		return context

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.object.member_fk.pk])


class UpdateResidence(UpdateView):

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.object.member_fk.pk])


class DeleteResidence(DeleteView):

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.object.member_fk.pk])
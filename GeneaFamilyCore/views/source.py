from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DeleteView

from GeneaFamilyCore.models import Source, Member


class CreateSource(CreateView):

	def form_valid(self, form):
		source_obj = form.save(commit=False)
		source_obj.member_fk = Member.objects.get(pk=self.kwargs['member_pk'])
		source_obj.save()
		return super(CreateSource, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CreateSource, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(pk=self.kwargs['member_pk'])
		return context

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.kwargs['member_pk']])


class DeleteSource(DeleteView):

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.object.get_member().pk])
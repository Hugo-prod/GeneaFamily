from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DeleteView

from GeneaFamilyCore.models import Baptism, Member


class CreateBaptism(CreateView):

	def dispatch(self, request, *args, **kwargs):
		""" If object is already exist, then redirect to update this"""
		if Member.objects.get(pk=self.kwargs['member_pk']).baptism_fk:
			return redirect(
				reverse('core:update_baptism',
						args=[Member.objects.get(
							pk=self.kwargs['member_pk']).baptism_fk.pk]))
		else:
			return super(CreateBaptism, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		baptism_obj = form.save()
		member_obj = Member.objects.get(pk=self.kwargs['member_pk'])
		member_obj.baptism_fk = baptism_obj
		member_obj.save()
		return super(CreateBaptism, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CreateBaptism, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(pk=self.kwargs['member_pk'])
		return context

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.kwargs['member_pk']])


class DeleteBaptism(DeleteView):

	def get_context_data(self, **kwargs):
		context = super(DeleteBaptism, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(pk=self.object.get_member().pk)
		return context

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.object.get_member().pk])

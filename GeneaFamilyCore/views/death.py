from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DeleteView

from GeneaFamilyCore.models import Death, Member


class CreateDeath(CreateView):

	def dispatch(self, request, *args, **kwargs):
		""" If object is already exist, then redirect to update this"""
		if Member.objects.get(pk=self.kwargs['member_pk']).death_fk:
			return redirect(
				reverse('core:update_death',
						args=[Member.objects.get(
							pk=self.kwargs['member_pk']).death_fk.pk]))
		else:
			return super(CreateDeath, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		death_obj = form.save()
		member_obj = Member.objects.get(pk=self.kwargs['member_pk'])
		member_obj.death_fk = death_obj
		member_obj.save()
		return super(CreateDeath, self).form_valid(form)

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.kwargs['member_pk']])


class DeleteDeath(DeleteView):

	def get_context_data(self, **kwargs):
		context = super(DeleteDeath, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(pk=self.object.get_member().pk)
		print(self.object)
		return context

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.object.get_member().pk])


class DeathAddWitness(CreateView):

	def form_valid(self, form):
		death_witness_obj = form.save(commit=False)
		death_witness_obj.death_fk = Death.objects.get(pk=self.kwargs['death_pk'])
		death_witness_obj.save()
		return super(DeathAddWitness, self).form_valid(form)

	def get_success_url(self):
		return reverse(
			'core:member_detail',
			args=[Member.objects.get(
				death_fk=Death.objects.get(
					pk=self.kwargs['death_pk'])).pk])


class DeathDeleteWitness(DeleteView):

	def get_context_data(self, **kwargs):
		context = super(DeathDeleteWitness, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(
			death_fk=self.object.death_fk)
		return context


	def get_success_url(self):
		return reverse(
			'core:member_detail',
			args=[Member.objects.get(
				death_fk=self.object.death_fk).pk])


class DeathAddComparer(CreateView):

	def form_valid(self, form):
		death_comparer_obj = form.save(commit=False)
		death_comparer_obj.death_fk = Death.objects.get(pk=self.kwargs['death_pk'])
		death_comparer_obj.save()
		return super(DeathAddComparer, self).form_valid(form)

	def get_success_url(self):
		return reverse(
			'core:member_detail',
			args=[Member.objects.get(
				death_fk=Death.objects.get(
					pk=self.kwargs['death_pk'])).pk])


class DeathDeleteComparer(DeleteView):

	def get_context_data(self, **kwargs):
		context = super(DeathDeleteWitness, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(
			death_fk=self.object.death_fk)
		return context


	def get_success_url(self):
		return reverse(
			'core:member_detail',
			args=[Member.objects.get(
				death_fk=self.object.death_fk).pk])
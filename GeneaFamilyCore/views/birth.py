from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DeleteView

from GeneaFamilyCore.models import Birth, Member


class CreateBirth(CreateView):

	def dispatch(self, request, *args, **kwargs):
		""" If object is already exist, then redirect to update this"""
		if Member.objects.get(pk=self.kwargs['member_pk']).birth_fk:
			return redirect(
				reverse('core:update_birth',
						args=[Member.objects.get(
							pk=self.kwargs['member_pk']).birth_fk.pk]))
		else:
			return super(CreateBirth, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		birth_obj = form.save()
		member_obj = Member.objects.get(pk=self.kwargs['member_pk'])
		member_obj.birth_fk = birth_obj
		member_obj.save()
		return super(CreateBirth, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CreateBirth, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(pk=self.kwargs['member_pk'])
		return context

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.kwargs['member_pk']])


class DeleteBirth(DeleteView):

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.object.get_member().pk])


class BirthAddWitness(CreateView):

	def form_valid(self, form):
		birth_witness_obj = form.save(commit=False)
		birth_witness_obj.birth_fk = Birth.objects.get(pk=self.kwargs['birth_pk'])
		birth_witness_obj.save()
		return super(BirthAddWitness, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(BirthAddWitness, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(
			birth_fk=Birth.objects.get(
				pk=self.kwargs['birth_pk']))
		return context

	def get_success_url(self):
		return reverse(
			'core:member_detail',
			args=[Member.objects.get(
				birth_fk=Birth.objects.get(
					pk=self.kwargs['birth_pk'])).pk])


class BirthDeleteWitness(DeleteView):

	def get_context_data(self, **kwargs):
		context = super(BirthDeleteWitness, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(
			birth_fk=self.object.birth_fk)
		return context


	def get_success_url(self):
		return reverse(
			'core:member_detail',
			args=[Member.objects.get(
				birth_fk=self.object.birth_fk).pk])


class BirthAddComparer(CreateView):

	def form_valid(self, form):
		birth_comparer_obj = form.save(commit=False)
		birth_comparer_obj.birth_fk = Birth.objects.get(pk=self.kwargs['birth_pk'])
		birth_comparer_obj.save()
		return super(BirthAddComparer, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(BirthAddComparer, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(
			birth_fk=Birth.objects.get(
				pk=self.kwargs['birth_pk']))
		return context

	def get_success_url(self):
		return reverse(
			'core:member_detail',
			args=[Member.objects.get(
				birth_fk=Birth.objects.get(
					pk=self.kwargs['birth_pk'])).pk])


class BirthDeleteComparer(DeleteView):

	def get_context_data(self, **kwargs):
		context = super(BirthDeleteComparer, self).get_context_data(**kwargs)
		context['member'] = Member.objects.get(
			birth_fk=self.object.birth_fk)
		return context


	def get_success_url(self):
		return reverse(
			'core:member_detail',
			args=[Member.objects.get(
				birth_fk=self.object.birth_fk).pk])
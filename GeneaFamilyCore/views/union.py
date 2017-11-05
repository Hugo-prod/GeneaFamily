from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DeleteView

from GeneaFamilyCore.models import Union, UnionWitness, UnionComparer, Family


class CreateUnion(CreateView):

	def dispatch(self, request, *args, **kwargs):
		""" If object is already exist, then redirect to update this"""
		if Family.objects.get(pk=self.kwargs['family_pk']).union_fk:
			return redirect(
				reverse('core:family_detail',
						args=[Family.objects.get(
							pk=self.kwargs['family_pk']).pk]))
		else:
			return super(CreateUnion, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		union_obj = form.save()
		family_obj = Family.objects.get(pk=self.kwargs['family_pk'])
		family_obj.union_fk = union_obj
		family_obj.save()
		return super(CreateUnion, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(CreateUnion, self).get_context_data(**kwargs)
		context['family'] = Family.objects.get(pk=self.kwargs['family_pk'])
		return context


class DeleteUnion(DeleteView):

	def get_success_url(self):
		return reverse('core:family_detail', args=[self.object.get_family().pk])


class UnionAddWitness(CreateView):

	def form_valid(self, form):
		union_witness_obj = form.save(commit=False)
		union_witness_obj.union_fk = Union.objects.get(pk=self.kwargs['union_pk'])
		union_witness_obj.save()
		return super(UnionAddWitness, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(UnionAddWitness, self).get_context_data(**kwargs)
		context['family'] = Family.objects.get(
			union_fk=Union.objects.get(
				pk=self.kwargs['union_pk']))
		return context

	def get_success_url(self):
		return reverse(
			'core:family_detail',
			args=[Family.objects.get(
				union_fk=Union.objects.get(
					pk=self.kwargs['union_pk'])).pk])


class UnionDeleteWitness(DeleteView):

	def get_context_data(self, **kwargs):
		context = super(UnionDeleteWitness, self).get_context_data(**kwargs)
		context['family'] = Family.objects.get(
			union_fk=self.object.union_fk)
		return context

	def get_success_url(self):
		return reverse(
			'core:family_detail',
			args=[Family.objects.get(
				union_fk=self.object.union_fk).pk])


class UnionAddComparer(CreateView):

	def form_valid(self, form):
		union_comparer_obj = form.save(commit=False)
		union_comparer_obj.union_fk = Union.objects.get(pk=self.kwargs['union_pk'])
		union_comparer_obj.save()
		return super(UnionAddComparer, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(UnionAddComparer, self).get_context_data(**kwargs)
		context['family'] = Family.objects.get(
			union_fk=Union.objects.get(
				pk=self.kwargs['union_pk']))
		return context

	def get_success_url(self):
		return reverse(
			'core:family_detail',
			args=[Family.objects.get(
				union_fk=Union.objects.get(
					pk=self.kwargs['union_pk'])).pk])


class UnionDeleteComparer(DeleteView):

	def get_context_data(self, **kwargs):
		context = super(UnionDeleteComparer, self).get_context_data(**kwargs)
		context['family'] = Family.objects.get(
			union_fk=self.object.union_fk)
		return context


	def get_success_url(self):
		return reverse(
			'core:family_detail',
			args=[Family.objects.get(
				union_fk=self.object.union_fk).pk])
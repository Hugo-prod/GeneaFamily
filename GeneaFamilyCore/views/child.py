from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DeleteView

from GeneaFamilyCore.models import Child, Family


class AddChild(CreateView):

	def get_initial(self):
		return {
			'father_pk':Family.objects.get(pk=self.kwargs['family_pk']).father_fk.pk,
			'mother_pk':Family.objects.get(pk=self.kwargs['family_pk']).mother_fk.pk,
			}

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.family_fk = Family.objects.get(pk=self.kwargs['family_pk'])
		self.object.save()
		return super(AddChild, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(AddChild, self).get_context_data(**kwargs)
		context['family'] = Family.objects.get(pk=self.kwargs['family_pk'])
		return context

	def get_success_url(self):
		return reverse('core:family_detail', args=[self.object.family_fk.pk])


class DeleteChild(DeleteView):

	def get_success_url(self):
		return reverse('core:family_detail', args=[self.object.family_fk.pk])
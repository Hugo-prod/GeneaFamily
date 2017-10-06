from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DeleteView

from GeneaFamilyCore.models import Union, UnionWitness, UnionComparer, Family


class CreateUnion(CreateView):

	def form_valid(self, form):
		union_obj = form.save()
		family_obj = Family.objects.get(pk=self.kwargs['family_pk'])
		family_obj.union_fk = union_obj
		family_obj.save()
		return super(CreateUnion, self).form_valid(form)

# TODO:
# 	- Add témoin/declarant
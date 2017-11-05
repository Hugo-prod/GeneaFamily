from django.conf.urls import url
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from GeneaFamilyCore.models import Union
from GeneaFamilyCore.forms.union import *
from GeneaFamilyCore.views.union import *

union_urlpatterns = [

	###########
	# Union #
	###########
	
	# Create Union and assign to Family
	url(r'^union/(?P<family_pk>\d+)/create$',
		CreateUnion.as_view(
			form_class=UnionForm,
			template_name='geneafamilycore/union/forms/create_union.html'),
				name='create_union'),

	# Update a union
	url(r'^union/(?P<pk>\d+)/update$',
		UpdateView.as_view(
			form_class=UnionForm,
			model=Union,
			template_name='geneafamilycore/union/forms/update_union.html'),
				name='update_union'),

	# Delete union
	# Attention delete à partir de la family.union_fk
	url(r'^union/(?P<pk>\d+)/delete$',
		DeleteUnion.as_view(
			model=Union,
			template_name='geneafamilycore/union/forms/delete_union.html'),
				name='delete_union'),

	# Union's detail
	url(r'^union/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Union,
			template_name='geneafamilycore/union/union_detail.html'),
				name='union_detail'),

	# All Unions
	url(r'^union/all$',
		ListView.as_view(
			model=Union,
			paginate_by=20,
			template_name='geneafamilycore/union/all_union.html'),
				name='all_union'),

	#############
	## WITNESS ##
	#############
	# Ajouter un témoin à la naissance
	url(r'^union/(?P<union_pk>\d+)/witness/add$',
		UnionAddWitness.as_view(
			form_class=UnionWitnessForm,
			template_name='geneafamilycore/union/forms/add_witness_union.html'),
				name='union_add_witness'),

	# Supprime l'object unionwitness
	url(r'^union/witness/(?P<pk>\d+)/remove$',
		UnionDeleteWitness.as_view(
			model=UnionWitness,
			template_name='geneafamilycore/union/forms/remove_witness_union.html'),
				name='union_remove_witness'),

	##############
	## COMPARER ##
	##############
	# Ajouter un comparant à la naissance
	url(r'^union/(?P<union_pk>\d+)/comparer/add$',
		UnionAddComparer.as_view(
			form_class=UnionComparerForm,
			template_name='geneafamilycore/union/forms/add_comparer_union.html'),
				name='union_add_comparer'),

	# Supprime l'object unionwitness
	url(r'^union/comparer/(?P<pk>\d+)/remove$',
		UnionDeleteComparer.as_view(
			model=UnionComparer,
			template_name='geneafamilycore/union/forms/remove_comparer_union.html'),
				name='union_remove_comparer'),
]
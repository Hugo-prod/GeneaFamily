from django.conf.urls import url
from django.views.generic import UpdateView, DetailView, ListView

from GeneaFamilyCore.models import Birth, BirthWitness, BirthComparer
from GeneaFamilyCore.forms.birth import BirthForm, BirthWitnessForm, BirthComparerForm
from GeneaFamilyCore.views.birth import *

birth_urlpatterns = [

	###########
	# Birth #
	###########
	
	# Create Birth and assign to Family
	url(r'^birth/(?P<member_pk>\d+)/create$',
		CreateBirth.as_view(
			form_class=BirthForm,
			template_name='geneafamilycore/birth/forms/create_birth.html'),
				name='create_birth'),

	# Update a birth
	url(r'^birth/(?P<pk>\d+)/update$',
		UpdateView.as_view(
			form_class=BirthForm,
			model=Birth,
			template_name='geneafamilycore/birth/forms/update_birth.html'),
				name='update_birth'),

	# Delete birth
	url(r'^birth/(?P<pk>\d+)/delete$',
		DeleteBirth.as_view(
			model=Birth,
			template_name='geneafamilycore/birth/forms/delete_birth.html'),
				name='delete_birth'),

	# Birth's detail
	url(r'^birth/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Birth,
			template_name='geneafamilycore/birth/birth_detail.html'),
				name='birth_detail'),

	# All Births
	url(r'^birth/all$',
		ListView.as_view(
			model=Birth,
			paginate_by=20,
			template_name='geneafamilycore/birth/all_birth.html'),
				name='all_birth'),

	#############
	## WITNESS ##
	#############
	# Ajouter un témoin à la naissance
	url(r'^birth/(?P<birth_pk>\d+)/witness/add$',
		BirthAddWitness.as_view(
			form_class=BirthWitnessForm,
			template_name='geneafamilycore/birth/forms/add_witness_birth.html'),
				name='birth_add_witness'),

	# Supprime l'object birthwitness
	url(r'^birth/witness/(?P<pk>\d+)/remove$',
		BirthDeleteWitness.as_view(
			model=BirthWitness,
			template_name='geneafamilycore/birth/forms/remove_witness_birth.html'),
				name='birth_remove_witness'),

	##############
	## COMPARER ##
	##############
	# Ajouter un comparant à la naissance
	url(r'^birth/(?P<birth_pk>\d+)/comparer/add$',
		BirthAddComparer.as_view(
			form_class=BirthComparerForm,
			template_name='geneafamilycore/birth/forms/add_comparer_birth.html'),
				name='birth_add_comparer'),

	# Supprime l'object birthwitness
	url(r'^birth/comparer/(?P<pk>\d+)/remove$',
		BirthDeleteComparer.as_view(
			model=BirthComparer,
			template_name='geneafamilycore/birth/forms/remove_comparer_birth.html'),
				name='birth_remove_comparer'),

]
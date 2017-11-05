from django.conf.urls import url
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from GeneaFamilyCore.models import Death, DeathComparer, DeathWitness
from GeneaFamilyCore.forms.death import DeathForm, DeathWitnessForm, DeathComparerForm
from GeneaFamilyCore.views.death import (
	CreateDeath, DeleteDeath,
	DeathAddWitness,  DeathDeleteWitness,
	DeathAddComparer, DeathDeleteComparer)

death_urlpatterns = [

	###########
	# Death #
	###########
	
	# Create Death and assign to Family
	url(r'^death/(?P<member_pk>\d+)/create$',
		CreateDeath.as_view(
			form_class=DeathForm,
			template_name='geneafamilycore/death/forms/create_death.html'),
				name='create_death'),

	# Update a death
	url(r'^death/(?P<pk>\d+)/update$',
		UpdateView.as_view(
			form_class=DeathForm,
			model=Death,
			template_name='geneafamilycore/death/forms/update_death.html'),
				name='update_death'),

	# Delete death
	# Attention delete à partir de la member.death_fk
	url(r'^death/(?P<pk>\d+)/delete$',
		DeleteDeath.as_view(
			model=Death,
			template_name='geneafamilycore/death/forms/delete_death.html',
			success_url='/'),
				name='delete_death'),

	# Death's detail
	url(r'^death/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Death,
			template_name='geneafamilycore/death/death_detail.html'),
				name='death_detail'),

	# All Deaths
	url(r'^death/all$',
		ListView.as_view(
			model=Death,
			paginate_by=20,
			template_name='geneafamilycore/death/all_death.html'),
				name='all_death'),

	#############
	## WITNESS ##
	#############
	# Ajouter un témoin à la naissance
	url(r'^death/(?P<death_pk>\d+)/witness/add$',
		DeathAddWitness.as_view(
			form_class=DeathWitnessForm,
			template_name='geneafamilycore/death/forms/add_witness_death.html'),
				name='death_add_witness'),

	# Supprime l'object deathwitness
	url(r'^death/witness/(?P<pk>\d+)/remove$',
		DeathDeleteWitness.as_view(
			model=DeathWitness,
			template_name='geneafamilycore/death/forms/remove_witness_death.html'),
				name='death_remove_witness'),

	##############
	## COMPARER ##
	##############
	# Ajouter un comparant à la naissance
	url(r'^death/(?P<death_pk>\d+)/comparer/add$',
		DeathAddComparer.as_view(
			form_class=DeathComparerForm,
			template_name='geneafamilycore/death/forms/add_comparer_death.html'),
				name='death_add_comparer'),

	# Supprime l'object deathwitness
	url(r'^death/witness/(?P<pk>\d+)/remove$',
		DeathDeleteComparer.as_view(
			model=DeathComparer,
			template_name='geneafamilycore/death/forms/remove_comparer_death.html'),
				name='death_remove_comparer'),
]
from django.conf.urls import url
from django.views.generic import DetailView, DeleteView, ListView

from GeneaFamilyCore.models import Residence
from GeneaFamilyCore.forms.residence import *
from GeneaFamilyCore.views.residence import *

residence_urlpatterns = [

	#############
	# RESIDENCE #
	#############

	# Create Residence and assign Member in Residence
	url(r'^residence/(?P<member_pk>\d+)/create$',
		CreateResidence.as_view(
			form_class=ResidenceForm,
			model=Residence,
			template_name='geneafamilycore/residence/forms/create_residence.html'),
				name='create_residence'),

	# Update a residence
	url(r'^residence/(?P<pk>\d+)/update$',
		UpdateResidence.as_view(
			form_class=ResidenceForm,
			model=Residence,
			template_name='geneafamilycore/residence/forms/update_residence.html'),
				name='update_residence'),

	# Delete residence
	url(r'^residence/(?P<pk>\d+)/delete$',
		DeleteResidence.as_view(
			model=Residence,
			template_name='geneafamilycore/residence/forms/delete_residence.html'),
				name='delete_residence'),

	# Residence's detail
	url(r'^residence/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Residence,
			template_name='geneafamilycore/residence/residence_detail.html'),
				name='residence_detail'),

	# All Residences
	# TODO: all residence d'une personne
	# url(r'^residence/all$',
	# 	ListView.as_view(
	# 		model=Residence,
	# 		paginate_by=20,
	# 		template_name='geneafamilycore/residence/all_residences.html'),
	# 			name='all_residences'),
]
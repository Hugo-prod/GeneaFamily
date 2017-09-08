from django.conf.urls import url
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from GeneaFamilyCore.models import Locality
from GeneaFamilyCore.forms import LocalityForm

urlpatterns = [

	############
	# LOCALITY #
	############
	# Create a locality
	url(r'^locality/create$',
		CreateView.as_view(
			form_class=LocalityForm,
			template_name='geneafamilycore/location/forms/create_locality.html'),
				name='create_locality'),

	# Update a locality
	url(r'^locality/(?P<pk>\d+)/update$',
		UpdateView.as_view(
			model=Locality,
			form_class=LocalityForm,
			template_name='geneafamilycore/location/forms/update_locality.html'),
				name='update_locality'),

	# Delete locality
	url(r'^locality/(?P<pk>\d+)/delete$',
		DeleteView.as_view(
			model=Locality,
			template_name='geneafamilycore/location/forms/delete_locality.html',
			success_url='/'),
				name='delete_locality'),

	# Locality's detail
	url(r'^locality/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Locality,
			template_name='geneafamilycore/location/locality_detail.html'),
				name='locality_detail'),

	# All Localitys
	url(r'^locality/all$',
		ListView.as_view(
			model=Locality,
			paginate_by=20,
			template_name='geneafamilycore/location/all_locations.html'),
				name='all_locations'),
]
from django.conf.urls import url
from django.views.generic import UpdateView, DetailView, ListView

from GeneaFamilyCore.models import Baptism
from GeneaFamilyCore.forms.baptism import BaptismForm
from GeneaFamilyCore.views.baptism import (
	CreateBaptism, DeleteBaptism)

baptism_urlpatterns = [

	###########
	# Baptism #
	###########

	# Create Baptism and assign to Member
	url(r'^baptism/(?P<member_pk>\d+)/create$',
		CreateBaptism.as_view(
			form_class=BaptismForm,
			template_name='geneafamilycore/baptism/forms/create_baptism.html'),
				name='create_baptism'),

	# Update a baptism
	url(r'^baptism/(?P<pk>\d+)/update$',
		UpdateView.as_view(
			model=Baptism,
			form_class=BaptismForm,
			template_name='geneafamilycore/baptism/forms/update_baptism.html'),
				name='update_baptism'),

	# Delete baptism
	url(r'^baptism/(?P<pk>\d+)/delete$',
		DeleteBaptism.as_view(
			model=Baptism,
			template_name='geneafamilycore/baptism/forms/delete_baptism.html'),
				name='delete_baptism'),

	# Baptism's detail
	url(r'^baptism/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Baptism,
			template_name='geneafamilycore/baptism/member_baptism_detail.html'),
				name='baptism_detail'),

	# All Baptisms
	url(r'^baptism/all$',
		ListView.as_view(
			model=Baptism,
			paginate_by=20,
			template_name='geneafamilycore/baptism/all_member_baptisms.html'),
				name='all_member_baptisms'),
]
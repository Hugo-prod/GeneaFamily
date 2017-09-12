from django.conf.urls import url
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from GeneaFamilyCore.models import Family
from GeneaFamilyCore.forms.family import FamilyForm

family_urlpatterns = [

	############
	# FAMILY #
	############
	# Create a family
	url(r'^family/create$',
		CreateView.as_view(
			form_class=FamilyForm,
			template_name='geneafamilycore/family/forms/create_family.html'),
				name='create_family'),

	# Update a family
	url(r'^family/(?P<pk>\d+)/update$',
		UpdateView.as_view(
			form_class=FamilyForm,
			template_name='geneafamilycore/family/forms/update_family.html'),
				name='update_family'),

	# Delete family
	url(r'^family/(?P<pk>\d+)/delete$',
		DeleteView.as_view(
			model=Family,
			template_name='geneafamilycore/family/forms/delete_family.html',
			success_url='/'),
				name='delete_family'),

	# Family's detail
	url(r'^family/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Family,
			template_name='geneafamilycore/family/family_detail.html'),
				name='family_detail'),

	# List a family
	url(r'^family/all$',
		ListView.as_view(
			model=Family,
			paginate_by=20,
			template_name='geneafamilycore/family/all_families.html'),
				name='all_families'),
]
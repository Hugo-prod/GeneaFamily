from django.conf.urls import url
from django.views.generic import UpdateView, DetailView, ListView

from GeneaFamilyCore.models import Source
from GeneaFamilyCore.forms.source import SourceForm
from GeneaFamilyCore.views.source import *

source_urlpatterns = [

	###########
	# Source #
	###########
	
	# Create Source and assign to member
	url(r'^source/(?P<member_pk>\d+)/create$',
		CreateSource.as_view(
			form_class=SourceForm,
			template_name='geneafamilycore/source/forms/create_source.html'),
				name='create_source'),

	# Update a source
	url(r'^source/(?P<pk>\d+)/update$',
		UpdateView.as_view(
			form_class=SourceForm,
			model=Source,
			template_name='geneafamilycore/source/forms/update_source.html'),
				name='update_source'),

	# Delete source
	url(r'^source/(?P<pk>\d+)/delete$',
		DeleteSource.as_view(
			model=Source,
			template_name='geneafamilycore/source/forms/delete_source.html'),
				name='delete_source'),

	# Source's detail
	url(r'^source/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Source,
			template_name='geneafamilycore/source/source_detail.html'),
				name='source_detail'),

	# All Sources
	url(r'^source/all$',
		ListView.as_view(
			model=Source,
			paginate_by=20,
			template_name='geneafamilycore/source/all_source.html'),
				name='all_source'),
]
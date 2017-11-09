from django.conf.urls import url
from django.views.generic import UpdateView, DetailView, DeleteView, ListView

from GeneaFamilyCore.models import Source, SourceMember
from GeneaFamilyCore.forms.source import SourceForm, SourceInvolvedMemberForm
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

	#####################
	## INVOLVED MEMBER ##
	#####################

	# Ajouter un membre (impliqué) à la source
	url(r'^source/(?P<source_pk>\d+)/member/add$',
		SourceAddInvolvedMember.as_view(
			form_class=SourceInvolvedMemberForm,
			template_name='geneafamilycore/source/forms/add_involved_member.html'),
				name='source_add_involved_member'),

	# Enlever un membre (impliqué) à la source
	url(r'^source/involved_member/(?P<pk>\d+)/remove$',
		SourceDeleteInvolvedMember.as_view(
			model=SourceMember,
			template_name='geneafamilycore/source/forms/remove_involved_member.html'),
				name='source_remove_involved_member'),
]
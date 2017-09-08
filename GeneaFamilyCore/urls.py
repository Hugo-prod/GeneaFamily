from django.conf.urls import url
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView

from .views import *
from .models import Member
from .forms import *

urlpatterns = [
	url(r'^$', 
		TemplateView.as_view(template_name='generic/index.html'), name='home'),

##########
# MEMBER #
##########

	# Create a member
	url(r'^member/create$',
		CreateView.as_view(
			form_class=MemberForm,
			template_name='geneafamilycore/forms/create_member.html'),
				name='create_member'),

	# Update a member
	url(r'^member/(?P<pk>\d+)/update$',
		UpdateView.as_view(
			model=Member,
			form_class=MemberForm,
			template_name='geneafamilycore/forms/update_member.html'),
				name='update_member'),

	# Delete member
	url(r'^member/(?P<pk>\d+)/delete$',
		DeleteView.as_view(
			model=Member,
			template_name='geneafamilycore/forms/delete_member.html',
			success_url='/'),
				name='delete_member'),

	# Member's detail
	url(r'^member/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Member,
			template_name='geneafamilycore/member_detail.html'),
				name='member_detail'),

	# All Members
	url(r'^member/all$',
		ListView.as_view(
			model=Member,
			paginate_by=20,
			template_name='geneafamilycore/all_members.html'),
				name='all_members'),


############
# LOCALITY #
############

	# Create a locality
	url(r'^locality/create$',
		CreateView.as_view(
			form_class=LocalityForm,
			template_name='geneafamilycore/forms/create_locality.html'),
				name='create_locality'),

	# Update a locality
	url(r'^locality/(?P<pk>\d+)/update$',
		UpdateView.as_view(
			model=Locality,
			form_class=LocalityForm,
			template_name='geneafamilycore/forms/update_locality.html'),
				name='update_locality'),

	# Delete locality
	url(r'^locality/(?P<pk>\d+)/delete$',
		DeleteView.as_view(
			model=Locality,
			template_name='geneafamilycore/forms/delete_locality.html',
			success_url='/'),
				name='delete_locality'),

	# Locality's detail
	url(r'^locality/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Locality,
			template_name='geneafamilycore/locality_detail.html'),
				name='locality_detail'),

	# All Localitys
	url(r'^locality/all$',
		ListView.as_view(
			model=Locality,
			paginate_by=20,
			template_name='geneafamilycore/all_locations.html'),
				name='all_locations'),


##############
# EVENT TYPE #
##############

	# Create a event_type
	url(r'^event_type/create$',
		CreateView.as_view(
			form_class=EventTypeForm,
			template_name='geneafamilycore/forms/create_event_type.html'),
				name='create_event_type'),

	# Update a event_type
	url(r'^event_type/(?P<slug>[-\w]+)-(?P<pk>\d+)/update$',
		UpdateView.as_view(
			model=EventType,
			form_class=UpdateEventTypeForm,
			template_name='geneafamilycore/forms/update_event_type.html'),
				name='update_event_type'),

	# Delete event_type
	url(r'^event_type/(?P<slug>[-\w]+)-(?P<pk>\d+)/delete$',
		DeleteView.as_view(
			model=EventType,
			template_name='geneafamilycore/forms/delete_event_type.html',
			success_url='/'),
				name='delete_event_type'),

	# EventType's detail
	url(r'^event_type/(?P<slug>[-\w]+)-(?P<pk>\d+)$',
		DetailView.as_view(
			model=EventType,
			template_name='geneafamilycore/event_type_detail.html'),
				name='event_type_detail'),

	# All EventTypes
	url(r'^event_type/all$',
		ListView.as_view(
			model=EventType,
			paginate_by=20,
			template_name='geneafamilycore/all_event_types.html'),
				name='all_event_types'),
]
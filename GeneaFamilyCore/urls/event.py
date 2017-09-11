from django.conf.urls import url
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from GeneaFamilyCore.models import Event, MemberEvent
from GeneaFamilyCore.views.event import CreateEvent, UpdateEvent

event_urlpatterns = [

	#########
	# EVENT #
	#########
	# Create Event and assign Member in MemberEvent
	url(r'^event/(?P<member_pk>\d+)/(?P<event_type_pk>\d+)/create$',
		CreateEvent.as_view(
			template_name='geneafamilycore/event/forms/create_event.html'),
				name='create_event'),

	# Update a event
	url(r'^event/(?P<member_event_pk>\d+)/(?P<event_type_pk>\d+)/update$',
		UpdateEvent.as_view(
			template_name='geneafamilycore/event/forms/update_event.html'),
				name='update_event'),

	# Delete event
	url(r'^event/(?P<pk>\d+)/delete$',
		DeleteView.as_view(
			model=MemberEvent,
			template_name='geneafamilycore/event/forms/delete_member_event.html',
			success_url='/'),
				name='delete_member_event'),

	# Event's detail
	url(r'^event/(?P<pk>\d+)$',
		DetailView.as_view(
			model=MemberEvent,
			template_name='geneafamilycore/event/member_event_detail.html'),
				name='event_detail'),

	# All Events
	url(r'^event/all$',
		ListView.as_view(
			model=MemberEvent,
			paginate_by=20,
			template_name='geneafamilycore/event/all_member_events.html'),
				name='all_member_events'),
]
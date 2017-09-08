from django.conf.urls import url
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from GeneaFamilyCore.models import EventType
from GeneaFamilyCore.forms.event_type import EventTypeForm, UpdateEventTypeForm

urlpatterns = [

	##############
	# EVENT TYPE #
	##############

	# Create a event_type
	url(r'^event_type/create$',
		CreateView.as_view(
			form_class=EventTypeForm,
			template_name='geneafamilycore/event_type/forms/create_event_type.html'),
				name='create_event_type'),

	# Update a event_type
	url(r'^event_type/(?P<slug>[-\w]+)-(?P<pk>\d+)/update$',
		UpdateView.as_view(
			model=EventType,
			form_class=UpdateEventTypeForm,
			template_name='geneafamilycore/event_type/forms/update_event_type.html'),
				name='update_event_type'),

	# Delete event_type
	url(r'^event_type/(?P<slug>[-\w]+)-(?P<pk>\d+)/delete$',
		DeleteView.as_view(
			model=EventType,
			template_name='geneafamilycore/event_type/forms/delete_event_type.html',
			success_url='/'),
				name='delete_event_type'),

	# EventType's detail
	url(r'^event_type/(?P<slug>[-\w]+)-(?P<pk>\d+)$',
		DetailView.as_view(
			model=EventType,
			template_name='geneafamilycore/event_type/event_type_detail.html'),
				name='event_type_detail'),

	# All EventTypes
	url(r'^event_type/all$',
		ListView.as_view(
			model=EventType,
			paginate_by=20,
			template_name='geneafamilycore/event_type/all_event_types.html'),
				name='all_event_types'),
]
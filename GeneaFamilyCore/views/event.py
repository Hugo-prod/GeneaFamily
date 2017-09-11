from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView

from GeneaFamilyCore.models import *
from GeneaFamilyCore.forms.event import EventDateForm, EventPeriodForm


class CreateEvent(CreateView):
	""" Create Event and assign Member in MemberEvent """

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.event_type_fk = self.event_type
		self.object.save()

		self.member = Member.objects.get(
			pk=self.kwargs['member_pk'])

		MemberEvent.objects.create(
			member_fk=self.member,
			event_fk=self.object)

		return super(CreateEvent, self).form_valid(form)

	def get_form_class(self):
		self.event_type = EventType.objects.get(
			pk=self.kwargs['event_type_pk'])

		if self.event_type.time_period_type == 'D':
			return EventDateForm
		else:
			return EventPeriodForm

	def get_context_data(self, **kwargs):
		context = super(CreateEvent, self).get_context_data(**kwargs)

		self.member = Member.objects.get(
			pk=self.kwargs['member_pk'])

		context['member'] = self.member
		context['event_type'] = self.event_type
		return context

	def get_success_url(self):
		return reverse('core:member_detail', args=[self.kwargs['member_pk']])


class UpdateEvent(UpdateView):

	def get_object(self):
		return Event.objects.get(
			pk=MemberEvent.objects.get(
				pk=self.kwargs['member_event_pk']).event_fk.pk)

	def get_form_class(self):
		self.event_type = EventType.objects.get(
			pk=self.kwargs['event_type_pk'])

		if self.event_type.time_period_type == 'D':
			return EventDateForm
		else:
			return EventPeriodForm

	def get_context_data(self, **kwargs):
		context = super(UpdateEvent, self).get_context_data(**kwargs)

		self.member_event = MemberEvent.objects.get(
			pk=self.kwargs['member_event_pk'])

		context['member_event'] = self.member_event
		return context

	def get_success_url(self):
		return reverse('core:member_detail',
			args=[MemberEvent.objects.get(
				pk=self.kwargs['member_event_pk']).member_fk.pk])
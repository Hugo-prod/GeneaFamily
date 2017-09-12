from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied, ValidationError

from autoslug import AutoSlugField


class Locality(models.Model):
	""" Locality """

	country = models.CharField(
		max_length=100,
		verbose_name="Pays")

	city = models.CharField(
		max_length=100,
		blank=True,
		verbose_name="Ville")

	additional_address_information = models.CharField(
		max_length=255,
		blank=True,
		verbose_name="Complément d'information de l'adresse")

	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)

	def get_absolute_url(self):
		return reverse('core:locality_detail', args=[int(self.id)])

	class Meta:
		ordering = ['country']


class EventType(models.Model):
	""" EventType """

	timePerdiodTypeChoices = (
		('D','Date'),
		('P', 'Durée'))

	name = models.CharField(
		max_length=100,
		verbose_name='Type d\'évenement',
		help_text='Ex: naissance, mariage, baptême, communion...')

	slug = AutoSlugField(populate_from='name')

	time_period_type = models.CharField(
		max_length=1,
		choices=timePerdiodTypeChoices,
		verbose_name='Type temporel',
		help_text= '''
		<p><u>Aide:</u></p>
		<p> - Une Date est égale à une date de naissance
		(Ex: Né(e) le 01/01/2000).</p>
		<p> - Une durée est égale à un temps exercé dans un profession
		(Ex: Boulanger de 01/01/2000 à 31/01/2001).</p>
		<p>Attention: Après validation ce paramètre 
		n\'est plus modifiable !</p>''')

	description = models.CharField(
		max_length=512,
		blank=True,
		help_text='Description du type de l\'èvenement')

	def get_absolute_url(self):
		return reverse('core:event_type_detail', args=[self.slug, int(self.id)])

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Event(models.Model):
	""" Event """

	event_type_fk = models.ForeignKey(
		EventType,
		verbose_name='Type d\'évènement')

	title = models.CharField(
		max_length=100,
		verbose_name='Titre')

	start_date = models.DateField(
		null=True,
		blank=True,
		verbose_name='Date')

	start_date_is_approximately = models.BooleanField(
		default=False,
		verbose_name='Environ',
		help_text='Cochez, si la date est une approximation')

	end_date = models.DateField(
		null=True,
		blank=True,
		verbose_name='Date de fin')

	end_date_is_approximately = models.BooleanField(
		default=False,
		verbose_name='Environ',
		help_text='Cochez, si la date est une approximation')

	content = models.TextField(
		max_length=1000,
		null=True,
		verbose_name='Contenu')

	# locality_fk = models.ForeignKey(
	# 	Locality,
	# 	verbose_name='Lieu')

	class Meta:
		ordering = ['id']


class Member(models.Model):
	""" Member """

	genderChoices = (
		('M', 'Homme'),
		('W', 'Femme'),
		('U', 'Inconnu(e)'),)

	first_name = models.CharField(
		max_length=50,
		verbose_name='Prénom')

	family_name = models.CharField(
		max_length=50,
		verbose_name='Nom de famille')

	gender = models.CharField(
		max_length=1,
		choices=genderChoices,
		verbose_name='Genre')

	def get_absolute_url(self):
		return reverse('core:member_detail', args=[int(self.id)])

	def __str__(self):
		return '{} {}'.format(self.first_name, self.family_name)

	def get_events(self):
		all_events = []
		for event_type in EventType.objects.all():
			if MemberEvent.objects.filter(
				member_fk=self,
				event_fk__event_type_fk__name=event_type.name).exists():
				all_events.append({
					'type': event_type,
					'list':MemberEvent.objects.filter(
						member_fk=self,
						event_fk__event_type_fk__name=event_type.name)
					})
		return all_events

	class Meta:
		ordering = ['family_name']


class MemberEvent(models.Model):
	""" MemberEvent: Associate an event to a member """

	member_fk = models.ForeignKey(Member)
	event_fk = models.ForeignKey(Event)

	def delete(self):
		Event.objects.get(pk=self.event_fk.pk).delete()
		super(MemberEvent, self).delete()

	def get_absolute_url(self):
		return reverse('core:member_detail', args=[int(self.member_fk.pk)])

	class Meta:
		ordering = ['id']


class Family(models.Model):

	mother_fk = models.ForeignKey(
		Member,
		related_name='mother',
		verbose_name='Mère',
		limit_choices_to={'gender': 'W'})
	
	father_fk = models.ForeignKey(
		Member,
		related_name='father',
		verbose_name='Père',
		limit_choices_to={'gender': 'M'})

	def full_clean(self, exclude=None, validate_unique=True):
		family_list = Family.objects.filter(
			mother_fk=self.mother_fk,
			father_fk=self.father_fk)
		if family_list:
			for family in family_list:
				if family.pk != self.pk:
					raise ValidationError('Cette famille existe déjà !')

	def get_absolute_url(self):
		return reverse('core:family_detail', args=[int(self.pk)])

	class Meta:
		ordering = ['id']


class Child(models.Model):

	family_fk = models.ForeignKey(Family)

	child_fk = models.ForeignKey(Member)
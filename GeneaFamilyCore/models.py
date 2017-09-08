from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied

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

	deleteable = models.BooleanField(default=True)

	description = models.CharField(
		max_length=512,
		blank=True,
		help_text='Description du type de l\'èvenement')

	def delete(self, *args, **kwargs):
		if not self.deleteable:
			raise PermissionDenied(
				'Vous ne pouvez pas supprimer ce type d\'évènement')
		super().delete(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('core:event_type_detail', args=[self.slug, int(self.id)])

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


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

	class Meta:
		ordering = ['family_name']
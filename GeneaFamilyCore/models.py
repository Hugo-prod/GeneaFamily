from django.db import models
from django.core.urlresolvers import reverse


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
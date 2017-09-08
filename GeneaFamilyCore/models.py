from django.db import models
from django.core.urlresolvers import reverse

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
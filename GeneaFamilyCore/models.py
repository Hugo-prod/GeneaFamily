from django.db import models
from django.db.models import Q
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

	locality_fk = models.ForeignKey(
		Locality,
		blank=True,
		null=True,
		verbose_name='Lieu')

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

	pseudonyme = models.CharField(
		blank=True,
		max_length=250,
		verbose_name='Surnoms')

	gender = models.CharField(
		max_length=1,
		choices=genderChoices,
		verbose_name='Genre')

	read = models.BooleanField(
		default=True,
		verbose_name='Sait lire',
		help_text='Si coché, l\'individu sait lire')
	
	write = models.BooleanField(
		default=True,
		verbose_name='Sait écrire',
		help_text='Si coché, l\'individu sait écrire')

	birth_fk = models.ForeignKey(
		'Birth',
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	death_fk = models.ForeignKey(
		'Death',
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	baptism_fk = models.ForeignKey(
		'Baptism',
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	military_fk = models.ForeignKey(
		'Military',
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

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

	def get_residences(self):
		return Residence.objects.filter(member_fk=self)

	def get_jobs(self):
		return Job.objects.filter(member_fk=self)

	def get_sources(self):
		return Source.objects.filter(member_fk=self)

	def get_parents(self):
		if Child.objects.filter(child_fk=self).exists():
			return Child.objects.get(child_fk=self).family_fk

	def get_families(self):
		if Family.objects.filter(Q(Q(father_fk=self) | Q(mother_fk=self))).exists():
			return Family.objects.filter(Q(Q(father_fk=self) | Q(mother_fk=self)))

	def get_age(self):
		if self.birth_fk and self.death_fk:
			return self.death_fk.date.year - self.birth_fk.date.year - \
				((self.death_fk.date.month, self.death_fk.date.day) < \
					(self.birth_fk.date.month, self.birth_fk.date.day))


	def get_absolute_url(self):
		return reverse('core:member_detail', args=[int(self.id)])

	def __str__(self):
		return '{} {}'.format(self.first_name, self.family_name)

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

	# FIXME: si on supprimer un membre qui est père ou mère, 
	# ça supprimer l'object Family ? (je pense que oui donc setnull)
	mother_fk = models.ForeignKey(
		Member,
		related_name='mother',
		verbose_name='Mère',
		limit_choices_to={'gender': 'W'},
		null=True)
	
	father_fk = models.ForeignKey(
		Member,
		related_name='father',
		verbose_name='Père',
		limit_choices_to={'gender': 'M'},
		null=True)

	union_fk = models.ForeignKey(
		'Union',
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	def get_family_name(self):
		# TODO: make this with union
		if self.father_fk:
			return self.father_fk.family_name
		else:
			return self.mother_fk.family_name

	def get_children(self):
		return Child.objects.filter(family_fk=self)

	def get_nb_children(self):
		return Child.objects.filter(family_fk=self).count()

	def full_clean(self, exclude=None, validate_unique=True):
		family_list = Family.objects.filter(
			mother_fk=self.mother_fk,
			father_fk=self.father_fk)
		if family_list:
			for family in family_list:
				if family.pk != self.pk:
					raise ValidationError('Cette famille existe déjà !')

	def get_absolute_url(self):
		return reverse('core:family_detail', args=[self.pk])

	def get_sources(self):
		return Source.objects.filter(source_type='F')

	class Meta:
		ordering = ['id']


class Child(models.Model):

	family_fk = models.ForeignKey(Family)

	child_fk = models.ForeignKey(
		Member,
		verbose_name='Enfant')

	def get_absolute_url(self):
		return reverse('core:family_detail', args=[self.family_fk.pk])


class Birth(models.Model):

	birth_type_Choices = (
		('L','Legitime'),
		('P','Pupille de la nation'),
		('M','Né(e) sans vie'),
		('N','Naturel'),
		('R','Naturel (Non reconnu(e))'),
		)

	birth_type = models.CharField(
		max_length=1,
		choices=birth_type_Choices,
		verbose_name='Statut de naissance')

	date = models.DateField(verbose_name='Date de naissance')

	time = models.TimeField(
		blank=True,
		null=True,
		verbose_name='Heure de naissance')

	date_is_approximately = models.BooleanField(
		default=False,
		verbose_name='Environ',
		help_text='Cochez cette case si la date est approximative.')

	locality_fk = models.ForeignKey(
		Locality,
		blank=True,
		null=True,
		verbose_name='Lieu',
		help_text='Lieu de naissance')

	def get_member(self):
		return Member.objects.get(birth_fk=self)

	def get_sources(self):
		return Source.objects.filter(source_type='N')

	def get_comparers(self):
		return BirthComparer.objects.filter(birth_fk=self)

	def get_witnesses(self):
		return BirthWitness.objects.filter(birth_fk=self)

	def get_absolute_url(self):
		return reverse(
			'core:member_detail',
			args=[Member.objects.get(birth_fk=self).pk])

	class Meta:
		ordering = ['date']



class BirthComparer(models.Model):

	birth_fk = models.ForeignKey(Birth)

	member_fk = models.ForeignKey(
		Member,
		verbose_name='Comparant')


class BirthWitness(models.Model):

	birth_fk = models.ForeignKey(Birth)

	member_fk = models.ForeignKey(
		Member,
		verbose_name='Témoin')


class Baptism(models.Model):

	date = models.DateField(
		blank=True,
		null=True,
		verbose_name='Date du baptême')

	time = models.TimeField(
		blank=True,
		null=True,
		verbose_name='Heure du baptême')

	date_is_approximately = models.BooleanField(
		default=False,
		verbose_name='Environ',
		help_text='Cochez cette case si la date est approximative.')

	godfather_fk = models.ForeignKey(
		Member,
		blank=True,
		null=True,
		related_name='godfather',
		limit_choices_to={'gender': 'M'},
		verbose_name='Parrain')

	godmother_fk = models.ForeignKey(
		Member,
		blank=True,
		null=True,
		related_name='godmother',
		limit_choices_to={'gender': 'W'},
		verbose_name='marraine')

	locality_fk = models.ForeignKey(
		Locality,
		blank=True,
		null=True,
		verbose_name='Lieu',
		help_text='Lieu du baptême')

	def get_member(self):
		return Member.objects.get(baptism_fk=self)

	def get_sources(self):
		return Source.objects.filter(source_type='B')

	def get_absolute_url(self):
		return reverse(
			'core:member_detail',
			args=[Member.objects.get(baptism_fk=self).pk])

	class Meta:
		ordering = ['date']


class Death(models.Model):

	death_type_Choices = (
		('N','Naturel'),
		('M','Maladie'),
		('I','Inconnue'),)

	date = models.DateField(
		blank=True,
		verbose_name='Date de décès')

	time = models.TimeField(
		blank=True,
		null=True,
		verbose_name='Heure de décès')

	date_is_approximately = models.BooleanField(
		default=False,
		verbose_name='Environ',
		help_text='Cochez cette case si la date est approximative.')

	death_reason = models.CharField(
		max_length=1,
		choices=death_type_Choices,
		verbose_name='Raison',
		help_text='Selectionnez la raison du décès.')

	locality_fk = models.ForeignKey(
		Locality,
		blank=True,
		null=True,
		verbose_name='Lieu',
		help_text='Lieu du décès')

	def get_member(self):
		return Member.objects.get(death_fk=self)

	def get_sources(self):
		return Source.objects.filter(source_type='B')

	def get_comparers(self):
		return DeathComparer.objects.filter(death_fk=self)

	def get_witnesses(self):
		return DeathWitness.objects.filter(death_fk=self)

	def get_absolute_url(self):
		return reverse(
			'core:member_detail',
			args=[Member.objects.get(death_fk=self).pk])

	class Meta:
		ordering = ['date']


class DeathComparer(models.Model):

	death_fk = models.ForeignKey(Death)

	member_fk = models.ForeignKey(
		Member,
		verbose_name='Comparant')


class DeathWitness(models.Model):

	death_fk = models.ForeignKey(Death)

	member_fk = models.ForeignKey(
		Member,
		verbose_name='Témoin')


class Union(models.Model):

	union_type_Choices = (
		('M','Mariage'),
		('U','Union libre'),
		('P','Pacse'),
		('D','Mariage posthume'),)

	union_type = models.CharField(
		max_length=1,
		choices=union_type_Choices,
		verbose_name='Type d\'union')

	start_date = models.DateField(
		blank=True,
		null=True,
		verbose_name='Date de l\'union')

	start_date_is_approximately = models.BooleanField(
		default=False,
		verbose_name='Environ',
		help_text='Cochez cette case si la date de début de l\'union est approximative.')

	end_date = models.DateField(
		blank=True,
		null=True,
		verbose_name='Date de fin de l\'union')

	end_date_is_approximately = models.BooleanField(
		default=False,
		verbose_name='Environ',
		help_text='Cochez cette case si la date de fin de l\'union est approximative.')

	locality_fk = models.ForeignKey(
		Locality,
		blank=True,
		null=True,
		verbose_name='Lieu',
		help_text='Lieu de l\'union')

	def get_family(self):
		return Family.objects.get(union_fk=self)

	def get_sources(self):
		return Source.objects.filter(source_type='U')

	def get_witnesses(self):
		return UnionWitness.objects.filter(union_fk=self)

	def get_comparers(self):
		return UnionComparer.objects.filter(union_fk=self)

	def get_absolute_url(self):
		return reverse(
			'core:family_detail',
			args=[Family.objects.get(union_fk=self).pk])

	class Meta:
		ordering = ['id']


class UnionWitness(models.Model):

	for_who_Choices = (
		('F','Le marié'),
		('M','La mariée'),
		('U','Non spéficié'),)

	union_fk = models.ForeignKey(Union)

	member_fk = models.ForeignKey(
		Member,
		verbose_name='Témoin')

	for_who = models.CharField(
		max_length=1,
		choices=for_who_Choices,
		verbose_name='Pour',
		help_text='Pour qui ce témoin acte sa présence')


class UnionComparer(models.Model):

	union_fk = models.ForeignKey(Union)

	member_fk = models.ForeignKey(
		Member,
		verbose_name='Comparant(e)')


class Military(models.Model):

	military_instructionChoices = (
		('0','Non-exercé'),
		('1','Exercé'))

	general_instructionChoices = (
		('0','ne sait ni lire ni écrire'),
		('1','sait lire seulement'),
		('2','sait lire et écrire'),
		('3','possède une instruction primaire plus développée'),
		('4','a obtenu le brevet de l\'enseignement primaire'),
		('5','bachelier, licencié, etc. (avec indication de diplôme)'),
		('X','dont on n\'a pas pu vérifier l\'instruction.' ))

	# Signalement
	head = models.CharField(
		max_length=50,
		blank=True,
		verbose_name='Visage')

	hair = models.CharField(
		max_length=50,
		blank=True,
		verbose_name='Cheveux')

	forehead = models.CharField(
		max_length=50,
		blank=True,
		verbose_name='Front')

	eyes = models.CharField(
		max_length=50,
		blank=True,
		verbose_name='Yeux')

	nose = models.CharField(
		max_length=50,
		blank=True,
		verbose_name='Nez')

	mouth = models.CharField(
		max_length=50,
		blank=True,
		verbose_name='Bouche')

	chin = models.CharField(
		max_length=50,
		blank=True,
		verbose_name='Menton')

	size = models.FloatField(
		blank=True,
		null=True,
		verbose_name='Taille')

	rectified_size = models.FloatField(
		blank=True,
		null=True,
		verbose_name='Taille')

	additional_note = models.TextField(
		blank=True,
		verbose_name='Remarque complémentaire')

	special_brand = models.TextField(
		blank=True,
		verbose_name='Marques particulières')

	# Degrè d'instruction
	military_instruction = models.CharField(
		max_length=1,
		blank=True,
		choices=military_instructionChoices,
		verbose_name='Degré d\'instruction militaire')

	general_instruction = models.CharField(
		max_length=1,
		blank=True,
		choices=general_instructionChoices,
		verbose_name='Degré d\'instruction général')

	# Matricule
	recruitment_matricul_number = models.IntegerField(
		blank=True,
		null=True,
		verbose_name='Numéro matricule du recrutement')

	mobilisation_class = models.IntegerField(
		blank=True,
		null=True,
		verbose_name='Classe de mobilisation')

	# Numéro de tirage 
	recruitment_draw = models.IntegerField(
		blank=True,
		null=True,
		verbose_name='Numéro de tirage')

	canton_recruitment = models.CharField(
		max_length=254,
		blank=True,
		verbose_name='Canton de recrutement')

	# Decision du conseil de révision et motifs
	advice_decision = models.TextField(
		blank=True,
		verbose_name='Décision du conseil de révision')

	advice_reason = models.TextField(
		blank=True,
		verbose_name='Motifs')

	def get_member(self):
		return Member.objects.get(military_fk=self)

	def get_sources(self):
		return Source.objects.filter(source_type='M')

	def get_absolute_url(self):
		return reverse('core:military_detail', args=[self.pk])

	class Meta:
		ordering = ['id']


class Residence(models.Model):

	member_fk = models.ForeignKey(
		'Member',
		verbose_name='Membre')

	locality_fk = models.ForeignKey(
		'Locality',
		blank=True,
		null=True,
		verbose_name='Lieu')

	date = models.DateField(
		null=True,
		blank=True,
		verbose_name='Date')

	date_is_approximately = models.BooleanField(
		default=False,
		verbose_name='Cochez si la date est approximative')

	class Meta:
		ordering = ['id']


class Job(models.Model):

	job_name = models.CharField(
		max_length=254,
		verbose_name='Metier',
		help_text='Veuillez inscrire le nom du métier')

	date = models.DateField(
		null=True,
		blank=True,
		verbose_name='Date')

	date_is_approximately = models.BooleanField(
		default=False,
		verbose_name='Cochez si la date est approximative')

	member_fk = models.ForeignKey(
		'Member',
		verbose_name='Membre')

	locality_fk = models.ForeignKey(
		'Locality',
		blank=True,
		null=True,
		verbose_name='Lieu')

	class Meta:
		ordering = ['id']


class Source(models.Model):

	source_typeChoices = (
		('G','Global'),
		('N','Naissance'),
		('D','Décès'),
		('B','Baptême'),
		('F','Famille'),
		('U','Union'),
		('M','Militaire'))

	member_fk = models.ForeignKey('Member')

	title = models.CharField(
		blank=True,
		null=True,
		max_length=250,
		verbose_name='Titre')

	source_type = models.CharField(
		max_length=1,
		choices=source_typeChoices,
		verbose_name='Sourcer')

	img_upload = models.ImageField(
		upload_to='source',
		blank=True,
		null=True,
		verbose_name='Photo')

	url_link = models.CharField(
		max_length=2048,
		blank=True,
		null=True,
		verbose_name='Lien de la source (URL)')

	page_link = models.CharField(
		max_length=250,
		blank=True,
		null=True,
		verbose_name='Numéro de page')

	additional_note = models.TextField(
		blank=True,
		null=True,
		verbose_name='Notes complémentaire')

	def __str__(self):
		return self.title

	def get_involved_member(self):
		return SourceMember.objects.filter(source_fk=self)

	def get_absolute_url(self):
		return reverse('core:source_detail', args=[self.pk])

	class Meta:
		ordering = ['id']


class SourceMember(models.Model):

	source_fk = models.ForeignKey(Source)

	member_fk = models.ForeignKey(
		Member,
		verbose_name='Membre')

	def get_absolute_url(self):
		return reverse('core:source_detail', args=[self.source_fk.pk])
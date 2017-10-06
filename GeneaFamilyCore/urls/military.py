from django.conf.urls import url
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from GeneaFamilyCore.models import Military
from GeneaFamilyCore.forms.military import *
from GeneaFamilyCore.views.military import CreateMilitary

military_urlpatterns = [

	############
	# Military #
	############
	
	# Créer un object military vide et redirect sur cette page
	url(r'^military/(?P<member_pk>\d+)/create$',
		CreateMilitary.as_view(
			template_name='geneafamilycore/military/forms/create_military.html'),
				name='create_military'),

	# Update a military
	url(r'^military/(?P<pk>\d+)/signalment/update$',
		UpdateView.as_view(
			form_class=MilitarySignalmentForm,
			template_name='geneafamilycore/military/forms/update_signalment_military.html'),
				name='update_signalment_military'),

	# Update a military
	url(r'^military/(?P<pk>\d+)/class/update$',
		UpdateView.as_view(
			form_class=MilitaryClassForm,
			template_name='geneafamilycore/military/forms/update_class_military.html'),
				name='update_class_military'),

	# Update a military
	url(r'^military/(?P<pk>\d+)/instruction/update$',
		UpdateView.as_view(
			form_class=MilitaryInstructionForm,
			template_name='geneafamilycore/military/forms/update_instruction_military.html'),
				name='update_instruction_military'),

	# Update a military
	url(r'^military/(?P<pk>\d+)/recruitment/update$',
		UpdateView.as_view(
			form_class=MilitaryRecruitmentForm,
			template_name='geneafamilycore/military/forms/update_recruitment_military.html'),
				name='update_recruitment_military'),

	# Update a military
	url(r'^military/(?P<pk>\d+)/advice/update$',
		UpdateView.as_view(
			form_class=MilitaryAdviceForm,
			template_name='geneafamilycore/military/forms/update_advice_military.html'),
				name='update_advice_military'),

	# Delete military
	url(r'^military/(?P<pk>\d+)/delete$',
		DeleteView.as_view(
			model=Military,
			template_name='geneafamilycore/military/forms/delete_military.html',
			success_url='/'),
				name='delete_military'),

	# Military's detail
	url(r'^military/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Military,
			template_name='geneafamilycore/military/military_detail.html'),
				name='military_detail'),

	# All Militarys
	url(r'^military/all$',
		ListView.as_view(
			model=Military,
			paginate_by=20,
			template_name='geneafamilycore/military/all_military.html'),
				name='all_member_militarys'),
]
from django.conf.urls import url
from django.views.generic import DetailView, DeleteView, ListView

from GeneaFamilyCore.models import Job
from GeneaFamilyCore.forms.job import *
from GeneaFamilyCore.views.job import *

job_urlpatterns = [

	########
	# JOBS #
	########

	# Create Job and assign Member in Job
	url(r'^job/(?P<member_pk>\d+)/create$',
		CreateJob.as_view(
			form_class=JobForm,
			model=Job,
			template_name='geneafamilycore/job/forms/create_job.html'),
				name='create_job'),

	# Update a job
	url(r'^job/(?P<pk>\d+)/update$',
		UpdateJob.as_view(
			form_class=JobForm,
			model=Job,
			template_name='geneafamilycore/job/forms/update_job.html'),
				name='update_job'),

	# Delete job
	url(r'^job/(?P<pk>\d+)/delete$',
		DeleteJob.as_view(
			model=Job,
			template_name='geneafamilycore/job/forms/delete_job.html'),
				name='delete_job'),

	# Job's detail
	url(r'^job/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Job,
			template_name='geneafamilycore/job/job_detail.html'),
				name='job_detail'),

	# All Jobs
	url(r'^job/all$',
		ListView.as_view(
			model=Job,
			paginate_by=20,
			template_name='geneafamilycore/job/all_jobs.html'),
				name='all_jobs'),
]